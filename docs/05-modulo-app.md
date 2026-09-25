# 05 — Aplicación Web Interactiva (`app.py`)

## ⚡ Documentación de la Aplicación Web Streamlit

---

## Descripción General

`app.py` es la capa de presentación del sistema. Implementa una aplicación web de página única con **6 módulos de navegación** usando Streamlit, Plotly y CSS personalizado con diseño Glassmorphism.

**Principio:** `app.py` no contiene lógica de negocio ni ML. Solo orquesta la presentación de datos y delega todo procesamiento a `ml_engine.py` y `data.py`.

---

## Configuración Inicial

```python
st.set_page_config(
    page_title="Educación Financiera RD | Diagnóstico e IA",
    page_icon="🇩🇴",
    layout="wide",
    initial_sidebar_state="expanded"
)
```

- **`layout="wide"`**: Usa el ancho completo del navegador para maximizar el espacio de visualizaciones
- **`initial_sidebar_state="expanded"`**: El menú lateral está visible por defecto

---

## Sistema de Estilos — Glassmorphism CSS

La aplicación implementa un diseño de **Dark Glassmorphism** inyectado como HTML:

```css
.stApp {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
}
.metric-card {
    background: rgba(30, 41, 59, 0.7);
    backdrop-filter: blur(4px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
}
```

**Badges de clasificación con colores semánticos:**
- `.badge-high` → `#ef4444` (Rojo — Alto Riesgo)
- `.badge-vulnerable` → `#f59e0b` (Ámbar — Vulnerable)
- `.badge-sustainable` → `#10b981` (Verde esmeralda — Sostenible)

---

## Carga de Datos con Cache

```python
@st.cache_data
def get_dataset():
    return ml_engine.generar_dataset_sintetico(n=3000, seed=42)

@st.cache_resource
def get_ml_model(df):
    return ml_engine.entrenar_modelo_clasificacion(df)

df_sim = get_dataset()
ml_results = get_ml_model(df_sim)
```

- `@st.cache_data` — Cachea el DataFrame (serializable, puede compartirse entre sesiones)
- `@st.cache_resource` — Cachea el modelo ML (objeto no serializable, compartido como recurso global)
- El modelo se entrena **una sola vez** al arrancar la app y se reutiliza en todas las interacciones

---

## Sidebar — Navegación

```python
menu = st.sidebar.radio("Seleccione un Módulo:", [
    "🏠 Inicio y Diagnóstico",
    "🤖 Predicción de Riesgo IA",
    "📊 Segmentación y Clusterización",
    "💰 Calculadora Costo-Efectividad",
    "🎯 Programas y Hoja de Ruta",
    "📚 Fuentes y Exportación"
])
```

La navegación usa un `radio` widget para selección única de módulo. El contenido principal cambia con bloques `if/elif`.

---

## Módulo 1: Inicio y Diagnóstico Nacional

**Elementos de UI:**
- **4 KPI Cards** en HTML personalizado (55%, 78.3%, 3%, 861,308)
- **Gráfico de Barras** (Plotly): Evolución inclusión financiera 2019→2023
- **Gráfico Pie/Donut** (Plotly): Distribución matrícula escolar por nivel
- **Gráfico Barras Horizontal** (Plotly): Indicadores de género y crédito (SB)
- **Lista numerada**: 6 causas estructurales identificadas

```python
fig_inc = px.bar(df_inc, x='anios', y='porcentaje_con_producto_financiero',
    color_discrete_sequence=['#38bdf8'])
fig_inc.update_layout(yaxis_range=[0, 100], template="plotly_dark")
```

---

## Módulo 2: Predictor de Riesgo IA

**Flujo de interacción:**

