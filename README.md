# Danger Theory: Detección de Crisis Financieras

Aplicación de la **Teoría del Peligro (Danger Theory)** para detectar crisis cambiarias mediante algoritmos evolutivos inspirados en inmunología biológica.

## Recursos

- **Libro interactivo:** [https://0xjoseangel.github.io/DANGER-THEORY-DT-/](https://0xjoseangel.github.io/DANGER-THEORY-DT-/)
- **Paper académico:** [`Paper/main.pdf`](Paper/main.pdf)

## Instalación rápida

```bash
# Clonar y entrar al repositorio
git clone https://github.com/0xjoseangel/DANGER-THEORY-DT-.git
cd DANGER-THEORY-DT-

# Crear entorno con todas las dependencias
conda env create -f environment.yml

# Activar entorno
conda activate dt
```

> Si ya tienes el entorno y quieres actualizarlo:
> ```bash
> conda env update -f environment.yml --prune
> ```

## Ejecución

```bash
# Ejecutar algoritmo principal
python run.py

# O explorar los notebooks
jupyter lab
```

## Estructura

```
├── run.py              # Script principal
├── src/                # Código fuente (data_loader, danger_theory, visualization)
├── notebooks/          # Jupyter notebooks (01-04)
├── data/               # Datos económicos (Excel)
├── Paper/              # Paper académico (LaTeX + PDF)
└── book/               # Fuentes del libro interactivo
```

## Autores

- **José Ángel Carretero Montes** y **Minerva Cebrián Marín**
- Supervisión: **Dr. José Luis Sáez Lozano** — Universidad de Granada

---

Proyecto de investigación académica. Datos de intervención cortesía del Dr. Alain Naef.
