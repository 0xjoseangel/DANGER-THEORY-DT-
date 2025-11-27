import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from deap import base, creator, tools, algorithms

# ==========================================
# 1. CARGA Y PREPARACIÓN DE DATOS (CON NAEF)
# ==========================================

def prepare_data_complete(file_rates, file_reserves, file_naef):
    """
    Fusión de:
    1. Tipos de Cambio (Diario)
    2. Reservas (Mensual -> Relleno)
    3. Intervenciones Naef (Diario -> La pieza clave)
    """
    # --- A. Cargar Tipos de Cambio ---
    # Asumimos que df_cleaned ya existe o se carga así:
    rates = pd.read_excel(file_rates, skiprows=3) # Ajusta skiprows según tu excel
    # Limpieza rápida basada en tu código anterior
    rates = rates.iloc[3:].copy()
    rates.columns = ['Basura', 'Date', 'DEM', 'ITL', 'ESP', 'GBP']
    rates['Date'] = pd.to_datetime(rates['Date'])
    rates['GBP'] = pd.to_numeric(rates['GBP'].astype(str).str.replace(',', '.'), errors='coerce')
    rates = rates[['Date', 'GBP']].dropna().sort_values('Date')

    # --- B. Cargar Reservas ---
    reserves = pd.read_excel(file_reserves)
    reserves['Date'] = pd.to_datetime(reserves['Date'], dayfirst=True)
    reserves = reserves.sort_values('Date')

    # --- C. Cargar Intervenciones Naef (Gen 10) ---
    # Usamos la hoja 'Main data clean' y decimal con coma
    naef = pd.read_excel(file_naef, sheet_name='Main data clean', decimal=',')
    naef = naef.iloc[:, [0, 1]] # Solo columnas Fecha y Total
    naef.columns = ['Date', 'Intervention']
    naef['Date'] = pd.to_datetime(naef['Date'], dayfirst=True)
    naef['Intervention'] = pd.to_numeric(naef['Intervention'], errors='coerce').fillna(0)

    # --- D. Fusión Maestra ---
    # Usamos las fechas de rates como base
    df = pd.merge(rates, reserves, on='Date', how='left')
    df = pd.merge(df, naef, on='Date', how='left')
    
    # Rellenos Lógicos
    df['Total Reserves'] = df['Total Reserves'].ffill() # Reservas: El dato se mantiene todo el mes
    df['Intervention'] = df['Intervention'].fillna(0)   # Naef: Si no hay dato, es 0 intervención
    
    # Filtro de Fechas (Zoom en la crisis)
    mask = (df['Date'] >= '1990-01-01') & (df['Date'] <= '1993-01-01')
    df = df.loc[mask].reset_index(drop=True)
    
    # Borrar inicio sin datos
    df = df.dropna(subset=['Total Reserves', 'GBP'])

    # --- E. INGENIERÍA DE GENES (NORMALIZACIÓN) ---
    
    # Gen 1: Reservas (Salud a largo plazo)
    df['Gen_Reservas'] = (df['Total Reserves'] - df['Total Reserves'].mean()) / df['Total Reserves'].std()
    
    # Gen 2: Precio (La señal engañosa)
    df['Gen_Precio'] = (df['GBP'] - df['GBP'].mean()) / df['GBP'].std()
    
    # Gen 3: Volatilidad (El miedo)
    df['Gen_Volatilidad'] = df['GBP'].rolling(30).std().fillna(0)
    # Normalizamos la volatilidad también para que pese igual
    df['Gen_Volatilidad'] = (df['Gen_Volatilidad'] - df['Gen_Volatilidad'].mean()) / df['Gen_Volatilidad'].std()
    
    # GEN 4 (NUEVO): INTERVENCIÓN (La señal de pánico)
    # Usamos valor absoluto: Tanto comprar como vender masivamente es peligro.
    df['Abs_Intervention'] = df['Intervention'].abs()
    # Normalizamos
    df['Gen_Intervencion'] = (df['Abs_Intervention'] - df['Abs_Intervention'].mean()) / df['Abs_Intervention'].std()

    return df

# --- EJECUTAR CARGA ---
# Ajusta las rutas a tus archivos reales
path_rates = 'data/tipoDeCambioEuropa.xlsx'
path_reserves = 'data/ReservesData.xlsx'
path_naef = 'data/Bank of England daily FX interventions, 1952-1995.xlsx' # El nuevo archivo

df_env = prepare_data_complete(path_rates, path_reserves, path_naef)
TARGET_DATE = pd.to_datetime('1992-09-16')

print("Datos cargados correctamente con Intervenciones de Naef.")
print(df_env[['Date', 'Gen_Intervencion']].tail())


