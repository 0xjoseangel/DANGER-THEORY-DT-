#!/usr/bin/env python3
"""
Danger Theory - Punto de entrada principal

Este script ejecuta el algoritmo de Danger Theory para detectar
señales de crisis financiera en la crisis de la Libra de 1992.

Uso:
    python run.py
"""

import pandas as pd
import matplotlib.pyplot as plt

from src.data_loader import load_default_data
from src.danger_theory import setup_evolutionary, run_evolution, calculate_signal
from src.visualization import plot_results, print_results


def main():
    """Función principal del algoritmo."""

    # 1. Cargar datos
    print("Cargando datos...")
    df_env = load_default_data()
    TARGET_DATE = pd.to_datetime('1992-09-16')

    print("✅ Datos cargados con 5 Genes (incluido Desempleo Real).")
    print(df_env[['Date', 'Unemployment', 'Gen_Desempleo']].head())

    # 2. Configurar algoritmo evolutivo
    print("\nConfigurando algoritmo evolutivo...")
    toolbox = setup_evolutionary(df_env, TARGET_DATE)

    # 3. Ejecutar evolución
    pop, log, hof = run_evolution(toolbox, population_size=150, generations=50)

    # 4. Obtener mejor solución
    best = hof[0]
    print_results(best)

    # 5. Visualizar resultados
    signal = calculate_signal(best, df_env)
    fig = plot_results(df_env, best, TARGET_DATE, signal)
    plt.show()

    return best, df_env, log


if __name__ == "__main__":
    best, df_env, log = main()
