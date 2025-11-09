# Aplicación de la Teoría del Peligro (Danger Theory) a la Crisis de la Libra de 1992

Este proyecto de investigación explora el uso de modelos computacionales inspirados en la inmunología biológica, específicamente la **Teoría del Peligro (Danger Theory)**, para detectar y explicar retrospectivamente la crisis cambiaria de la libra esterlina en septiembre de 1992 ("Miércoles Negro").

El objetivo principal es determinar si un algoritmo basado en DT, calibrado mediante algoritmos evolutivos, puede identificar señales de "estrés financiero" (danger signals) de forma más eficaz que los indicadores macroeconómicos tradicionales previos al colapso del Mecanismo de Tipos de Cambio (MTC).

## Requisitos Previos

Para ejecutar este proyecto es necesario tener instalado **Anaconda** (o Miniconda) y `git`.

### 🐧 Guía de instalación de Anaconda en Linux

Si aún no tienes Anaconda instalado en tu distribución de Linux, sigue estos pasos rápidos mediante terminal:

1.  **Descargar el instalador:**
    ```bash
    wget [https://repo.anaconda.com/archive/Anaconda3-latest-Linux-x86_64.sh](https://repo.anaconda.com/archive/Anaconda3-latest-Linux-x86_64.sh)
    ```
2.  **Ejecutar el script de instalación:**
    ```bash
    bash Anaconda3-latest-Linux-x86_64.sh
    ```
    *Sigue las instrucciones en pantalla. Escribe 'yes' para aceptar la licencia y confirma la ubicación de instalación por defecto.*
3.  **Inicializar Conda (Importante):**
    Al finalizar, te preguntará si quieres inicializar Anaconda. Responde `yes`. Si te lo saltaste, ejecuta manualmente:
    ```bash
    source ~/anaconda3/bin/activate
    conda init
    ```
4.  **Reiniciar terminal:** Cierra y abre una nueva terminal para que los cambios surtan efecto.

---

## ⚙️ Instalación del Entorno del Proyecto

Para garantizar que todos trabajamos con las mismas versiones de las librerías y evitar conflictos (especialmente en distribuciones como Arch Linux), usaremos un entorno virtual de `conda`.

1.  **Clonar el repositorio:**
    ```bash
    git clone git@github.com:0xjoseangel/DANGER-THEORY-DT-.git
    cd Investigacion_DT_1992
    ```

2.  **Crear y activar el entorno:**
    ```bash
    conda create -n dt_project python
    conda activate dt_project
    ```

3.  **Instalar dependencias:**
    Usamos `conda-forge` para evitar problemas de compatibilidad con sistemas estrictos (como el error `externally-managed-environment`):
    ```bash
    conda install -c conda-forge pandas numpy matplotlib seaborn scikit-learn deap jupyterlab
    ```

---

## 🚀 Uso

Todo el trabajo exploratorio y de modelado se realiza mediante **Jupyter Notebooks** por su facilidad para combinar código, visualizaciones y explicaciones.

1.  **Asegúrate de que el entorno está activo:**
    ```bash
    conda activate dt_project
    ```
    *(Deberías ver `(dt_project)` al inicio de tu línea de comandos).*

2.  **Lanzar Jupyter Lab:**
    ```bash
    jupyter lab
    ```
    Esto abrirá automáticamente una pestaña en tu navegador web donde podrás ver los archivos del proyecto, crear nuevos notebooks (`.ipynb`) y ejecutar el código.

## 📂 Estructura del Repositorio (Tentativa)

* `data/`: Carpeta para almacenar los archivos CSV/Excel con las series temporales económicas (tipos de cambio, interés, reservas).
* `notebooks/`: Jupyter notebooks con los experimentos progresivos (ej. `01_analisis_exploratorio.ipynb`, `02_modelo_dt_basico.ipynb`).
* `src/`: (Opcional) Scripts de Python puro si necesitamos modularizar el algoritmo DT.
* `README.md`: Información general del proyecto.
