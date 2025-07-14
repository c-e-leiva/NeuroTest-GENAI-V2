# app.py
# Aplicación principal de Streamlit para el Test Cognitivo con IA Generativa.
# Integra preguntas interactivas, clasificación automática, informe personalizado y descarga en PDF.

import streamlit as st
import plotly.graph_objects as go
import re  # Usado para validar formato de correo electrónico

# --- Importación de módulos personalizados necesarios ---
from utils.visualizacion import graficar_radar, graficar_barras     # Visualizaciones en radar y barras
from utils.test_data import test_cognitivo                          # Diccionario con las preguntas del test
from utils.sheets import guardar_resultados_test                    # Función para guardar resultados en Google Sheets
from utils.interaccion import respuestas_interactivas, clasificar_y_recomendar  # Evaluación y recomendaciones
from utils.report_generator_gpt import generar_informe_gpt          # Informe automático con IA
from utils.export_pdf_streamlit import generar_pdf_streamlit        # Generación de PDF desde texto
from data.generador import leer_datos_reales                        # Lectura de dataset para el modelo
from model.classifier import entrenar_modelo, predecir_riesgo       # Entrenamiento y predicción de riesgo
from access.login import mostrar_login                              # Componente de login por clave

# --- Seguridad: sólo permite continuar si el usuario ingresó correctamente la clave ---
if not st.session_state.get("acceso_autorizado", False):
    mostrar_login()
    st.stop()

# --- Configuración general de la interfaz de Streamlit ---
st.set_page_config(page_title="Test Cognitivo IA", layout="centered")
st.markdown("<h1 style='text-align: center;'>🧠 Test Cognitivo con IA 🤖 Recomendaciones Educativas</h1>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>Completá el siguiente test con las respuestas disponibles, luego presioná <b>Enviar respuestas</b>.</div>", unsafe_allow_html=True)

# --- Lectura de secretos privados ---
SHEET_URL = st.secrets["SHEET_PUBLIC_URL"]
VISUALIZAR_DATOS_PASSWORD1 = st.secrets["VISUALIZAR_DATOS_PASSWORD1"]

# --- Inicialización de variables de sesión ---
if "puntajes" not in st.session_state:
    st.session_state.puntajes = {}
if "formulario_enviado" not in st.session_state:
    st.session_state.formulario_enviado = False

# === FORMULARIO PRINCIPAL DE TEST ===
with st.form("form_test"):
    # --- Datos personales del usuario ---
    st.markdown("""
        <div style='background-color: #f0f8ff; padding: 20px; border-radius: 10px;'>
            <h3 style='text-align: center; color: #1f4e79;'>📏 Datos personales</h3>
    """, unsafe_allow_html=True)

    nombre = st.text_input("Nombre completo *")
    edad = st.number_input("Edad *", min_value=0, max_value=120, step=1)
    ocupacion = st.text_input("Ocupación *")
    nivel_educativo = st.selectbox("Nivel educativo *", ["Primaria", "Secundaria", "Terciario", "Universitario", "Posgrado"])
    correo = st.text_input("Correo electrónico *")
    st.markdown("</div><hr>", unsafe_allow_html=True)

    # --- Organización visual de áreas cognitivas ---
    col1, col2 = st.columns(2)
    respuestas = {}
    areas_col1 = ["Memoria", "Atención"]
    areas_col2 = ["Lenguaje", "Razonamiento"]

    # --- Render de preguntas para cada área ---
    def render_areas(col, areas):
        total_puntaje_area = 0
        for area in areas:
            col.markdown(f"""
                <div style='background-color: #f9f9f9; padding: 10px; border-radius: 8px; margin-bottom: 15px;'>
                    <h4 style='color: #2c3e50;'>{area}</h4>
            """, unsafe_allow_html=True)
            preguntas = test_cognitivo[area]
            for i, pregunta in enumerate(preguntas):
                opciones = pregunta["opciones"]
                mapa_opciones = {f"{k}) {v[0]}": k for k, v in opciones.items()}
                seleccion_etiqueta = col.radio(
                    f"{pregunta['pregunta']}",
                    options=list(mapa_opciones.keys()),
                    key=f"{area}_{i}"
                )
                seleccion = mapa_opciones[seleccion_etiqueta]
                total_puntaje_area += opciones[seleccion][1]
            respuestas[area] = total_puntaje_area
            col.markdown("</div>", unsafe_allow_html=True)

    render_areas(col1, areas_col1)
    render_areas(col2, areas_col2)

    # --- Botón de envío del formulario ---
    enviado = st.form_submit_button("Enviar respuestas")

