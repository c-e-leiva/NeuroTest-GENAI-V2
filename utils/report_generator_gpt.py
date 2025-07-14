# report_generator_pdf.py
# Este módulo utiliza la API de OpenAI para generar un informe personalizado
# a partir de los resultados del test cognitivo, usando un prompt bien diseñado
# que habla directamente al usuario (segunda persona).

import openai               # Cliente para acceder a la API de OpenAI (GPT)
import streamlit as st      # Para obtener la API key desde el entorno seguro de Streamlit

# Asigna la clave de API desde secrets.toml (debe estar configurada en Streamlit Cloud o local)
openai.api_key = st.secrets["OPENAI_API_KEY"]

def generar_informe_gpt(resultados_dict, nombre_usuario="El usuario", edad=None):
    """
    Genera un informe textual empático y directo al usuario a partir de los resultados del test.

    Parámetros:
        resultados_dict (dict): Puntajes por área (Memoria, Atención, etc.).
        nombre_usuario (str): Nombre de quien realizó el test.
        edad (int, optional): Edad de la persona.

    Retorna:
        str: Texto del informe generado por GPT.
    """

    # Prompt actualizado: lenguaje claro, en segunda persona, empático y personalizado
    prompt = f"""
Sos un profesional en neurociencia cognitiva. A continuación, se presentan los resultados de un test cognitivo:

- Nombre: {nombre_usuario}
- Edad: {edad if edad else "No especificada"}
- Resultados:
  - Memoria: {resultados_dict.get("Memoria", "No evaluado")}
  - Atención: {resultados_dict.get("Atención", "No evaluado")}
  - Lenguaje: {resultados_dict.get("Lenguaje", "No evaluado")}
  - Razonamiento: {resultados_dict.get("Razonamiento", "No evaluado")}

Redactá un informe personalizado, empático y directo para la persona que hizo el test (no hablés en tercera persona).
Usá un estilo amable y profesional, escribiendo en segunda persona (vos, tu memoria, tus habilidades).

Incluí:
1. Una breve explicación de qué evalúa cada área cognitiva.
2. En áreas donde se obtuvo un nivel "sin riesgo", incluí un refuerzo positivo corto (¡Felicidades! / ¡Muy bien!).
3. En áreas con riesgo "leve", "moderado" o "alto":
   - Explicá en qué consiste ese resultado
   - Posibles causas comunes o factores que podrían influir
   - Recomendaciones concretas: ejercicios, rutinas o sugerencias útiles

Al final, brindá sugerencias generales para estimular la cognición de forma integral.

No incluyas saludos ni firma.
"""

    # Solicitud al modelo GPT-4 Turbo para generar el informe
    response = openai.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    # Devuelve el texto generado limpio
    return response.choices[0].message.content.strip()
