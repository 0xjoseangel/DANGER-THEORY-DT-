# Guía Completa: Acceso a Fuentes de Datos para Modelo Danger Theory
## Crisis Monetaria Reino Unido 1992

---

## 📋 ÍNDICE

1. [Bank of England - Millennium of Data](#1-bank-of-england---millennium-of-data)
2. [Bank of England - Base de Datos Interactiva](#2-bank-of-england---base-de-datos-interactiva)
3. [Dr. Alain Naef - Datos Intervenciones 1992](#3-dr-alain-naef---datos-intervenciones-1992)
4. [OECD - Datos Macroeconómicos](#4-oecd---datos-macroeconómicos)
5. [IMF - International Financial Statistics](#5-imf---international-financial-statistics)
6. [Deutsche Bundesbank](#6-deutsche-bundesbank)
7. [BIS - Bank for International Settlements](#7-bis---bank-for-international-settlements)
8. [FRED - Federal Reserve Economic Data](#8-fred---federal-reserve-economic-data)
9. [Tabla Resumen de Variables](#tabla-resumen-variables-por-fuente)
10. [Plan de Acción Recomendado](#plan-de-acción-recomendado)

---

## 1. BANK OF ENGLAND - MILLENNIUM OF DATA

### 🎯 PRIORIDAD: **MÁXIMA** (Empezar aquí)

### 📥 Descarga Directa

**Archivo Excel completo (28MB):**
```
https://www.bankofengland.co.uk/-/media/boe/files/statistics/research-datasets/a-millennium-of-macroeconomic-data-for-the-uk.xlsx
```

### Métodos de Acceso

#### Opción 1: Descarga Directa (Recomendada)
1. Copiar URL arriba en navegador
2. Descarga automática del Excel
3. Abrir en Excel/LibreOffice

#### Opción 2: Vía Página Oficial
1. Ir a: `https://www.bankofengland.co.uk/statistics/research-datasets`
2. Buscar "A millennium of macroeconomic data"
3. Click en enlace de descarga

#### Opción 3: FRED St. Louis (Serie por Serie)
- **URL**: `https://fred.stlouisfed.org/categories/33839`
- **Ventaja**: Descarga CSV individual por serie
- **Series disponibles**: 133 series temporales

#### Opción 4: Kaggle
- **URL**: `https://www.kaggle.com/bank-of-england/a-millennium-of-macroeconomic-data`
- Requiere cuenta gratuita
- Formato CSV

### 📊 Contenido del Dataset

**Cobertura temporal**: 1086 - 2016 (actualizado a 2016)

**Hojas del Excel organizadas por categoría:**

| Categoría | Contenido 1992 | Frecuencia |
|-----------|----------------|------------|
| **GDP & Cuentas Nacionales** | PIB real/nominal UK | Anual/Trimestral |
| **Inflación y Precios** | IPC, RPI, deflactor GDP | Mensual/Anual |
| **Tipos de Interés** | Bank Rate, Consols, tasas mercado | Diaria/Mensual |
| **Tipos de Cambio** | GBP/USD, índices efectivos | Diaria/Mensual |
| **Sector Bancario** | M0, M1, M2, M3, crédito | Mensual |
| **Balance BoE** | Reservas, operaciones, activos | Mensual |
| **Mercado Laboral** | Empleo, desempleo, salarios | Trimestral |
| **Comercio Exterior** | Importaciones, exportaciones | Trimestral |

### 📧 Contacto para Dudas

**Email**: `ryland.thomas@bankofengland.co.uk`
- **Persona**: Dr. Ryland Thomas
- **Afiliación**: ESCoE / Bank of England
- **Rol**: Curador del dataset junto a Sylaja Srinivasan

---

## 2. BANK OF ENGLAND - BASE DE DATOS INTERACTIVA

### 🎯 PRIORIDAD: **ALTA** (Para datos diarios GBP/USD)

### 🔍 Acceso a la Base de Datos

**URL Principal**: `https://www.bankofengland.co.uk/boeapps/database/`

### Tutorial: Descargar GBP/USD Diario 1992

#### Paso 1: Navegación
1. Ir a la URL principal
2. Click en **"Interest & exchange rates data"**
3. O directamente: **"GBP daily spot rates"**

#### Paso 2: Búsqueda de Serie
**Tres opciones:**
- **Por tópico**: Browse → Exchange Rates → Spot rates → GBP/USD
- **Búsqueda directa**: Escribir "USD GBP spot"
- **Por código**: Series tienen códigos de 7 caracteres (ej: `XUDLUSS` = GBP/USD spot)

#### Paso 3: Selección de Rango
1. En "Selection Summary"
2. **From date**: `01/01/1992`
3. **To date**: `31/12/1992`
4. Click **"View data"**

#### Paso 4: Descarga
1. Click **"Download"**
2. Formatos disponibles:
   - **CSV** (recomendado para Python/R)
   - **Excel**
   - **XML** (incluye metadatos)

### Series Relevantes para tu Modelo

| Serie | Código | Descripción | Frecuencia |
|-------|--------|-------------|------------|
| GBP/USD spot | XUDLUSS | Tipo de cambio spot diario | Diaria desde 1975 |
| GBP/DEM spot | XUDLBK73 | Tipo cambio vs Marco alemán | Diaria |
| Bank Rate | IUQABEDR | Tasa de interés oficial BoE | Diaria |
| Reservas | (Varias) | Reservas internacionales | Mensual |

### ⚠️ Importante

- Cobertura histórica varía por serie (algunas desde 1963)
- Para 1992, principales series GBP/USD están disponibles
- Tipos de cambio **NO son oficiales**, representan mercado de Londres

### 📧 Soporte Técnico

**Email**: `BEEDSQueries@bankofengland.co.uk`

---

## 3. DR. ALAIN NAEF - DATOS INTERVENCIONES 1992

### 🎯 PRIORIDAD: **CRÍTICA** (Clave para "respuesta inmune" del modelo)

### 📚 Sobre el Investigador

- **Nombre**: Dr. Alain Naef
- **Afiliación**: Assistant Professor, ESSEC Business School + Banque de France
- **Especialización**: Historia cambiaria UK, Crisis 1992, Intervenciones FX
- **Google Scholar**: `https://scholar.google.com/citations?user=lBbtYPYAAAAJ`

### 📥 Datasets Disponibles

#### Dataset 1: Intervenciones Diarias BoE 1952-1995

**Harvard Dataverse:**
```
https://doi.org/10.7910/DVN/KHNQG9
```

**Pasos de acceso:**
1. Ir al DOI arriba
2. Click en pestaña "Files" o "Data & Analysis"
3. Ver lista de archivos (.dta, .csv, .xlsx)
4. Click "Download" en archivo deseado
5. **NO requiere registro**

**Contenido:**
- Intervenciones FX diarias del Bank of England
- Período: 1952 - 1995 (incluye 1992 completo)
- Formato: Stata, CSV, Excel

#### Dataset 2: "An Exchange Rate History of UK 1945-1992"

**Harvard Dataverse:**
```
https://doi.org/10.7910/DVN/NXRRBI
```

**Open Science Framework (más fácil):**
```
https://osf.io/mkwtz/
```

**Pasos OSF (recomendado):**
1. Ir a URL OSF
2. Click en carpeta "Files"
3. Explorar archivos disponibles
4. Click derecho → Download
5. **NO requiere cuenta**

#### Dataset 3: Crisis ERM 1992-93 (EL MÁS RELEVANTE)

**OSF/SocArxiv:**
```
https://doi.org/10.17605/OSF.IO/274WD
```

**Alternativa directa:**
```
https://osf.io/274wd/
```

**Pasos:**
1. Ir a cualquiera de las URLs
2. Click en "Files"
3. Descargar archivos de replicación

**Contenido esperado:**
- Intervenciones diarias bancos centrales europeos 1986-1992
- Tipos de cambio ERM
- Variables macroeconómicas crisis 1992
- Archivos de replicación del paper "Imported or Home Grown? The 1992-3 EMS Crisis"

### 📚 Publicación Relacionada

**Paper clave:**
- **Título**: "Imported or Home Grown? The 1992-3 EMS Crisis"
- **Autores**: Barry Eichengreen & Alain Naef
- **Journal**: Journal of International Economics, 2022
- **Datos usados**: Intervenciones diarias + archivos desclasificados BoE

**Libro:**
- **Título**: "An Exchange Rate History of the United Kingdom, 1945–1992"
- **Autor**: Alain Naef
- **Editorial**: Cambridge University Press
- **Datasets**: Todos disponibles en Harvard Dataverse

### ✉️ Template Email para Contactar Dr. Naef

```
Subject: Request for High-Frequency Data on 1992 ERM Crisis

Dear Dr. Naef,

I am [tu nombre], a researcher at [tu institución] developing a danger 
theory model to predict currency crises, with a focus on the 1992 
Black Wednesday event.

I have downloaded your excellent datasets from Harvard Dataverse 
(doi:10.7910/DVN/KHNQG9 and doi:10.17605/OSF.IO/274WD) on Bank of 
England daily interventions and the EMS crisis. These have been 
invaluable for my research.

I am writing to inquire if you might have access to, or know of 
sources for:

1. Intraday (hourly) exchange rate data for GBP/USD and GBP/DEM 
   during 1992
2. Intraday intervention data from Bank of England during 
   September 1992
3. Additional high-frequency market data from the ERM crisis period

My model aims to detect accumulation of systemic stress (analogous 
to "danger signals" in immunology) before currency collapses. 
Higher-frequency data would significantly improve the model's 
predictive capacity.

I understand such data may not exist publicly, but I would greatly 
appreciate any guidance on potential sources or archived materials.

Thank you for your invaluable work. Your book "An Exchange Rate 
History of the United Kingdom" has been a cornerstone reference 
for my research.

Best regards,
[Tu nombre]
[Tu afiliación]
[Tu email]
```

---

## 4. OECD - DATOS MACROECONÓMICOS

### 🎯 PRIORIDAD: **ALTA** (Comparación UK-Alemania)

### 📥 Dallas Fed - Real-Time Historical Dataset

**URL Principal:**
```
https://www.dallasfed.org/research/international/oecd
```

**Características:**
- 26 países OECD
- 13 variables macroeconómicas
- Frecuencia trimestral
- Período: 1957 - 1998

**Variables disponibles (13):**
1. GDP Real
2. GDP Nominal
3. GDP Deflator
4. Industrial Production
5. Manufacturing Production
6. Unemployment Rate
7. Consumer Price Index (CPI)
8. Money Supply
9. Imports
10. Exports
11. Capacity Utilization
12. Capital Formation
13. Net Capital Movements

**Formato de datos:**
- Un archivo Excel por país por variable
- Estructura "vintage": cada columna = fecha de publicación del dato
- Permite análisis real-time (dato como se conocía en cada momento)

### Pasos de Descarga

1. **Acceder a página principal**
   - Ir a URL Dallas Fed arriba

2. **Navegar por país**
   - Buscar "United Kingdom"
   - Buscar "Germany"

3. **Seleccionar variables**
   - Para 1992, seleccionar:
     - CPI (inflación)
     - GDP Real/Nominal
     - Unemployment
     - Imports/Exports

4. **Descargar Excel**
   - Click en variable deseada
   - Descarga automática archivo Excel

5. **Interpretar estructura**
   - **Filas**: Trimestres (1992 Q1, Q2, Q3, Q4)
   - **Columnas**: "Vintages" (fechas de publicación)
   - Para 1992, usar columnas de 1992-1993 para datos "real-time"

### ⚠️ Limitaciones

- Dataset cubre hasta **1998 Q4**
- Para datos post-1999, usar OECD oficial
- Frecuencia **trimestral** (no mensual)

### 📧 Contacto

**Nota**: Dallas Fed indica que no proporcionan soporte técnico al ser proyecto académico no comercial. Alternativa: contactar biblioteca universitaria.

### 🌐 OECD Official Data Portal (Complementario)

**Para datos adicionales o post-1999:**

**OECD.Stat:**
```
https://stats.oecd.org/
```

**Pasos:**
1. Click "Data Explorer"
2. Seleccionar "Main Economic Indicators"
3. Filtrar:
   - **Country**: United Kingdom, Germany
   - **Indicator**: CPI, Interest Rates, GDP, etc.
   - **Time**: 1992
   - **Frequency**: Monthly/Quarterly
4. Click "Export" → CSV o Excel

**OECD Data Portal General:**
```
https://www.oecd.org/en/data.html
```

---

## 5. IMF - INTERNATIONAL FINANCIAL STATISTICS

### 🎯 PRIORIDAD: **ALTA** (Reservas, Balance de Pagos)

### 🌐 Acceso Nuevo IMF Data Portal

**URL Principal:**
```
https://data.imf.org/
```

**Nota importante**: Desde agosto 2025, el antiguo sistema en `legacydata.imf.org` ya no se actualiza.

### 📊 IFS - Datos Ahora Integrados por Tópicos

International Financial Statistics (IFS) ahora está organizado por temas, accesible vía datasets existentes en el portal.

**Cobertura:**
- ~200 países y áreas
- ~32,000 series temporales
- Datos desde 1948
- Actualización mensual

### Categorías Relevantes para tu Modelo 1992

| Categoría | Variables UK/Germany 1992 |
|-----------|---------------------------|
| **Exchange Rates** | GBP/USD, DEM/USD, tipos cruzados |
| **Balance of Payments** | Cuenta corriente, balanza comercial |
| **International Liquidity** | **Reservas internacionales** (CRÍTICO) |
| **Money & Banking** | Agregados monetarios, crédito |
| **Interest Rates** | Tasas interbancarias, bonos |
| **Prices** | IPC, deflactores |
| **Government Accounts** | Finanzas públicas, deuda |
| **National Accounts** | PIB, componentes del gasto |

### Pasos de Acceso

#### Método 1: Portal Principal

1. **Ir a**: `https://data.imf.org/`

2. **Buscar "International Financial Statistics"**
   - O navegar: Data Resources → IFS

3. **Filtrar por país**
   - Seleccionar: United Kingdom
   - Seleccionar: Germany

4. **Seleccionar indicadores**
   - Ejemplo: "International Reserves"
   - Ejemplo: "Balance of Payments - Current Account"

5. **Definir período**
   - Start: January 1992
   - End: December 1992

6. **Descargar**
   - Formato: Excel, CSV
   - Opción: Incluir metadatos

#### Método 2: Por Tópico Específico

**Reservas Internacionales (CRÍTICO para tu modelo):**

Navigate to:
```
Data Portal → Currency Composition of Official Foreign Exchange 
Reserves (COFER)
```

**O buscar directamente:**
- "International Liquidity"
- Filter: United Kingdom, 1992
- Series: Total Reserves minus Gold

### API Access (Para automatización)

**Documentación API:**
```
https://data.imf.org/ → API Resources
```

**Ejemplo filtro IFS:**
- Parameter: `c[IFS_Flag]=True`
- Permite obtener solo datos IFS

### 📧 Contacto

**Email**: `datahelp@imf.org`

**Uso académico UK:**
- URL: `https://discover.ukdataservice.ac.uk/doi/imfifs`
- Acceso gratuito para universidades UK
- DOIs citables por edición mensual

---

## 6. DEUTSCHE BUNDESBANK

### 🎯 PRIORIDAD: **MEDIA** (Datos Alemania comparativos)

### 🌐 Time Series Databases

**URL Principal:**
```
https://www.bundesbank.de/en/statistics/time-series-databases
```

### Datos Relevantes 1992

| Categoría | Series Disponibles |
|-----------|-------------------|
| **Tipos de Interés** | Tasa de referencia Bundesbank, interbancarias |
| **Inflación** | IPC Alemania mensual |
| **Tipo de Cambio** | DEM/USD, DEM/GBP |
| **Balanza de Pagos** | Cuenta corriente, comercio |
| **Reservas** | Reservas internacionales Bundesbank |

### Pasos de Acceso

1. Ir a URL principal
2. Buscar "Historical data" o "Statistics"
3. Navegar por categoría de interés
4. Seleccionar período: 1992
5. Descargar CSV o Excel

### Contacto

**Página de estadísticas:**
```
https://www.bundesbank.de/en/statistics
```

---

## 7. BIS - BANK FOR INTERNATIONAL SETTLEMENTS

### 🎯 PRIORIDAD: **MEDIA** (Contexto internacional)

### 🌐 BIS Data Portal

**URL:**
```
https://data.bis.org
```

### Datos Relevantes

- Tipos de cambio efectivos
- Actividad bancaria internacional
- Balances bancos centrales
- Flujos de capital transfronterizos

### 📧 Contacto

**Email**: `statistics@bis.org`

**Historical Timeline:**
```
https://www.bis.org/about/chronology.htm
```
- Eventos clave 1992 documentados

---

## 8. FRED - FEDERAL RESERVE ECONOMIC DATA

### 🎯 PRIORIDAD: **MEDIA-ALTA** (Fácil acceso, múltiples fuentes)

### 🌐 FRED Database

**URL:**
```
https://fred.stlouisfed.org/
```

### Series Relevantes 1992

**Tipo de Cambio:**
- **DEXUSUK**: US Dollars to British Pound (diario)
- Disponible desde 1971

**Datos UK vía FRED:**
- GDP UK
- Inflation UK
- Interest Rates UK

**Datos Germany:**
- Variables macro Alemania

### Ventajas FRED

✅ Interfaz muy amigable
✅ Descarga directa CSV
✅ Gráficos interactivos
✅ API gratuita disponible
✅ Integra datos de múltiples fuentes (incluido BoE, OECD, IMF)

### Pasos de Uso

1. Ir a `https://fred.stlouisfed.org/`
2. Buscar: "GBP USD exchange rate"
3. Seleccionar serie DEXUSUK
4. Definir rango: 01/01/1992 - 31/12/1992
5. Click "Download" → CSV

---

## TABLA RESUMEN: VARIABLES POR FUENTE

| Variable / Señal Peligro | Fuente Principal | Fuente Alternativa | Frecuencia |
|---------------------------|------------------|-------------------|------------|
| **Tipo cambio GBP/USD diario** | BoE Database | FRED (DEXUSUK) | Diaria |
| **Tipo cambio GBP/DEM diario** | BoE Database | Bundesbank | Diaria |
| **Intervenciones FX BoE** | Naef Harvard Dataverse | - | Diaria |
| **Reservas BoE** | Naef + IMF IFS | BoE Millennium | Mensual |
| **Inflación UK** | BoE Millennium | OECD Dallas Fed | Mensual |
| **Inflación Alemania** | OECD Dallas Fed | Bundesbank | Mensual |
| **Tipos interés BoE** | BoE Database | BoE Millennium | Diaria |
| **Tipos interés Bundesbank** | Bundesbank | BIS | Diaria |
| **GDP UK** | BoE Millennium | OECD | Trimestral |
| **GDP Alemania** | OECD Dallas Fed | IMF | Trimestral |
| **Cuenta corriente UK** | IMF IFS | OECD | Trimestral |
| **Desempleo UK** | BoE Millennium | OECD | Mensual |
| **Oferta monetaria UK** | BoE Database | IMF | Mensual |
| **Balance comercial UK** | IMF IFS | OECD | Mensual |
| **Deuda/PIB UK** | IMF | OECD | Anual |

---

## PLAN DE ACCIÓN RECOMENDADO

### Fase 1: Datos Esenciales (Semana 1)

**Prioridad MÁXIMA:**

1. ✅ **Descargar BoE Millennium of Data**
   - URL directa Excel
   - Extraer: inflación, tipos interés, GDP, tipo cambio

2. ✅ **Contactar Dr. Alain Naef**
   - Usar template email proporcionado
   - Solicitar datasets Harvard Dataverse
   - Preguntar por datos intradía

3. ✅ **Descargar intervenciones diarias 1992**
   - Dataset Naef OSF: `https://osf.io/274wd/`
   - Crítico para "respuesta inmune"

4. ✅ **Obtener GBP/USD diario**
   - BoE Database: seguir tutorial paso a paso
   - Alternativa: FRED serie DEXUSUK

### Fase 2: Datos Complementarios (Semana 2)

5. ⬜ **OECD Dallas Fed dataset**
   - Descargar UK: CPI, GDP, Unemployment
   - Descargar Germany: CPI, GDP
   - Para análisis comparativo UK-Alemania

6. ⬜ **IMF IFS - Reservas**
   - International Liquidity → Total Reserves
   - UK y contexto europeo
   - Mensual 1990-1993

7. ⬜ **Bundesbank datos Alemania**
   - Tipos de interés 1992
   - Inflación
   - Para comparación divergencia macro

### Fase 3: Variables Derivadas (Semana 3)

8. ⬜ **Calcular indicadores propios:**
   - Volatilidad GBP/USD (rolling window)
   - Spread bid-ask (estimado de datos diarios)
   - Divergencia inflacionaria UK-Germany
   - Ratio intervenciones/reservas
   - Efectividad intervenciones (£ gastadas por bp ganado)

9. ⬜ **Compilar eventos políticos:**
   - Cronología BIS
   - Papers Dr. Naef
   - Declaraciones Bundesbank (buscar en archivos históricos)

### Fase 4: Integración (Semana 4)

10. ⬜ **Consolidar base de datos unificada**
    - Frecuencia común: diaria (interpolar mensual si necesario)
    - Alinear calendarios
    - Manejar datos faltantes
    - Crear variables lag

11. ⬜ **Validación cruzada**
    - Verificar consistencia entre fuentes
    - Documentar discrepancias
    - Identificar gaps

---

## NOTAS FINALES

### Sobre Datos Intradía

Como discutimos, **datos intradía (horas/minutos) para 1992 NO existen públicamente**. Opciones:

1. **Enfocarte en datos diarios** (suficiente para danger theory)
2. **Contactar Dr. Naef** (podría tener archivos adicionales BoE)
3. **Buscar archivos desclasificados BoE** (requiere investigación archivística)

### Licencias y Citas

- **BoE Millennium**: Citar trabajos originales, libre uso académico
- **Naef Datasets**: Citar papers asociados (DOIs en Harvard Dataverse)
- **OECD Dallas Fed**: Citar working paper No. 96
- **IMF**: Libre uso, citar fuente

### Recomendación Final

**Empieza con:**
1. BoE Millennium (datos macro UK completos)
2. Datasets Naef (intervenciones - ÚNICO)
3. BoE Database (GBP/USD diario)

Estas 3 fuentes te darán **80% de lo que necesitas**. El resto es complementario.

---

## CONTACTOS RÁPIDOS

| Institución | Email | Propósito |
|-------------|-------|-----------|
| **Dr. Alain Naef** | Via Google Scholar | Datos intervenciones, consultas 1992 |
| **BoE Historical Data** | ryland.thomas@bankofengland.co.uk | Dudas Millennium dataset |
| **BoE Database Queries** | BEEDSQueries@bankofengland.co.uk | Problemas técnicos descarga |
| **IMF Data Help** | datahelp@imf.org | Acceso IFS, dudas datos |
| **BIS Statistics** | statistics@bis.org | Datos BIS |

---

**Última actualización**: Noviembre 2025
**Autor de la guía**: Asistente de investigación
**Para**: Modelo Danger Theory - Crisis 1992