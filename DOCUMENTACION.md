# 📚 Documentación Técnica — Análisis Financiero con Python & Streamlit

> **Proyecto:** Análisis de Precios de Acciones con Python, Plotly y Streamlit  
> **Institución:** Universidad Francisco de Paula Santander Ocaña (UFHEC) — Semillero de Datos  
> **Autor:** Feibert  
> **Versión:** 1.0.0  
> **Fecha:** Septiembre 2026

---

## 📋 Tabla de Contenidos

1. [Introducción y Contexto](#1-introducción-y-contexto)
2. [Descripción del Problema](#2-descripción-del-problema)
3. [Objetivos SMART](#3-objetivos-smart)
4. [Arquitectura del Proyecto](#4-arquitectura-del-proyecto)
5. [Dataset: precios_acciones.csv](#5-dataset-precios_accionescsv)
6. [Notebook: DataPython.ipynb](#6-notebook-datapythonipynb)
7. [Visualizaciones HTML](#7-visualizaciones-html)
8. [Aplicación Streamlit (app.py)](#8-aplicación-streamlit-apppy)
9. [Guía de Instalación Paso a Paso](#9-guía-de-instalación-paso-a-paso)
10. [Despliegue en Streamlit Cloud](#10-despliegue-en-streamlit-cloud)
11. [Integración con GitHub](#11-integración-con-github)
12. [Stack Tecnológico](#12-stack-tecnológico)
13. [Métricas y Resultados](#13-métricas-y-resultados)
14. [Preguntas Frecuentes](#14-preguntas-frecuentes)

---

## 1. Introducción y Contexto

Este proyecto nace dentro del **Semillero de Datos y Tecnología** de la UFHEC como ejercicio práctico integrador de ciencia de datos aplicada al sector financiero.

### ¿Qué se construyó?

Una solución completa de análisis de datos que incluye:

- **Descarga y procesamiento** de datos financieros históricos con `yfinance` y `pandas`
- **Visualizaciones interactivas** con `Plotly Express` y `Plotly Graph Objects`
- **Simulación de inversión** basada en datos reales de mercado
- **Informe automático** generado por Google Gemini AI
- **Aplicación web** desplegada en la nube con Streamlit

### Empresas Analizadas

| Ticker | Empresa | Sector |
|--------|---------|--------|
| AAPL | Apple Inc. | Tecnología del Consumidor |
| MSFT | Microsoft Corporation | Software / Cloud |
| NVDA | Nvidia Corporation | Semiconductores / IA |

---

## 2. Descripción del Problema

En el contexto financiero actual, los inversores particulares y corporativos necesitan herramientas accesibles que les permitan:

1. **Analizar** el comportamiento histórico de activos financieros
2. **Visualizar** tendencias de manera interactiva y comprensible
3. **Simular** escenarios de inversión basados en datos reales
4. **Comparar** el rendimiento entre diferentes activos

La barrera de entrada al análisis financiero profesional ha sido históricamente alta, requiriendo acceso a plataformas costosas como Bloomberg Terminal o Reuters Eikon.

> **¿Cómo podemos usar Python y la IA para democratizar el acceso al análisis financiero?**

Este proyecto demuestra que con herramientas open-source de Python es posible construir análisis de calidad profesional de forma gratuita y accesible.

---

## 3. Objetivos SMART

### S — Específico (Specific)
Analizar los precios de cierre históricos de **AAPL, MSFT y NVDA** durante el período **septiembre 2025 – septiembre 2026**, utilizando Python, Pandas y Plotly, consumiendo datos desde el archivo `precios_acciones.csv`.

### M — Medible (Measurable)
- Generar exactamente **3 visualizaciones interactivas**:
  - Cotización histórica (líneas temporales)
  - Simulación de inversión de $1,000 USD
  - Precio promedio comparativo (barras)
- Calcular métricas estadísticas: media, mediana, desviación estándar, mín/máx
- Correlación entre las tres acciones

### A — Alcanzable (Achievable)
- Construir una app funcional con Streamlit (framework conocido por el equipo)
- Consumir el CSV local `precios_acciones.csv` sin dependencias externas de red
- Desplegar en Streamlit Cloud (plataforma gratuita)
- Alojar código en repositorio GitHub público

### R — Relevante (Relevant)
- Aplica competencias del semillero: Python, pandas, plotly, análisis de datos
- Resuelve una necesidad real: democratización del análisis financiero
- Integra tecnologías actuales: IA Generativa, web apps, cloud

### T — Temporal (Time-bound)
- Período de análisis: **252 días hábiles** (Sep 2025 – Sep 2026)
- Entregable completado: **Segundo semestre académico 2026**

---

## 4. Arquitectura del Proyecto

```
┌─────────────────────────────────────────────────────────┐
│                    ENTRADA DE DATOS                      │
│                                                          │
│  precios_acciones.csv  ←→  DataPython.ipynb (Colab)     │
│        │                          │                      │
│        │ pandas.read_csv()        │ yfinance.download()  │
│        ▼                          ▼                      │
│  DataFrame: Date, AAPL, MSFT, NVDA (252 filas)          │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                 PROCESAMIENTO                            │
│                                                          │
│  • Filtrado por fecha y ticker                           │
│  • Cálculo de inversión normalizada                      │
│  • Estadísticas descriptivas (describe)                  │
│  • Matriz de correlación                                 │
│  • Precio promedio (mean)                                │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                 VISUALIZACIONES                          │
│                                                          │
│  Plotly Express & Graph Objects (template: plotly_dark)  │
│                                                          │
│  📉 cotizacion_historica.html  →  px.line()             │
│  💰 inversion.html             →  px.line() + hline     │
│  📊 precio_promedio.html       →  px.bar()              │
│  📦 Box plots                  →  px.box()              │
│  🔗 Heatmap correlación        →  go.Heatmap()          │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│              APLICACIÓN STREAMLIT (app.py)               │
│                                                          │
│  ┌─────────┐ ┌────────────┐ ┌──────────────────────┐   │
│  │ Landing │ │ Dashboard  │ │ Documentación        │   │
│  │ Page    │ │ Análisis   │ │ Técnica              │   │
│  └─────────┘ └────────────┘ └──────────────────────┘   │
│                                                          │
│  Sidebar: Filtros de fecha, tickers, capital             │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                  DESPLIEGUE                              │
│                                                          │
│  GitHub Repository → Streamlit Cloud                     │
│  (Conexión directa, auto-deploy en cada push)            │
└─────────────────────────────────────────────────────────┘
```

---

## 5. Dataset: precios_acciones.csv

### Descripción

El archivo `precios_acciones.csv` contiene **252 registros** de precios de cierre ajustados descargados desde Yahoo Finance usando la librería `yfinance`.

### Estructura del archivo

```csv
Date,AAPL,MSFT,NVDA
2025-09-19,244.596,513.703,176.247
2025-09-22,255.137,510.251,183.171
...
2026-09-18,336.130,493.779,222.270
```

### Estadísticas del Dataset

| Estadística | AAPL | MSFT | NVDA |
|-------------|------|------|------|
| **Mínimo** | ~$207 | ~$413 | ~$110 |
| **Máximo** | ~$337 | ~$538 | ~$262 |
| **Promedio** | ~$281 | ~$446 | ~$196 |
| **Registros** | 252 | 252 | 252 |

### Cómo se generó

```python
import yfinance as yf
import pandas as pd

tickers = ["AAPL", "NVDA", "MSFT"]
datos = yf.download(tickers, period="1y")
precios = datos["Close"]
precios.to_csv("precios_acciones.csv")
```

### Cómo se consume en app.py

```python
@st.cache_data(show_spinner=False)
def cargar_datos():
    ruta = os.path.join(os.path.dirname(__file__), "precios_acciones.csv")
    df = pd.read_csv(ruta, parse_dates=["Date"], index_col="Date")
    df.sort_index(inplace=True)
    return df
```

El decorador `@st.cache_data` asegura que el CSV se cargue solo una vez, mejorando el rendimiento de la aplicación.

---

## 6. Notebook: DataPython.ipynb

### Secciones del Notebook

| # | Sección | Descripción |
|---|---------|-------------|
| 1 | Instalación de Librerías | `pip install plotly yfinance google-generativeai pandas nbformat` |
| 2 | Importación de Librerías | `import plotly.express as px`, `import yfinance as yf`, etc. |
| 3 | Obtención de Datos | `yf.download(["AAPL","NVDA","MSFT"], period="1y")` |
| 4 | Exploración de Datos | `.head()`, `.tail()`, `.describe()` |
| 5 | Cotización Histórica | `px.line()` con template `plotly_dark` |
| 6 | Precio Promedio | `precios.mean()` + `px.bar()` |
| 7 | Simulación de Inversión | `(precios / precios.iloc[0]) * 1000` + `px.line()` |
| 8 | Informe con Gemini AI | `google.generativeai` + análisis automático |

### Código Clave — Cotización Histórica

```python
fig = px.line(
    precios,
    title="Cotización Histórica: AAPL, MSFT & NVDA",
    labels={"Date": "Fecha", "value": "Precio (USD)"},
    template="plotly_dark"
)
fig.show()
fig.write_html("cotizacion_historica.html")
```

### Código Clave — Precio Promedio

```python
precios_promedio = precios.mean().to_frame().reset_index()
precios_promedio.columns = ["Empresa", "Precio Promedio"]

fig_barras = px.bar(
    precios_promedio,
    x="Empresa",
    y="Precio Promedio",
    color="Empresa",
    title="Precio Promedio: Apple, Microsoft & Nvidia",
    template="plotly_dark",
    text_auto='.2f'
)
```

### Código Clave — Simulación de Inversión

```python
# Fórmula: Inversión = (Precio_actual / Precio_inicial) * $1,000
inversion = (precios / precios.iloc[0]) * 1000

fig_inversion = px.line(
    inversion,
    title="Comportamiento de la inversión que inicia en $1.000 USD",
    labels={"Date": "Fecha", "value": "Inversión en USD"},
    template="plotly_dark"
)
```

---

## 7. Visualizaciones HTML

El proyecto incluye tres archivos HTML generados desde el notebook con Plotly:

### cotizacion_historica.html
- **Tipo:** Gráfico de líneas (`px.line`)
- **Eje X:** Fecha (Sep 2025 – Sep 2026)
- **Eje Y:** Precio de cierre en USD
- **Series:** AAPL (azul), MSFT (rojo), NVDA (verde)
- **Template:** `plotly_dark`
- **Interactivo:** Zoom, pan, hover, leyenda desplegable

### inversion.html
- **Tipo:** Gráfico de líneas (`px.line`)
- **Eje X:** Fecha
- **Eje Y:** Valor de la inversión en USD
- **Capital base:** $1,000 USD al inicio del período
- **Fórmula:** `valor = (precio_t / precio_0) × 1000`

### precio_promedio.html
- **Tipo:** Gráfico de barras (`px.bar`)
- **Eje X:** Empresa (AAPL, MSFT, NVDA)
- **Eje Y:** Precio promedio en USD
- **Texto:** Valor numérico sobre cada barra (`.2f`)

---

## 8. Aplicación Streamlit (app.py)

### Estructura del código

```
app.py
├── Configuración de página (st.set_page_config)
├── CSS personalizado (glassmorphism, dark theme)
├── Funciones de carga de datos (@st.cache_data)
├── Componentes UI reutilizables
│   ├── render_metric_card()
│   └── render_section_header()
├── Páginas
│   ├── pagina_landing()         ← 🏠 Landing Page
│   ├── pagina_dashboard(df)     ← 📊 Dashboard principal
│   └── pagina_documentacion()   ← 📚 Documentación técnica
├── Sidebar
│   └── render_sidebar()         ← Navegación + filtros
└── main()                       ← Punto de entrada
```

### Páginas de la Aplicación

#### 🏠 Landing Page
- Hero section con título y badges de tecnologías
- Descripción del problema
- Objetivos SMART (componentes visuales)
- Tabla del equipo
- Cards de visualizaciones con enlaces a HTML
- CTA al dashboard

#### 📊 Dashboard
- **Sidebar:** Filtros de acciones, rango de fechas, capital de inversión
- **KPIs:** Métricas de precio actual y variación por empresa
- **Tab 1:** Cotización histórica con `plotly graph_objects`
- **Tab 2:** Simulación de inversión con línea de capital base
- **Tab 3:** Gráfico de barras de precio promedio
- **Tab 4:** Tabla de datos con descarga CSV
- **Tab 5:** Estadísticas descriptivas, correlación y box plots

#### 📚 Documentación
- Estructura del proyecto (árbol de archivos)
- Schema del dataset
- Stack tecnológico
- Comandos de instalación y despliegue

### Diseño Visual

La aplicación usa un sistema de diseño **glassmorphism dark** con:
- Paleta: Indigo (#6366f1), Violeta (#8b5cf6), Cyan (#06b6d4)
- Tipografía: Inter + Space Grotesk (Google Fonts)
- Efectos: backdrop-filter blur, gradientes, bordes con opacidad
- Animaciones: hover transitions suaves

---

## 9. Guía de Instalación Paso a Paso

### Paso 1: Verificar Python

```powershell
python --version
# Debe ser Python 3.11 o superior
```

### Paso 2: Clonar el Repositorio

```powershell
git clone https://github.com/feibert-ufhec/analisis-financiero-python.git
cd analisis-financiero-python
```

### Paso 3: Crear Entorno Virtual

```powershell
# Crear el entorno
python -m venv .venv

# Activar en Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Verificar activación (verás (.venv) en el prompt)
```

### Paso 4: Instalar Dependencias

```powershell
pip install -r requirements.txt

# Verificar instalación
pip list | findstr -i "streamlit plotly pandas"
```

### Paso 5: Ejecutar la Aplicación

```powershell
streamlit run app.py
```

La aplicación se abrirá automáticamente en:  
👉 `http://localhost:8501`

### Paso 6: Verificar Archivos de Datos

Asegúrate de que estos archivos estén en el mismo directorio que `app.py`:

```
✅ precios_acciones.csv
✅ cotizacion_historica.html
✅ inversion.html
✅ precio_promedio.html
✅ DataPython.ipynb
```

---

## 10. Despliegue en Streamlit Cloud

### Requisitos Previos
- Cuenta en [GitHub](https://github.com)
- Cuenta en [Streamlit Cloud](https://share.streamlit.io) (gratuita)
- Repositorio con `app.py` y `requirements.txt` en la raíz

### Paso a Paso

#### 1. Preparar el Repositorio

```bash
# Asegúrate de tener todos los archivos
git status

# Agregar todos los archivos
git add .

# Hacer commit
git commit -m "feat: aplicación Streamlit completa con análisis financiero"

# Subir a GitHub
git push origin main
```

#### 2. Crear la App en Streamlit Cloud

1. Ve a [share.streamlit.io](https://share.streamlit.io)
2. Haz clic en **"New app"**
3. Conecta tu cuenta de GitHub si no lo has hecho
4. Selecciona:
   - **Repository:** `tu-usuario/analisis-financiero-python`
   - **Branch:** `main`
   - **Main file path:** `app.py`
5. Haz clic en **"Deploy!"**

#### 3. Esperar el Despliegue

El proceso toma ~2-3 minutos. Streamlit Cloud:
- Clona el repositorio
- Instala las dependencias de `requirements.txt`
- Ejecuta `app.py`
- Asigna una URL pública

#### 4. URL Pública

Tu aplicación estará disponible en:
```
https://[usuario]-[repo]-app-[hash].streamlit.app
```

#### 5. Auto-Deploy

Cada vez que hagas `git push` a la rama `main`, Streamlit Cloud automáticamente re-desplegará la aplicación.

---

## 11. Integración con GitHub

### Estructura del Repositorio

```
📁 analisis-financiero-python/
├── 📄 .gitignore
├── 📄 README.md              ← Documentación principal
├── 📄 DOCUMENTACION.md       ← Este archivo
├── 📄 app.py                 ← Aplicación Streamlit
├── 📄 requirements.txt       ← Dependencias
├── 📊 precios_acciones.csv   ← Dataset
├── 📓 DataPython.ipynb       ← Notebook
├── 🌐 cotizacion_historica.html
├── 🌐 inversion.html
└── 🌐 precio_promedio.html
```

### Comandos Git Esenciales

```bash
# Ver estado del repositorio
git status

# Agregar cambios
git add .

# Hacer commit con mensaje descriptivo
git commit -m "tipo: descripción breve del cambio"

# Subir cambios
git push origin main

# Ver historial de commits
git log --oneline -10

# Ver ramas disponibles
git branch -a
```

### Convención de Commits

| Prefijo | Descripción |
|---------|-------------|
| `feat:` | Nueva funcionalidad |
| `fix:` | Corrección de bug |
| `docs:` | Cambios en documentación |
| `style:` | Cambios de formato/estilo |
| `refactor:` | Refactorización de código |
| `data:` | Actualización de datos |

---

## 12. Stack Tecnológico

### Python Libraries

| Librería | Versión | Propósito |
|----------|---------|-----------|
| `streamlit` | ≥1.37 | Framework web para data apps |
| `pandas` | ≥2.0 | Manipulación y análisis de datos |
| `plotly` | ≥5.24 | Visualizaciones interactivas |
| `numpy` | ≥1.26 | Computación numérica |
| `yfinance` | ≥0.2 | Descarga datos Yahoo Finance (notebook) |
| `google-generativeai` | ≥0.8 | Integración con Gemini AI (notebook) |

### Servicios y Plataformas

| Servicio | Uso |
|----------|-----|
| **Streamlit Cloud** | Hosting gratuito de la app |
| **GitHub** | Control de versiones + CI/CD |
| **Google Colab** | Ejecución del notebook original |
| **Yahoo Finance** | Fuente original de datos de mercado |

---

## 13. Métricas y Resultados

### Rendimiento de Acciones (Sep 2025 – Sep 2026)

| Empresa | Precio Inicial | Precio Final | Variación % |
|---------|---------------|--------------|-------------|
| **AAPL** | $244.60 | $336.13 | **+37.4%** 🟢 |
| **MSFT** | $513.70 | $493.78 | **-3.9%** 🔴 |
| **NVDA** | $176.25 | $222.27 | **+26.1%** 🟢 |

### Simulación de Inversión ($1,000 USD)

| Empresa | Capital Final | Ganancia/Pérdida |
|---------|--------------|-----------------|
| **AAPL** | ~$1,374 | **+$374 (+37.4%)** |
| **MSFT** | ~$961 | **-$39 (-3.9%)** |
| **NVDA** | ~$1,261 | **+$261 (+26.1%)** |

### Precios Promedio del Período

| Empresa | Precio Promedio |
|---------|----------------|
| **AAPL** | ~$281 USD |
| **MSFT** | ~$446 USD |
| **NVDA** | ~$196 USD |

---

## 14. Preguntas Frecuentes

### ¿Por qué los datos del CSV pueden diferir ligeramente de Yahoo Finance?

Los precios de cierre en el CSV son **ajustados por dividendos y splits**. El valor de cierre ajustado puede diferir del precio de cierre simple. La librería `yfinance` aplica estos ajustes automáticamente con la opción `auto_adjust=True` (default desde versiones recientes).

### ¿Se pueden agregar más acciones al análisis?

Sí. Para agregar más tickers:
1. Modifica el notebook para incluirlos en `tickers = ["AAPL", "NVDA", "MSFT", "GOOGL"]`
2. Re-exporta el CSV
3. Actualiza `acciones_disponibles` en `app.py`

### ¿La app funciona sin conexión a internet?

Sí. La aplicación consume únicamente el CSV local `precios_acciones.csv`. No requiere conexión a internet durante la ejecución (solo para las fuentes de Google Fonts del CSS).

### ¿Cómo actualizar los datos del CSV?

```python
import yfinance as yf
tickers = ["AAPL", "NVDA", "MSFT"]
datos = yf.download(tickers, period="1y")
precios = datos["Close"]
precios.to_csv("precios_acciones.csv")
```

### ¿Dónde están los archivos HTML originales?

Los tres HTML (`cotizacion_historica.html`, `inversion.html`, `precio_promedio.html`) se generaron en el notebook con `fig.write_html("nombre.html")` y están incluidos en el repositorio.

---

<div align="center">

**📊 Análisis Financiero con Python · UFHEC Semillero de Datos · 2026**

Desarrollado por **Feibert** | [GitHub](https://github.com/feibert-ufhec/analisis-financiero-python)

</div>
