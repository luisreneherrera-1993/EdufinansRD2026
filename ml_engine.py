"""
Modulo de Machine Learning y Analisis Predictivo para Educacion Financiera en RD.
Basado en el Cuaderno de Investigacion 'Cuaderno_Educacion_Financiera_RD.ipynb'.
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def generar_dataset_sintetico(n=3000, seed=42):
    """
    Genera un dataset sintético calibrado con las tasas empíricas de la ENIEF 2023 y BCRD.
    """
    np.random.seed(seed)
    
    # Variables sociodemográficas
    zona = np.random.choice([0, 1], size=n, p=[0.35, 0.65])  # 0: Rural, 1: Urbano
    genero = np.random.choice([0, 1], size=n, p=[0.52, 0.48])  # 0: Mujer, 1: Hombre
    educacion = np.random.choice([0, 1, 2], size=n, p=[0.40, 0.45, 0.15])  # 0: Primaria, 1: Secundaria, 2: Superior
    ingreso = np.clip(np.random.lognormal(mean=9.8, sigma=0.7, size=n), 6000, 200000)
    educ_finan = np.random.choice([0, 1], size=n, p=[0.92, 0.08])  # 0: No recibió, 1: Sí recibió
    
    # Score logístico de bancarización / inclusión
    score = -1.2 + 0.6*zona + 0.3*genero + 0.8*educacion + 0.00003*ingreso + 1.5*educ_finan
    prob = 1 / (1 + np.exp(-score))
    bancarizado = (np.random.rand(n) < prob).astype(int)
    
    # Perfil de Riesgo:
    # 0: Alto Riesgo (Excluido / Ingreso < 18,000 DOP)
    # 1: Vulnerable (Bancarizado con bajo ingreso o informal)
    # 2: Sostenible (Bancarizado + Educación Financiera o Ingresos sólidos)
    perfil = np.where(
        bancarizado == 0,
        np.where(ingreso < 18000, 0, 1),
        np.where(educ_finan == 1, 2, np.where(ingreso > 45000, 2, 1))
    )
    
    df = pd.DataFrame({
        'Zona': zona,
        'Genero': genero,
        'Educacion': educacion,
        'Ingreso_DOP': ingreso,
        'Educacion_Financiera': educ_finan,
        'Bancarizado': bancarizado,
        'Perfil_Riesgo': perfil
    })
    
    return df

def entrenar_modelo_clasificacion(df):
    """
    Entrena un modelo Random Forest Classifier para predecir el Perfil de Riesgo Económico.
    """
    X = df[['Zona', 'Genero', 'Educacion', 'Ingreso_DOP', 'Educacion_Financiera']]
    y = df['Perfil_Riesgo']
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_scaled, y)
    
    y_pred = rf.predict(X_scaled)
    acc = accuracy_score(y, y_pred)
    report = classification_report(y, y_pred, target_names=['Alto Riesgo', 'Vulnerable', 'Sostenible'], output_dict=True)
    cm = confusion_matrix(y, y_pred)
    
    feature_importances = pd.DataFrame({
        'Caracteristica': ['Zona (Urbana/Rural)', 'Género', 'Nivel Educativo', 'Ingreso Mensual', 'Recibió Edu. Financiera'],
        'Importancia': rf.feature_importances_
    }).sort_values(by='Importancia', ascending=False)
    
    return {
        'model': rf,
        'scaler': scaler,
        'accuracy': acc,
        'report': report,
        'confusion_matrix': cm,
        'feature_importances': feature_importances
    }

def realizar_clustering_kmeans(df, n_clusters=3):
    """
    Realiza la segmentación K-Means de los perfiles sociodemográficos.
    """
    X = df[['Zona', 'Genero', 'Educacion', 'Ingreso_DOP', 'Educacion_Financiera']]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    df_clustered = df.copy()
    df_clustered['Cluster'] = kmeans.fit_predict(X_scaled)
    
    # Nombres interpretativos para clusters
    cluster_labels = {
        0: 'Segmento Vulnerable Rural',
        1: 'Segmento Urbano Promedio',
        2: 'Segmento Consolidado / Bancarizado'
    }
    df_clustered['Nombre_Cluster'] = df_clustered['Cluster'].map(cluster_labels)
    
    return df_clustered, kmeans

def predecir_perfil_usuario(model_dict, zona, genero, educacion, ingreso_dop, educ_finan):
    """
    Realiza una predicción individual basada en las entradas del usuario.
    """
    model = model_dict['model']
    scaler = model_dict['scaler']
    
    X_user = np.array([[zona, genero, educacion, ingreso_dop, educ_finan]])
    X_user_scaled = scaler.transform(X_user)
    
    pred_class = model.predict(X_user_scaled)[0]
    probabilities = model.predict_proba(X_user_scaled)[0]
    
    etiquetas = {0: 'Alto Riesgo Económico', 1: 'Vulnerable', 2: 'Sostenible'}
    colores = {0: '#e74c3c', 1: '#f39c12', 2: '#2ecc71'}
    
    recomendaciones = {
        0: "Se recomienda acceso prioritario a programas estatales de bancarización básica, subsidios condicionados y talleres comunitarios de presupuesto y ahorro básico.",
        1: "Se sugiere capacitación en manejo responsable del crédito, estructuración de presupuesto familiar y micro-ahorro formal para prevenir sobreendeudamiento.",
        2: "Perfil apto para inclusión en instrumentos de inversión formal, seguros de vida/salud, planes de pensiones y emprendimiento de mayor escala."
    }
    
    return {
        'clase_id': pred_class,
        'etiqueta': etiquetas[pred_class],
        'color': colores[pred_class],
        'probabilidades': {
            'Alto Riesgo': round(probabilities[0] * 100, 2),
            'Vulnerable': round(probabilities[1] * 100, 2),
            'Sostenible': round(probabilities[2] * 100, 2)
        },
        'recomendacion': recomendaciones[pred_class]
    }

def calcular_costo_efectividad(estudiantes_totales, costo_usd_estudiante=6.6, tasa_cambio_dop=60.0):
    """
    Calcula los presupuestos y proyecciones de costo-efectividad.
    """
    costo_total_usd = estudiantes_totales * costo_usd_estudiante
    costo_total_dop = costo_total_usd * tasa_cambio_dop
    
    # Impacto estimado basado en Frisancho (2017) BID
    impacto_estudiantes_sd = 0.14  # Desviaciones estándar en conocimiento
    impacto_docentes_sd = 0.30
    
    return {
        'estudiantes': estudiantes_totales,
        'costo_unitario_usd': costo_usd_estudiante,
        'costo_total_usd': costo_total_usd,
        'costo_total_dop': costo_total_dop,
        'impacto_estudiantes_sd': impacto_estudiantes_sd,
        'impacto_docentes_sd': impacto_docentes_sd
    }
