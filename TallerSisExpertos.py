# -*- coding: utf-8 -*-
"""
RespirAI - Sistema experto para diagnóstico básico de enfermedades respiratorias
Autor: Juan Diego Rojas Vargas, Juan Martin Trejos, Victoria Elizabeth Roa González y Hania Valentina Carreño Baquero
Tema: Medicina (diagnóstico básico de enfermedades respiratorias comunes)
"""

# ----- Base de conocimiento -----
reglas = [
    {
        "condiciones": ["fiebre_alta", "dolores_musculares", "fatiga_intensa"],
        "diagnostico": "Gripe",
        "recomendacion": "Reposo, hidratación y control de temperatura."
    },
    {
        "condiciones": ["tos_leve", "congestion_nasal"],
        "excluir": ["fiebre_alta"],
        "diagnostico": "Resfriado común",
        "recomendacion": "Descanso, buena hidratación y evitar cambios bruscos de temperatura."
    },
    {
        "condiciones": ["picazon_ojos", "estornudos_frecuentes"],
        "excluir": ["fiebre_alta", "dolores_musculares"],
        "diagnostico": "Alergia respiratoria",
        "recomendacion": "Evitar alérgenos y consultar al médico si los síntomas persisten."
    },
    {
        "condiciones": ["fiebre", "fatiga_extrema"],
        "diagnostico": "Reposo e hidratación recomendados",
        "recomendacion": "Tomar líquidos, descansar y monitorear la temperatura."
    },
    {
        "condiciones": ["sintomas_mas_10_dias"],
        "excluir": ["fiebre"],
        "diagnostico": "Consulta médica necesaria",
        "recomendacion": "Acudir a un profesional de la salud para revisión detallada."
    }
]

# ----- Motor de inferencia -----
def diagnosticar(sintomas_usuario):
    print("\n=== Diagnóstico del sistema experto RespirAI ===\n")

    encontrado = False
    for regla in reglas:
        condiciones = regla.get("condiciones", [])
        excluir = regla.get("excluir", [])

        # Verifica si se cumplen todas las condiciones
        if all(c in sintomas_usuario for c in condiciones) and not any(e in sintomas_usuario for e in excluir):
            print(f"Posible diagnóstico: {regla['diagnostico']}")
            print(f"Recomendación: {regla['recomendacion']}\n")
            encontrado = True

    if not encontrado:
        print("No se pudo determinar una enfermedad específica.")
        print("Recomendación: consulte a un médico si los síntomas persisten.\n")

# ----- Ejecución principal -----
if __name__ == "__main__":
    print("=== Sistema Experto: RespirAI ===")
    print("Ingrese los síntomas presentes separados por comas.")
    print("Ejemplo: fiebre_alta, dolores_musculares, fatiga_intensa\n")

    entrada = input("Síntomas: ").lower().replace(" ", "")
    sintomas_usuario = entrada.split(",")

    diagnosticar(sintomas_usuario)
