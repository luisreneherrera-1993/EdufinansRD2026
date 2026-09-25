# 01 — Descripción del Proyecto

## 🇩🇴 Plataforma de Diagnóstico, Modelado de IA y Estrategia de Educación Financiera en República Dominicana

**Proyecto:** Práctica Final Python 2026  
**Institución:** Universidad Federico Henríquez y Carvajal (UFHEC)  
**Desarrollador:** Luis Rene Herrera  
**Fecha:** Septiembre 2026  

---

## ¿Qué es este proyecto?

Es una **plataforma interactiva de soporte a decisiones públicas** que combina análisis de datos empíricos, aprendizaje automático (Machine Learning) y simulación de políticas para estudiar y proponer soluciones a la baja inclusión financiera en República Dominicana.

El proyecto responde a una realidad documentada: **solo el 55% de los adultos dominicanos posee algún producto financiero** (ENIEF 2023) y apenas el **3% de los hogares ha recibido educación financiera formal** (ENIF 2019). Ante este diagnóstico, la plataforma propone una hoja de ruta concreta para la **curricularización obligatoria de la Educación Económica y Financiera (EEF)** en el sistema educativo dominicano.

---

## 🎯 Objetivos

### Objetivo General
Analizar, clasificar y simular la costo-efectividad de la implementación nacional de la Educación Económica y Financiera en República Dominicana mediante herramientas de ciencia de datos e inteligencia artificial.

### Objetivos Específicos

| # | Objetivo | Tecnología |
|---|----------|------------|
| 1 | **Diagnosticar** la situación actual de inclusión financiera en RD (ENIF 2019 / ENIEF 2023) | Pandas · Plotly · Streamlit |
| 2 | **Entrenar modelos de IA** para clasificar perfiles de vulnerabilidad económica | Scikit-Learn (Random Forest) |
| 3 | **Segmentar** la población dominicana en grupos sociodemográficos homogéneos | Scikit-Learn (K-Means) |
| 4 | **Simular escenarios presupuestarios** de cobertura nacional educativa | NumPy · Pandas |
| 5 | **Proporcionar una herramienta visual e interactiva** para tomadores de decisión | Streamlit · Plotly |

---

## 📋 Contexto y Justificación

### La Brecha de Inclusión Financiera en RD

Según la **Segunda Encuesta Nacional de Inclusión Financiera (ENIEF 2023)** del Banco Central:

- **55%** de la población adulta posee al menos un producto financiero formal
- **70%** de los hogares no cubre sus gastos mensuales básicos
- **45%** de los adultos no tiene acceso a ningún servicio bancario
- Solo el **3%** de hogares ha recibido educación financiera (ENIF 2019)
- Las mujeres presentan **mayor morosidad relativa** pero enfrentan **más barreras de acceso** al crédito

### La Solución Propuesta

Basada en evidencia experimental del **BID (Banco Interamericano de Desarrollo)**, el piloto *"Finanzas en mi Colegio"* implementado en Perú (Frisancho, 2017) demostró que con un costo de **US$6.60 por estudiante/año** es posible lograr mejoras de:
- **+0.14 Desviaciones Estándar** en conocimiento financiero estudiantil
- **+0.30 Desviaciones Estándar** en competencias docentes

Aplicando esta evidencia a República Dominicana:
- **861,308 estudiantes** de secundaria pública
- Costo total: **US$5.68 millones/año**
- Equivalente a **menos del 2%** del gasto anual en útiles/uniformes escolares del MINERD (RD$4.69 mil millones)

---

## 📊 Indicadores Clave (KPIs del Proyecto)

| Indicador | Valor | Fuente |
|-----------|-------|--------|
| Inclusión financiera adulta (2023) | 55% | ENIEF 2023 · BCRD |
| Aprendió a ahorrar eficientemente | 78.3% | ENIEF 2023 · BCRD |
| Hogares con educación financiera (2019) | 3% | ENIF 2019 · BCRD |
| Estudiantes de secundaria pública | 861,308 | MINERD 2024-2025 |
| Costo unitario BID por estudiante | US$6.60 | Frisancho (2017) · BID |
| Costo nacional secundaria pública | US$5.68M | Cálculo propio |
| Registros sintéticos calibrados | 3,000 | Dataset ENIEF-calibrado |
| Precisión modelo Random Forest | >90% | Evaluación propia |

---

## 🌟 Impacto Esperado

1. **Reducción de la vulnerabilidad económica** de la población rural de bajos ingresos
2. **Aumento de la bancarización** en hogares actualmente excluidos del sistema formal
3. **Reducción de la brecha de género** en acceso a servicios financieros
4. **Herramienta de decisión** para BCRD, MINERD, SB e INAFOCAM
5. **Modelo replicable** para otros países de la región LATAM

---

*Continúa en → [02 — Arquitectura del Sistema](02-arquitectura-sistema.md)*
