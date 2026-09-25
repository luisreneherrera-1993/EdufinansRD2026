"""
Datos recopilados a partir de fuentes verificables sobre educación financiera
en República Dominicana. Cada bloque incluye su fuente para trazabilidad.
"""

# ---------------------------------------------------------------------------
# 1. Indicadores de inclusión y educación financiera
# ---------------------------------------------------------------------------
INCLUSION_FINANCIERA = {
    "anios": [2019, 2023],
    "porcentaje_con_producto_financiero": [51, 55],
    "fuente": "Banco Central de la República Dominicana, ENIEF 2023 "
              "(Resumen Ejecutivo, marzo 2024).",
}

BENEFICIOS_EDUCACION_FINANCIERA = {
    "indicador": [
        "Aprendió a ahorrar de forma más efectiva",
        "Mejoró el control de sus ingresos",
    ],
    "porcentaje": [78.3, 69.4],
    "fuente": "Banco Central de la República Dominicana, ENIEF 2023.",
}

HOGARES_ENIF_2019 = {
    "indicador": [
        "Hogares beneficiados por algún programa\nde educación financiera",
        "Hogares que no logran cubrir\nlos gastos del mes",
    ],
    "porcentaje": [3, 70],
    "fuente": "Banco Central de la República Dominicana, Primera Encuesta "
              "Nacional de Inclusión Financiera (ENIF) 2019, citada por la "
              "Superintendencia de Bancos (sb.gob.do).",
}

GENERO_CREDITO = {
    "indicador": [
        "Mujeres que reportan requisitos\nadicionales al solicitar crédito",
        "Confianza general en su\nentidad financiera",
        "Morosidad - mujeres",
        "Morosidad - hombres",
    ],
    "porcentaje": [26, 84, 1.4, 2.0],
    "fuente": "Superintendencia de Bancos, informe 'Hacia un sistema "
              "financiero inclusivo y sostenible 2025'; OPD-FUNGLODE, "
              "citado por Infobae (marzo 2026).",
}

OCDE_COMPARATIVO = {
    "descripcion": "Puntuación promedio global de alfabetización financiera "
                   "de adultos (26 países evaluados) fue de 12.7 puntos; "
                   "los países latinoamericanos participantes se ubicaron "
                   "entre las calificaciones más bajas del grupo.",
    "fuente": "OCDE/INFE, Encuesta Internacional de Alfabetización "
              "Financiera de Adultos 2020, citada por sb.gob.do.",
}

# ---------------------------------------------------------------------------
# 2. Matrícula del sistema educativo dominicano (año escolar 2024-2025)
# ---------------------------------------------------------------------------
MATRICULA = {
    "nivel": ["Inicial", "Primario", "Secundario", "Adultos"],
    "estudiantes": [388743, 1186589, 861308, 203694],
    "sector_publico_total": 2063758,
    "sector_privado_total": 576576,
    "fuente": "Ministerio de Educación de la República Dominicana, "
              "presidencia.gob.do (inicio año escolar 2024-2025).",
}

# ---------------------------------------------------------------------------
# 3. Causas estructurales
# ---------------------------------------------------------------------------
CAUSAS = [
    "Ausencia histórica de una asignatura formal y evaluada de educación "
    "económica y financiera en el currículo dominicano.",
    "Baja capacitación docente sostenida: talleres puntuales del Banco "
    "Central-MINERD-INAFOCAM, sin continuidad garantizada.",
    "Concentración de programas de educación financiera en la banca "
    "privada y la RSE (p. ej. AFP Crecer/CODESPA en 14 provincias).",
    "Brecha digital y territorial que dificulta llevar contenidos a zonas "
    "rurales y fronterizas.",
    "Informalidad laboral y baja bancarización familiar.",
    "Desigualdad de género en el acceso a crédito y documentación formal.",
]

# ---------------------------------------------------------------------------
# 4. Ejes estratégicos
# ---------------------------------------------------------------------------
EJES_ESTRATEGICOS = [
    {
        "eje": "Eje 1 — Currícularización permanente",
        "descripcion": "Convertir la educación económica y financiera en "
                        "un componente obligatorio y evaluado del "
                        "currículo, desde primaria hasta el politécnico.",
    },
    {
        "eje": "Eje 2 — Formación docente continua y certificada",
        "descripcion": "Institucionalizar la capacitación vía INAFOCAM, "
                        "con certificación, actualización periódica y "
                        "materiales estandarizados.",
    },
    {
        "eje": "Eje 3 — Equidad territorial y de género",
        "descripcion": "Priorizar regiones y provincias con menor "
                        "inclusión financiera y mayor ruralidad; enfoque "
                        "diferenciado para mujeres del sector informal.",
    },
    {
        "eje": "Eje 4 — Evaluación de impacto y datos abiertos",
        "descripcion": "Medir resultados con instrumentos comparables a "
                        "la ENIEF y a las pruebas PISA de competencia "
                        "financiera.",
    },
]

