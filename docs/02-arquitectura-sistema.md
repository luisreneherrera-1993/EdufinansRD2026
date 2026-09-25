# 02 — Arquitectura del Sistema

## 🏗️ Arquitectura y Estructura del Proyecto

---

## Estructura de Archivos

```
Practica final Python 2026/
│
├── index.html                              # 🌐 Landing Page (GitHub Pages)
├── README.md                               # 📄 Documentación principal del repo
├── requirements.txt                        # 📦 Dependencias Python
│
├── main.py                                 # 🚀 Punto de entrada / Script lanzador
├── app.py                                  # ⚡ Aplicación Web Streamlit (6 módulos)
├── ml_engine.py                            # 🧠 Motor de Machine Learning
├── data.py                                 # 🗃️ Módulo de datos empíricos calibrados
│
├── Cuaderno_Educacion_Financiera_RD.ipynb  # 📓 Análisis exploratorio Jupyter
│
├── assets/
│   └── images/                             # 🖼️ Imágenes de la landing page
│       ├── hero_banner.jpg
│       ├── ai_predictor.jpg
│       ├── kmeans_clustering.jpg
│       ├── cost_effectiveness.jpg
│       └── roadmap_phases.jpg
│
├── docs/                                   # 📚 Documentación técnica paso a paso
│   ├── README.md                           # Índice de documentación
│   ├── 01-descripcion-proyecto.md
│   ├── 02-arquitectura-sistema.md          # (este archivo)
│   ├── 03-modulo-datos.md
│   ├── 04-modulo-ml.md
│   ├── 05-modulo-app.md
│   ├── 06-instalacion-ejecucion.md
│   └── 07-fuentes-referencias.md
│
├── Datos Investigativos/                   # 📊 Datos e investigaciones de apoyo
└── __pycache__/                            # Cache Python (auto-generado)
```

---

## Flujo de Datos del Sistema

```
┌─────────────────────────────────────────────────────────────────┐
│                    FUENTES DE INFORMACIÓN                        │
│  BCRD · ENIEF 2023 · SB · MINERD · BID · OCDE · UNESCO         │
└──────────────────────┬──────────────────────────────────────────┘
                       │ Datos empíricos calibrados
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│                        data.py                                   │
│  • Constantes y diccionarios de datos reales                    │
│  • Indicadores ENIF/ENIEF · Matrícula · Gasto público          │
│  • Programas educativos · Fases estratégicas                    │
└──────────────────────┬──────────────────────────────────────────┘
                       │ import data as data_module
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│                      ml_engine.py                                │
│  ┌─────────────────────┐   ┌──────────────────────────────┐    │
│  │ generar_dataset_    │   │  entrenar_modelo_            │    │
│  │ sintetico(n=3000)   │──▶│  clasificacion()             │    │
│  │ • Distribuciones    │   │  • RandomForestClassifier    │    │
│  │   lognormales ENIEF │   │  • StandardScaler            │    │
│  │ • Score logístico   │   │  • accuracy, CM, features    │    │
│  └─────────────────────┘   └──────────────────────────────┘    │
│  ┌─────────────────────┐   ┌──────────────────────────────┐    │
│  │ realizar_clustering │   │  predecir_perfil_usuario()   │    │
│  │ _kmeans(k=3)        │   │  • Predicción individual     │    │
│  │ • 3 segmentos       │   │  • Probabilidades 3 clases   │    │
│  │   sociodemográficos │   │  • Recomendación estratégica │    │
│  └─────────────────────┘   └──────────────────────────────┘    │
│  ┌────────────────────────────────────────────────────────┐    │
│  │ calcular_costo_efectividad(estudiantes, usd, tasa)     │    │
│  │ • Proyección USD/DOP · Impacto BID · Comparativa      │    │
│  └────────────────────────────────────────────────────────┘    │
└──────────────────────┬──────────────────────────────────────────┘
                       │ import ml_engine
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│                        app.py                                    │
│  Módulo 1: 🏠 Inicio y Diagnóstico (KPIs + Charts Plotly)      │
│  Módulo 2: 🤖 Predicción de Riesgo IA (Random Forest Form)     │
│  Módulo 3: 📊 Segmentación K-Means (3D Scatter)                │
│  Módulo 4: 💰 Calculadora Costo-Efectividad (Simulator)        │
│  Módulo 5: 🎯 Programas y Hoja de Ruta (Timeline)              │
│  Módulo 6: 📚 Fuentes y Exportación CSV                        │
└──────────────────────┬──────────────────────────────────────────┘
                       │ subprocess.run(streamlit run app.py)
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│                       main.py                                    │
│  Script lanzador que invoca Streamlit automáticamente           │
└──────────────────────┬──────────────────────────────────────────┘
                       │ HTTP
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│               INTERFAZ WEB · localhost:8501                      │
│  Glassmorphism Dashboard · Plotly Interactive · Streamlit UI    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Decisiones de Diseño Arquitectónico

### 1. Separación de Responsabilidades (SoC)

| Módulo | Responsabilidad Única |
|--------|-----------------------|
| `data.py` | Única fuente de verdad de datos empíricos y estructurados |
| `ml_engine.py` | Toda la lógica de ML encapsulada, sin dependencias de UI |
| `app.py` | Presentación y UX exclusivamente, delega la lógica a ml_engine |
| `main.py` | Solo punto de entrada, sin lógica de negocio |

### 2. Caching de Streamlit

Se usan los decoradores `@st.cache_data` y `@st.cache_resource` para evitar regenerar el dataset y reentrenar el modelo en cada interacción del usuario:

```python
@st.cache_data
def get_dataset():
    return ml_engine.generar_dataset_sintetico(n=3000, seed=42)

@st.cache_resource
def get_ml_model(df):
    return ml_engine.entrenar_modelo_clasificacion(df)
```

### 3. Seed Fija para Reproducibilidad

Todas las operaciones aleatorias usan `seed=42` y `random_state=42` para garantizar que los resultados sean **completamente reproducibles** en cualquier máquina.

### 4. Dataset Sintético Calibrado

En lugar de depender de microdatos privados de la ENIEF (no públicos), el sistema genera un dataset sintético de 3,000 registros calibrado con las **proporciones y distribuciones reales** publicadas por el BCRD:
- 35% rural / 65% urbano
- 52% mujeres / 48% hombres
- Distribución lognormal de ingresos (media 9.8, sigma 0.7)
- 92% sin educación financiera previa

---

## Patrones de UI — Glassmorphism

La aplicación implementa un diseño moderno **Dark Glassmorphism** con:

```css
/* Tarjetas con efecto vidrio */
background: rgba(30, 41, 59, 0.7);
backdrop-filter: blur(4px);
border: 1px solid rgba(255, 255, 255, 0.1);
box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
```

Paleta de colores del sistema:
- **Fondo principal:** `#0f172a` (Dark Navy)
- **Acento principal:** `#38bdf8` (Sky Teal)
- **Alto Riesgo:** `#ef4444` (Red)
- **Vulnerable:** `#f59e0b` (Amber)
- **Sostenible:** `#10b981` (Emerald)

---

*Continúa en → [03 — Módulo de Datos](03-modulo-datos.md)*
