# generador.py
# Este módulo se encarga de cargar datos reales desde un archivo CSV para ser utilizados
# en el entrenamiento del modelo de clasificación de riesgo cognitivo.

from pathlib import Path  # Para construir rutas de archivos de forma segura y multiplataforma
import pandas as pd       # Biblioteca para manipulación de datos en estructuras tipo DataFrame

def leer_datos_reales():
    """
    Lee un archivo CSV con datos reales y devuelve un DataFrame
    con las columnas necesarias para entrenamiento del modelo.
    """

    # Ruta al archivo CSV que contiene los datos reales
    # Se usa Path(__file__).parent para obtener el directorio donde se encuentra este archivo
    ruta_csv = Path(__file__).parent / "datos_reales.csv"

    # Carga los datos del CSV en un DataFrame de pandas
    df = pd.read_csv(ruta_csv)

    # Selección de columnas clave utilizadas como features (input) y target (output)
    columnas = ["Memoria", "Atención", "Lenguaje", "Razonamiento", "riesgo"]
    data = df[columnas]  # Se filtra el DataFrame original para quedarse solo con esas columnas

    # Se devuelve un nuevo DataFrame con las columnas seleccionadas
    return pd.DataFrame(data, columns=columnas)
