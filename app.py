"""
===============================================================================
PLATAFORMA DE DIAGNÓSTICO, MODELADO DE IA Y ESTRATEGIA DE EDUCACIÓN FINANCIERA
EN REPÚBLICA DOMINICANA (UFHEC 2026)
===============================================================================
Aplicación web interactiva desarrollada con Streamlit, Plotly, Pandas y Scikit-Learn.
Basada en datos oficiales del Banco Central de la RD (BCRD), MINERD, SB, BID y OCDE.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import ml_engine
import data as data_module

# -----------------------------------------------------------------------------
# Configuración de la Página
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Educación Financiera RD | Diagnóstico e IA",
    page_icon="🇩🇴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# Estilos CSS Personalizados (Diseño Moderno & Glassmorphism)
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    /* Estilos generales */
    .main {
        background-color: #0e1117;
    }
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
    }
    .metric-card {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        backdrop-filter: blur(4px);
        transition: transform 0.2s ease;
    }
    .metric-card:hover {
        transform: translateY(-5px);
        border-color: #38bdf8;
    }
    .metric-value {
        font-size: 2.2rem;
        font-weight: 800;
        color: #38bdf8;
        margin-bottom: 5px;
    }
    .metric-title {
        font-size: 0.9rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .badge-high {
        background-color: #ef4444;
        color: white;
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: bold;
    }
    .badge-vulnerable {
        background-color: #f59e0b;
        color: white;
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: bold;
    }
    .badge-sustainable {
        background-color: #10b981;
        color: white;
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: bold;
    }
    .header-banner {
        background: linear-gradient(90deg, #1e3a8a 0%, #0369a1 100%);
        padding: 24px;
        border-radius: 16px;
        margin-bottom: 25px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
    }
    .header-banner h1 {
        color: #ffffff;
        font-weight: 800;
        margin: 0;
        font-size: 2.2rem;
    }
    .header-banner p {
        color: #e0f2fe;
        margin-top: 8px;
        font-size: 1.05rem;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Carga de Datos y Modelos en Cache
# -----------------------------------------------------------------------------
@st.cache_data
def get_dataset():
    return ml_engine.generar_dataset_sintetico(n=3000, seed=42)

@st.cache_resource
def get_ml_model(df):
    return ml_engine.entrenar_modelo_clasificacion(df)

df_sim = get_dataset()
ml_results = get_ml_model(df_sim)

# -----------------------------------------------------------------------------
# Sidebar Navigation
# -----------------------------------------------------------------------------
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/9/9f/Flag_of_the_Dominican_Republic.svg", width=60)
st.sidebar.title("Financial Education in the Dominican Republic")
st.sidebar.caption("Proyecto Final Python 2026 — UFHEC")
st.sidebar.caption("Sustentado por Luis Rene Herrera ")

menu = st.sidebar.radio(
    "Seleccione un Módulo:",
    [
        "🏠 Inicio y Diagnóstico",
        "🤖 Predicción de Riesgo IA",
        "📊 Segmentación y Clusterización",
        "💰 Calculadora Costo-Efectividad",
        "🎯 Programas y Hoja de Ruta",
        "📚 Fuentes y Exportación"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("""
