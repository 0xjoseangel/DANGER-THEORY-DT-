# Danger Theory: Detección de Crisis Financieras

Aplicación de la **Teoría del Peligro (Danger Theory)** para detectar la crisis cambiaria de la Libra Esterlina de septiembre de 1992 ("Miércoles Negro").

Este proyecto utiliza algoritmos evolutivos inspirados en inmunología biológica para identificar "señales de peligro" en datos económicos antes del colapso del Mecanismo Europeo de Tipos de Cambio (MTC).

---

## Tabla de Contenidos

1. [Requisitos del Sistema](#requisitos-del-sistema)
2. [Instalación Paso a Paso](#instalación-paso-a-paso)
3. [Ejecución del Proyecto](#ejecución-del-proyecto)
4. [Estructura del Proyecto](#estructura-del-proyecto)
5. [Descripción de los Módulos](#descripción-de-los-módulos)
6. [Los 5 Genes del Algoritmo](#los-5-genes-del-algoritmo)
7. [Notebooks Disponibles](#notebooks-disponibles)

---

## Requisitos del Sistema

- **Sistema Operativo:** Linux, macOS o Windows
- **Python:** 3.10 o superior
- **Gestor de entornos:** Anaconda o Miniconda
- **Git:** Para clonar el repositorio

---

## Instalación Paso a Paso

### 1. Instalar Anaconda (si no lo tienes)

#### Linux

```bash
# Descargar el instalador
wget https://repo.anaconda.com/archive/Anaconda3-latest-Linux-x86_64.sh

# Ejecutar el instalador
bash Anaconda3-latest-Linux-x86_64.sh
```

Sigue las instrucciones en pantalla:
- Escribe `yes` para aceptar la licencia
- Confirma la ubicación de instalación (pulsa Enter para usar la predeterminada)
- Cuando pregunte si quieres inicializar Anaconda, responde `yes`

```bash
# Reinicia la terminal o ejecuta:
source ~/.bashrc
```

#### macOS

```bash
# Descargar el instalador
curl -O https://repo.anaconda.com/archive/Anaconda3-latest-MacOSX-x86_64.sh

# Ejecutar el instalador
bash Anaconda3-latest-MacOSX-x86_64.sh
```

#### Windows

1. Descarga el instalador desde: https://www.anaconda.com/download
2. Ejecuta el `.exe` y sigue el asistente de instalación
3. Marca la opción "Add Anaconda to PATH" durante la instalación

### 2. Clonar el Repositorio

```bash
git clone https://github.com/TU_USUARIO/DANGER-THEORY-DT-.git
cd DANGER-THEORY-DT-
```

### 3. Crear el Entorno Virtual

```bash
# Crear un entorno llamado 'dt' con Python
conda create -n dt python=3.11 -y

# Activar el entorno
conda activate dt
```

**Nota:** Verás `(dt)` al inicio de tu línea de comandos cuando el entorno esté activo.

### 4. Instalar las Dependencias

```bash
# Instalar todas las librerías necesarias
conda install -c conda-forge pandas numpy matplotlib seaborn scikit-learn deap jupyterlab openpyxl scipy statsmodels -y
```

**Librerías instaladas:**

| Librería | Uso |
|----------|-----|
| `pandas` | Manipulación de datos |
| `numpy` | Cálculos numéricos |
| `matplotlib` | Visualización de gráficos |
| `seaborn` | Gráficos estadísticos |
| `scikit-learn` | Machine Learning |
| `deap` | Algoritmos evolutivos |
| `jupyterlab` | Entorno de notebooks |
| `openpyxl` | Lectura de archivos Excel |
| `scipy` | Funciones científicas |
| `statsmodels` | Modelos estadísticos |

### 5. Verificar la Instalación

```bash
# Comprobar que Python funciona
python --version

# Comprobar que las librerías están instaladas
python -c "import pandas; import deap; print('Instalación correcta')"
```

---

## Ejecución del Proyecto

### Opción 1: Ejecutar el Script Principal (`run.py`)

El archivo `run.py` ejecuta el algoritmo completo de Danger Theory:

```bash
# Asegúrate de estar en el directorio del proyecto
cd DANGER-THEORY-DT-

# Activa el entorno (si no está activo)
conda activate dt

# Ejecuta el algoritmo
python run.py
```

**¿Qué hace `run.py`?**

1. **Carga los datos** económicos desde los archivos Excel en `data/`
2. **Prepara los 5 genes** (variables normalizadas): Reservas, Precio, Volatilidad, Intervención, Desempleo
3. **Ejecuta el algoritmo evolutivo** con 150 agentes durante 50 generaciones
4. **Muestra los resultados**: el mejor agente encontrado y sus pesos
5. **Genera gráficos** mostrando:
   - El punto de salida predicho vs. la crisis real
   - La importancia de cada gen (peso asignado)

### Opción 2: Usar los Jupyter Notebooks

Los notebooks contienen análisis detallados con explicaciones paso a paso:

```bash
# Activa el entorno
conda activate dt

# Inicia Jupyter Lab
jupyter lab
```

Se abrirá una ventana en tu navegador. Navega a la carpeta `notebooks/` y abre el notebook deseado.

### Opción 3: Ejecutar el Script Legacy (`algo.py`)

Para compatibilidad con versiones anteriores:

```bash
python algo.py
```

Hace lo mismo que `run.py` pero con el formato original del código.

### Opción 4: Importar como Módulo en tu Propio Código

```python
from src.data_loader import load_default_data
from src.danger_theory import setup_evolutionary, run_evolution
from src.visualization import plot_results
import pandas as pd

# Cargar datos
df = load_default_data()
target_date = pd.to_datetime('1992-09-16')

# Configurar y ejecutar el algoritmo
toolbox = setup_evolutionary(df, target_date)
pop, log, hof = run_evolution(toolbox, population_size=150, generations=50)

# El mejor agente está en hof[0]
best = hof[0]
print("Mejor agente:", best)
```

---

## Estructura del Proyecto

```
DANGER-THEORY-DT-/
│
├── run.py                    # Punto de entrada principal
├── algo.py                   # Script legacy (compatibilidad)
├── README.md                 # Este archivo
├── environment.yml           # Especificación del entorno Conda
├── requirements.txt          # Dependencias Python (alternativo a Conda)
├── .gitignore                # Archivos ignorados por Git
│
├── src/                      # CÓDIGO FUENTE MODULARIZADO
│   ├── __init__.py           # Inicializador del paquete
│   ├── data_loader.py        # Funciones de carga y preparación de datos
│   ├── danger_theory.py      # Algoritmo evolutivo y función de evaluación
│   └── visualization.py      # Funciones para generar gráficos
│
├── notebooks/                # JUPYTER NOTEBOOKS (seguir en orden)
│   ├── 01_contexto_crisis_1992.ipynb    # Contexto histórico
│   ├── 02_desarrollo_algoritmo.ipynb    # Desarrollo del algoritmo
│   ├── 03_validacion_robustez.ipynb     # Test con datos sintéticos
│   └── 04_validacion_crisis_mexico.ipynb # Validación en México 1994
│
├── data/                     # DATOS ECONÓMICOS (archivos Excel)
│   ├── tipoDeCambioEuropa.xlsx
│   ├── ReservesData.xlsx
│   ├── Bank of England daily FX interventions, 1952-1995.xlsx
│   ├── Unemployement.xlsx
│   ├── ExchangeRateData.xlsx
│   └── ... (datos de México para validación)
│
├── docs/                     # DOCUMENTACIÓN
│   ├── Fuente Datos Crisis Libra 1992.md
│   ├── Fuente Datos Crisis Libra 1992.pdf
│   └── PROMT E INFORME.docx
│
└── archivos_AlainNaef/       # DOCUMENTACIÓN HISTÓRICA
    └── archives/             # Documentos originales de investigación
```

---

## Descripción de los Módulos

### `src/data_loader.py`

Contiene las funciones para cargar y preparar los datos económicos:

- **`prepare_data_complete()`**: Carga los 4 archivos Excel, los fusiona por fecha y calcula los 5 genes normalizados.
- **`load_default_data()`**: Wrapper que carga los datos usando las rutas por defecto.

### `src/danger_theory.py`

Implementa el algoritmo evolutivo basado en DEAP:

- **`setup_evolutionary()`**: Configura el entorno evolutivo (población, operadores genéticos).
- **`eval_danger_theory()`**: Función de fitness que evalúa cada agente.
- **`run_evolution()`**: Ejecuta el algoritmo genético durante N generaciones.
- **`calculate_signal()`**: Calcula la señal de peligro para un agente dado.

### `src/visualization.py`

Funciones para visualizar los resultados:

- **`plot_results()`**: Genera el gráfico completo (precio + punto de salida + importancia de genes).
- **`plot_gene_importance()`**: Gráfico de barras con los pesos de cada gen.
- **`print_results()`**: Imprime los pesos del mejor agente en consola.

### `run.py`

Script principal que orquesta todo el proceso:

1. Importa los módulos de `src/`
2. Carga los datos con `load_default_data()`
3. Configura el algoritmo con `setup_evolutionary()`
4. Ejecuta la evolución con `run_evolution()`
5. Muestra resultados con `print_results()` y `plot_results()`

---

## Los 5 Genes del Algoritmo

El algoritmo utiliza 5 variables económicas, cada una normalizada usando Z-Score para hacerlas comparables:

| Gen | Variable | Significado | Fuente |
|-----|----------|-------------|--------|
| 1 | **Reservas** | Reservas internacionales del Bank of England | IMF International Financial Statistics |
| 2 | **Precio** | Tipo de cambio GBP/DEM | Bank of England Database |
| 3 | **Volatilidad** | Desviación estándar del precio (ventana 30 días) | Calculado |
| 4 | **Intervención** | Intervenciones del Banco Central en el mercado FX | Dr. Alain Naef |
| 5 | **Desempleo** | Tasa de desempleo del Reino Unido | Datos históricos UK |

### ¿Cómo funciona?

Cada agente tiene 5 pesos (uno por gen). La señal de peligro se calcula como:

```
Señal = w₁·Reservas + w₂·Precio + w₃·Volatilidad + w₄·Intervención + w₅·Desempleo
```

Cuando la señal supera un umbral (0.5), el agente "vende" (predice la crisis).

El algoritmo evolutivo busca los pesos óptimos que permitan detectar la crisis con la mayor anticipación posible sin ser demasiado temprano.

---

## Notebooks Disponibles

Los notebooks siguen una **narrativa didáctica progresiva**. Se recomienda seguirlos en orden:

| # | Notebook | Descripción |
|---|----------|-------------|
| 1 | `01_contexto_crisis_1992.ipynb` | **Contexto histórico**: El MEC, el Miércoles Negro, análisis de tipos de cambio y reservas, la "Gran Divergencia" |
| 2 | `02_desarrollo_algoritmo.ipynb` | **Desarrollo del algoritmo**: Danger Theory, ETL, normalización Z-Score, DEAP, función de fitness, resultados |
| 3 | `03_validacion_robustez.ipynb` | **Test de robustez**: Escenario sintético "trampa del precio" para verificar que el modelo no es trend-following |
| 4 | `04_validacion_crisis_mexico.ipynb` | **Validación cruzada**: Aplicación a la Crisis del Tequila (México 1994), calibración de umbral, agente nativo |

### Flujo Recomendado

```
01_contexto_crisis_1992 → 02_desarrollo_algoritmo → 03_validacion_robustez → 04_validacion_crisis_mexico
        ↓                         ↓                         ↓                         ↓
   Entender el              Construir el              Verificar                 Generalizar a
    problema                 algoritmo                robustez                 otros contextos
```

---

## Generación del Libro PDF

El proyecto incluye la configuración para generar un **libro profesional en PDF** usando Jupyter Book.

### Estructura del Libro

```
book/
├── _config.yml          # Configuración del libro
├── _toc.yml             # Tabla de contenidos
├── intro.md             # Portada e introducción
├── 00_resumen.md        # Resumen ejecutivo
├── 01_contexto_*.ipynb  # → Capítulo 1 (enlace simbólico)
├── 02_desarrollo_*.ipynb # → Capítulo 2 (enlace simbólico)
├── 03_validacion_*.ipynb # → Capítulo 3 (enlace simbólico)
├── 04_validacion_*.ipynb # → Capítulo 4 (enlace simbólico)
├── 05_conclusiones.md   # Conclusiones
├── 06_referencias.md    # Bibliografía
└── references.bib       # Referencias BibTeX
```

### Instalación de Dependencias

```bash
# Activar el entorno
conda activate dt

# Instalar Jupyter Book
pip install jupyter-book

# Para generar PDF, también necesitas LaTeX:
# Ubuntu/Debian:
sudo apt-get install texlive-latex-extra texlive-fonts-recommended texlive-lang-spanish latexmk

# Arch Linux:
sudo pacman -S texlive-most texlive-langspanish

# macOS (con Homebrew):
brew install --cask mactex
```

### Generar el Libro

```bash
# Generar versión HTML (rápido, para previsualizar)
jupyter-book build book/

# Ver el resultado en el navegador
# Abrir: book/_build/html/index.html

# Generar versión PDF (requiere LaTeX)
jupyter-book build book/ --builder pdflatex

# El PDF estará en: book/_build/latex/danger_theory.pdf
```

### Alternativa: Generar PDF sin LaTeX

Si no tienes LaTeX instalado, puedes usar `pyppeteer`:

```bash
pip install pyppeteer
jupyter-book build book/ --builder pdfhtml
```

---

## Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'deap'"

```bash
conda activate dt
conda install -c conda-forge deap -y
```

### Error: "externally-managed-environment"

Este error ocurre en algunas distribuciones Linux. Solución: usar Conda en lugar de pip.

### Los notebooks no encuentran los datos

Asegúrate de ejecutar Jupyter desde el directorio raíz del proyecto:

```bash
cd DANGER-THEORY-DT-
jupyter lab
```

### El gráfico no se muestra

Si usas un entorno sin interfaz gráfica, añade al inicio del script:

```python
import matplotlib
matplotlib.use('Agg')  # Backend sin GUI
```

---

## Autores

Este proyecto ha sido realizado por:

- **José Ángel Carretero Montes**
- **Minerva Cebrián Marín**

Con la supervisión de:

- **Dr. José Luis Sáez Lozano** — Universidad de Granada

---

## Licencia

Proyecto de investigación académica. Datos de intervención cortesía del Dr. Alain Naef.
