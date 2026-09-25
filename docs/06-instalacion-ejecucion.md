# 06 — Guía de Instalación y Ejecución

## 🚀 Cómo Instalar y Ejecutar el Proyecto

---

## Prerrequisitos del Sistema

| Requisito | Versión Mínima | Verificación |
|-----------|---------------|--------------|
| Python | 3.10+ | `python --version` |
| pip | 22.0+ | `pip --version` |
| Jupyter Notebook | Opcional (para `.ipynb`) | `jupyter --version` |
| Navegador Web | Chrome / Firefox / Edge | — |

> **Nota para Windows:** Se recomienda usar **PowerShell** o **Símbolo del Sistema** con permisos de administrador para la instalación de paquetes.

---

## Paso 1: Clonar o Descargar el Proyecto

### Opción A: Clonar con Git
```bash
git clone https://github.com/TU_USUARIO/practica-final-python-2026.git
cd "practica-final-python-2026"
```

### Opción B: Descarga Directa (ZIP)
1. Descargar el archivo ZIP desde GitHub
2. Extraer en la ubicación deseada
3. Abrir terminal en la carpeta extraída

---

## Paso 2: Crear un Entorno Virtual (Recomendado)

```bash
# Crear entorno virtual
python -m venv venv

# Activar en Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Activar en Windows (CMD)
venv\Scripts\activate.bat

# Activar en Linux/macOS
source venv/bin/activate
```

> ⚠️ Si PowerShell bloquea la ejecución de scripts, ejecute primero:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

---

## Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

### Dependencias Instaladas

| Paquete | Versión | Uso |
|---------|---------|-----|
| `streamlit` | ≥1.30.0 | Framework de la aplicación web |
| `pandas` | ≥2.0.0 | Manipulación de DataFrames |
| `numpy` | ≥1.24.0 | Operaciones matriciales y distribuciones |
| `scikit-learn` | ≥1.3.0 | Random Forest, K-Means, StandardScaler |
| `plotly` | ≥5.15.0 | Gráficos interactivos 2D y 3D |
| `matplotlib` | ≥3.7.0 | Gráficos para Jupyter Notebook |
| `seaborn` | ≥0.12.0 | Visualizaciones estadísticas en Jupyter |
| `joblib` | ≥1.3.0 | Serialización de modelos ML |

**Tiempo estimado de instalación:** 2-5 minutos (dependiendo de la conexión)

---

## Paso 4: Ejecutar la Aplicación Web

### Opción A: Vía Script Principal (Recomendada)
```bash
python main.py
```

Salida esperada en terminal:
```
=====================================================================
 🇩🇴 PLATAFORMA DE EDUCACIÓN FINANCIERA EN REPÚBLICA DOMINICANA
=====================================================================
Iniciando la aplicación web interactiva (Streamlit)...
Si no se abre automáticamente el navegador, diríjase a: http://localhost:8501

  You can now view your Streamlit app in your browser.
  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

### Opción B: Directamente con Streamlit
```bash
streamlit run app.py
```

### Opción C: Con Configuración Personalizada
```bash
streamlit run app.py --server.port 8502 --server.headless true
```

---

## Paso 5: Explorar el Cuaderno Jupyter

```bash
# Lanzar Jupyter
jupyter notebook Cuaderno_Educacion_Financiera_RD.ipynb

# O con JupyterLab (si está instalado)
jupyter lab Cuaderno_Educacion_Financiera_RD.ipynb
```

El cuaderno incluye:
- Análisis exploratorio de datos (EDA) completo
- Visualizaciones con Seaborn y Matplotlib
- Entrenamiento y evaluación del modelo Random Forest
- Análisis de clusters K-Means con visualizaciones 2D
- Todos los cálculos documentados paso a paso con Markdown

---

## Solución de Problemas Comunes

### Error: `ModuleNotFoundError: No module named 'streamlit'`
```bash
# Verificar que el entorno virtual está activado
pip install streamlit
# O reinstalar todas las dependencias
pip install -r requirements.txt --force-reinstall
```

### Error: `OSError: [WinError 10013] An attempt was made to access a socket in a way forbidden`
El puerto 8501 está en uso. Usar un puerto diferente:
```bash
streamlit run app.py --server.port 8502
```

### Error: `ImportError: cannot import name 'ml_engine'`
Asegúrese de ejecutar desde el directorio raíz del proyecto donde están `ml_engine.py` y `app.py`.

### La app carga muy lento la primera vez
Es normal. El modelo Random Forest se entrena al iniciar y luego se cachea. Las interacciones posteriores son instantáneas.

### Gráficos 3D no se muestran correctamente
Actualice su navegador o cambie a Chrome/Firefox. Los gráficos Plotly 3D requieren WebGL habilitado.

---

## Estructura de Archivos Necesaria

Para que la app funcione, estos archivos deben estar en el mismo directorio:

```
✅ app.py          — Aplicación principal
✅ ml_engine.py    — Motor de ML
✅ data.py         — Datos empíricos
✅ main.py         — Lanzador (opcional)
✅ requirements.txt — Dependencias
```

---

*Continúa en → [07 — Fuentes y Referencias](07-fuentes-referencias.md)*
