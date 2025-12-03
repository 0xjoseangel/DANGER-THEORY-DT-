import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from deap import base, creator, tools, algorithms

# ==========================================
# 1. CARGA Y PREPARACIÓN DE DATOS (AHORA CON DESEMPLEO REAL)
# ==========================================

def prepare_data_complete(file_rates, file_reserves, file_naef, file_unemp):
    
    # --- A. Cargar Tipos de Cambio ---
    rates = pd.read_excel(file_rates, skiprows=3)
    rates = rates.iloc[3:].copy()
    rates.columns = ['Basura', 'Date', 'DEM', 'ITL', 'ESP', 'GBP']
    rates['Date'] = pd.to_datetime(rates['Date'])
    rates['GBP'] = pd.to_numeric(rates['GBP'].astype(str).str.replace(',', '.'), errors='coerce')
    rates = rates[['Date', 'GBP']].dropna().sort_values('Date')

    # --- B. Cargar Reservas ---
    reserves = pd.read_excel(file_reserves)
    reserves['Date'] = pd.to_datetime(reserves['Date'], dayfirst=True)
    reserves = reserves.sort_values('Date')

    # --- C. Cargar Intervenciones Naef ---
    naef = pd.read_excel(file_naef, sheet_name='Main data clean', decimal=',')
    naef = naef.iloc[:, [0, 1]] 
    naef.columns = ['Date', 'Intervention']
    naef['Date'] = pd.to_datetime(naef['Date'], dayfirst=True)
    naef['Intervention'] = pd.to_numeric(naef['Intervention'], errors='coerce').fillna(0)

    # --- D. CARGAR DESEMPLEO (NUEVO) ---
    # Leemos el archivo tal cual me lo has enseñado
    unemp = pd.read_excel(file_unemp)
    
    # Tu Excel tiene una cabecera rara en la fila 1 ("Unemployment Rate")
    # y los datos empiezan abajo. Vamos a renombrar columnas a la fuerza.
    unemp = unemp.iloc[:, 0:2] # Solo queremos las dos primeras columnas
    unemp.columns = ['DateStr', 'Unemployment']
    
    # Convertimos "1990 JAN" a fecha real (1990-01-01)
    # %Y = Año (1990), %b = Mes Abreviado (JAN, FEB...)
    unemp['Date'] = pd.to_datetime(unemp['DateStr'], format='%Y %b', errors='coerce')
    
    # Limpiamos (borramos la fila del título si no se convirtió bien)
    unemp = unemp.dropna(subset=['Date'])
    unemp = unemp.sort_values('Date')

    # --- E. FUSIÓN MAESTRA ---
    # Usamos las fechas de rates (diario) como base
    df = pd.merge(rates, reserves, on='Date', how='left')
    df = pd.merge(df, naef, on='Date', how='left')
    df = pd.merge(df, unemp[['Date', 'Unemployment']], on='Date', how='left') # Añadimos Desempleo
    
    df = df.sort_values('Date')
    
    # --- F. RELLENOS (CRÍTICO) ---
    # Reservas y Desempleo son MENSUALES -> Rellenamos hacia adelante (ffill)
    # "Si hoy es día 5 y no hay dato, usa el del día 1"
    df['Total Reserves'] = df['Total Reserves'].ffill()
    df['Unemployment'] = df['Unemployment'].ffill()
    
    # Intervención es DIARIA -> Si no hay dato, es 0
    df['Intervention'] = df['Intervention'].fillna(0)
    
    # Filtro de Fechas
    mask = (df['Date'] >= '1990-01-01') & (df['Date'] <= '1993-01-01')
    df = df.loc[mask].reset_index(drop=True)
    df = df.dropna(subset=['Total Reserves', 'GBP', 'Unemployment'])

    # --- G. NORMALIZACIÓN (GENES) ---
    
    # Gen 1: Reservas
    df['Gen_Reservas'] = (df['Total Reserves'] - df['Total Reserves'].mean()) / df['Total Reserves'].std()
    
    # Gen 2: Precio
    df['Gen_Precio'] = (df['GBP'] - df['GBP'].mean()) / df['GBP'].std()
    
    # Gen 3: Volatilidad
    vol = df['GBP'].rolling(30).std().fillna(0)
    df['Gen_Volatilidad'] = (vol - vol.mean()) / vol.std()
    
    # Gen 4: Intervención (Naef)
    abs_int = df['Intervention'].abs()
    df['Gen_Intervencion'] = (abs_int - abs_int.mean()) / (abs_int.std() + 1e-6)
    
    # GEN 5: DESEMPLEO (NUEVO)
    # Normalizamos igual que los demás
    df['Gen_Desempleo'] = (df['Unemployment'] - df['Unemployment'].mean()) / df['Unemployment'].std()

    return df

