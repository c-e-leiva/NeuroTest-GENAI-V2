# classifier.py
# Este módulo entrena un modelo de clasificación (Random Forest) con datos cognitivos
# y lo utiliza para predecir el nivel de riesgo cognitivo de nuevos usuarios.

from sklearn.ensemble import RandomForestClassifier  # Clasificador basado en árboles de decisión
from sklearn.model_selection import train_test_split  # Para dividir el dataset en entrenamiento y prueba
from sklearn.metrics import classification_report     # Para evaluar el desempeño del modelo

def entrenar_modelo(df):
    # Separa las características (X) del target (y)
    X = df[['Memoria', 'Atención', 'Lenguaje', 'Razonamiento']]  # Variables predictoras
    y = df['riesgo']  # Variable objetivo

    # Divide el dataset en conjunto de entrenamiento y prueba (80% - 20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Inicializa el clasificador Random Forest con una semilla fija para reproducibilidad
    modelo = RandomForestClassifier(random_state=42)

    # Entrena el modelo con los datos de entrenamiento
    modelo.fit(X_train, y_train)

    # Predice los resultados del conjunto de prueba
    y_pred = modelo.predict(X_test)

    # Muestra en consola un reporte con métricas del modelo (precision, recall, f1, etc.)
    print("Reporte de clasificación del modelo:")
    print(classification_report(y_test, y_pred))

    # Devuelve el modelo entrenado
    return modelo

def predecir_riesgo(modelo, puntajes):
    import pandas as pd  # Importación local para evitar dependencias innecesarias si no se llama esta función

    # Convierte el diccionario de puntajes en un DataFrame con una sola fila
    df_input = pd.DataFrame([puntajes])

    # Usa el modelo para predecir el riesgo cognitivo
    pred = modelo.predict(df_input)[0]

    # Devuelve la predicción (por ejemplo: 'Sin riesgo', 'Leve', etc.)
    return pred
