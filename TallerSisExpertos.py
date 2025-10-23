# -*- coding: utf-8 -*-
"""
RespirAI - Sistema experto interactivo para diagnóstico básico de enfermedades respiratorias
Autor: Juan Diego Rojas Vargas
Versión extendida: 25 reglas / 20 hechos
"""

# ----- Base de conocimiento -----
reglas = [
    # ---- GRIPE ----
    {"condiciones": ["fiebre", "dolores_musculares", "fatiga"], "diagnostico": "Gripe leve", "recomendacion": "Reposo e hidratación.", "prioridad": 70},
    {"condiciones": ["fiebre", "dolores_musculares", "fatiga", "dolor_cabeza"], "diagnostico": "Gripe moderada", "recomendacion": "Medicamentos antipiréticos y reposo.", "prioridad": 75},
    {"condiciones": ["fiebre", "dolores_musculares", "fatiga", "tos_seca"], "diagnostico": "Gripe fuerte", "recomendacion": "Acudir al médico si la fiebre persiste más de 3 días.", "prioridad": 80},

    # ---- RESFRIADO COMÚN ----
    {"condiciones": ["tos_leve", "congestion_nasal"], "excluir": ["fiebre"], "diagnostico": "Resfriado común leve", "recomendacion": "Descanso y buena hidratación.", "prioridad": 50},
    {"condiciones": ["tos_leve", "congestion_nasal", "dolor_garganta"], "excluir": ["fiebre"], "diagnostico": "Resfriado común con irritación de garganta", "recomendacion": "Beber líquidos tibios y usar humidificador.", "prioridad": 55},
    {"condiciones": ["tos_leve", "congestion_nasal", "dolor_cabeza"], "excluir": ["fiebre"], "diagnostico": "Resfriado con cefalea", "recomendacion": "Descansar y tomar analgésicos suaves.", "prioridad": 60},

    # ---- ALERGIA ----
    {"condiciones": ["picazon_ojos", "estornudos_frecuentes"], "excluir": ["fiebre"], "diagnostico": "Alergia leve", "recomendacion": "Evitar polvo y alérgenos comunes.", "prioridad": 55},
    {"condiciones": ["picazon_ojos", "estornudos_frecuentes", "congestion_nasal"], "excluir": ["fiebre"], "diagnostico": "Alergia respiratoria estacional", "recomendacion": "Usar antihistamínicos si es necesario.", "prioridad": 60},
    {"condiciones": ["estornudos_frecuentes", "congestion_nasal", "tos_leve"], "excluir": ["fiebre"], "diagnostico": "Alergia con irritación nasal", "recomendacion": "Evitar ambientes cerrados y ventilar la habitación.", "prioridad": 58},

    # ---- BRONQUITIS ----
    {"condiciones": ["tos_fuerte", "dificultad_respirar", "dolor_pecho"], "diagnostico": "Bronquitis aguda", "recomendacion": "Consultar al médico y evitar el humo del tabaco.", "prioridad": 85},
    {"condiciones": ["tos_fuerte", "dificultad_respirar", "fatiga"], "diagnostico": "Bronquitis moderada", "recomendacion": "Usar broncodilatadores y mantenerse hidratado.", "prioridad": 80},
    {"condiciones": ["tos_fuerte", "flema"], "diagnostico": "Bronquitis leve", "recomendacion": "Descansar y evitar cambios bruscos de temperatura.", "prioridad": 70},

    # ---- COVID-19 ----
    {"condiciones": ["fiebre", "tos_seca", "dificultad_respirar"], "diagnostico": "COVID-19 leve", "recomendacion": "Aislamiento y seguimiento médico.", "prioridad": 90},
    {"condiciones": ["fiebre", "tos_seca", "dificultad_respirar", "perdida_olfato"], "diagnostico": "COVID-19 probable", "recomendacion": "Aislamiento y prueba diagnóstica inmediata.", "prioridad": 95},
    {"condiciones": ["fiebre", "tos_fuerte", "fatiga", "perdida_olfato", "dificultad_respirar"], "diagnostico": "COVID-19 severo", "recomendacion": "Buscar atención médica urgente.", "prioridad": 100},

    # ---- SINUSITIS ----
    {"condiciones": ["dolor_cabeza", "congestion_nasal", "presion_facial"], "diagnostico": "Sinusitis leve", "recomendacion": "Inhalar vapor y mantenerse hidratado.", "prioridad": 65},
    {"condiciones": ["dolor_cabeza", "congestion_nasal", "fiebre"], "diagnostico": "Sinusitis aguda", "recomendacion": "Consultar al médico si dura más de 7 días.", "prioridad": 70},

    # ---- FARINGITIS ----
    {"condiciones": ["dolor_garganta", "fiebre", "dificultad_tragar"], "diagnostico": "Faringitis bacteriana", "recomendacion": "Consultar para posible antibiótico.", "prioridad": 75},
    {"condiciones": ["dolor_garganta", "tos_leve"], "excluir": ["fiebre"], "diagnostico": "Faringitis viral leve", "recomendacion": "Beber líquidos y evitar irritantes.", "prioridad": 55},

    # ---- NEUMONÍA ----
    {"condiciones": ["fiebre", "dificultad_respirar", "dolor_pecho", "tos_fuerte"], "diagnostico": "Neumonía probable", "recomendacion": "Atención médica inmediata.", "prioridad": 95},
    {"condiciones": ["fiebre", "fatiga", "tos_fuerte"], "diagnostico": "Infección pulmonar leve", "recomendacion": "Descanso y seguimiento médico.", "prioridad": 80},

    # ---- CONSULTA MÉDICA ----
    {"condiciones": ["sintomas_mas_10_dias"], "excluir": ["fiebre"], "diagnostico": "Consulta médica necesaria", "recomendacion": "Acudir a un profesional de la salud.", "prioridad": 99},
    {"condiciones": ["fatiga", "tos_leve", "sintomas_mas_10_dias"], "diagnostico": "Cansancio prolongado con tos", "recomendacion": "Se recomienda evaluación médica.", "prioridad": 85},
    {"condiciones": ["tos_leve", "dolor_garganta", "fatiga"], "diagnostico": "Infección respiratoria leve", "recomendacion": "Reposo e hidratación.", "prioridad": 60},
    {"condiciones": ["fiebre", "dificultad_respirar", "dolor_pecho"], "diagnostico": "Posible infección pulmonar", "recomendacion": "Buscar atención médica urgente.", "prioridad": 95},
    {"condiciones": ["tos_fuerte", "dolor_garganta", "fatiga"], "diagnostico": "Infección respiratoria persistente", "recomendacion": "Consulta médica para descartar complicaciones.", "prioridad": 75}
]

