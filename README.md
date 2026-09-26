# 🇩🇴 Plataforma de Diagnóstico, Modelado de IA y Estrategia de Educación Financiera en República Dominicana

<!-- Tecnologías Core -->
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B?logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3%2B-F7931E?logo=scikit-learn&logoColor=white)

<!-- Ciencia de Datos -->
![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.24%2B-013243?logo=numpy&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.15%2B-3F4F75?logo=plotly&logoColor=white)

<!-- Herramientas -->
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7%2B-11557C?logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-0.12%2B-4C72B0?logoColor=white)

<!-- Proyecto -->
![UFHEC](https://img.shields.io/badge/UFHEC-Práctica%20Final%202026-006400)
![Licencia](https://img.shields.io/badge/Licencia-MIT-yellow)
![Estado](https://img.shields.io/badge/Estado-Completado-brightgreen)
![Landing Page](https://img.shields.io/badge/🌐%20Landing%20Page-Ver%20Online-38bdf8)

<!-- ML Tags -->
![Random Forest](https://img.shields.io/badge/ML-Random%20Forest-9B59B6)
![K-Means](https://img.shields.io/badge/ML-K--Means%20Clustering-E74C3C)
![Datos](https://img.shields.io/badge/Datos-BCRD%20%7C%20MINERD%20%7C%20BID-1ABC9C)

---

## 🔗 Entregables del Proyecto

| # | Entregable | Descripción | Enlace |
|---|-----------|-------------|--------|
| 1 | 📁 **Repositorio GitHub** | Código fuente completo del proyecto | [![GitHub](https://img.shields.io/badge/GitHub-EdufinansRD2026-181717?logo=github&logoColor=white)](https://github.com/luisreneherrera-1993/EdufinansRD2026) |
| 2 | 🌐 **Landing Page** | Presentación visual del proyecto (GitHub Pages) | [![Landing](https://img.shields.io/badge/🌐%20Ver%20Landing%20Page-38bdf8)](https://luisreneherrera-1993.github.io/EdufinansRD2026/) |
| 3 | ⚡ **App Streamlit** | Plataforma interactiva con IA desplegada en la nube | [![Streamlit](https://img.shields.io/badge/Streamlit-EdufinansRD2026-FF4B4B?logo=streamlit&logoColor=white)](https://edufinansrd2026.streamlit.app/) |
| 4 | 📚 **Documentación** | Documentación técnica paso a paso en `/docs/` | [![Docs](https://img.shields.io/badge/Docs-Ver%20en%20GitHub-1ABC9C?logo=github&logoColor=white)](https://github.com/luisreneherrera-1993/EdufinansRD2026/tree/main/docs) |

---
## 📋 Table of Contents / Índice
1. [Descripción](#-descripción)
2. [Objetivo](#-objetivo)
3. [Funcionalidades](#-funcionalidades)
4. [Tecnologías Utilizadas](#-tecnologías-utilizadas)
5. [Estructura del Proyecto](#-estructura-del-proyecto)
6. [Instrucciones de Ejecución](#-instrucciones-de-ejecución)
7. [Documentación Técnica](docs/README.md)
8. [Fuentes y Referencias Oficiales](#-fuentes-y-referencias-oficiales)

---

## 📝 Descripción

Esta aplicación interactiva es un sistema de soporte a decisiones públicas y diagnóstico analítico basado en datos reales y calibrados de la **Primera y Segunda Encuesta Nacional de Inclusión Financiera (ENIF 2019 / ENIEF 2023)** del **Banco Central de la República Dominicana (BCRD)**, informes de la **Superintendencia de Bancos (SB)**, el **Ministerio de Educación (MINERD)** y evidencia experimental internacional del **Banco Interamericano de Desarrollo (BID)** y la **OCDE**.

El sistema integra:
- Un **módulo de datos empíricos y trazables (`data.py`)**.
- Un **cuaderno de investigación y modelado cuantitativo (`Cuaderno_Educacion_Financiera_RD.ipynb`)**.
- Un **motor de inteligencia artificial y aprendizaje automático (`ml_engine.py`)**.
- Una **plataforma web interactiva con interfaz tipo Dashboard Glassmorphism (`app.py` / `main.py`)**.

El proyecto propone una hoja de ruta concreta para la **curricularización obligatoria de la educación económica y financiera** en el sistema educativo dominicano, evaluando su viabilidad económica, costo-efectividad e impacto en la reducción de la brecha de género y la bancarización informal.

---

## 🎯 Objetivo

El objetivo principal de esta plataforma es **analizar, clasificar y simular la costo-efectividad de la implementación nacional de la Educación Económica y Financiera en República Dominicana**.

### Objetivos Específicos:
1. **Diagnosticar** la situación actual de inclusión financiera en RD (donde solo el 55% de la población adulta posee un producto financiero y el 70% de los hogares no cubre sus gastos mensuales).
2. **Entrenar modelos de Inteligencia Artificial (Random Forest & K-Means)** para clasificar perfiles de vulnerabilidad económica (`Alto Riesgo`, `Vulnerable`, `Sostenible`) e identificar agrupamientos sociodemográficos.
3. **Simular escenarios presupuestarios** basados en el costo unitario de **US$6.60 por estudiante/año** (Piloto BID - Perú), demostrando que la cobertura nacional en secundaria pública (861,308 estudiantes) requiere apenas **US$5.68 millones**, equivalente a menos del 2% del gasto social anual en útiles escolares del MINERD.
4. **Proporcionar una herramienta visual e interactiva** para la toma de decisiones por parte de autoridades educativas y financieras (BCRD, MINERD, SB, INAFOCAM).

---

## ⚙️ Funcionalidades

La aplicación web cuenta con 6 módulos interactivos principales:

1. **🏠 Inicio y Diagnóstico Nacional:**
   - Métricas KPI clave (Tasas de inclusión, aprendizaje de ahorro, cobertura de programas).
   - Visualización gráfica interactiva de la evolución 2019-2023 y la matrícula escolar por nivel (2024-2025).
   - Indicadores de brecha de género en el sistema financiero (morosidad vs barreras de acceso).

2. **🤖 Predictor de Riesgo y Vulnerabilidad Económica (Random Forest):**
   - Formulario interactivo en tiempo real donde el usuario ingresa atributos sociodemográficos (Zona, Género, Educación, Ingreso Mensual en RD$, Educación Financiera previa).
   - Clasificación instantánea del perfil (`Alto Riesgo Económico`, `Vulnerable`, `Sostenible`).
   - Gráfico de barras de probabilidades y recomendaciones estratégicas personalizadas.
   - Reporte de métricas del modelo (Precisión, Matriz de Confusión e Importancia de Características).

3. **📊 Segmentación Poblacional (Algoritmo K-Means):**
   - Visualización Scatter 3D en escala logarítmica de clusters sociodemográficos.
   - Tabla comparativa de promedios de ingresos, tasas de bancarización y niveles de riesgo por segmento.

4. **💰 Calculadora y Simulador de Costo-Efectividad:**
   - Selección dinámica de escenarios de cobertura (Piloto 50k, Secundaria Pública 861k, Total Público 2M o personalizado vía slider).
   - Ajuste de costo unitario por estudiante (USD) y tasa de cambio (RD$/USD).
   - Proyección del impacto esperado en desviaciones estándar (+0.14 DE en estudiantes, +0.30 DE en docentes).
   - Gráficos comparativos con el gasto social público ejecutado en paquetes escolares (RD$4.69 mil millones).

5. **🎯 Programas Educativos y Hoja de Ruta Estratégica:**
   - Catálogo detallado de contenidos y programas propuestos por nivel: *Mis Primeras Finanzas*, *Educación Económica y Financiera*, *Finanzas para Emprender*, *Finanzas en Familia* y *Formación Docente*.
   - Hoja de ruta dividida en 4 Fases (Diseño, Piloto, Escalamiento Nacional y Consolidación) con barras de avance cronológico.

6. **📚 Fuentes y Exportación de Datos:**
   - Botón de descarga en formato CSV del dataset sintético generado (3,000 registros calibrados).
   - Botón de descarga de la lista de fuentes institucionales verificadas.
   - Enlaces directos a las publicaciones del BCRD, SB, MINERD, BID, OCDE y UNESCO.

---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje de Programación:** Python 3.10+
- **Framework Web de Interfaz:** [Streamlit](https://streamlit.io/) (v1.30+)
- **Machine Learning & Ciencia de Datos:**
  - [Scikit-Learn](https://scikit-learn.org/) (Random Forest Classifier, K-Means Clustering, StandardScaler)
  - [Pandas](https://pandas.pydata.org/) (Manipulación y estructuración de dataframes)
  - [NumPy](https://numpy.org/) (Generación de distribuciones log-normales y operaciones matriciales)
- **Visualización Gráfica Interactiva:**
  - [Plotly Express & Graph Objects](https://plotly.com/python/) (Gráficos 3D, Pie, Bar y Scatter)
  - [Seaborn](https://seaborn.pydata.org/) & [Matplotlib](https://matplotlib.org/) (Generación de gráficos para el cuaderno Jupyter)
- **Entorno de Cuadernos:** Jupyter Notebook (`.ipynb`)

---

## 📁 Estructura del Proyecto

```text
Practica final Python 2026/
├── Cuaderno_Educacion_Financiera_RD.ipynb   # Cuaderno Jupyter con diagnóstico, ML y análisis
├── data.py                                  # Módulo con datos empíricos y fuentes del BCRD/MINERD
├── ml_engine.py                             # Motor de Machine Learning (Random Forest & K-Means)
├── app.py                                   # Aplicación Web Interactiva principal (Streamlit)
├── main.py                                  # Script lanzador principal ejecutable
├── requirements.txt                         # Dependencias y librerías necesarias
└── README.md                                # Documentación completa del proyecto
```

---

## 🚀 Instrucciones de Ejecución

Siga estos sencillos pasos para instalar y ejecutar la aplicación en su entorno local:

### 1. Prerrequisitos
Asegúrese de tener instalado **Python 3.10 o superior** y `pip`. Puede verificar ejecutando:
```bash
python --version
```

### 2. Clonar o Ubicarse en el Directorio del Proyecto
Abra su terminal o consola de comandos en la carpeta del proyecto:
```bash
cd "Practica final Python 2026"
```

### 3. Instalar las Dependencias
Ejecute el siguiente comando para instalar todas las librerías necesarias especificadas en `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la Aplicación Web Interactiva

Opción A (Recomendada - Vía Script Principal):
```bash
python main.py
```

Opción B (Directamente con Streamlit):
```bash
streamlit run app.py
```

Al ejecutar cualquiera de estos comandos, la aplicación se abrirá automáticamente en su navegador web en la dirección:
`http://localhost:8501`

### 5. Ejecutar o Inspeccionar el Cuaderno Jupyter
Para explorar el análisis paso a paso y volver a ejecutar el modelo dentro de Jupyter:
```bash
jupyter notebook Cuaderno_Educacion_Financiera_RD.ipynb
```

---

## 📚 Fuentes y Referencias Oficiales

1. **Banco Central de la República Dominicana (BCRD):** *Resumen Ejecutivo ENIEF 2023* & *Guía de Habilidades Económicas*.
2. **Superintendencia de Bancos (SB):** *Informe Hacia un Sistema Financiero Inclusivo y Sostenible 2025*.
3. **Ministerio de Educación (MINERD) & Banreservas:** *Acuerdo Marco de Educación Financiera Escolar (2024)*.
4. **Banco Interamericano de Desarrollo (BID):** *Frisancho, V. (2017). Evaluación Experimental del Piloto Finanzas en mi Colegio*.
5. **OCDE / INFE:** *Encuesta Internacional de Alfabetización Financiera de Adultos (2020)*.

---
**Desarrollado para:** Práctica Final de Python 2026 — Universidad Federico Henríquez y Carvajal (UFHEC).
