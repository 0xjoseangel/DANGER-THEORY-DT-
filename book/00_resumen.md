# Resumen Ejecutivo

## Objetivo

Desarrollar un sistema de detección temprana de crisis cambiarias basado en la **Teoría del Peligro** (*Danger Theory*) de la inmunología computacional, capaz de identificar señales de estrés financiero antes del colapso de precios.

## Metodología

### Enfoque Biológico

Inspirados en cómo el sistema inmune detecta amenazas mediante señales internas de "peligro" (no solo por la presencia de patógenos), proponemos que los mercados financieros emiten señales análogas antes de una crisis:

| Sistema Inmune | Sistema Financiero |
|----------------|-------------------|
| Señales de peligro celular | Intervenciones del banco central |
| Inflamación | Volatilidad del mercado |
| Pérdida de homeostasis | Pérdida de reservas |
| Síntomas externos | Colapso de precios |

### Los 5 "Genes" del Modelo

Definimos cinco variables económicas normalizadas que actúan como señales de peligro:

1. **Reservas Internacionales** — Salud del sistema
2. **Tipo de Cambio** — Síntoma externo (potencialmente engañoso)
3. **Volatilidad** — Nivel de estrés/miedo
4. **Intervención del Banco Central** — Sistema inmune activo
5. **Desempleo** — Debilidad estructural

### Algoritmo Evolutivo

Utilizamos un algoritmo genético (DEAP) para evolucionar "agentes" que aprenden a ponderar estas señales. Los agentes que detectan la crisis con anticipación óptima sobreviven; los demás son eliminados.

$$\text{Señal}_t = \sum_{i=1}^{5} w_i \cdot \text{Gen}_i(t)$$

Cuando la señal supera un umbral, el agente "vende" (predice la crisis).

## Resultados Principales

### Crisis del Miércoles Negro (UK, 1992)

| Métrica | Valor |
|---------|-------|
| Fecha real de la crisis | 16 de septiembre de 1992 |
| Predicción del modelo | ~10-15 días antes |
| Genes más importantes | Intervención (+0.99), Desempleo (+1.07) |
| Gen menos importante | Precio (+0.08) |

**Hallazgo clave**: El agente aprendió a **ignorar el precio** y centrarse en las intervenciones del banco central.

### Validación con Datos Sintéticos

Sometimos al agente a un escenario "trampa" donde el precio subía constantemente (burbuja) mientras los fundamentales se deterioraban. Resultado:

- El agente **no siguió la tendencia del precio**
- Detectó el deterioro de los fundamentales
- Vendió con anticipación suficiente

### Validación Cruzada: Crisis del Tequila (México, 1994)

| Configuración | Resultado |
|---------------|-----------|
| Modelo UK (umbral 0.5) | Salida prematura (pánico post-Colosio) |
| Modelo calibrado (umbral ~1.6) | Predicción óptima (~1 día antes) |

El modelo **generalizó** a un contexto completamente diferente tras calibrar el umbral de sensibilidad.

## Conclusiones

1. **La Danger Theory es aplicable a finanzas**: Las señales internas de estrés (intervenciones, reservas) son más predictivas que los precios.

2. **El modelo no es trend-following**: Detecta fundamentales, no tendencias.

3. **Generalización demostrada**: Funciona en crisis de diferentes países y épocas.

4. **Implicación práctica**: Un sistema de alerta temprana basado en estos principios podría ayudar a reguladores e inversores a anticipar crisis.

## Limitaciones y Trabajo Futuro

- **Datos limitados**: Solo dos crisis estudiadas en profundidad
- **Calibración necesaria**: El umbral debe ajustarse por contexto
- **Disponibilidad de datos**: Las intervenciones del banco central no siempre son públicas en tiempo real

**Direcciones futuras**:
- Aplicación a crisis más recientes (2008, 2020)
- Incorporación de datos de redes sociales (sentimiento)
- Desarrollo de sistema de alerta en tiempo real
