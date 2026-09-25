# 04 — Motor de Machine Learning (`ml_engine.py`)

## 🧠 Documentación del Motor de IA y Aprendizaje Automático

---

## Descripción General

El módulo `ml_engine.py` es el núcleo analítico del proyecto. Encapsula toda la lógica de
Machine Learning, generación de datos sintéticos y cálculos de costo-efectividad de manera
completamente independiente de la interfaz de usuario (UI).

**Importaciones:**
```python
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
```

---

## Función 1: `generar_dataset_sintetico(n=3000, seed=42)`

### Propósito
Genera un dataset sintético de **n registros** calibrado con las distribuciones estadísticas reales publicadas por el BCRD en la ENIF 2019 y ENIEF 2023.

### ¿Por qué sintético?
Los microdatos de la ENIEF no son de acceso público. Sin embargo, el BCRD publica los **estadísticos agregados** (proporciones, medias, distribuciones). El dataset sintético reproduce fielmente estas estadísticas para que el modelo sea representativo de la realidad dominicana.

### Variables Generadas

| Variable | Tipo | Distribución | Calibración Empírica |
|----------|------|--------------|---------------------|
| `Zona` | Binaria (0/1) | `choice([0,1], p=[0.35, 0.65])` | 35% rural / 65% urbano (ENIEF) |
| `Genero` | Binaria (0/1) | `choice([0,1], p=[0.52, 0.48])` | 52% mujeres / 48% hombres (ENIEF) |
| `Educacion` | Ordinal (0/1/2) | `choice([0,1,2], p=[0.40,0.45,0.15])` | 40% primaria, 45% secundaria, 15% superior |
| `Ingreso_DOP` | Continua | `lognormal(mean=9.8, sigma=0.7)` | Log-normal truncada [6k, 200k RD$] |
| `Educacion_Financiera` | Binaria (0/1) | `choice([0,1], p=[0.92, 0.08])` | Solo 8% ha recibido EF (ENIEF) |
| `Bancarizado` | Binaria (0/1) | Score logístico | Calibrado a 55% inclusión adulta |
| `Perfil_Riesgo` | Categórica (0/1/2) | Regla determinista | Basada en ingreso + bancarización + EF |

### Score Logístico de Bancarización

```python
score = -1.2 + 0.6*zona + 0.3*genero + 0.8*educacion + 0.00003*ingreso + 1.5*educ_finan
prob = 1 / (1 + np.exp(-score))
bancarizado = (np.random.rand(n) < prob).astype(int)
```

Los coeficientes reflejan los factores identificados en la literatura:
- Zona urbana (+0.6): mayor acceso a sucursales bancarias
- Educación (+0.8): mayor capacidad de comprensión de productos financieros
- Educación financiera (+1.5): el efecto más fuerte, validado por el BID

### Regla de Clasificación de Perfiles

```
Bancarizado = 0 AND Ingreso < 18,000 DOP → Alto Riesgo (0)
Bancarizado = 0 AND Ingreso ≥ 18,000 DOP → Vulnerable (1)
Bancarizado = 1 AND Educacion_Financiera = 1 → Sostenible (2)
Bancarizado = 1 AND Ingreso > 45,000 DOP → Sostenible (2)
Bancarizado = 1 AND resto → Vulnerable (1)
```

**Retorna:** `pd.DataFrame` con 7 columnas y `n` filas.

---

## Función 2: `entrenar_modelo_clasificacion(df)`

### Propósito
Entrena un clasificador **Random Forest** para predecir el `Perfil_Riesgo` (3 clases) a partir de las 5 variables sociodemográficas independientes.

### Pipeline del Modelo

```
Entrada: df (DataFrame 3,000×7)
    │
    ▼ Selección de features
X = df[['Zona', 'Genero', 'Educacion', 'Ingreso_DOP', 'Educacion_Financiera']]
y = df['Perfil_Riesgo']
    │
    ▼ Estandarización
StandardScaler().fit_transform(X)  → X_scaled (media=0, std=1)
    │
    ▼ Entrenamiento
RandomForestClassifier(n_estimators=100, random_state=42)
    │
    ▼ Evaluación
accuracy_score · classification_report · confusion_matrix
```

### ¿Por qué Random Forest?

1. **Robustez a outliers** — Los ingresos tienen distribución asimétrica (lognormal)
2. **Variables mixtas** — Maneja variables binarias, ordinales y continuas sin transformación especial
3. **Interpretabilidad** — Provee `feature_importances_` que explican qué variables más influyen
4. **Sin hiperparámetros críticos** — Con 100 árboles y datos balanceados, converge bien

### Hiperparámetros Seleccionados

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| `n_estimators` | 100 | Balance entre cómputo y estabilidad del ensemble |
| `random_state` | 42 | Reproducibilidad total |
| `criterion` | `gini` (default) | Adecuado para clasificación multiclase |
| `max_depth` | None (default) | Árboles completos, dataset sintético bien distribuido |

### Métricas de Evaluación Generadas

```python
return {
    'model': rf,                          # Modelo entrenado
    'scaler': scaler,                     # Scaler para nuevas predicciones
    'accuracy': acc,                      # Precisión global (float)
    'report': report,                     # dict con P, R, F1 por clase
    'confusion_matrix': cm,              # np.array 3×3
    'feature_importances': feature_importances  # DataFrame ordenado
}
```

