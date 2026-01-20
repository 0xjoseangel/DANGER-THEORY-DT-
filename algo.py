"""
Danger Theory - Script principal (Legacy)

Este archivo mantiene compatibilidad con el código original.
Para nuevos usos, se recomienda usar run.py o importar desde src/.

Uso:
    python algo.py
"""

import pandas as pd
import matplotlib.pyplot as plt

# Importar desde los módulos reorganizados
from src.data_loader import prepare_data_complete, load_default_data
from src.danger_theory import setup_evolutionary, run_evolution, calculate_signal
from src.visualization import plot_results, print_results, GENE_NAMES

# ==========================================
# 1. CARGA Y PREPARACIÓN DE DATOS
# ==========================================

path_rates = 'data/tipoDeCambioEuropa.xlsx'
path_reserves = 'data/ReservesData.xlsx'
path_naef = 'data/Bank of England daily FX interventions, 1952-1995.xlsx'
path_unemp = 'data/Unemployement.xlsx'

df_env = prepare_data_complete(path_rates, path_reserves, path_naef, path_unemp)
TARGET_DATE = pd.to_datetime('1992-09-16')

print("✅ Datos cargados con 5 Genes (incluido Desempleo Real).")
print(df_env[['Date', 'Unemployment', 'Gen_Desempleo']].head())

# ==========================================
# 2. CONFIGURACIÓN Y EJECUCIÓN EVOLUTIVA
# ==========================================

toolbox = setup_evolutionary(df_env, TARGET_DATE)

def main():
    """Función principal del algoritmo evolutivo."""
    pop, log, hof = run_evolution(toolbox, population_size=150, generations=50)
    return pop, log, hof

pop, log, hof = main()
best = hof[0]

# ==========================================
# 3. RESULTADOS
# ==========================================

print_results(best)

# Gráfica
signal = calculate_signal(best, df_env)
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
plt.bar(GENE_NAMES, best, color=colors)
plt.axhline(0, color='black')
plt.title("Importancia de los Genes (Pesos)")

plt.tight_layout()
plt.show()
