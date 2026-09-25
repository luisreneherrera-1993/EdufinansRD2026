# 07 — Fuentes y Referencias Académicas

## 📚 Fuentes Institucionales y Referencias Bibliográficas

---

## Fuentes de Datos Primarias

### 1. Banco Central de la República Dominicana (BCRD)

| Documento | Año | Datos Utilizados |
|-----------|-----|-----------------|
| Primera Encuesta Nacional de Inclusión Financiera (ENIF) | 2019 | Tasas de inclusión 49%, 3% hogares con EF |
| Segunda Encuesta Nacional de Inclusión Financiera (ENIEF) | 2023 | Inclusión 55%, distribuciones sociodemográficas |
| Guía de Habilidades Económicas y Financieras | 2023 | Marco conceptual de EF para políticas públicas |
| Resumen Ejecutivo ENIEF 2023 | 2023 | KPIs resumidos de inclusión financiera RD |

**URL Oficial:** https://www.bancentral.gov.do/

---

### 2. Superintendencia de Bancos de la República Dominicana (SB)

| Documento | Año | Datos Utilizados |
|-----------|-----|-----------------|
| Informe "Hacia un Sistema Financiero Inclusivo y Sostenible" | 2025 | Brecha de género: morosidad femenina 15% vs 11% masculina |
| Boletín de Indicadores Financieros | 2024 | Tasas de crédito de consumo por género |

**URL Oficial:** https://www.supbanco.gov.do/

---

### 3. Ministerio de Educación de la República Dominicana (MINERD)

| Documento | Año | Datos Utilizados |
|-----------|-----|-----------------|
| Datos de Matrícula Escolar 2024-2025 | 2024 | 861,308 estudiantes secundaria pública |
| Presupuesto Ejecutado Paquetes Escolares | 2023 | RD$4,690 millones en útiles/uniformes |
| Acuerdo Marco de Educación Financiera Escolar (con Banreservas) | 2024 | Marco institucional para EF escolar |
| Currículo Dominicano Revisado (CDR) | 2016 | Base curricular para integración de EEF |

**URL Oficial:** https://www.ministeriodeeducacion.gob.do/

---

### 4. Banco Interamericano de Desarrollo (BID)

| Documento | Año | Datos Utilizados |
|-----------|-----|-----------------|
| Frisancho, V. — "Evaluación Experimental del Programa Finanzas en mi Colegio" | 2017 | Costo US$6.60/estudiante/año; +0.14 DE estudiantes; +0.30 DE docentes |
| BID — "Educación Financiera en América Latina y el Caribe" | 2020 | Marco regional de referencia |

**Relevancia:** Esta evaluación experimental es la **base empírica fundamental** del proyecto. Proporciona los parámetros de costo-efectividad usados en el simulador.

**Referencia completa:**
> Frisancho, V. (2017). *Improving Financial Literacy in Peru: The Long-Run Effects of School-Based Financial Education.* Working Paper IDB-WP-800. Inter-American Development Bank. Washington, D.C.

---

### 5. OCDE / INFE (International Network on Financial Education)

| Documento | Año | Datos Utilizados |
|-----------|-----|-----------------|
| Encuesta Internacional de Alfabetización Financiera de Adultos | 2020 | Parámetros comparativos internacionales de EF |
| Core Competencies Framework on Financial Literacy for Youth | 2015 | Marco de competencias para programas escolares |
| Recomendación del Consejo sobre EF | 2020 | Estándar internacional de políticas de EF |

**URL Oficial:** https://www.oecd.org/financial/education/

---

### 6. UNESCO

| Documento | Año | Datos Utilizados |
|-----------|-----|-----------------|
| Education for Sustainable Development Goals — Learning Objectives | 2017 | Integración de EF en ODS 4 (Educación de Calidad) |

---

## Referencias Académicas Complementarias

```
1. Lusardi, A., & Mitchell, O. S. (2014). The economic importance of financial literacy:
   Theory and evidence. Journal of Economic Literature, 52(1), 5-44.

2. Kaiser, T., & Menkhoff, L. (2017). Does financial education impact financial literacy
   and financial behavior, and if so, when? World Bank Economic Review, 31(3), 611-630.

3. Bernheim, B. D., Garrett, D. M., & Maki, D. M. (2001). Education and saving:
   The long-term effects of high school financial curriculum mandates.
   Journal of Public Economics, 80(3), 435-465.

4. Xu, L., & Zia, B. (2012). Financial literacy around the world: An overview of the
   evidence with practical suggestions for the way forward.
   World Bank Policy Research Working Paper 6107.

5. Carpena, F., Cole, S., Shapiro, J., & Zia, B. (2011). Unpacking the causal chain of
   financial literacy. World Bank Policy Research Working Paper 5798.
```

---

## Notas Metodológicas sobre el Dataset Sintético

El dataset de 3,000 registros es **sintético** (no contiene datos personales reales) pero está **calibrado** con los estadísticos publicados por el BCRD:

| Parámetro | Valor Empírico (ENIEF 2023) | Valor en Dataset |
|-----------|----------------------------|-----------------|
| % Zona Urbana | ~65% | 65% |
| % Mujeres | ~52% | 52% |
| % Sin educación financiera | ~92% | 92% |
| % Con algún producto financiero | 55% | ~55% (por score logístico) |
| Ingreso mediano mensual | ~RD$18,000 | ~RD$18,000 (lognormal) |

Esta metodología de generación de datos sintéticos calibrados es estándar en investigación de privacidad de datos y en simulación de políticas públicas cuando los microdatos no son de acceso libre.

---

## Cómo Citar este Proyecto

```
Herrera, L. R. (2026). Plataforma de Diagnóstico, Modelado de IA y Estrategia de
Educación Financiera en República Dominicana. Práctica Final Python 2026.
Universidad Federico Henríquez y Carvajal (UFHEC). Santo Domingo, República Dominicana.
Disponible en: https://github.com/[usuario]/practica-final-python-2026
```

---

*← Volver al [Índice de Documentación](README.md)*