**Fuentes Principales:**
- Banco Central RD (ENIEF 2023)
- Superintendencia de Bancos (SB)
- Ministerio de Educación (MINERD)
- Banco Interamericano de Desarrollo (BID)
""")

# =============================================================================
# MÓDULO 1: INICIO Y DIAGNÓSTICO
# =============================================================================
if menu == "🏠 Inicio y Diagnóstico":
    st.markdown("""
        <div class="header-banner">
            <h1>📊 Diagnóstico Nacional de Educación e Inclusión Financiera en RD</h1>
            <p>Análisis integral de los indicadores sociodemográficos, brechas de inclusión y matriculación educativa en la República Dominicana.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # KPI Grid
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-value">55%</div>
                <div class="metric-title">Inclusión Financiera Adulta (2023)</div>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-value">78.3%</div>
                <div class="metric-title">Aprendió a Ahorrar Eficientemente</div>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-value">3%</div>
                <div class="metric-title">Hogares con Edu. Financiera (2019)</div>
            </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-value">861,308</div>
                <div class="metric-title">Estudiantes de Secundaria</div>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Gráficos Interactivos
    c1, c2 = st.columns(2)
    
    with c1:
        st.subheader("📈 Evolución de la Inclusión Financiera (2019-2023)")
        df_inc = pd.DataFrame(data_module.INCLUSION_FINANCIERA)
        fig_inc = px.bar(
            df_inc, x='anios', y='porcentaje_con_producto_financiero',
            text='porcentaje_con_producto_financiero',
            labels={'anios': 'Año', 'porcentaje_con_producto_financiero': 'Porcentaje (%)'},
            color_discrete_sequence=['#38bdf8']
        )
        fig_inc.update_traces(texttemplate='%{text}%', textposition='outside')
        fig_inc.update_layout(yaxis_range=[0, 100], template="plotly_dark", height=380)
        st.plotly_chart(fig_inc, use_container_width=True)
        st.caption(f"Fuente: {data_module.INCLUSION_FINANCIERA['fuente']}")
        
    with c2:
        st.subheader("🎒 Distribución de Matrícula Escolar (2024-2025)")
        df_mat = pd.DataFrame({
            'Nivel': data_module.MATRICULA['nivel'],
            'Estudiantes': data_module.MATRICULA['estudiantes']
        })
        fig_mat = px.pie(
            df_mat, names='Nivel', values='Estudiantes',
            hole=0.4,
            color_discrete_sequence=px.colors.sequential.Teal
        )
        fig_mat.update_layout(template="plotly_dark", height=380)
        st.plotly_chart(fig_mat, use_container_width=True)
        st.caption(f"Fuente: {data_module.MATRICULA['fuente']}")
        
    st.markdown("---")
    
    # Brechas de Género e Indicadores de Impacto
    c3, c4 = st.columns(2)
    
    with c3:
        st.subheader("⚖️ Indicadores de Género y Crédito (SB / ENIEF)")
        df_gen = pd.DataFrame({
            'Indicador': data_module.GENERO_CREDITO['indicador'],
            'Porcentaje (%)': data_module.GENERO_CREDITO['porcentaje']
        })
        fig_gen = px.bar(
            df_gen, y='Indicador', x='Porcentaje (%)',
            orientation='h', color='Porcentaje (%)',
            color_continuous_scale='Reds'
        )
        fig_gen.update_layout(template="plotly_dark", height=350)
        st.plotly_chart(fig_gen, use_container_width=True)
        
    with c4:
        st.subheader("📌 Causas Estructurales Identificadas")
        for idx, causa in enumerate(data_module.CAUSAS, 1):
            st.markdown(f"**{idx}.** {causa}")

