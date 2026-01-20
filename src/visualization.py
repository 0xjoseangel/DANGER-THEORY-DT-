"""
Módulo de visualización.

Contiene funciones para crear gráficos y visualizaciones
de los resultados del algoritmo de Danger Theory.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


GENE_NAMES = ['Reservas', 'Precio', 'Volatilidad', 'Intervención', 'Desempleo']


def plot_results(df_env, individual, target_date, signal=None, figsize=(14, 8)):
    """
    Genera el gráfico completo de resultados.

    Parameters
    ----------
    df_env : pd.DataFrame
        DataFrame con los datos
    individual : list
        Mejor individuo encontrado
    target_date : pd.Timestamp
        Fecha objetivo de la crisis
    signal : pd.Series, optional
        Señal precalculada (si no se proporciona, se calcula)
    figsize : tuple
        Tamaño de la figura

    Returns
    -------
    matplotlib.figure.Figure
        Figura con los gráficos
    """
    if signal is None:
        signal = (individual[0] * df_env['Gen_Reservas']) + \
                 (individual[1] * df_env['Gen_Precio']) + \
                 (individual[2] * df_env['Gen_Volatilidad']) + \
                 (individual[3] * df_env['Gen_Intervencion']) + \
                 (individual[4] * df_env['Gen_Desempleo'])

    exit_idx = signal[signal > 0.5].index.min()

    fig = plt.figure(figsize=figsize)

    # Subplot 1: Decisión
    plt.subplot(2, 1, 1)
    plt.plot(df_env['Date'], df_env['GBP'], label='Precio GBP', color='gray', alpha=0.5)
    plt.axvline(target_date, color='red', linestyle='--', label='Crisis (16-Sep-1992)')

    if pd.notna(exit_idx):
        date = df_env.loc[exit_idx, 'Date']
        price = df_env.loc[exit_idx, 'GBP']
        plt.plot(date, price, 'ro', markersize=10, label='Señal de salida')
        plt.axvline(date, color='green', linewidth=2, label='Predicción')
        plt.title(f"Salida: {date.date()} ({(target_date-date).days} días antes)")
    else:
        plt.title("Sin señal de salida detectada")

    plt.xlabel('Fecha')
    plt.ylabel('Tipo de cambio GBP')
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Subplot 2: Importancia Genes
    plt.subplot(2, 1, 2)
    colors = ['red' if x < 0 else 'green' for x in individual]
    plt.bar(GENE_NAMES, individual, color=colors)
    plt.axhline(0, color='black')
    plt.title("Importancia de los Genes (Pesos)")
    plt.ylabel('Peso')
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    return fig


def plot_gene_importance(individual, figsize=(10, 6)):
    """
    Genera un gráfico de barras con la importancia de cada gen.

    Parameters
    ----------
    individual : list
        Lista de pesos de los genes
    figsize : tuple
        Tamaño de la figura

    Returns
    -------
    matplotlib.figure.Figure
        Figura con el gráfico
    """
    fig, ax = plt.subplots(figsize=figsize)

    colors = ['red' if x < 0 else 'green' for x in individual]
    bars = ax.bar(GENE_NAMES, individual, color=colors)

    ax.axhline(0, color='black', linewidth=0.5)
    ax.set_title("Importancia de los Genes (Pesos del Mejor Agente)")
    ax.set_ylabel('Peso')
    ax.grid(True, alpha=0.3, axis='y')

    # Añadir valores en las barras
    for bar, val in zip(bars, individual):
        height = bar.get_height()
        ax.annotate(f'{val:.2f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3 if height >= 0 else -10),
                    textcoords="offset points",
                    ha='center', va='bottom' if height >= 0 else 'top')

    plt.tight_layout()
    return fig


def print_results(individual):
    """
    Imprime los resultados del mejor agente.

    Parameters
    ----------
    individual : list
        Lista de pesos del mejor agente
    """
    print(f"\n--- MEJOR AGENTE ---")
    for name, val in zip(GENE_NAMES, individual):
        print(f"{name}: {val:.2f}")
