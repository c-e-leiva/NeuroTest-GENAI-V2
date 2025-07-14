# interaccion.py
# Este módulo gestiona la interacción con el usuario en modo consola.
# Permite realizar el test cognitivo, calcular puntajes por área
# y clasificar el nivel de riesgo junto con recomendaciones personalizadas.

def respuestas_interactivas(test):
    # Inicializa los puntajes de cada área cognitiva en 0
    puntajes = {"memoria": 0, "atencion": 0, "lenguaje": 0, "razonamiento": 0}

    # Mapeo para mantener consistencia entre claves del diccionario y formato de nombres
    mapeo = {"Memoria": "Memoria", "Atención": "Atención", "Lenguaje": "Lenguaje", "Razonamiento": "Razonamiento"}

    # Recorre cada categoría del test y sus preguntas
    for categoria, preguntas in test.items():
        print(f"\nCategoría: {categoria}\n")

        for i, pregunta in enumerate(preguntas, 1):
            # Muestra la pregunta con sus opciones
            print(f"{i}. {pregunta['pregunta']}")
            for key, (texto, _) in pregunta["opciones"].items():
                print(f"   {key}) {texto}")

            # Solicita al usuario que elija una opción válida (a, b, c o d)
            while True:
                opcion = input("Tu respuesta (a, b, c, d): ").lower()
                if opcion in pregunta["opciones"]:
                    break
                else:
                    print("Opción inválida, ingresa a, b, c o d.")

            # Suma el puntaje correspondiente según la opción elegida
            puntaje = pregunta["opciones"][opcion][1]
            puntajes[mapeo[categoria]] += puntaje

    # Devuelve los puntajes acumulados por área
    return puntajes

def clasificar_y_recomendar(puntajes):
    # Diccionario de recomendaciones por área cognitiva
    recomendaciones = {
        "Memoria": "Practicar ejercicios de memoria como juegos de recordar objetos o secuencias.",
        "Atención": "Realizar actividades que mejoren la concentración, como rompecabezas o mindfulness.",
        "Lenguaje": "Ejercitar el vocabulario y comprensión lectora con lectura diaria y juegos de palabras.",
        "Razonamiento": "Resolver problemas lógicos y matemáticos para fortalecer el razonamiento.",
    }

    niveles = {}  # Diccionario para almacenar la clasificación de riesgo y recomendación por área

    # Clasifica el nivel de riesgo en base al puntaje total por área
    for area, puntaje in puntajes.items():
        if puntaje < 6:
            niveles[area] = ("Alto riesgo", recomendaciones[area])
        elif puntaje < 9:
            niveles[area] = ("Moderado riesgo", recomendaciones[area])
        elif puntaje < 12:
            niveles[area] = ("Leve riesgo", recomendaciones[area])
        else:
            niveles[area] = ("Sin riesgo", "Excelente desempeño en esta área.")

    # Devuelve un diccionario con el nivel de riesgo y recomendación por área
    return niveles
