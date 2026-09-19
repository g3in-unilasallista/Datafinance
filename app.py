"""
╔══════════════════════════════════════════════════════════════════╗
║    ANÁLISIS FINANCIERO - Apple, Microsoft & Nvidia               ║
║    Universidad Francisco de Paula Santander Ocaña (UFHEC)        ║
║    Semillero de Datos · Python & Ciencia de Datos                ║
╚══════════════════════════════════════════════════════════════════╝

Aplicación principal de Streamlit para análisis de precios de acciones
bursátiles de AAPL, MSFT y NVDA con visualizaciones interactivas y
simulación de inversión de $1,000 USD.

Autor  : Feibert (UFHEC - Semillero de Datos)
Versión: 1.0.0
Fecha  : Septiembre 2026
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import os

# ──────────────────────────────────────────────────────────────────
# CONFIGURACIÓN DE PÁGINA
# ──────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="📊 Análisis Financiero UFHEC | AAPL · MSFT · NVDA",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://github.com/feibert-ufhec/analisis-financiero-python",
        "Report a bug": "https://github.com/feibert-ufhec/analisis-financiero-python/issues",
        "About": "# Análisis Financiero con Python\nDesarrollado en el Semillero de Datos · UFHEC",
    },
)

# ──────────────────────────────────────────────────────────────────
# CSS PERSONALIZADO
# ──────────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    /* ─── Variables de color ─────────────────────────────────── */
    :root {
        --primary: #6366f1;
        --secondary: #8b5cf6;
        --accent: #06b6d4;
        --success: #10b981;
        --warning: #f59e0b;
        --danger: #ef4444;
        --bg-dark: #0f0f1a;
        --bg-card: #1a1a2e;
        --bg-glass: rgba(99, 102, 241, 0.08);
        --text-primary: #f1f5f9;
        --text-muted: #94a3b8;
        --border: rgba(99, 102, 241, 0.25);
    }

    /* ─── Fuente Global ──────────────────────────────────────── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* ─── Fondo principal ────────────────────────────────────── */
    .stApp {
        background: linear-gradient(135deg, #0f0f1a 0%, #1a1a2e 50%, #0d0d1f 100%);
        background-attachment: fixed;
    }

    /* ─── Hero / Landing ─────────────────────────────────────── */
    .hero-section {
        background: linear-gradient(135deg,
            rgba(99, 102, 241, 0.15) 0%,
            rgba(139, 92, 246, 0.10) 50%,
            rgba(6, 182, 212, 0.08) 100%);
        border: 1px solid var(--border);
        border-radius: 24px;
        padding: 3rem 3.5rem;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(20px);
    }

    .hero-section::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -20%;
        width: 500px;
        height: 500px;
        background: radial-gradient(circle, rgba(99,102,241,0.12) 0%, transparent 70%);
        pointer-events: none;
    }

    .hero-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, #818cf8, #c084fc, #38bdf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1.2;
        margin-bottom: 0.5rem;
    }

    .hero-subtitle {
        font-size: 1.15rem;
        color: var(--text-muted);
        font-weight: 400;
        margin-bottom: 1.5rem;
    }

    .hero-badge {
        display: inline-block;
        background: rgba(99, 102, 241, 0.2);
        border: 1px solid rgba(99, 102, 241, 0.4);
        color: #818cf8;
        padding: 0.3rem 0.85rem;
        border-radius: 999px;
        font-size: 0.78rem;
        font-weight: 600;
        letter-spacing: 0.04em;
        text-transform: uppercase;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }

    /* ─── Tarjetas de métricas ───────────────────────────────── */
    .metric-card {
        background: var(--bg-glass);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 1.4rem 1.6rem;
        text-align: center;
        backdrop-filter: blur(12px);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .metric-card:hover {
        border-color: rgba(99, 102, 241, 0.6);
        box-shadow: 0 8px 32px rgba(99, 102, 241, 0.2);
        transform: translateY(-2px);
    }

    .metric-card .label {
        font-size: 0.78rem;
        font-weight: 600;
        color: var(--text-muted);
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-bottom: 0.4rem;
    }

    .metric-card .value {
        font-size: 1.9rem;
        font-weight: 800;
        font-family: 'Space Grotesk', sans-serif;
        line-height: 1.1;
    }

    .metric-card .delta {
        font-size: 0.82rem;
        font-weight: 600;
        margin-top: 0.3rem;
    }

    /* ─── Secciones ──────────────────────────────────────────── */
    .section-header {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--text-primary);
        border-left: 4px solid var(--primary);
        padding-left: 1rem;
        margin: 1.5rem 0 1rem 0;
    }

    .section-card {
        background: rgba(26, 26, 46, 0.6);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 1.5rem;
        backdrop-filter: blur(8px);
        margin-bottom: 1.5rem;
    }

    /* ─── SMART Objectives ───────────────────────────────────── */
    .smart-item {
        display: flex;
        align-items: flex-start;
        gap: 0.85rem;
        padding: 0.85rem 1rem;
        background: var(--bg-glass);
        border: 1px solid var(--border);
        border-radius: 12px;
        margin-bottom: 0.6rem;
    }

    .smart-badge {
        width: 36px;
        height: 36px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 800;
        font-size: 0.85rem;
        flex-shrink: 0;
    }

    .smart-text strong {
        display: block;
        font-size: 0.85rem;
        font-weight: 700;
        margin-bottom: 0.1rem;
    }

    .smart-text p {
        font-size: 0.8rem;
        color: var(--text-muted);
        margin: 0;
        line-height: 1.4;
    }

    /* ─── Tabla de datos ─────────────────────────────────────── */
    .dataframe {
        background: transparent !important;
        border-radius: 12px;
        overflow: hidden;
    }

    /* ─── Info boxes ─────────────────────────────────────────── */
    .info-box {
        background: rgba(6, 182, 212, 0.08);
        border: 1px solid rgba(6, 182, 212, 0.3);
        border-radius: 12px;
        padding: 1rem 1.2rem;
        margin: 1rem 0;
        color: #7dd3fc;
        font-size: 0.9rem;
    }

    .info-box strong {
        color: #38bdf8;
    }

    /* ─── Sidebar ────────────────────────────────────────────── */
    section[data-testid="stSidebar"] {
        background: rgba(15, 15, 26, 0.95) !important;
        border-right: 1px solid var(--border);
    }

    section[data-testid="stSidebar"] .stSelectbox label,
    section[data-testid="stSidebar"] .stSlider label,
    section[data-testid="stSidebar"] .stMultiSelect label {
        color: var(--text-muted) !important;
        font-size: 0.82rem !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
    }

    /* ─── Ocultar footer de Streamlit ────────────────────────── */
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}

    /* ─── Tab styling ────────────────────────────────────────── */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        background: rgba(26, 26, 46, 0.4);
        border-radius: 12px;
        padding: 0.4rem;
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        color: var(--text-muted) !important;
        font-weight: 600;
        font-size: 0.85rem;
        padding: 0.5rem 1.2rem;
    }

    .stTabs [aria-selected="true"] {
        background: var(--primary) !important;
        color: white !important;
    }

    /* ─── Divider ────────────────────────────────────────────── */
    .gradient-divider {
        height: 2px;
        background: linear-gradient(90deg, var(--primary), var(--secondary), var(--accent), transparent);
        border: none;
        margin: 2rem 0;
        border-radius: 2px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ──────────────────────────────────────────────────────────────────
# CARGA DE DATOS
# ──────────────────────────────────────────────────────────────────
@st.cache_data(show_spinner=False)
def cargar_datos():
    """
    Carga el dataset precios_acciones.csv desde el directorio raíz.
    Retorna un DataFrame con índice de fecha y columnas AAPL, MSFT, NVDA.
    """
    ruta = os.path.join(os.path.dirname(__file__), "precios_acciones.csv")
    df = pd.read_csv(ruta, parse_dates=["Date"], index_col="Date")
    df.sort_index(inplace=True)
    return df


# ──────────────────────────────────────────────────────────────────
# COMPONENTES UI REUTILIZABLES
# ──────────────────────────────────────────────────────────────────
def render_metric_card(label: str, value: str, delta: str, color: str, emoji: str = ""):
    """Renderiza una tarjeta de métrica con glassmorphism."""
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="label">{emoji} {label}</div>
            <div class="value" style="color:{color};">{value}</div>
            <div class="delta" style="color:{color}cc;">{delta}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_section_header(title: str):
    """Renderiza un encabezado de sección con borde izquierdo."""
    st.markdown(f'<div class="section-header">{title}</div>', unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────────
# PÁGINA: LANDING
# ──────────────────────────────────────────────────────────────────
def pagina_landing():
    """Renderiza la Landing Page del proyecto."""

    # ── Hero ──────────────────────────────────────────────────────
    st.markdown(
        """
        <div class="hero-section">
            <div class="hero-title">📊 Análisis Financiero con Python</div>
            <div class="hero-subtitle">
                Exploración, visualización y simulación de inversiones en
                <strong>Apple · Microsoft · Nvidia</strong> — Período 2025–2026
            </div>
            <span class="hero-badge">🏫 UFHEC</span>
            <span class="hero-badge">🐍 Python</span>
            <span class="hero-badge">📈 Finanzas</span>
            <span class="hero-badge">🤖 Google Gemini AI</span>
            <span class="hero-badge">📊 Plotly</span>
            <span class="hero-badge">☁️ Streamlit Cloud</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Sección: Problema ─────────────────────────────────────────
    render_section_header("🔍 Planteamiento del Problema")
    st.markdown(
        """
        <div class="section-card">
            <p style="color:#cbd5e1; line-height:1.8; font-size:0.95rem;">
            En el contexto financiero actual, los inversores particulares y corporativos necesitan
            herramientas accesibles que les permitan analizar el comportamiento histórico de
            acciones bursátiles de manera visual, rápida y confiable.
            <br><br>
            Las tres empresas analizadas —<strong style="color:#818cf8;">Apple (AAPL)</strong>,
            <strong style="color:#f87171;">Microsoft (MSFT)</strong> y
            <strong style="color:#34d399;">Nvidia (NVDA)</strong>— representan los pilares de
            la innovación tecnológica mundial. Comprender su comportamiento durante el último año
            es fundamental para la toma de decisiones de inversión fundamentada en datos.
            <br><br>
            <strong style="color:#f1f5f9;">¿Cómo podemos utilizar Python y la Inteligencia Artificial
            para democratizar el acceso al análisis financiero profesional?</strong>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Sección: Objetivos SMART ──────────────────────────────────
    render_section_header("🎯 Objetivos SMART del Proyecto")

    smart_items = [
        {
            "letra": "S",
            "titulo": "Específico (Specific)",
            "desc": "Analizar los precios de cierre históricos de AAPL, MSFT y NVDA durante el período 2025–2026 usando Python, Pandas y Plotly, consumiendo datos desde el archivo precios_acciones.csv.",
            "color_bg": "rgba(99,102,241,0.25)",
            "color_txt": "#818cf8",
        },
        {
            "letra": "M",
            "titulo": "Medible (Measurable)",
            "desc": "Generar 3 visualizaciones interactivas clave (cotización histórica, simulación de inversión de $1,000 USD y precio promedio por empresa) con métricas estadísticas cuantificables.",
            "color_bg": "rgba(139,92,246,0.25)",
            "color_txt": "#c084fc",
        },
        {
            "letra": "A",
            "titulo": "Alcanzable (Achievable)",
            "desc": "Construir una aplicación web funcional con Streamlit que consuma el CSV local y los gráficos HTML existentes, desplegada en Streamlit Cloud con repositorio GitHub público.",
            "color_bg": "rgba(6,182,212,0.25)",
            "color_txt": "#38bdf8",
        },
        {
            "letra": "R",
            "titulo": "Relevante (Relevant)",
            "desc": "El proyecto aplica competencias de ciencia de datos e inteligencia artificial para resolver una necesidad real del sector financiero, alineándose con el semillero de investigación en Datos y Tecnología de la UFHEC.",
            "color_bg": "rgba(16,185,129,0.25)",
            "color_txt": "#34d399",
        },
        {
            "letra": "T",
            "titulo": "Temporal (Time-bound)",
            "desc": "El análisis cubre exactamente 252 días hábiles bursátiles (septiembre 2025 – septiembre 2026), con entregables completados en el segundo semestre académico 2026.",
            "color_bg": "rgba(245,158,11,0.25)",
            "color_txt": "#fbbf24",
        },
    ]

    for item in smart_items:
        st.markdown(
            f"""
            <div class="smart-item">
                <div class="smart-badge" style="background:{item['color_bg']}; color:{item['color_txt']};">
                    {item['letra']}
                </div>
                <div class="smart-text">
                    <strong style="color:{item['color_txt']};">{item['titulo']}</strong>
                    <p>{item['desc']}</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)

    # ── Sección: Equipo ───────────────────────────────────────────
    render_section_header("👥 Equipo del Proyecto")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(
            """
            <div class="section-card">
                <table style="width:100%; border-collapse:collapse; font-size:0.88rem; color:#cbd5e1;">
                    <thead>
                        <tr style="border-bottom:1px solid rgba(99,102,241,0.3);">
                            <th style="text-align:left; padding:0.6rem; color:#818cf8;">Nombre</th>
                            <th style="text-align:left; padding:0.6rem; color:#818cf8;">Rol</th>
                            <th style="text-align:left; padding:0.6rem; color:#818cf8;">Institución</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td style="padding:0.7rem 0.6rem; font-weight:600; color:#f1f5f9;">Feibert</td>
                            <td style="padding:0.7rem 0.6rem;">Analista de Datos / Desarrollador</td>
                            <td style="padding:0.7rem 0.6rem;">UFHEC · Semillero de Datos</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="section-card" style="text-align:center;">
                <div style="font-size:3rem; margin-bottom:0.5rem;">🏫</div>
                <div style="font-weight:700; color:#818cf8; font-size:0.9rem;">UFHEC</div>
                <div style="font-size:0.78rem; color:#94a3b8; margin-top:0.3rem;">
                    Universidad Francisco<br>de Paula Santander<br>Ocaña
                </div>
                <div style="margin-top:0.8rem; font-size:0.72rem; color:#64748b; border-top:1px solid rgba(99,102,241,0.2); padding-top:0.7rem;">
                    Semillero de Datos<br>Python & Ciencia de Datos
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)

    # ── Sección: Visualizaciones ──────────────────────────────────
    render_section_header("🖼️ Visualizaciones del Proyecto")
    st.markdown(
        """
        <div class="info-box">
            <strong>📌 Nota:</strong> Las siguientes visualizaciones fueron generadas en el notebook
            <code>DataPython.ipynb</code> usando Plotly Express con template <code>plotly_dark</code>.
            Haz clic en cada enlace para abrir la visualización interactiva completa.
        </div>
        """,
        unsafe_allow_html=True,
    )

    col_v1, col_v2, col_v3 = st.columns(3)

    with col_v1:
        st.markdown(
            """
            <div class="metric-card" style="text-align:center; padding:1.5rem;">
                <div style="font-size:2.5rem; margin-bottom:0.5rem;">📉</div>
                <div style="font-weight:700; color:#818cf8; font-size:0.95rem; margin-bottom:0.4rem;">
                    Cotización Histórica
                </div>
                <div style="font-size:0.78rem; color:#94a3b8; margin-bottom:0.9rem;">
                    Evolución de precios de cierre<br>Sep 2025 – Sep 2026
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        # Botón para abrir el HTML
        base_path = os.path.dirname(os.path.abspath(__file__))
        st.markdown(
            f'<a href="cotizacion_historica.html" target="_blank">'
            f'<button style="width:100%;background:rgba(99,102,241,0.2);border:1px solid rgba(99,102,241,0.4);'
            f'color:#818cf8;padding:0.5rem;border-radius:8px;cursor:pointer;font-size:0.82rem;font-weight:600;">'
            f'🔗 Ver Gráfico Interactivo</button></a>',
            unsafe_allow_html=True,
        )

    with col_v2:
        st.markdown(
            """
            <div class="metric-card" style="text-align:center; padding:1.5rem;">
                <div style="font-size:2.5rem; margin-bottom:0.5rem;">💰</div>
                <div style="font-weight:700; color:#c084fc; font-size:0.95rem; margin-bottom:0.4rem;">
                    Simulación de Inversión
                </div>
                <div style="font-size:0.78rem; color:#94a3b8; margin-bottom:0.9rem;">
                    Rendimiento de $1,000 USD<br>invertidos al inicio del período
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<a href="inversion.html" target="_blank">'
            f'<button style="width:100%;background:rgba(139,92,246,0.2);border:1px solid rgba(139,92,246,0.4);'
            f'color:#c084fc;padding:0.5rem;border-radius:8px;cursor:pointer;font-size:0.82rem;font-weight:600;">'
            f'🔗 Ver Gráfico Interactivo</button></a>',
            unsafe_allow_html=True,
        )

    with col_v3:
        st.markdown(
            """
            <div class="metric-card" style="text-align:center; padding:1.5rem;">
                <div style="font-size:2.5rem; margin-bottom:0.5rem;">📊</div>
                <div style="font-weight:700; color:#38bdf8; font-size:0.95rem; margin-bottom:0.4rem;">
                    Precio Promedio
                </div>
                <div style="font-size:0.78rem; color:#94a3b8; margin-bottom:0.9rem;">
                    Comparativa de precio medio<br>por empresa en todo el período
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<a href="precio_promedio.html" target="_blank">'
            f'<button style="width:100%;background:rgba(6,182,212,0.2);border:1px solid rgba(6,182,212,0.4);'
            f'color:#38bdf8;padding:0.5rem;border-radius:8px;cursor:pointer;font-size:0.82rem;font-weight:600;">'
            f'🔗 Ver Gráfico Interactivo</button></a>',
            unsafe_allow_html=True,
        )

    st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)

    # ── CTA ───────────────────────────────────────────────────────
    st.markdown(
        """
        <div style="text-align:center; padding:2rem 1rem;">
            <div style="font-family:'Space Grotesk',sans-serif; font-size:1.4rem; font-weight:700;
                color:#f1f5f9; margin-bottom:0.5rem;">
                ¿Listo para explorar los datos?
            </div>
            <div style="color:#94a3b8; font-size:0.9rem; margin-bottom:1.5rem;">
                Navega a la sección <strong style="color:#818cf8;">📊 Dashboard</strong>
                en el menú lateral para comenzar el análisis interactivo
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ──────────────────────────────────────────────────────────────────
# PÁGINA: DASHBOARD PRINCIPAL
# ──────────────────────────────────────────────────────────────────
def pagina_dashboard(df: pd.DataFrame):
    """Renderiza el dashboard principal de análisis financiero."""

    # ── Filtros en sidebar ─────────────────────────────────────────
    st.sidebar.markdown("---")
    st.sidebar.markdown(
        '<div style="font-size:0.85rem;font-weight:700;color:#818cf8;'
        'text-transform:uppercase;letter-spacing:0.05em;margin-bottom:0.5rem;">'
        "⚙️ Configuración del Análisis</div>",
        unsafe_allow_html=True,
    )

    # Selector de acciones
    acciones_disponibles = ["AAPL", "MSFT", "NVDA"]
    acciones_seleccionadas = st.sidebar.multiselect(
        "Acciones a analizar",
        options=acciones_disponibles,
        default=acciones_disponibles,
        help="Selecciona las empresas que deseas incluir en los gráficos.",
    )

    # Selector de rango de fechas
    fecha_min = df.index.min().date()
    fecha_max = df.index.max().date()
    rango_fechas = st.sidebar.date_input(
        "Rango de Fechas",
        value=(fecha_min, fecha_max),
        min_value=fecha_min,
        max_value=fecha_max,
    )

    # Capital de inversión
    capital = st.sidebar.slider(
        "Capital de Inversión (USD)",
        min_value=100,
        max_value=10000,
        value=1000,
        step=100,
        format="$%d",
        help="Ajusta el capital inicial para la simulación de inversión.",
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown(
        """
        <div style="font-size:0.72rem;color:#475569;text-align:center;line-height:1.6;">
        📁 Datos: <code>precios_acciones.csv</code><br>
        📓 Notebook: <code>DataPython.ipynb</code><br>
        🔄 252 días hábiles bursátiles
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Validación de selección ─────────────────────────────────────
    if not acciones_seleccionadas:
        st.warning("⚠️ Selecciona al menos una acción en el panel lateral.")
        return

    # Filtrar datos por fecha
    try:
        fecha_inicio = pd.Timestamp(rango_fechas[0])
        fecha_fin = pd.Timestamp(rango_fechas[1])
    except (IndexError, TypeError):
        fecha_inicio = pd.Timestamp(fecha_min)
        fecha_fin = pd.Timestamp(fecha_max)

    df_filtrado = df.loc[fecha_inicio:fecha_fin, acciones_seleccionadas]

    # ── Métricas KPI ────────────────────────────────────────────────
    render_section_header("📌 Indicadores Clave")

    COLORES_TICKER = {"AAPL": "#818cf8", "MSFT": "#f87171", "NVDA": "#34d399"}
    EMOJIS_TICKER = {"AAPL": "🍎", "MSFT": "🪟", "NVDA": "💚"}

    kpi_cols = st.columns(len(acciones_seleccionadas))
    for i, ticker in enumerate(acciones_seleccionadas):
        serie = df_filtrado[ticker].dropna()
        precio_actual = serie.iloc[-1]
        precio_inicial = serie.iloc[0]
        cambio_pct = ((precio_actual - precio_inicial) / precio_inicial) * 100
        arrow = "▲" if cambio_pct >= 0 else "▼"
        color_delta = "#10b981" if cambio_pct >= 0 else "#ef4444"

        with kpi_cols[i]:
            render_metric_card(
                label=ticker,
                value=f"${precio_actual:,.2f}",
                delta=f"{arrow} {cambio_pct:+.2f}% en el período",
                color=COLORES_TICKER.get(ticker, "#818cf8"),
                emoji=EMOJIS_TICKER.get(ticker, "📈"),
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Tabs de análisis ────────────────────────────────────────────
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "📉 Cotización Histórica",
            "💰 Simulación de Inversión",
            "📊 Precio Promedio",
            "📋 Datos Brutos",
            "📐 Estadísticas",
        ]
    )

    # ─────────────────────────────────────────────────────────────────
    # TAB 1: COTIZACIÓN HISTÓRICA
    # ─────────────────────────────────────────────────────────────────
    with tab1:
        render_section_header("📉 Cotización Histórica de Acciones")
        st.markdown(
            """
            <div class="info-box">
            Evolución de los <strong>precios de cierre ajustados</strong> de cada empresa durante
            el período seleccionado. Los datos provienen de <code>precios_acciones.csv</code>
            (fuente original: Yahoo Finance vía <code>yfinance</code>).
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Gráfico de líneas — cotización histórica
        fig_hist = go.Figure()
        color_map = {"AAPL": "#818cf8", "MSFT": "#f87171", "NVDA": "#34d399"}

        for ticker in acciones_seleccionadas:
            serie = df_filtrado[ticker].dropna()
            fig_hist.add_trace(
                go.Scatter(
                    x=serie.index,
                    y=serie.values,
                    name=ticker,
                    mode="lines",
                    line=dict(color=color_map.get(ticker, "#818cf8"), width=2.5),
                    hovertemplate=(
                        f"<b>{ticker}</b><br>"
                        "Fecha: %{x|%d %b %Y}<br>"
                        "Precio: <b>$%{y:,.2f}</b><extra></extra>"
                    ),
                )
            )

        fig_hist.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(15,15,26,0)",
            plot_bgcolor="rgba(15,15,26,0.4)",
            title=dict(
                text="📈 Precios de Cierre — Apple, Microsoft & Nvidia",
                font=dict(size=16, family="Space Grotesk"),
                x=0.02,
            ),
            xaxis=dict(
                title="Fecha",
                gridcolor="rgba(99,102,241,0.12)",
                showgrid=True,
            ),
            yaxis=dict(
                title="Precio de Cierre (USD)",
                gridcolor="rgba(99,102,241,0.12)",
                tickformat="$,.0f",
            ),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1,
                bgcolor="rgba(15,15,26,0.6)",
                bordercolor="rgba(99,102,241,0.3)",
                borderwidth=1,
            ),
            hovermode="x unified",
            height=520,
            margin=dict(l=60, r=20, t=60, b=60),
        )

        st.plotly_chart(fig_hist, use_container_width=True)

        # Botón para ver HTML original
        st.markdown(
            """
            <div style="text-align:center;margin-top:0.5rem;">
                <a href="cotizacion_historica.html" target="_blank"
                   style="text-decoration:none;">
                    <span style="background:rgba(99,102,241,0.2);border:1px solid rgba(99,102,241,0.4);
                    color:#818cf8;padding:0.45rem 1.2rem;border-radius:8px;font-size:0.82rem;
                    font-weight:600;cursor:pointer;">
                        🔗 Abrir visualización HTML original
                    </span>
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ─────────────────────────────────────────────────────────────────
    # TAB 2: SIMULACIÓN DE INVERSIÓN
    # ─────────────────────────────────────────────────────────────────
    with tab2:
        render_section_header(f"💰 Simulación de Inversión — ${capital:,} USD")
        st.markdown(
            f"""
            <div class="info-box">
            Simula el comportamiento de una inversión de <strong>${capital:,} USD</strong>
            realizada en el primer día del período seleccionado.
            Fórmula: <code>Valor = (Precio_actual / Precio_inicial) × {capital}</code>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Calcular inversión
        inversion = (df_filtrado / df_filtrado.iloc[0]) * capital

        fig_inv = go.Figure()
        color_map_inv = {"AAPL": "#818cf8", "MSFT": "#f87171", "NVDA": "#34d399"}

        for ticker in acciones_seleccionadas:
            serie_inv = inversion[ticker].dropna()
            valor_final = serie_inv.iloc[-1]
            ganancia_pct = ((valor_final - capital) / capital) * 100

            fig_inv.add_trace(
                go.Scatter(
                    x=serie_inv.index,
                    y=serie_inv.values,
                    name=f"{ticker} (${valor_final:,.0f})",
                    mode="lines",
                    line=dict(color=color_map_inv.get(ticker, "#818cf8"), width=2.5),
                    fill="tozeroy",
                    fillcolor=color_map_inv.get(ticker, "#818cf8").replace("#", "rgba(")
                    + ",0.04)".replace("rgba(", "rgba("),
                    hovertemplate=(
                        f"<b>{ticker}</b><br>"
                        "Fecha: %{x|%d %b %Y}<br>"
                        "Valor: <b>$%{y:,.2f}</b><extra></extra>"
                    ),
                )
            )

        # Línea de capital base
        fig_inv.add_hline(
            y=capital,
            line_dash="dash",
            line_color="rgba(255,255,255,0.3)",
            annotation_text=f"Capital inicial: ${capital:,}",
            annotation_position="bottom right",
            annotation_font_color="rgba(255,255,255,0.5)",
        )

        fig_inv.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(15,15,26,0)",
            plot_bgcolor="rgba(15,15,26,0.4)",
            title=dict(
                text=f"💰 Rendimiento de Inversión — Capital Inicial: ${capital:,} USD",
                font=dict(size=16, family="Space Grotesk"),
                x=0.02,
            ),
            xaxis=dict(
                title="Fecha",
                gridcolor="rgba(99,102,241,0.12)",
            ),
            yaxis=dict(
                title="Valor de la Inversión (USD)",
                gridcolor="rgba(99,102,241,0.12)",
                tickformat="$,.0f",
            ),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1,
                bgcolor="rgba(15,15,26,0.6)",
                bordercolor="rgba(99,102,241,0.3)",
                borderwidth=1,
            ),
            hovermode="x unified",
            height=520,
            margin=dict(l=60, r=20, t=70, b=60),
        )

        st.plotly_chart(fig_inv, use_container_width=True)

        # Resumen de resultados
        st.markdown("**📋 Resumen de Rendimiento Final**")
        cols_res = st.columns(len(acciones_seleccionadas))
        for i, ticker in enumerate(acciones_seleccionadas):
            serie_inv = inversion[ticker].dropna()
            valor_final = serie_inv.iloc[-1]
            ganancia_abs = valor_final - capital
            ganancia_pct = (ganancia_abs / capital) * 100
            with cols_res[i]:
                render_metric_card(
                    label=f"{ticker} — Valor Final",
                    value=f"${valor_final:,.2f}",
                    delta=f"{'▲' if ganancia_abs >= 0 else '▼'} ${abs(ganancia_abs):,.2f} ({ganancia_pct:+.1f}%)",
                    color=COLORES_TICKER.get(ticker, "#818cf8"),
                    emoji=EMOJIS_TICKER.get(ticker, "📈"),
                )

        st.markdown(
            """
            <div style="text-align:center;margin-top:1rem;">
                <a href="inversion.html" target="_blank" style="text-decoration:none;">
                    <span style="background:rgba(139,92,246,0.2);border:1px solid rgba(139,92,246,0.4);
                    color:#c084fc;padding:0.45rem 1.2rem;border-radius:8px;font-size:0.82rem;
                    font-weight:600;">
                        🔗 Abrir visualización HTML original
                    </span>
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ─────────────────────────────────────────────────────────────────
    # TAB 3: PRECIO PROMEDIO
    # ─────────────────────────────────────────────────────────────────
    with tab3:
        render_section_header("📊 Precio Promedio por Empresa")
        st.markdown(
            """
            <div class="info-box">
            Precio medio de cierre de cada empresa durante el período seleccionado.
            Gráfico de barras con <strong>Plotly Dark template</strong>, replicando el análisis
            del notebook <code>DataPython.ipynb</code>.
            </div>
            """,
            unsafe_allow_html=True,
        )

        precios_prom = df_filtrado.mean().reset_index()
        precios_prom.columns = ["Empresa", "Precio Promedio"]

        fig_barras = px.bar(
            precios_prom,
            x="Empresa",
            y="Precio Promedio",
            color="Empresa",
            color_discrete_map={"AAPL": "#818cf8", "MSFT": "#f87171", "NVDA": "#34d399"},
            title="📊 Precio Promedio: Apple, Microsoft & Nvidia",
            labels={"Precio Promedio": "Precio Promedio (USD)", "Empresa": "Empresa"},
            template="plotly_dark",
            text_auto=".2f",
        )

        fig_barras.update_traces(
            textfont_size=14,
            textposition="outside",
            marker_line_width=0,
        )

        fig_barras.update_layout(
            paper_bgcolor="rgba(15,15,26,0)",
            plot_bgcolor="rgba(15,15,26,0.4)",
            showlegend=False,
            yaxis=dict(
                gridcolor="rgba(99,102,241,0.12)",
                tickformat="$,.0f",
                title="Precio Promedio (USD)",
            ),
            xaxis=dict(title="Empresa"),
            height=480,
            margin=dict(l=60, r=20, t=70, b=60),
        )

        st.plotly_chart(fig_barras, use_container_width=True)

        st.markdown(
            """
            <div style="text-align:center;margin-top:0.5rem;">
                <a href="precio_promedio.html" target="_blank" style="text-decoration:none;">
                    <span style="background:rgba(6,182,212,0.2);border:1px solid rgba(6,182,212,0.4);
                    color:#38bdf8;padding:0.45rem 1.2rem;border-radius:8px;font-size:0.82rem;font-weight:600;">
                        🔗 Abrir visualización HTML original
                    </span>
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ─────────────────────────────────────────────────────────────────
    # TAB 4: DATOS BRUTOS
    # ─────────────────────────────────────────────────────────────────
    with tab4:
        render_section_header("📋 Datos del CSV — precios_acciones.csv")
        st.markdown(
            f"""
            <div class="info-box">
            Dataset completo cargado desde <code>precios_acciones.csv</code>.
            Mostrando <strong>{len(df_filtrado)}</strong> registros para el período seleccionado.
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Mostrar tabla formateada
        df_display = df_filtrado.copy()
        for col in df_display.columns:
            df_display[col] = df_display[col].apply(lambda x: f"${x:,.4f}" if pd.notna(x) else "—")
        df_display.index = df_display.index.strftime("%Y-%m-%d")
        df_display.index.name = "Fecha"

        st.dataframe(
            df_display,
            use_container_width=True,
            height=500,
        )

        # Descarga del CSV filtrado
        csv_bytes = df_filtrado.to_csv().encode("utf-8")
        st.download_button(
            label="⬇️ Descargar datos filtrados (CSV)",
            data=csv_bytes,
            file_name="precios_acciones_filtrado.csv",
            mime="text/csv",
            help="Descarga el subconjunto de datos visible en la tabla.",
        )

    # ─────────────────────────────────────────────────────────────────
    # TAB 5: ESTADÍSTICAS
    # ─────────────────────────────────────────────────────────────────
    with tab5:
        render_section_header("📐 Estadísticas Descriptivas")
        st.markdown(
            """
            <div class="info-box">
            Estadísticas descriptivas calculadas con <code>pandas.DataFrame.describe()</code>,
            equivalente al análisis realizado en la sección 4 del notebook.
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Estadísticas descriptivas
        stats = df_filtrado.describe().T
        stats_display = stats.copy()
        for col in stats_display.columns:
            stats_display[col] = stats_display[col].apply(
                lambda x: f"${x:,.4f}" if col not in ["count"] else f"{x:.0f}"
            )

        st.dataframe(stats_display, use_container_width=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Mapa de correlación
        render_section_header("🔗 Correlación entre Acciones")
        if len(acciones_seleccionadas) > 1:
            corr = df_filtrado.corr()
            fig_corr = go.Figure(
                data=go.Heatmap(
                    z=corr.values,
                    x=corr.columns.tolist(),
                    y=corr.columns.tolist(),
                    colorscale=[
                        [0.0, "#1a1a2e"],
                        [0.5, "#4c1d95"],
                        [1.0, "#818cf8"],
                    ],
                    text=np.round(corr.values, 3),
                    texttemplate="%{text}",
                    textfont={"size": 16, "color": "white"},
                    showscale=True,
                    zmin=0,
                    zmax=1,
                )
            )
            fig_corr.update_layout(
                template="plotly_dark",
                paper_bgcolor="rgba(15,15,26,0)",
                plot_bgcolor="rgba(15,15,26,0)",
                title=dict(
                    text="Matriz de Correlación de Precios",
                    font=dict(size=15, family="Space Grotesk"),
                ),
                height=380,
                margin=dict(l=40, r=40, t=60, b=40),
            )
            st.plotly_chart(fig_corr, use_container_width=True)
        else:
            st.info("Selecciona más de una acción para ver la correlación.")

        # Box plots
        render_section_header("📦 Distribución de Precios (Box Plot)")
        df_melt = df_filtrado.reset_index().melt(
            id_vars="Date", var_name="Ticker", value_name="Precio"
        )
        fig_box = px.box(
            df_melt,
            x="Ticker",
            y="Precio",
            color="Ticker",
            color_discrete_map={"AAPL": "#818cf8", "MSFT": "#f87171", "NVDA": "#34d399"},
            template="plotly_dark",
            title="Distribución de Precios de Cierre por Empresa",
            labels={"Precio": "Precio (USD)", "Ticker": "Empresa"},
        )
        fig_box.update_layout(
            paper_bgcolor="rgba(15,15,26,0)",
            plot_bgcolor="rgba(15,15,26,0.4)",
            showlegend=False,
            height=440,
            yaxis=dict(tickformat="$,.0f", gridcolor="rgba(99,102,241,0.12)"),
        )
        st.plotly_chart(fig_box, use_container_width=True)


# ──────────────────────────────────────────────────────────────────
# PÁGINA: DOCUMENTACIÓN
# ──────────────────────────────────────────────────────────────────
def pagina_documentacion():
    """Renderiza la página de documentación técnica del proyecto."""

    st.markdown(
        """
        <div class="hero-section">
            <div class="hero-title">📚 Documentación Técnica</div>
            <div class="hero-subtitle">
                Guía completa de la arquitectura, datos y metodología del proyecto
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_section_header("🗂️ Estructura del Proyecto")
    st.code(
        """
📁 Streamlit/
├── 📄 app.py                      ← Aplicación principal (este archivo)
├── 📄 requirements.txt            ← Dependencias Python
├── 📄 README.md                   ← Documentación del proyecto
├── 📄 DOCUMENTACION.md            ← Guía técnica detallada
├── 📄 .gitignore                  ← Archivos excluidos de Git
│
├── 📊 precios_acciones.csv        ← Dataset principal (AAPL, MSFT, NVDA)
├── 📓 DataPython.ipynb            ← Notebook Jupyter original
│
├── 🌐 cotizacion_historica.html   ← Gráfico interactivo Plotly
├── 🌐 inversion.html              ← Simulación de inversión Plotly
└── 🌐 precio_promedio.html        ← Gráfico de barras Plotly
        """,
        language="text",
    )

    render_section_header("📊 Dataset — precios_acciones.csv")
    st.markdown(
        """
        <div class="section-card">
            <table style="width:100%;border-collapse:collapse;font-size:0.88rem;color:#cbd5e1;">
                <thead>
                    <tr style="border-bottom:1px solid rgba(99,102,241,0.3);">
                        <th style="text-align:left;padding:0.6rem;color:#818cf8;">Campo</th>
                        <th style="text-align:left;padding:0.6rem;color:#818cf8;">Tipo</th>
                        <th style="text-align:left;padding:0.6rem;color:#818cf8;">Descripción</th>
                        <th style="text-align:left;padding:0.6rem;color:#818cf8;">Ejemplo</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="border-bottom:1px solid rgba(99,102,241,0.1);">
                        <td style="padding:0.6rem;font-weight:600;">Date</td>
                        <td style="padding:0.6rem;color:#38bdf8;">datetime</td>
                        <td style="padding:0.6rem;">Fecha de negociación (días hábiles)</td>
                        <td style="padding:0.6rem;font-family:monospace;">2025-09-19</td>
                    </tr>
                    <tr style="border-bottom:1px solid rgba(99,102,241,0.1);">
                        <td style="padding:0.6rem;font-weight:600;">AAPL</td>
                        <td style="padding:0.6rem;color:#38bdf8;">float64</td>
                        <td style="padding:0.6rem;">Precio de cierre ajustado de Apple Inc.</td>
                        <td style="padding:0.6rem;font-family:monospace;">244.596</td>
                    </tr>
                    <tr style="border-bottom:1px solid rgba(99,102,241,0.1);">
                        <td style="padding:0.6rem;font-weight:600;">MSFT</td>
                        <td style="padding:0.6rem;color:#38bdf8;">float64</td>
                        <td style="padding:0.6rem;">Precio de cierre ajustado de Microsoft Corp.</td>
                        <td style="padding:0.6rem;font-family:monospace;">513.703</td>
                    </tr>
                    <tr>
                        <td style="padding:0.6rem;font-weight:600;">NVDA</td>
                        <td style="padding:0.6rem;color:#38bdf8;">float64</td>
                        <td style="padding:0.6rem;">Precio de cierre ajustado de Nvidia Corp.</td>
                        <td style="padding:0.6rem;font-family:monospace;">176.247</td>
                    </tr>
                </tbody>
            </table>
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_section_header("🔧 Stack Tecnológico")
    tech_col1, tech_col2 = st.columns(2)
    with tech_col1:
        st.markdown(
            """
            **Backend & Análisis**
            - `Python 3.11+` — Lenguaje base
            - `pandas 2.x` — Manipulación de datos
            - `numpy` — Cálculos numéricos
            - `yfinance` — Descarga de datos bursátiles
            - `google-generativeai` — Informe con Gemini AI

            **Visualización**
            - `plotly 5.x` — Gráficos interactivos
            - `plotly.express` — API de alto nivel
            - `plotly.graph_objects` — Trazos personalizados
            """,
            unsafe_allow_html=False,
        )
    with tech_col2:
        st.markdown(
            """
            **Frontend & Despliegue**
            - `streamlit 1.x` — Framework web
            - `Streamlit Cloud` — Hosting gratuito
            - `GitHub` — Control de versiones

            **Entorno de Desarrollo**
            - `Google Colab` — Notebook original
            - `Jupyter` — Formato `.ipynb`
            - `pip` — Gestor de paquetes
            """,
            unsafe_allow_html=False,
        )

    render_section_header("🚀 Instrucciones de Despliegue")
    st.code(
        """
# 1. Clonar el repositorio
git clone https://github.com/feibert-ufhec/analisis-financiero-python.git
cd analisis-financiero-python

# 2. Crear entorno virtual (recomendado)
python -m venv .venv
.venv\\Scripts\\activate       # Windows
source .venv/bin/activate    # Linux/Mac

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar localmente
streamlit run app.py

# 5. Abrir en el navegador
# → http://localhost:8501
        """,
        language="bash",
    )


# ──────────────────────────────────────────────────────────────────
# SIDEBAR PRINCIPAL
# ──────────────────────────────────────────────────────────────────
def render_sidebar():
    """Renderiza el sidebar de navegación."""
    with st.sidebar:
        st.markdown(
            """
            <div style="text-align:center;padding:1rem 0 0.5rem;">
                <div style="font-size:2.5rem;">📊</div>
                <div style="font-family:'Space Grotesk',sans-serif;font-size:1.05rem;
                    font-weight:700;color:#f1f5f9;margin-top:0.3rem;">
                    Análisis Financiero
                </div>
                <div style="font-size:0.72rem;color:#64748b;margin-top:0.2rem;">
                    AAPL · MSFT · NVDA
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div style="height:1px;background:linear-gradient(90deg,'
            'transparent,rgba(99,102,241,0.5),transparent);margin:0.8rem 0;"></div>',
            unsafe_allow_html=True,
        )

        # Navegación
        st.markdown(
            '<div style="font-size:0.72rem;font-weight:700;color:#64748b;'
            'text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.4rem;">'
            "Navegación</div>",
            unsafe_allow_html=True,
        )

        pagina = st.radio(
            label="Seleccionar página",
            options=["🏠 Landing Page", "📊 Dashboard", "📚 Documentación"],
            label_visibility="collapsed",
        )

        st.markdown(
            '<div style="height:1px;background:linear-gradient(90deg,'
            'transparent,rgba(99,102,241,0.5),transparent);margin:0.8rem 0;"></div>',
            unsafe_allow_html=True,
        )

        # Info del dataset
        st.markdown(
            '<div style="font-size:0.72rem;font-weight:700;color:#64748b;'
            'text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.6rem;">'
            "Sobre el Dataset</div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div style="font-size:0.78rem;color:#94a3b8;line-height:1.7;">
            🗓️ <b>Período:</b> Sep 2025 – Sep 2026<br>
            📈 <b>Tickers:</b> AAPL, MSFT, NVDA<br>
            📁 <b>Registros:</b> 252 días hábiles<br>
            🔗 <b>Fuente:</b> Yahoo Finance (yfinance)
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div style="height:1px;background:linear-gradient(90deg,'
            'transparent,rgba(99,102,241,0.5),transparent);margin:0.8rem 0;"></div>',
            unsafe_allow_html=True,
        )

        # GitHub link
        st.markdown(
            """
            <div style="text-align:center;padding:0.5rem 0;">
                <a href="https://github.com/feibert-ufhec/analisis-financiero-python"
                   target="_blank" style="text-decoration:none;">
                    <div style="background:rgba(99,102,241,0.15);border:1px solid rgba(99,102,241,0.3);
                        border-radius:10px;padding:0.55rem;font-size:0.8rem;color:#818cf8;font-weight:600;">
                        🐙 Ver en GitHub
                    </div>
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Footer
        st.markdown(
            """
            <div style="font-size:0.68rem;color:#334155;text-align:center;
                margin-top:1.5rem;line-height:1.6;">
                Desarrollado por <b style="color:#4f46e5;">Feibert</b><br>
                UFHEC · Semillero de Datos<br>
                v1.0.0 · Sep 2026
            </div>
            """,
            unsafe_allow_html=True,
        )

    return pagina


# ──────────────────────────────────────────────────────────────────
# PUNTO DE ENTRADA PRINCIPAL
# ──────────────────────────────────────────────────────────────────
def main():
    """Función principal que orquesta la aplicación Streamlit."""

    # Renderizar sidebar y obtener página seleccionada
    pagina = render_sidebar()

    # Cargar datos
    with st.spinner("⏳ Cargando dataset financiero..."):
        df = cargar_datos()

    # Routing
    if pagina == "🏠 Landing Page":
        pagina_landing()
    elif pagina == "📊 Dashboard":
        pagina_dashboard(df)
    elif pagina == "📚 Documentación":
        pagina_documentacion()


if __name__ == "__main__":
    main()
