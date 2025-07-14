# login.py
# Este módulo gestiona el acceso inicial a la app NeuroTest mediante una clave.
# Utiliza Streamlit para generar una interfaz de login visual y segura.

import streamlit as st  # Librería para crear aplicaciones web interactivas en Python

# Cargar clave de acceso desde el archivo .streamlit/secrets.toml
# Esta clave es necesaria para que los usuarios autorizados puedan iniciar el test
CLAVE_ACCESO = st.secrets["VISUALIZAR_DATOS_PASSWORD1"]

def mostrar_login():
    # Configura el título y diseño de la pestaña del navegador
    st.set_page_config(page_title="NeuroTest - Iniciar sesión", layout="centered")

    # Encabezado visual personalizado con HTML embebido
    st.markdown(
        """
        <div style='text-align: center; margin-bottom: 30px;'>
            <h1>🧠 Bienvenido a NeuroTest 🤖</h1>
            <p style='font-size:17px;'>
                Una herramienta interactiva para explorar tus habilidades cognitivas.<br>
                Completá un test personalizado y recibí un informe generado por <strong>IA Generativa.</strong> 
            </p>
        </div>
        """,
        unsafe_allow_html=True  # Permite renderizar el HTML personalizado
    )

    # Línea divisoria y título del formulario
    st.markdown("---")
    st.markdown("### 🔐 Iniciar sesión")
    st.info("Este acceso es necesario para comenzar el test. Usá la clave autorizada.")

    # Campo para ingresar la clave de acceso (enmascarado por seguridad)
    password = st.text_input("Clave de acceso", type="password", placeholder="Ingresá la clave")

    # Botón para enviar la clave y validar
    if st.button("Ingresar"):
        if password == CLAVE_ACCESO:
            # Si la clave es correcta, se guarda el estado de acceso autorizado en la sesión
            st.session_state["acceso_autorizado"] = True
            st.success("✔️ Acceso autorizado. ¡Bienvenido/a a NeuroTest!")
            st.rerun()  # Reinicia la app para que se actualice el flujo
        else:
            # Si la clave es incorrecta, se muestra un mensaje de error
            st.error("❌ Clave incorrecta. Verificá e intentá de nuevo.")