```
Usuario completa formulario
    │  zona, genero, educacion, ingreso, educ_finan
    ▼
st.form_submit_button("🔍 Evaluar Perfil Económico")
    │
    ▼
ml_engine.predecir_perfil_usuario(ml_results, ...)
    │
    ▼
Mostrar:
  • Badge de clasificación (HTML con color semántico)
  • Gráfico de barras de probabilidades (Plotly)
  • st.warning con recomendación estratégica
    │
    ▼ (sección separada)
Métricas del Modelo:
  • st.metric("Precisión Global", f"{acc*100:.2f}%")
  • Feature Importances (Plotly bar horizontal)
  • Matriz de Confusión (st.dataframe con background_gradient)
```

**Gestión de estado:**
```python
if submit_btn or 'prediction_done' in st.session_state:
    st.session_state['prediction_done'] = True
```
Permite que el resultado persista después de una interacción (no se borra al refrescar).

---

## Módulo 3: Segmentación y Clusterización

```python
df_clustered, kmeans_model = ml_engine.realizar_clustering_kmeans(df_sim, n_clusters=3)

fig_3d = px.scatter_3d(
    df_clustered.sample(1000, random_state=42),  # 1k puntos para rendimiento
    x='Ingreso_DOP', y='Educacion', z='Zona',
    color='Nombre_Cluster',
    log_x=True,  # Escala logarítmica para ingreso (distribución lognormal)
)
```

**Tabla resumen por cluster:**
```python
summary_df = df_clustered.groupby('Nombre_Cluster').agg({
    'Ingreso_DOP': ['mean', 'median', 'std'],
    'Bancarizado': 'mean',
    'Educacion_Financiera': 'mean',
    'Perfil_Riesgo': lambda x: (x == 0).mean()
})
```

---

## Módulo 4: Calculadora Costo-Efectividad

**Controles interactivos:**
```python
opcion_cobertura = st.selectbox("Escenario de Cobertura:", [
    "Personalizado", "Piloto (50,000)", "Secundaria (861,308)", "Primaria+Secundaria (2,047,897)"
])
est_val = st.slider("Estudiantes:", 10000, 2500000, 861308)  # solo si Personalizado
costo_unit_usd = st.number_input("Costo Unitario (USD):", value=6.6)
tasa_dop = st.number_input("Tasa de Cambio:", value=60.0)
```

**Comparativa visual:**
```python
df_comp = pd.DataFrame({
    'Concepto': ['Educación Financiera', 'Gasto MINERD Útiles'],
    'Monto en USD ($)': [calc_res['costo_total_usd'], gasto_utiles_usd]
})
fig_comp = px.bar(df_comp, color_discrete_sequence=['#38bdf8', '#ef4444'])
```

---

## Módulo 5: Programas y Hoja de Ruta

**Tabs anidados:**
```python
tab1, tab2, tab3 = st.tabs(["🏛️ Ejes Estratégicos", "📘 Programas", "🚀 Fases"])

with tab1:
    for eje in data_module.EJES_ESTRATEGICOS:
        with st.expander(f"📌 {eje['eje']}", expanded=True):
            st.write(eje['descripcion'])

with tab3:
    for fase in data_module.FASES:
        st.markdown(f"### 🗓️ {fase['fase']} ({fase['periodo']})")
        st.progress((fase['duracion_meses'] / 18))  # 18 meses = 100%
```

---

## Módulo 6: Fuentes y Exportación

```python
# Exportar dataset sintético
csv_sim = df_sim.to_csv(index=False).encode('utf-8')
st.download_button("📄 Descargar Dataset ENIEF Calibrado (CSV)", csv_sim,
    file_name="dataset_educacion_financiera_rd.csv", mime="text/csv")

# Exportar lista de fuentes
df_fuentes = pd.DataFrame(data_module.FUENTES, columns=['Institucion', 'Titulo', 'URL'])
csv_fuentes = df_fuentes.to_csv(index=False).encode('utf-8')
st.download_button("🔗 Descargar Fuentes Oficiales (CSV)", csv_fuentes,
    file_name="fuentes_investigacion_rd.csv", mime="text/csv")
```

---

*Continúa en → [06 — Guía de Instalación y Ejecución](06-instalacion-ejecucion.md)*