# ---------------------------------------------------------------------------
# 5. Programas educativos propuestos por nivel
# ---------------------------------------------------------------------------
PROGRAMAS = [
    {
        "nivel": "Inicial y Primario (1.º-6.º)",
        "programa": "Mis Primeras Finanzas",
        "contenidos": "Valor del dinero, necesidad vs. deseo, ahorro en "
                       "alcancía, hábitos básicos.",
        "actor_lider": "MINERD / BCRD",
    },
    {
        "nivel": "Secundario (1.º-6.º)",
        "programa": "Educación Económica y Financiera (módulo en Matemática)",
        "contenidos": "Presupuesto personal, tarjetas de crédito/débito, "
                       "ahorro formal, riesgos del sobreendeudamiento, "
                       "sistema financiero regulado.",
        "actor_lider": "MINERD / BCRD / SB",
    },
    {
        "nivel": "Técnico-Profesional / Politécnico",
        "programa": "Finanzas para Emprender",
        "contenidos": "Costeo, financiamiento formal para Mipymes, "
                       "pensiones (AFP), seguros básicos.",
        "actor_lider": "MINERD / INFOTEP / Superintendencias",
    },
    {
        "nivel": "Educación de Adultos",
        "programa": "Finanzas en Familia",
        "contenidos": "Presupuesto del hogar, remesas, prevención de "
                       "fraude financiero, banca digital.",
        "actor_lider": "MINERD (subsistema de adultos) / Banca Múltiple",
    },
    {
        "nivel": "Formación docente",
        "programa": "Certificación continua en Educación Económica y "
                     "Financiera",
        "contenidos": "Actualización de contenidos, didáctica financiera, "
                       "uso de la Guía del BCRD.",
        "actor_lider": "INAFOCAM / BCRD",
    },
]

# ---------------------------------------------------------------------------
# 6. Fases de ejecución
# ---------------------------------------------------------------------------
FASES = [
    {
        "fase": "Fase 1 — Diseño y línea base",
        "periodo": "Año 1",
        "actividades": "Actualizar la ENEEF, definir competencias por "
                        "nivel, aplicar línea base equivalente a la "
                        "ENIEF en una muestra de secundaria, priorizar "
                        "regiones con menor inclusión financiera.",
        "inicio_mes": 0, "duracion_meses": 12,
    },
    {
        "fase": "Fase 2 — Piloto",
        "periodo": "Año 1-2",
        "actividades": "Implementar el módulo en escuelas piloto (con "
                        "grupo de comparación), capacitar docentes vía "
                        "INAFOCAM, medir resultados a 6 y 12 meses.",
        "inicio_mes": 8, "duracion_meses": 12,
    },
    {
        "fase": "Fase 3 — Escalamiento nacional",
        "periodo": "Año 2-3",
        "actividades": "Extender el módulo a todo el nivel secundario "
                        "público y progresivamente a primaria; certificar "
                        "docentes; distribuir materiales vía República "
                        "Digital.",
        "inicio_mes": 18, "duracion_meses": 18,
    },
    {
        "fase": "Fase 4 — Consolidación y evaluación",
        "periodo": "Año 3-4",
        "actividades": "Incorporar la educación financiera en "
                        "instrumentos nacionales de evaluación, publicar "
                        "nueva ENIEF comparativa, sostener con "
                        "financiamiento público permanente.",
        "inicio_mes": 33, "duracion_meses": 15,
    },
]

# ---------------------------------------------------------------------------
# 7. Costo-efectividad
# ---------------------------------------------------------------------------
COSTO_POR_ESTUDIANTE_USD = 6.6  # Frisancho (2017), BID - piloto Perú

ESCALAMIENTO_REFERENCIA = [
    {"etapa": "Piloto (Fase 2)", "estudiantes": 50000},
    {"etapa": "Secundaria pública nacional", "estudiantes": 861308},
    {"etapa": "Primaria + secundaria públicas", "estudiantes": 2047897},
]

EFECTIVIDAD_ESPERADA = {
    "indicador": [
        "Conocimiento financiero\nestudiantil (Perú, piloto BID)",
        "Conocimiento financiero\ndocente (Perú, piloto BID)",
    ],
    "valor_de": [0.14, 0.30],
    "unidad": "Desviaciones estándar de mejora",
    "fuente": "Frisancho, V. (2017), 'Evaluación Experimental del Piloto "
              "Finanzas en mi Colegio', BID (publications.iadb.org).",
}

RCT_META_ANALISIS = {
    "n_estudios": 76,
    "n_paises": 33,
    "n_personas": 160000,
    "conclusion": "La educación financiera mejora de forma significativa "
                  "el conocimiento y el comportamiento financiero, "
                  "incluso ajustando por sesgo de publicación, a costos "
                  "relativamente bajos.",
    "fuente": "Kaiser, Lusardi, Menkhoff y Urban (2020), vía CEPR/VoxEU y "
              "Stanford Graduate School of Business.",
}