# =============================================================================
# MÓDULO 2: PREDICCIÓN DE RIESGO IA
# =============================================================================
elif menu == "🤖 Predicción de Riesgo IA":
    st.markdown("""
        <div class="header-banner">
            <h1>🤖 Predictor de Riesgo y Vulnerabilidad Económica (Random Forest)</h1>
            <p>Utilice nuestro modelo entrenado con el dataset representativo de la ENIEF para clasificar el perfil de un ciudadano o estudiante.</p>
        </div>
    """, unsafe_allow_html=True)
    
    col_form, col_res = st.columns([1, 1])
    
    with col_form:
        st.subheader("📝 Formulario de Entrada de Datos")
        with st.form("form_prediccion"):
            zona_input = st.selectbox("Zona de Residencia:", options=[0, 1], format_func=lambda x: "Rural" if x == 0 else "Urbana")
            genero_input = st.selectbox("Género:", options=[0, 1], format_func=lambda x: "Mujer" if x == 0 else "Hombre")
            educ_input = st.selectbox("Nivel Educativo Alcanzado:", options=[0, 1, 2], format_func=lambda x: ["Primario", "Secundario", "Superior / Universitario"][x])
            ingreso_input = st.number_input("Ingreso Mensual Estimado (RD$):", min_value=0, max_value=500000, value=25000, step=1000)
            educ_finan_input = st.selectbox("¿Ha recibido Educación Financiera previa?:", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Sí")
            
            submit_btn = st.form_submit_button("🔍 Evaluar Perfil Económico")
            
    with col_res:
        st.subheader("🎯 Resultado de la Evaluación IA")
        if submit_btn or 'prediction_done' in st.session_state:
            st.session_state['prediction_done'] = True
            
            res = ml_engine.predecir_perfil_usuario(
                ml_results, zona_input, genero_input, educ_input, ingreso_input, educ_finan_input
            )
            
            badge_class = "badge-high" if res['clase_id'] == 0 else ("badge-vulnerable" if res['clase_id'] == 1 else "badge-sustainable")
            
            st.markdown(f"""
                <div style="text-align: center; padding: 25px; background: rgba(30, 41, 59, 0.8); border-radius: 16px; margin-bottom: 20px;">
                    <h3 style="color: #cbd5e1; margin-bottom: 10px;">Perfil Clasificado:</h3>
                    <span class="{badge_class}" style="font-size: 1.4rem;">{res['etiqueta']}</span>
                </div>
            """, unsafe_allow_html=True)
            
            st.write("##### 📊 Distribución de Probabilidades del Modelo:")
            df_probs = pd.DataFrame({
                'Perfil': list(res['probabilidades'].keys()),
                'Probabilidad (%)': list(res['probabilidades'].values())
            })
            fig_probs = px.bar(
                df_probs, x='Perfil', y='Probabilidad (%)',
                color='Perfil',
                color_discrete_map={'Alto Riesgo': '#ef4444', 'Vulnerable': '#f59e0b', 'Sostenible': '#10b981'}
            )
            fig_probs.update_layout(template="plotly_dark", height=280, showlegend=False)
            st.plotly_chart(fig_probs, use_container_width=True)
            
            st.warning(f"💡 **Recomendación Estratégica:**\n{res['recomendacion']}")
            
    st.markdown("---")
    st.subheader("📈 Métricas Globales del Modelo Random Forest")
    
    col_m1, col_m2 = st.columns([1, 1])
    with col_m1:
        st.metric("Precisión Global (Accuracy)", f"{ml_results['accuracy'] * 100:.2f}%")
        st.write("##### Importancia de Características (Feature Importances)")
        fig_feat = px.bar(
            ml_results['feature_importances'], x='Importancia', y='Caracteristica',
            orientation='h', color='Importancia', color_continuous_scale='Viridis'
        )
        fig_feat.update_layout(template="plotly_dark", height=300)
        st.plotly_chart(fig_feat, use_container_width=True)
        
    with col_m2:
        st.write("##### Matriz de Confusión")
        cm_df = pd.DataFrame(
            ml_results['confusion_matrix'],
            index=['Real: Alto Riesgo', 'Real: Vulnerable', 'Real: Sostenible'],
            columns=['Pred: Alto Riesgo', 'Pred: Vulnerable', 'Pred: Sostenible']
        )
        st.dataframe(cm_df.style.background_gradient(cmap='Blues'), use_container_width=True)

# =============================================================================
# MÓDULO 3: SEGMENTACIÓN Y CLUSTERIZACIÓN
# =============================================================================
elif menu == "📊 Segmentación y Clusterización":
    st.markdown("""
        <div class="header-banner">
            <h1>📊 Segmentación Poblacional (Algoritmo K-Means)</h1>
            <p>Descubrimiento no supervisado de patrones de vulnerabilidad sociodemográfica e ingreso en la población dominicana.</p>
        </div>
    """, unsafe_allow_html=True)
    
    df_clustered, kmeans_model = ml_engine.realizar_clustering_kmeans(df_sim, n_clusters=3)
    
    st.subheader("🌐 Visualización 3D de Clusters Sociodemográficos")
    fig_3d = px.scatter_3d(
        df_clustered.sample(1000, random_state=42),
        x='Ingreso_DOP', y='Educacion', z='Zona',
        color='Nombre_Cluster',
        symbol='Bancarizado',
        opacity=0.7,
        log_x=True,
        labels={'Ingreso_DOP': 'Ingreso Mensual DOP (Escala Log)', 'Educacion': 'Nivel Educativo', 'Zona': 'Zona (0:Rural, 1:Urbana)'},
        color_discrete_sequence=px.colors.qualitative.Set1
    )
    fig_3d.update_layout(template="plotly_dark", height=600)
    st.plotly_chart(fig_3d, use_container_width=True)
    
    st.markdown("---")
    st.subheader("📋 Resumen Estadístico por Cluster Identificado")
    
    summary_df = df_clustered.groupby('Nombre_Cluster').agg({
        'Ingreso_DOP': ['mean', 'median', 'std'],
        'Bancarizado': 'mean',
        'Educacion_Financiera': 'mean',
        'Perfil_Riesgo': lambda x: (x == 0).mean() # Proporción de alto riesgo
    }).reset_index()
    
    summary_df.columns = [
        'Nombre del Cluster', 'Ingreso Promedio (RD$)', 'Ingreso Mediano (RD$)', 'Desv. Est. Ingreso',
        'Tasa Bancarización', 'Tasa Edu. Financiera', 'Proporción Alto Riesgo'
    ]
    
    # Formato porcentual
    summary_df['Tasa Bancarización'] = (summary_df['Tasa Bancarización'] * 100).round(2).astype(str) + '%'
    summary_df['Tasa Edu. Financiera'] = (summary_df['Tasa Edu. Financiera'] * 100).round(2).astype(str) + '%'
    summary_df['Proporción Alto Riesgo'] = (summary_df['Proporción Alto Riesgo'] * 100).round(2).astype(str) + '%'
    summary_df['Ingreso Promedio (RD$)'] = summary_df['Ingreso Promedio (RD$)'].map("RD${:,.2f}".format)
    summary_df['Ingreso Mediano (RD$)'] = summary_df['Ingreso Mediano (RD$)'].map("RD${:,.2f}".format)
    
    st.dataframe(summary_df, use_container_width=True)

# =============================================================================
# MÓDULO 4: CALCULADORA DE COSTO-EFECTIVIDAD
# =============================================================================
elif menu == "💰 Calculadora Costo-Efectividad":
    st.markdown("""
        <div class="header-banner">
            <h1>💰 Calculadora y Simulador de Costo-Efectividad</h1>
            <p>Proyección del presupuesto requerido y del impacto esperado en el sistema educativo nacional basado en el modelo evaluado por el BID (Frisancho, 2017).</p>
        </div>
    """, unsafe_allow_html=True)
    
    c_param, c_out = st.columns([1, 1])
    
    with c_param:
        st.subheader("⚙️ Parámetros de Escalamiento")
        
        opcion_cobertura = st.selectbox(
            "Seleccionar Escenario de Cobertura:",
            options=["Personalizado", "Piloto (Fase 2 - 50,000)", "Secundaria Pública Nacional (861,308)", "Primaria + Secundaria Públicas (2,047,897)"]
        )
        
        if opcion_cobertura == "Piloto (Fase 2 - 50,000)":
            est_val = 50000
        elif opcion_cobertura == "Secundaria Pública Nacional (861,308)":
            est_val = 861308
        elif opcion_cobertura == "Primaria + Secundaria Públicas (2,047,897)":
            est_val = 2047897
        else:
            est_val = st.slider("Número de Estudiantes a Beneficiar:", min_value=10000, max_value=2500000, value=861308, step=10000)
            
        costo_unit_usd = st.number_input("Costo Unitario por Estudiante (USD):", min_value=1.0, max_value=50.0, value=6.6, step=0.5)
        tasa_dop = st.number_input("Tasa de Cambio (RD$ por 1 USD):", min_value=50.0, max_value=75.0, value=60.0, step=0.5)
        
    calc_res = ml_engine.calcular_costo_efectividad(est_val, costo_usd_estudiante=costo_unit_usd, tasa_cambio_dop=tasa_dop)
    
    with c_out:
        st.subheader("📊 Resultados de la Proyección Presupuestaria")
        
        k1, k2 = st.columns(2)
        k1.metric("Costo Total (USD)", f"US${calc_res['costo_total_usd']:,.2f}")
        k2.metric("Costo Total (DOP)", f"RD${calc_res['costo_total_dop']:,.2f}")
        
        st.markdown("""
            <div style="background: rgba(16, 185, 129, 0.15); border: 1px solid #10b981; border-radius: 12px; padding: 18px; margin-top: 15px;">
                <h4 style="color: #10b981; margin: 0 0 8px 0;">📈 Impacto Esperado (Evaluación BID)</h4>
                <ul>
                    <li><b>Mejora en Conocimiento Estudiantil:</b> +0.14 Desviaciones Estándar</li>
                    <li><b>Mejora en Capacitación Docente:</b> +0.30 Desviaciones Estándar</li>
                    <li><b>Costo por Estudiante:</b> US$6.60 / RD$396.00 al año</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    st.subheader("⚖️ Comparativa con la Escala del Gasto Social Educativo de RD")
    
    gasto_utiles_dop = data_module.GASTO_PAQUETE_ESCOLAR_RD['monto_rd']
    gasto_utiles_usd = gasto_utiles_dop / tasa_dop
    
    df_comp = pd.DataFrame({
        'Concepto': ['Educación Financiera Nacional (Secundaria)', 'Gasto Anual en Utiles/Uniformes Gratuitos (MINERD)'],
        'Monto en USD ($)': [calc_res['costo_total_usd'], gasto_utiles_usd]
    })
    
    fig_comp = px.bar(
        df_comp, x='Concepto', y='Monto en USD ($)',
        color='Concepto', text_auto='.2s',
        color_discrete_sequence=['#38bdf8', '#ef4444']
    )
    fig_comp.update_layout(template="plotly_dark", height=380, showlegend=False)
    st.plotly_chart(fig_comp, use_container_width=True)
    st.caption("Demuestra que la curricularización nacional representa una fracción mínima (< 2%) del gasto de equipamiento escolar anual.")

# =============================================================================
# MÓDULO 5: PROGRAMAS Y HOJA DE RUTA
# =============================================================================
elif menu == "🎯 Programas y Hoja de Ruta":
    st.markdown("""
        <div class="header-banner">
            <h1>🎯 Programas Propuestos y Hoja de Ruta Estratégica</h1>
            <p>Ejes estratégicos, programas por nivel educativo y fases institucionales de implementación.</p>
        </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["🏛️ Ejes Estratégicos", "📘 Programas Educativos", "🚀 Fases de Ejecución"])
    
    with tab1:
        st.subheader("Ejes Estratégicos Nacionales")
        for eje in data_module.EJES_ESTRATEGICOS:
            with st.expander(f"📌 {eje['eje']}", expanded=True):
                st.write(eje['descripcion'])
                
    with tab2:
        st.subheader("Programas Específicos por Nivel Educativo")
        df_prog = pd.DataFrame(data_module.PROGRAMAS)
        st.table(df_prog)
        
    with tab3:
        st.subheader("Cronograma Institucional de Ejecución (4 Años)")
        for fase in data_module.FASES:
            with st.container():
                st.markdown(f"### 🗓️ {fase['fase']} ({fase['periodo']})")
                st.markdown(f"**Actividades Clave:** {fase['actividades']}")
                st.progress((fase['duracion_meses'] / 18))
                st.markdown("<hr>", unsafe_allow_html=True)

# =============================================================================
# MÓDULO 6: FUENTES Y EXPORTACIÓN
# =============================================================================
elif menu == "📚 Fuentes y Exportación":
    st.markdown("""
        <div class="header-banner">
            <h1>📚 Fuentes de Información y Exportación de Datos</h1>
            <p>Acceda a los repositorios de datos originales y descargue los datasets analizados en formato CSV.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.subheader("📥 Exportación de Datasets y Resultados")
    
    col_d1, col_d2 = st.columns(2)
    
    with col_d1:
        csv_sim = df_sim.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📄 Descargar Dataset Sintético Calibrado ENIEF (CSV)",
            data=csv_sim,
            file_name="dataset_educacion_financiera_rd.csv",
            mime="text/csv"
        )
        
    with col_d2:
        # Generar reporte de fuentes
        df_fuentes = pd.DataFrame(data_module.FUENTES, columns=['Institucion', 'Titulo_Documento', 'URL'])
        csv_fuentes = df_fuentes.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="🔗 Descargar Lista de Fuentes Oficiales (CSV)",
            data=csv_fuentes,
            file_name="fuentes_investigacion_rd.csv",
            mime="text/csv"
        )
        
    st.markdown("---")
    st.subheader("📖 Listado Completo de Fuentes Consultadas")
    
    for inst, titulo, url in data_module.FUENTES:
        st.markdown(f"- **[{inst}]** [{titulo}]({url})")