# --- EJECUTAR CARGA ---
# Asegúrate de que el nombre del archivo es EXACTO (cuidado con la 'e' extra en Unemployement)
path_rates = 'data/tipoDeCambioEuropa.xlsx'
path_reserves = 'data/ReservesData.xlsx'
path_naef = 'data/Bank of England daily FX interventions, 1952-1995.xlsx'
path_unemp = 'data/Unemployement.xlsx' 

df_env = prepare_data_complete(path_rates, path_reserves, path_naef, path_unemp)
TARGET_DATE = pd.to_datetime('1992-09-16')

print("✅ Datos cargados con 5 Genes (incluido Desempleo Real).")
print(df_env[['Date', 'Unemployment', 'Gen_Desempleo']].head()) # Verificar que se ve bien


# ==========================================
# 2. CONFIGURACIÓN EVOLUTIVA (5 GENES)
# ==========================================

if "FitnessMax" in creator.__dict__: del creator.FitnessMax
if "Individual" in creator.__dict__: del creator.Individual

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, -1.0, 1.0)
# AHORA N=5
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=5)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# ==========================================
# 3. EVALUACIÓN
# ==========================================

def eval_danger_theory(individual):
    w_res, w_price, w_vol, w_int, w_unemp = individual # 5 Pesos
    threshold = 0.5
    
    # Señal combinada
    signals = (w_res * df_env['Gen_Reservas']) + \
              (w_price * df_env['Gen_Precio']) + \
              (w_vol * df_env['Gen_Volatilidad']) + \
              (w_int * df_env['Gen_Intervencion']) + \
              (w_unemp * df_env['Gen_Desempleo'])
              
    triggers = signals[signals > threshold]
    
    if triggers.empty: return -100.0,
    
    exit_idx = triggers.index[0]
    exit_date = df_env.loc[exit_idx, 'Date']
    
    # Estrategia de Codicia (Greed)
    if exit_date > TARGET_DATE: return -50.0,
    
    days_before = (TARGET_DATE - exit_date).days
    
    if days_before == 0: return 20.0,
    elif 1 <= days_before <= 20: return 100.0 - (days_before * 1.5), 
    elif 21 <= days_before <= 90: return 50.0 - (days_before * 0.2),
    else: return -20.0, 

toolbox.register("evaluate", eval_danger_theory)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.2, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# ==========================================
# 4. EJECUCIÓN
# ==========================================

def main():
    random.seed(42)
    pop = toolbox.population(n=150)
    hof = tools.HallOfFame(1)
    
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("max", np.max)
    
    print("Evolucionando con 5 Genes...")
    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=50, 
                                   stats=stats, halloffame=hof, verbose=True)
    return pop, log, hof

pop, log, hof = main()
best = hof[0]

# --- RESULTADOS ---
genes_names = ['Reservas', 'Precio', 'Volatilidad', 'Intervención', 'Desempleo']

print(f"\n--- MEJOR AGENTE ---")
for name, val in zip(genes_names, best):
    print(f"{name}: {val:.2f}")

# Gráfica
signal = (best[0]*df_env['Gen_Reservas']) + (best[1]*df_env['Gen_Precio']) + \
         (best[2]*df_env['Gen_Volatilidad']) + (best[3]*df_env['Gen_Intervencion']) + \
         (best[4]*df_env['Gen_Desempleo'])

exit_idx = signal[signal > 0.5].index.min()

plt.figure(figsize=(14, 8))

# Subplot 1: Decisión
plt.subplot(2, 1, 1)
plt.plot(df_env['Date'], df_env['GBP'], label='Precio GBP', color='gray', alpha=0.5)
plt.axvline(TARGET_DATE, color='red', linestyle='--')
if pd.notna(exit_idx):
    date = df_env.loc[exit_idx, 'Date']
    price = df_env.loc[exit_idx, 'GBP']
    plt.plot(date, price, 'ro', markersize=10)
    plt.axvline(date, color='green', linewidth=2)
    plt.title(f"Salida: {date.date()} ({(TARGET_DATE-date).days} días antes)")

# Subplot 2: Importancia Genes
plt.subplot(2, 1, 2)
colors = ['red' if x < 0 else 'green' for x in best]
plt.bar(genes_names, best, color=colors)
plt.axhline(0, color='black')
plt.title("Importancia de los Genes (Pesos)")

plt.tight_layout()
plt.show()