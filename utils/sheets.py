# sheets.py
# Este módulo permite conectar y escribir resultados en una hoja de cálculo de Google Sheets
# utilizando credenciales seguras y Streamlit. Guarda los datos del test y feedback del usuario.

import streamlit as st                     # Para acceder a secrets y mostrar errores en la app
import gspread                             # Cliente para interactuar con Google Sheets
from google.oauth2.service_account import Credentials  # Para autenticación con cuenta de servicio
import datetime                            # Para registrar la fecha y hora del test

# Permisos necesarios para acceder y editar hojas de cálculo y archivos en Google Drive
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def conectar_google_sheets():
    try:
        # Se obtienen las credenciales desde secrets (archivo .streamlit/secrets.toml)
        creds_dict = st.secrets["google_service_account"]

        # Se crea un objeto de credenciales con los scopes definidos
        creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)

        # Se autoriza el cliente gspread con las credenciales
        client = gspread.authorize(creds)

        # Se accede a la URL pública de la hoja definida también en secrets
        sheet_url = st.secrets["SHEET_PUBLIC_URL"]

        # Se abre la hoja por URL y se accede a la pestaña llamada "Resultados"
        return client.open_by_url(sheet_url).worksheet("Resultados")

    except Exception as e:
        # En caso de error, se muestra el mensaje y se interrumpe la ejecución
        st.error(f"Error al conectar con Google Sheets: {e}")
        raise

def escribir_en_hoja(hoja, fila):
    # Agrega una fila al final de la hoja de cálculo con los datos recibidos
    hoja.append_row(fila)

def guardar_resultados_test(respuestas, utilidad, datos_personales):
    # Se conecta a la hoja de cálculo
    hoja = conectar_google_sheets()

    # Se obtiene la fecha y hora actual para registrar el momento del test
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Se arma una fila con los datos personales, resultados por área y feedback de utilidad
    fila = [
        fecha,
        datos_personales.get("nombre", ""),
        datos_personales.get("edad", ""),
        datos_personales.get("ocupacion", ""),
        datos_personales.get("nivel_educativo", ""),
        datos_personales.get("correo", "")
    ] + [respuestas.get(area, 0) for area in ["Memoria", "Atención", "Lenguaje", "Razonamiento"]] + [utilidad]

    # Se escribe la fila en la hoja
    escribir_en_hoja(hoja, fila)