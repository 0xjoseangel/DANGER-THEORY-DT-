"""
Módulo de carga y preparación de datos.

Contiene funciones para cargar los datos económicos desde archivos Excel
y prepararlos para el algoritmo de Danger Theory.
"""

import pandas as pd
import numpy as np


def prepare_data_complete(file_rates, file_reserves, file_naef, file_unemp):
    """
    Carga y prepara los datos completos con 5 genes.

    Parameters
    ----------
    file_rates : str
        Ruta al archivo de tipos de cambio
    file_reserves : str
        Ruta al archivo de reservas
    file_naef : str
        Ruta al archivo de intervenciones del Bank of England
    file_unemp : str
        Ruta al archivo de desempleo

    Returns
    -------
    pd.DataFrame
        DataFrame con los datos procesados y los 5 genes normalizados
    """

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

    # --- D. CARGAR DESEMPLEO ---
    unemp = pd.read_excel(file_unemp)
    unemp = unemp.iloc[:, 0:2]
    unemp.columns = ['DateStr', 'Unemployment']
    unemp['Date'] = pd.to_datetime(unemp['DateStr'], format='%Y %b', errors='coerce')
    unemp = unemp.dropna(subset=['Date'])
    unemp = unemp.sort_values('Date')

    # --- E. FUSIÓN MAESTRA ---
    df = pd.merge(rates, reserves, on='Date', how='left')
    df = pd.merge(df, naef, on='Date', how='left')
    df = pd.merge(df, unemp[['Date', 'Unemployment']], on='Date', how='left')

    df = df.sort_values('Date')

    # --- F. RELLENOS ---
    df['Total Reserves'] = df['Total Reserves'].ffill()
    df['Unemployment'] = df['Unemployment'].ffill()
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

    # GEN 5: DESEMPLEO
    df['Gen_Desempleo'] = (df['Unemployment'] - df['Unemployment'].mean()) / df['Unemployment'].std()

    return df


def load_default_data(data_path='data'):
    """
    Carga los datos usando las rutas por defecto.

    Parameters
    ----------
    data_path : str
        Ruta base a la carpeta de datos

    Returns
    -------
    pd.DataFrame
        DataFrame con los datos procesados
    """
    path_rates = f'{data_path}/tipoDeCambioEuropa.xlsx'
    path_reserves = f'{data_path}/ReservesData.xlsx'
    path_naef = f'{data_path}/Bank of England daily FX interventions, 1952-1995.xlsx'
    path_unemp = f'{data_path}/Unemployement.xlsx'

    return prepare_data_complete(path_rates, path_reserves, path_naef, path_unemp)
