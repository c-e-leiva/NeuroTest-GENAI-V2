# test_data.py
# Este módulo contiene el contenido del test cognitivo organizado por áreas.
# Cada área incluye una lista de preguntas, opciones de respuesta y puntajes asociados.

test_cognitivo = {
    "Memoria": [
        # Preguntas que evalúan la memoria episódica, memoria reciente y recuerdos específicos
        {"pregunta": "¿Recordás qué comiste ayer?",
         "opciones": {"a": ("Sí", 3), "b": ("No", 0), "c": ("Más o menos", 2), "d": ("No sé", 1)}},

        {"pregunta": "¿Dónde dejaste las llaves la última vez que las usaste?",
         "opciones": {"a": ("En un lugar fijo", 3), "b": ("En varios lugares", 1), "c": ("No recuerdo", 0), "d": ("No sé", 1)}},

        {"pregunta": "¿Qué hiciste en tu cumpleaños hace dos años?",
         "opciones": {"a": ("Fiesta con amigos/familia", 3), "b": ("Algo tranquilo", 2), "c": ("No recuerdo", 0), "d": ("No sé", 1)}},

        {"pregunta": "¿Podés decir tu número telefónico sin mirarlo?",
         "opciones": {"a": ("Sí", 3), "b": ("No", 0), "c": ("Algo sí, algo no", 2), "d": ("No sé", 1)}},

        {"pregunta": "¿Recordás qué ropa llevabas el último fin de semana?",
         "opciones": {"a": ("Sí", 3), "b": ("No", 0), "c": ("Una parte sí", 2), "d": ("No sé", 1)}},
    ],

    "Atención": [
        # Preguntas que evalúan la atención sostenida, concentración, detección de detalles y respuesta rápida
        {"pregunta": "En la serie 2, 4, 6, 7, ¿qué número sigue?",
         "opciones": {"a": ("8", 3), "b": ("9", 2), "c": ("10", 1), "d": ("No sé", 1)}},

        {"pregunta": "¿Qué palabra es diferente?",
         "opciones": {"a": ("Azul", 3), "b": ("Rojo", 3), "c": ("Manzana", 0), "d": ("No sé", 1)}},

        {"pregunta": "¿Cuántas veces aparece la letra 'a' en: 'La araña anda agitada'?",
         "opciones": {"a": ("2", 0), "b": ("7", 1), "c": ("9", 2), "d": ("No sé", 1)}},

        {"pregunta": "Si escuchás música y alguien te llama, ¿qué hacés primero?",
         "opciones": {"a": ("Ignoro el llamado", 0), "b": ("Presto atención al llamado", 3), "c": ("Sigo cantando", 1), "d": ("No sé", 1)}},

        {"pregunta": "¿Cuál es la última letra de esta pregunta?",
         "opciones": {"a": ("a", 1), "b": ("?", 0), "c": ("e", 3), "d": ("No sé", 1)}},
    ],

    "Lenguaje": [
        # Preguntas que evalúan comprensión de vocabulario, estructura gramatical y semántica
        {"pregunta": "¿Cuál es el antónimo de 'rápido'?",
         "opciones": {"a": ("Veloz", 0), "b": ("Lento", 3), "c": ("Fuerte", 1), "d": ("No sé", 1)}},

        {"pregunta": "Completa: 'El perro ____ en el parque.'",
         "opciones": {"a": ("corrió", 3), "b": ("corriendo", 1), "c": ("correr", 0), "d": ("No sé", 1)}},

        {"pregunta": "¿Qué palabra no encaja?",
         "opciones": {"a": ("Mesa", 3), "b": ("Silla", 3), "c": ("Libro", 0), "d": ("No sé", 1)}},

        {"pregunta": "¿Qué significa 'benevolente'?",
         "opciones": {"a": ("Malicioso", 0), "b": ("Bondadoso", 3), "c": ("Rápido", 1), "d": ("No sé", 1)}},

        {"pregunta": "¿Qué parte de la oración es el verbo? 'María corre todos los días'",
         "opciones": {"a": ("María", 0), "b": ("corre", 3), "c": ("todos", 1), "d": ("No sé", 1)}},
    ],

    "Razonamiento": [
        # Preguntas que evalúan razonamiento lógico, inferencia, secuencias y resolución de problemas
        {"pregunta": "Si todos los gatos son animales y algunos animales son mascotas, ¿los gatos son mascotas?",
         "opciones": {"a": ("Sí, todos", 2), "b": ("Algunos pueden ser", 3), "c": ("No", 1), "d": ("No sé", 1)}},

        {"pregunta": "Si hoy es martes, ¿qué día será dentro de 4 días?",
         "opciones": {"a": ("Sábado", 3), "b": ("Domingo", 2), "c": ("Lunes", 1), "d": ("No sé", 1)}},

        {"pregunta": "¿Qué número sigue en la secuencia 3, 6, 9, 12?",
         "opciones": {"a": ("13", 1), "b": ("14", 0), "c": ("15", 3), "d": ("No sé", 1)}},

        {"pregunta": "En una caja hay 5 manzanas y 3 naranjas. ¿Probabilidad de sacar una naranja?",
         "opciones": {"a": ("3/8", 3), "b": ("5/8", 1), "c": ("1/2", 2), "d": ("No sé", 1)}},

        {"pregunta": "Si un tren sale a las 6 y llega a las 10, ¿cuántas horas viajó?",
         "opciones": {"a": ("4", 3), "b": ("5", 0), "c": ("3", 1), "d": ("No sé", 1)}},
    ]
}