# === VALIDACIÓN DE DATOS DEL FORMULARIO ===
if enviado:
    campos_vacios = not nombre or edad == 0 or not ocupacion or not nivel_educativo or not correo
    correo_valido = re.match(r"[^@]+@[^@]+\.[^@]+", correo)

    if campos_vacios or not correo_valido:
        st.warning("⚠️ Por favor completá todos los campos obligatorios correctamente. El correo debe tener un formato válido.")
    else:
        # Guardar los datos correctamente validados en el estado de la sesión
        st.session_state.formulario_enviado = True
        st.session_state.puntajes = respuestas
        st.session_state.datos_personales = {
            "nombre": nombre,
            "edad": edad,
            "ocupacion": ocupacion,
            "nivel_educativo": nivel_educativo,
            "correo": correo
        }

# === RESULTADOS Y ANÁLISIS DESPUÉS DEL ENVÍO ===
if st.session_state.formulario_enviado:
    respuestas = st.session_state.puntajes
    datos_personales = st.session_state.datos_personales

    # Mostrar puntajes por área cognitiva
    st.subheader("📊 Resultados por Área")
    for area, pt in respuestas.items():
        st.markdown(f"<div style='margin-bottom: 10px;'><strong>{area.capitalize()}</strong>: {pt} puntos</div>", unsafe_allow_html=True)

   # --- Visualización dual ajustada con tamaño personalizado ---
    st.markdown("### 🧩 Visualización de Resultados Cognitivos")
    col_graf1, col_graf2 = st.columns([1, 1], gap="large")

    with col_graf1:
        st.markdown("**🔹 Perfil Global (Radar)**")
        st.plotly_chart(graficar_radar(respuestas, width=360, height=360), use_container_width=False)

    with col_graf2:
        st.markdown("**🔸 Comparación por Área (Barras con colores)**")
        st.plotly_chart(graficar_barras(respuestas, width=360, height=360), use_container_width=False)


    # Mostrar recomendaciones por nivel de riesgo
    recomendaciones = clasificar_y_recomendar(respuestas)
    st.subheader("✅ Clasificación y Recomendaciones")
    for area, (nivel, reco) in recomendaciones.items():
        st.markdown(f"- **{area.capitalize()}**: {nivel} — {reco}")

    # Entrenamiento del modelo y predicción de riesgo global
    st.info("Entrenando modelo para predecir riesgo general...")
    df_sintetico = leer_datos_reales()
    modelo = entrenar_modelo(df_sintetico)
    riesgo_predicho = predecir_riesgo(modelo, respuestas)
    st.success(f"🔍 Riesgo general predicho: **{riesgo_predicho}**")

    # Generación del informe usando GPT (sólo si aún no se generó)
    st.subheader("📝 Informe personalizado")
    if "texto_gpt" not in st.session_state:
        st.session_state.texto_gpt = generar_informe_gpt(
            respuestas,
            datos_personales["nombre"],
            datos_personales["edad"]
        )
    st.markdown(st.session_state.texto_gpt)

    # Encuesta de utilidad del sistema
    utilidad = st.radio(
        "¿Cómo calificarías esta evaluación?",
        ["⭐☆☆☆☆ (1)", "⭐⭐☆☆☆ (2)", "⭐⭐⭐☆☆ (3)", "⭐⭐⭐⭐☆ (4)", "⭐⭐⭐⭐⭐ (5)"],
        index=None,
        key="utilidad"
    )

    # Si se selecciona una calificación, se habilita la descarga y se guarda en Sheets
    if utilidad:
        st.session_state['utilidad_seleccionada'] = utilidad
        pdf_generado = generar_pdf_streamlit(st.session_state.texto_gpt)

        if st.download_button(
            label="📄 Descargar reporte en PDF",
            data=pdf_generado,
            file_name="reporte_neurotest.pdf",
            mime="application/pdf"
        ):
            guardar_resultados_test(respuestas, utilidad, datos_personales)
            st.session_state.pdf_descargado = True

    # Visualización opcional de los datos en la hoja de cálculo (requiere clave)
    if st.session_state.get("pdf_descargado", False):
        st.markdown("---")
        st.header("🔐 Visualizar Datos")

        if not st.session_state.get("clave_valida", False):
            with st.form("form_visualizar_datos"):
                clave_ingresada = st.text_input("Ingresá la clave para visualizar los datos:", type="password", key="clave_visualizar_datos")
                enviar = st.form_submit_button("Visualizar Datos")

                if enviar:
                    if clave_ingresada.strip() == VISUALIZAR_DATOS_PASSWORD1.strip():
                        st.session_state["clave_valida"] = True
                        st.success("✅ Clave correcta. Abrí la hoja de cálculo en una nueva pestaña 👇")
                        st.markdown(f"[Abrir Hoja de Datos]({SHEET_URL})", unsafe_allow_html=True)
                    else:
                        st.error("❌ Clave incorrecta. Intentalo de nuevo.")
        else:
            st.success("✅ Clave ya validada. Abrí la hoja de cálculo en una nueva pestaña 👇")
            st.markdown(f"[Abrir Hoja de Datos]({SHEET_URL})", unsafe_allow_html=True)
