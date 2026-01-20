"""
Danger Theory - Módulo principal

Este paquete contiene la implementación del algoritmo de Teoría del Peligro
aplicado a la detección de crisis financieras.
"""

from .data_loader import prepare_data_complete, load_default_data
from .danger_theory import setup_evolutionary, eval_danger_theory, run_evolution
from .visualization import plot_results, plot_gene_importance

__all__ = [
    'prepare_data_complete',
    'load_default_data',
    'setup_evolutionary',
    'eval_danger_theory',
    'run_evolution',
    'plot_results',
    'plot_gene_importance'
]
