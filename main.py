"""
Punto de Entrada Principal (Main Runner)
Plataforma de Educación Financiera en República Dominicana
UFHEC 2026
"""

import sys
import subprocess
import os

def main():
    print("=====================================================================")
    print(" 🇩🇴 PLATAFORMA DE EDUCACIÓN FINANCIERA EN REPÚBLICA DOMINICANA")
    print("=====================================================================")
    print("Iniciando la aplicación web interactiva (Streamlit)...")
    print("Si no se abre automáticamente el navegador, diríjase a: http://localhost:8501")
    print("---------------------------------------------------------------------\n")
    
    app_path = os.path.join(os.path.dirname(__file__), "app.py")
    
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", app_path], check=True)
    except KeyboardInterrupt:
        print("\n[!] Aplicación detenida por el usuario.")
    except Exception as e:
        print(f"\n[X] Error al iniciar Streamlit: {e}")
        print("Intente ejecutar manualmente: streamlit run app.py")

if __name__ == "__main__":
    main()