# ----- Lista de posibles síntomas (20 hechos) -----
sintomas_posibles = [
    "fiebre",
    "dolores_musculares",
    "fatiga",
    "tos_leve",
    "tos_fuerte",
    "tos_seca",
    "congestion_nasal",
    "dolor_cabeza",
    "dolor_garganta",
    "dificultad_respirar",
    "dolor_pecho",
    "picazon_ojos",
    "estornudos_frecuentes",
    "flema",
    "perdida_olfato",
    "presion_facial",
    "dificultad_tragar",
    "sintomas_mas_10_dias",
    "nauseas",
    "vomito"
]

# ----- Función para preguntar síntomas -----
def preguntar_sintomas():
    sintomas_usuario = []
    print("\nResponde con 'si' o 'no' a las siguientes preguntas:\n")
    for sintoma in sintomas_posibles:
        texto = sintoma.replace('_', ' ')
        respuesta = input(f"¿Tiene {texto}? (si/no): ").strip().lower()
        if respuesta == "si":
            sintomas_usuario.append(sintoma)
        elif respuesta == "no":
            sintomas_usuario.append("no_" + sintoma)
    return sintomas_usuario

# ----- Motor de inferencia -----
def diagnosticar(sintomas_usuario):
    print("\n=== Diagnóstico del sistema experto RespirAI ===\n")
    candidatos = []
    for regla in reglas:
        condiciones = regla.get("condiciones", [])
        excluir = regla.get("excluir", [])
        if all(c in sintomas_usuario for c in condiciones) and not any(e in sintomas_usuario for e in excluir):
            candidatos.append(regla)

    if not candidatos:
        print("No se pudo determinar una enfermedad específica.")
        print("Recomendación: consulte a un médico si los síntomas persisten.\n")
        return

    mejor = max(candidatos, key=lambda r: r.get("prioridad", 0))
    print(f"Posible diagnóstico: {mejor['diagnostico']}")
    print(f"Recomendación: {mejor['recomendacion']}\n")

# ----- Ejecución principal -----
if __name__ == "__main__":
    print("=== Sistema Experto Interactivo: RespirAI ===")
    print("Diagnóstico básico de enfermedades respiratorias comunes.\n")

    sintomas_usuario = preguntar_sintomas()
    diagnosticar(sintomas_usuario)