GASTO_PAQUETE_ESCOLAR_RD = {
    "monto_rd": 4690384443.95,
    "descripcion": "Uniformes, calzado y útiles escolares gratuitos, año "
                    "lectivo 2024-2025 (referencia de escala de gasto "
                    "social ya movilizado por el sistema educativo).",
    "fuente": "Presidencia de la República Dominicana / eldia.com.do.",
}

# ---------------------------------------------------------------------------
# 8. Fuentes consultadas (listado completo)
# ---------------------------------------------------------------------------
FUENTES = [
    ("Superintendencia de Bancos de la República Dominicana",
     "La educación financiera, un beneficio para usuarios/as y entidades",
     "https://sb.gob.do/publicaciones/blog-institucional/la-educacion-financiera-un-beneficio-para-usuariosas-y-entidades/"),
    ("Presidencia de la República Dominicana",
     "Informe 'Hacia un sistema financiero inclusivo y sostenible 2025'",
     "https://presidencia.gob.do/noticias/inclusion-financiera-y-sostenibilidad-sb-revela-avances-y-desafios"),
    ("Banco Central de la República Dominicana",
     "Resumen Ejecutivo ENIEF 2023",
     "https://cdn.bancentral.gov.do/documents/sala-de-prensa/noticias/documents/Resumen-Ejecutivo-ENIEF-2023.pdf"),
    ("Banco Central de la República Dominicana",
     "Guía para desarrollar tus habilidades económicas y financieras",
     "https://cdn.bancentral.gov.do/documents/sefbcrd/documents/Guia-para-desarrollar-tus-habilidades-economicas-y-financieras.pdf"),
    ("ENEEF", "Estrategia Nacional de Educación Económica y Financiera",
     "http://eneef.do/"),
    ("Ministerio de Educación (MINERD)",
     "Acuerdo Banreservas-MINERD para educación financiera (dic. 2024)",
     "https://www.ministeriodeeducacion.gob.do/comunicaciones/noticias/raquel-pena-encabeza-firma-de-acuerdo-entre-banreservas-y-el-minerd-para-llevar-educacion-financiera-a-centros-educativos"),
    ("INAFOCAM",
     "MINERD, Banco Central e Inafocam formarán docentes en Educación "
     "Económica y Financiera",
     "https://inafocam.edu.do/index.php/noticias/item/634-minerd-banco-central-e-inafocam-formaran-docentes-en-educacion-economica-y-financiera"),
    ("UNESCO",
     "Estatus socioeconómico y educación en la República Dominicana",
     "https://unesdoc.unesco.org/ark:/48223/pf0000374695"),
    ("Infobae",
     "La desigualdad económica y política limita el impacto educativo de "
     "las mujeres en RD (OPD-FUNGLODE, 2026)",
     "https://www.infobae.com/republica-dominicana/2026/03/16/la-desigualdad-economica-y-politica-limita-el-impacto-educativo-de-las-mujeres-en-republica-dominicana-segun-estudio/"),
    ("elDinero.com.do", "Cobertura de la ENIEF 2023",
     "https://eldinero.com.do/280500/educacion-financiera-falta-fortalecer-pero-desde-las-escuelas/"),
    ("Instituto OMG",
     "Inclusión Financiera en RD - FinTechs y educación financiera como "
     "catalizadores",
     "https://www.iomg.edu.do/post/inclusi%C3%B3n-financiera-en-rd-fintechs-y-educaci%C3%B3n-financiera-como-catalizadores"),
    ("CODESPA", "Programa 'Creciendo Contigo' (AFP Crecer)",
     "https://www.codespa.org/blog/2021/06/10/educacion-financiera-republica-dominicana/"),
    ("Alliance for Financial Inclusion (AFI)",
     "La educación financiera en América Latina y el Caribe: estudio de "
     "casos",
     "https://www.afi-global.org/wp-content/uploads/2024/09/Financial-Education-in-Latin-America-and-the-Caribbean-v.2_SP_hv.pdf"),
    ("Banco Interamericano de Desarrollo (BID)",
     "Frisancho, V., Evaluación Experimental del Piloto Finanzas en mi "
     "Colegio (Perú)",
     "https://publications.iadb.org/es/metadata/14044/evaluacion-experimental-del-piloto-finanzas-en-mi-colegio"),
    ("Asobancaria",
     "El impacto de la educación financiera en colegios",
     "https://www.asobancaria.com/wp-content/uploads/2022/12/1359_BE.pdf"),
    ("CEPR / VoxEU",
     "Financial education is effective and efficient (Kaiser et al. 2020)",
     "https://cepr.org/voxeu/columns/financial-education-effective-and-efficient"),
    ("Presidencia de la República Dominicana",
     "Matrícula escolar 2024-2025",
     "https://presidencia.gob.do/noticias/ministerio-de-educacion-convoca-mas-de-2640000-estudiantes-para-inicio-del-ano-escolar"),
]
