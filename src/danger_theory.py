"""
Módulo del algoritmo de Danger Theory.

Contiene la configuración evolutiva y las funciones de evaluación
para el algoritmo genético basado en la Teoría del Peligro.
"""

import random
import numpy as np
from deap import base, creator, tools, algorithms


# Variable global para almacenar los datos del entorno
_df_env = None
_target_date = None


def setup_evolutionary(df_env, target_date):
    """
    Configura el entorno evolutivo con DEAP.

    Parameters
    ----------
    df_env : pd.DataFrame
        DataFrame con los datos preparados
    target_date : pd.Timestamp
        Fecha objetivo de la crisis

    Returns
    -------
    base.Toolbox
        Toolbox configurado para el algoritmo evolutivo
    """
    global _df_env, _target_date
    _df_env = df_env
    _target_date = target_date

    # Limpiar creadores existentes
    if "FitnessMax" in creator.__dict__:
        del creator.FitnessMax
    if "Individual" in creator.__dict__:
        del creator.Individual

    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    toolbox.register("attr_float", random.uniform, -1.0, 1.0)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=5)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("evaluate", eval_danger_theory)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.2, indpb=0.2)
    toolbox.register("select", tools.selTournament, tournsize=3)

    return toolbox


def eval_danger_theory(individual):
    """
    Función de evaluación para un individuo del algoritmo genético.

    Parameters
    ----------
    individual : list
        Lista de 5 pesos (genes) para evaluar

    Returns
    -------
    tuple
        Tupla con el valor de fitness
    """
    global _df_env, _target_date

    w_res, w_price, w_vol, w_int, w_unemp = individual
    threshold = 0.5

    # Señal combinada
    signals = (w_res * _df_env['Gen_Reservas']) + \
              (w_price * _df_env['Gen_Precio']) + \
              (w_vol * _df_env['Gen_Volatilidad']) + \
              (w_int * _df_env['Gen_Intervencion']) + \
              (w_unemp * _df_env['Gen_Desempleo'])

    triggers = signals[signals > threshold]

    if triggers.empty:
        return -100.0,

    exit_idx = triggers.index[0]
    exit_date = _df_env.loc[exit_idx, 'Date']

    # Estrategia de Codicia (Greed)
    if exit_date > _target_date:
        return -50.0,

    days_before = (_target_date - exit_date).days

    if days_before == 0:
        return 20.0,
    elif 1 <= days_before <= 20:
        return 100.0 - (days_before * 1.5),
    elif 21 <= days_before <= 90:
        return 50.0 - (days_before * 0.2),
    else:
        return -20.0,


def run_evolution(toolbox, population_size=150, generations=50, seed=42, verbose=True):
    """
    Ejecuta el algoritmo evolutivo.

    Parameters
    ----------
    toolbox : base.Toolbox
        Toolbox configurado con DEAP
    population_size : int
        Tamaño de la población
    generations : int
        Número de generaciones
    seed : int
        Semilla para reproducibilidad
    verbose : bool
        Si mostrar progreso

    Returns
    -------
    tuple
        (población final, log de estadísticas, hall of fame)
    """
    random.seed(seed)
    pop = toolbox.population(n=population_size)
    hof = tools.HallOfFame(1)

    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("max", np.max)

    if verbose:
        print("Evolucionando con 5 Genes...")

    pop, log = algorithms.eaSimple(
        pop, toolbox,
        cxpb=0.5, mutpb=0.2, ngen=generations,
        stats=stats, halloffame=hof, verbose=verbose
    )

    return pop, log, hof


def calculate_signal(individual, df_env):
    """
    Calcula la señal combinada para un individuo dado.

    Parameters
    ----------
    individual : list
        Lista de 5 pesos
    df_env : pd.DataFrame
        DataFrame con los datos

    Returns
    -------
    pd.Series
        Serie con la señal calculada
    """
    return (individual[0] * df_env['Gen_Reservas']) + \
           (individual[1] * df_env['Gen_Precio']) + \
           (individual[2] * df_env['Gen_Volatilidad']) + \
           (individual[3] * df_env['Gen_Intervencion']) + \
           (individual[4] * df_env['Gen_Desempleo'])