# ==========================================
# 2. CONFIGURACIÓN DEL ALGORITMO EVOLUTIVO
# ==========================================

# Limpieza previa de DEAP
if "FitnessMax" in creator.__dict__: del creator.FitnessMax
if "Individual" in creator.__dict__: del creator.Individual

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
# AHORA TENEMOS 4 GENES (Antes eran 3)
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, -1.0, 1.0)
# n=4 porque ahora son: [Reservas, Precio, Volatilidad, Intervención]
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=4)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# ==========================================
# 3. LÓGICA DE SUPERVIVENCIA (FITNESS)
# ==========================================

def eval_danger_theory(individual):
    w_res, w_price, w_vol, w_int = individual # Desempaquetamos 4 genes
    threshold = 0.5
    
    # Calculamos la señal de alarma del agente
    # Señal = (w1*Reservas) + (w2*Precio) + (w3*Volatilidad) + (w4*Intervención)
    signals = (w_res * df_env['Gen_Reservas']) + \
              (w_price * df_env['Gen_Precio']) + \
              (w_vol * df_env['Gen_Volatilidad']) + \
              (w_int * df_env['Gen_Intervencion'])
              
    # ¿Cuándo salta la alarma?
    triggers = signals[signals > threshold]
    
    if triggers.empty:
        return -100.0, # Nunca salió, murió en la crisis
    
    # Fecha de salida
    exit_idx = triggers.index[0]
    exit_date = df_env.loc[exit_idx, 'Date']
    
    # --- CÁLCULO DE PUNTUACIÓN (STRATEGY: GREED) ---
    
    if exit_date > TARGET_DATE:
        return -50.0, # Salió tarde (perdió capital)
    
    days_before = (TARGET_DATE - exit_date).days
    
    if days_before == 0:
        return 20.0, # Demasiado riesgo esperar al mismo día
        
    elif 1 <= days_before <= 20:
        # ZONA ÓPTIMA: Detectó la intervención masiva días antes
        # Cuanto más cerca, más puntos (Codicia)
        return 100.0 - (days_before * 1.5), 
        
    elif 21 <= days_before <= 90:
        # Zona segura pero poco rentable
        return 50.0 - (days_before * 0.2),
        
    else:
        # Salió meses antes (Paranoia de 1991). Castigo fuerte para que vuelva a entrar.
        return -20.0, 

toolbox.register("evaluate", eval_danger_theory)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.2, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# ==========================================
# 4. EJECUCIÓN
# ==========================================

def main():
    random.seed(42)
    pop = toolbox.population(n=150) # Más población para explorar mejor
    hof = tools.HallOfFame(1)
    
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("max", np.max)
    
    print("Iniciando evolución con Datos de Naef (Gen 10)...")
    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=50, 
                                   stats=stats, halloffame=hof, verbose=True)
    return pop, log, hof

# --- CORRER ---
pop, log, hof = main()
best = hof[0]

print(f"\n--- MEJOR AGENTE ENCONTRADO ---")
print(f"Pesos Genéticos:")
print(f"  1. Reservas:     {best[0]:.2f}")
print(f"  2. Precio:       {best[1]:.2f}")
print(f"  3. Volatilidad:  {best[2]:.2f}")
print(f"  4. INTERVENCIÓN: {best[3]:.2f} (¡Mira este valor!)")

# --- GRÁFICA FINAL ---
# Reconstruir señal
signal = (best[0]*df_env['Gen_Reservas']) + (best[1]*df_env['Gen_Precio']) + \
         (best[2]*df_env['Gen_Volatilidad']) + (best[3]*df_env['Gen_Intervencion'])

exit_idx = signal[signal > 0.5].index.min()

plt.figure(figsize=(14, 7))
plt.plot(df_env['Date'], df_env['GBP'], label='GBP (Precio)', color='gray', alpha=0.5)
plt.axvline(TARGET_DATE, color='red', linestyle='--', label='Miércoles Negro')

if pd.notna(exit_idx):
    date = df_env.loc[exit_idx, 'Date']
    price = df_env.loc[exit_idx, 'GBP']
    plt.plot(date, price, 'ro', markersize=15, label='Salida Agente (Danger Theory)')
    plt.axvline(date, color='green', linewidth=2, alpha=0.7)
    print(f"Fecha de Salida: {date.date()} ({(TARGET_DATE - date).days} días antes)")

# Pintar las intervenciones abajo para ver la correlación
ax2 = plt.gca().twinx()
ax2.bar(df_env['Date'], df_env['Intervention'], color='orange', alpha=0.3, label='Intervención Naef')
ax2.set_ylabel('Intervención (Millones $)')

plt.title('Validación Danger Theory con Datos Naef (Gen 10)')
plt.legend(loc='upper left')
plt.show()