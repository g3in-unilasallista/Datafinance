# 📊 Análisis Financiero con Python & Streamlit

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.37+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.x-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![License](https://img.shields.io/badge/Licencia-MIT-22c55e?style=for-the-badge)
![UFHEC](https://img.shields.io/badge/UFHEC-Semillero%20de%20Datos-6366f1?style=for-the-badge)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://analisis-financiero-ufhec.streamlit.app)

</div>

---

## 🚀 Descripción

Aplicación web interactiva desarrollada en **Python + Streamlit** que analiza el comportamiento histórico de las acciones de **Apple (AAPL)**, **Microsoft (MSFT)** y **Nvidia (NVDA)** durante el período **septiembre 2025 – septiembre 2026**.

Desarrollada como ejercicio del **Semillero de Datos** de la Universidad Francisco de Paula Santander Ocaña (**UFHEC**), este proyecto demuestra cómo Python y la Inteligencia Artificial pueden democratizar el análisis financiero profesional.

---

## ✨ Características

| Característica | Descripción |
|---|---|
| 🏠 **Landing Page** | Presentación del proyecto con problema, objetivos SMART y equipo |
| 📉 **Cotización Histórica** | Gráfico de líneas interactivo con evolución de precios |
| 💰 **Simulación de Inversión** | Rendimiento de capital configurable (default: $1,000 USD) |
| 📊 **Precio Promedio** | Gráfico de barras comparativo por empresa |
| 📋 **Datos Brutos** | Tabla filtrable con descarga CSV |
| 📐 **Estadísticas** | Métricas descriptivas, correlación y box plots |
| 🎨 **Dark Theme** | Diseño glassmorphism con paleta de colores premium |

---

## 📁 Estructura del Proyecto

```text
📁 Streamlit/
├── 📄 app.py                      ← Aplicación principal de Streamlit
├── 📄 requirements.txt            ← Dependencias Python
├── 📄 README.md                   ← Este archivo
├── 📄 DOCUMENTACION.md            ← Documentación técnica paso a paso
├── 📄 .gitignore                  ← Archivos excluidos de Git
│
├── 📊 precios_acciones.csv        ← Dataset principal
├── 📓 DataPython.ipynb            ← Notebook Jupyter original (Google Colab)
│
├── 🌐 cotizacion_historica.html   ← Visualización interactiva Plotly
├── 🌐 inversion.html              ← Simulación de inversión Plotly
└── 🌐 precio_promedio.html        ← Gráfico de barras Plotly
```

---

## ⚡ Instalación y Ejecución Local

### Requisitos Previos

- Python 3.11 o superior
- pip (gestor de paquetes)
- Git

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/feibert-ufhec/analisis-financiero-python.git
cd analisis-financiero-python

# 2. Crear entorno virtual
python -m venv .venv

# Activar en Windows
.venv\Scripts\activate

# Activar en Linux/macOS
source .venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar la aplicación
streamlit run app.py
```

La aplicación se abrirá automáticamente en `http://localhost:8501` 🎉

---

## ☁️ Despliegue en Streamlit Cloud

1. **Fork** este repositorio en tu cuenta de GitHub
2. Ve a [share.streamlit.io](https://share.streamlit.io)
3. Conecta tu cuenta de GitHub
4. Selecciona el repositorio → archivo `app.py`
5. ¡Haz clic en **Deploy**! ✅

---

## 📊 Dataset

**Archivo:** `precios_acciones.csv`

| Campo | Tipo | Descripción |
|---|---|---|
| `Date` | datetime | Fecha de negociación (días hábiles) |
| `AAPL` | float64 | Precio de cierre ajustado de Apple Inc. |
| `MSFT` | float64 | Precio de cierre ajustado de Microsoft Corp. |
| `NVDA` | float64 | Precio de cierre ajustado de Nvidia Corp. |

- **Período:** 19/09/2025 → 18/09/2026
- **Registros:** 252 días hábiles bursátiles
- **Fuente original:** Yahoo Finance (`yfinance`)

---

## 🛠️ Stack Tecnológico

| Tecnología | Versión | Uso |
|---|---|---|
| Python | 3.11+ | Lenguaje base |
| Streamlit | 1.37+ | Framework web |
| Pandas | 2.x | Manipulación de datos |
| Plotly | 5.x | Visualizaciones interactivas |
| NumPy | 1.26+ | Cálculos numéricos |
| yfinance | 0.2+ | Descarga de datos (notebook) |
| Google Gemini | 0.8+ | Informe con IA (notebook) |

---

## 🎯 Objetivos SMART

| Criterio | Descripción |
|---|---|
| **S**pecífico | Analizar precios de cierre de AAPL, MSFT y NVDA con Python |
| **M**edible | 3 visualizaciones interactivas + métricas estadísticas |
| **A**lcanzable | App funcional desplegada en Streamlit Cloud |
| **R**elevante | Aplica ciencia de datos al sector financiero real |
| **T**emporal | Período 2025–2026, entregable semestre II 2026 |

---

## 🖼️ Visualizaciones

### Cotización Histórica
> Evolución de precios de cierre de las tres empresas durante el período completo.
> 🔗 [Ver cotizacion_historica.html](cotizacion_historica.html)

### Simulación de Inversión
> Valor de una inversión de $1,000 USD si se hubiera realizado al inicio del período.
> 🔗 [Ver inversion.html](inversion.html)

### Precio Promedio
> Comparativa del precio medio de cada empresa en todo el período.
> 🔗 [Ver precio_promedio.html](precio_promedio.html)

---

## 👥 Equipo

| Nombre | Rol | Institución |
|---|---|---|
| **Feibert** | Analista de Datos / Desarrollador | UFHEC · Semillero de Datos |

---

## 📄 Licencia

Este proyecto está licenciado bajo la **Licencia MIT**. Ver [LICENSE](LICENSE) para más detalles.

---

<div align="center">

Hecho con ❤️ y 🐍 Python por **Feibert** — UFHEC Semillero de Datos · 2026

[![GitHub](https://img.shields.io/badge/GitHub-feibert--ufhec-181717?style=flat-square&logo=github)](https://github.com/feibert-ufhec/analisis-financiero-python)

</div>
