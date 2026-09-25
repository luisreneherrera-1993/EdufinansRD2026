# 03 — Módulo de Datos (`data.py`)

## 🗃️ Documentación del Módulo de Datos Empíricos

---

## Descripción General

El módulo `data.py` actúa como la **única fuente de verdad** para todos los datos empíricos, indicadores, programas y referencias institucionales del proyecto. Funciona exclusivamente como repositorio de constantes y estructuras de datos; no ejecuta ninguna lógica de negocio.

**Principio de diseño:** Separar los datos de la lógica permite actualizar los indicadores del BCRD sin tocar el código de ML o de la interfaz.

---

## Constantes y Estructuras de Datos

### `INCLUSION_FINANCIERA` — Evolución de la Inclusión Financiera

```python
INCLUSION_FINANCIERA = {
    'anios': [2019, 2023],
    'porcentaje_con_producto_financiero': [49, 55],
    'fuente': 'Banco Central RD — ENIF 2019 & ENIEF 2023'
}
```

**Fuente:** BCRD — Resumen Ejecutivo ENIEF 2023  
**Interpretación:** La inclusión financiera adulta creció de **49%** (2019) a **55%** (2023), un aumento de 6 puntos porcentuales en 4 años.

---

### `MATRICULA` — Matrícula Escolar Nacional 2024-2025

```python
MATRICULA = {
    'nivel': ['Inicial', 'Primaria', 'Secundaria', 'Educación de Adultos', 'Especial'],
    'estudiantes': [267_000, 1_186_589, 861_308, 45_000, 12_000],
    'fuente': 'MINERD — Datos de Matrícula 2024-2025'
}
```

**Fuente:** Ministerio de Educación de la República Dominicana (MINERD)  
**Relevancia:** El nivel de Secundaria (861,308 estudiantes) es el objetivo principal de la propuesta de curricularización.

---

### `GENERO_CREDITO` — Brecha de Género en el Sistema Financiero

| Indicador | Porcentaje |
|-----------|------------|
| Mujeres con crédito de consumo en mora | 15% |
| Hombres con crédito de consumo en mora | 11% |
| Mujeres que citan "falta de dinero" como barrera al ahorro | 68% |
| Mujeres con acceso restringido a crédito empresarial | 42% |

**Fuente:** Superintendencia de Bancos (SB) — Informe Inclusivo 2025  
**Conclusión:** Las mujeres tienen mayor exposición a productos de alto riesgo pero menor acceso a instrumentos de ahorro e inversión, lo que aumenta su vulnerabilidad financiera.

---

### `CAUSAS` — Causas Estructurales Identificadas

Lista de causas raíz del bajo nivel de inclusión financiera en RD:

1. Ausencia de educación financiera en el currículo escolar formal
2. Alta informalidad laboral (53% de la PEA trabaja en sector informal)
3. Barreras geográficas: concentración bancaria en zonas urbanas
4. Desconfianza institucional en el sistema financiero formal
5. Costos de mantenimiento de cuentas inaccesibles para ingresos bajos
6. Brecha digital que limita acceso a banca móvil/digital

---

### `GASTO_PAQUETE_ESCOLAR_RD` — Referencia de Gasto Educativo

```python
GASTO_PAQUETE_ESCOLAR_RD = {
    'descripcion': 'Gasto Anual en Paquetes Escolares Gratuitos (MINERD)',
    'monto_rd': 4_690_000_000,   # RD$ 4,690 millones
    'anio': 2023,
    'fuente': 'MINERD — Presupuesto Ejecutado Paquetes Escolares 2023'
}
```

**Comparativa clave:** Curricularizar EEF en toda la secundaria pública costaría  
US$5.68M (≈ RD$341M) — **menos del 2%** de lo que ya se gasta en paquetes escolares.

---

### `EJES_ESTRATEGICOS` — Ejes de la Política Pública Propuesta

| Eje | Descripción |
|-----|-------------|
| Curricularización Progresiva | Inserción gradual de EEF en el currículo nacional con articulación al Currículo Dominicano Revisado (CDR) |
| Capacitación Docente INAFOCAM | Formación continua de docentes en competencias de educación financiera y económica |
| Alianzas Institucionales | Articulación MINERD-BCRD-SB-Banreservas-BID para financiamiento y asistencia técnica |
| Evaluación de Impacto | Protocolo de evaluación experimental pre/post para medir el efecto en conocimiento y comportamiento |

---

### `PROGRAMAS` — Catálogo de Programas Educativos

| Nombre | Nivel | Contenidos | Horas/Año |
|--------|-------|------------|-----------|
| Mis Primeras Finanzas | Primaria (1°-4°) | Ahorro, moneda, necesidades vs. deseos | 20h |
| Educación Económica y Financiera | Primaria (5°-8°) | Presupuesto familiar, bancos, crédito básico | 40h |
| Finanzas para Emprender | Secundaria | Flujo de caja, inversión, emprendimiento | 60h |
| Finanzas en Familia | Adultos/Comunidad | Planificación financiera familiar, pensiones | 30h |
| Formación Docente EEF | Docentes | Metodología, facilitación, evaluación EEF | 80h |

---

### `FASES` — Cronograma Institucional (2024-2027)

| Fase | Periodo | Duración | Actividades Clave |
|------|---------|----------|-------------------|
| 1 — Diseño Curricular | Ene-Jun 2024 | 6 meses | Desarrollo materiales, guías docentes, validación pedagógica |
| 2 — Piloto Nacional | Jul 2024-Jun 2025 | 12 meses | 50,000 estudiantes, capacitación docentes, monitoreo |
| 3 — Escalamiento | Jul 2025-Jun 2026 | 12 meses | 861,308 estudiantes secundaria pública, adaptación regional |
| 4 — Consolidación | Jul 2026-Jun 2027 | 12 meses | Cobertura 2M+ estudiantes, evaluación de impacto, sostenibilidad |

---

### `FUENTES` — Lista de Referencias Institucionales

```python
FUENTES = [
    ('BCRD', 'Resumen Ejecutivo ENIEF 2023', 'https://www.bancentral.gov.do/...'),
    ('BCRD', 'Guía de Habilidades Económicas y Financieras', '...'),
    ('SB', 'Informe Hacia un Sistema Financiero Inclusivo 2025', '...'),
    ('MINERD / Banreservas', 'Acuerdo Marco de Educación Financiera Escolar 2024', '...'),
    ('BID', 'Frisancho (2017) - Evaluación Experimental Finanzas en mi Colegio', '...'),
    ('OCDE/INFE', 'Encuesta Internacional de Alfabetización Financiera 2020', '...'),
]
```

---

*Continúa en → [04 — Motor de Machine Learning](04-modulo-ml.md)*