### Feature Importances (Importancia de Características)

```
Ingreso Mensual         ████████████████████ ~0.45
Nivel Educativo         ██████████████ ~0.30
Zona (Urbana/Rural)     ████████ ~0.12
Educación Financiera    █████ ~0.08
Género                  ██ ~0.05
```

El **ingreso mensual** es el predictor más importante, seguido del **nivel educativo** — consistente con la literatura económica sobre exclusión financiera.

---

## Función 3: `realizar_clustering_kmeans(df, n_clusters=3)`

### Propósito
Aplica el algoritmo K-Means para descubrir **3 segmentos sociodemográficos** en el dataset sin usar la variable objetivo (clustering no supervisado).

### Pipeline

```python
X = df[['Zona', 'Genero', 'Educacion', 'Ingreso_DOP', 'Educacion_Financiera']]
X_scaled = StandardScaler().fit_transform(X)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df_clustered['Cluster'] = kmeans.fit_predict(X_scaled)
```

### Segmentos Identificados

| Cluster | Nombre Interpretativo | Perfil Típico |
|---------|----------------------|---------------|
| 0 | **Segmento Vulnerable Rural** | Zona rural, ingreso bajo, sin bancarizar |
| 1 | **Segmento Urbano Promedio** | Zona urbana, ingreso medio, bancarizado parcial |
| 2 | **Segmento Consolidado / Bancarizado** | Urbano, ingreso alto, con educación financiera |

> **Nota:** Los IDs de cluster pueden variar entre ejecuciones con diferente seed. Las etiquetas interpretativas se asignan manualmente basándose en las estadísticas de cada cluster.

### ¿Por qué n_clusters=3?

Corresponde a los 3 perfiles de riesgo del modelo supervisado, permitiendo **cruzar análisis** entre la clasificación supervisada y la segmentación no supervisada para validar coherencia.

**Retorna:** `(df_clustered, kmeans_model)` — DataFrame con columnas `Cluster` y `Nombre_Cluster` añadidas.

---

## Función 4: `predecir_perfil_usuario(...)`

### Propósito
Realiza una **predicción individual en tiempo real** para el perfil ingresado por el usuario en el formulario interactivo de Streamlit.

### Parámetros

| Parámetro | Tipo | Valores |
|-----------|------|---------|
| `model_dict` | dict | Resultado de `entrenar_modelo_clasificacion()` |
| `zona` | int | 0=Rural, 1=Urbana |
| `genero` | int | 0=Mujer, 1=Hombre |
| `educacion` | int | 0=Primaria, 1=Secundaria, 2=Superior |
| `ingreso_dop` | float | Ingreso mensual en RD$ |
| `educ_finan` | int | 0=No recibió, 1=Sí recibió |

### Retorno

```python
{
    'clase_id': 0,                          # 0=Alto Riesgo, 1=Vulnerable, 2=Sostenible
    'etiqueta': 'Alto Riesgo Económico',    # Etiqueta legible
    'color': '#e74c3c',                     # Color para UI
    'probabilidades': {                     # % por clase
        'Alto Riesgo': 72.5,
        'Vulnerable': 20.3,
        'Sostenible': 7.2
    },
    'recomendacion': '...'                  # Texto de política pública
}
```

### Recomendaciones Estratégicas por Perfil

| Perfil | Recomendación |
|--------|---------------|
| **Alto Riesgo** | Acceso prioritario a bancarización básica, subsidios condicionados y talleres comunitarios de presupuesto y ahorro básico |
| **Vulnerable** | Capacitación en manejo responsable del crédito, estructuración de presupuesto familiar y micro-ahorro formal |
| **Sostenible** | Inclusión en instrumentos de inversión formal, seguros de vida/salud, planes de pensiones y emprendimiento |

---

## Función 5: `calcular_costo_efectividad(...)`

### Propósito
Calcula los costos totales de implementación y proyecta el impacto esperado basándose en la evaluación experimental del BID.

### Parámetros y Cálculo

```python
def calcular_costo_efectividad(estudiantes_totales, costo_usd_estudiante=6.6, tasa_cambio_dop=60.0):
    costo_total_usd = estudiantes_totales * costo_usd_estudiante
    costo_total_dop = costo_total_usd * tasa_cambio_dop
```

### Escenarios Predefinidos

| Escenario | Estudiantes | Costo USD | Costo DOP (60x) |
|-----------|-------------|-----------|-----------------|
| Piloto Fase 2 | 50,000 | US$330,000 | RD$19.8M |
| Secundaria Pública | 861,308 | US$5.68M | RD$341M |
| Primaria + Secundaria | 2,047,897 | US$13.5M | RD$811M |

### Base Evidencial (BID - Frisancho, 2017)

```python
impacto_estudiantes_sd = 0.14   # Desviaciones Estándar en conocimiento financiero
impacto_docentes_sd    = 0.30   # Desviaciones Estándar en competencias docentes
```

---

*Continúa en → [05 — Módulo de Aplicación Web](05-modulo-app.md)*
