# 🧠 NeuroTest-GENAI-V2 – Evaluación Cognitiva con IA Generativa 🤖  
> Informe personalizado con GPT-4 Turbo y visualización de habilidades cognitivas  
> 🔁 Este proyecto es una evolución del asistente [Neurotest_cognitivo_IA (v1)](https://github.com/c-e-leiva/Neurotest_cognitivo_IA)

![GPT-4 Turbo](https://img.shields.io/badge/GPT--4-Turbo-%237235c9?style=for-the-badge&logo=openai&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-%23FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

---

## ✨ ¿Qué es NeuroTest-GENAI-V2?

**NeuroTest-GENAI-V2** es una aplicación interactiva desarrollada con Python y Streamlit que permite realizar un test cognitivo rápido y accesible, con resultados interpretados y redactados por inteligencia artificial generativa.

El sistema evalúa memoria, atención, lenguaje y razonamiento. Al finalizar, ofrece un informe motivador con recomendaciones prácticas y una visualización clara de tu perfil cognitivo.

---

## 🧩 Características principales

- ✅ Test interactivo dividido en 4 áreas cognitivas.
- 🧠 Análisis e informe generados con **GPT-4 Turbo**.
- 📄 Descarga del resultado en PDF personalizado.
- 📊 Visualización en dos formatos: radar (perfil general) y barras (comparación directa).
- 🔐 Acceso protegido con login por contraseña.
- ☁️ Almacenamiento automático en **Google Sheets**.

---

## 📊 Visualización de resultados

El sistema incluye dos gráficos complementarios:

- **Radar (Spider Chart)**: muestra tu perfil cognitivo global en una vista circular equilibrada.
- **Barras horizontales coloreadas**: ordena tus puntajes de menor a mayor, con colores según nivel de riesgo:
  - 🟩 Verde: Sin riesgo  
  - 🟨 Leve  
  - 🟧 Moderado  
  - 🟥 Alto

Estas visualizaciones permiten interpretar de forma rápida qué áreas requieren más atención o están más fortalecidas.

---

## ⚙️ ¿Cómo funciona por detrás?

El flujo general de NeuroTest-GENAI-V2 es el siguiente:

1. **app.py** lanza la interfaz de usuario en Streamlit.
2. El usuario accede mediante una contraseña validada en `access/login.py`.
3. Se solicitan datos personales y se presenta el test (`utils/test_data.py`).
4. Las respuestas se procesan y se calcula un puntaje por área (`utils/interaccion.py`).
5. Se genera un análisis del riesgo global con un modelo entrenado (`model/classifier.py`).
6. El informe se redacta automáticamente con lenguaje natural usando GPT-4 (`utils/report_generator_gpt.py`).
7. El sistema muestra resultados visuales (`utils/visualizacion.py`) y permite exportar un PDF (`utils/export_pdf_streamlit.py`).
8. Todo se guarda automáticamente en una hoja de cálculo de Google Sheets (`utils/sheets.py`).

> La aplicación sigue una arquitectura modular, lo que facilita su mantenimiento, extensión y reutilización.

---
## 🚀 Tecnologías utilizadas

- `OpenAI GPT-4 Turbo` – generación de informes personalizados.
- `Streamlit` – interfaz interactiva.
- `Plotly` – visualización en gráficos radar y barras.
- `ReportLab` – creación de PDFs en memoria.
- `Google Sheets API + gspread` – almacenamiento automático.
- `scikit-learn` – clasificación de riesgo cognitivo.
- `pandas`, `numpy`, `dotenv` – manipulación de datos y configuración.

---

## ▶️ Cómo usar

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/NeuroTest-GENAI-V2.git
cd NeuroTest-GENAI-V2
```

### 2. Crear entorno virtual

```bash
python -m venv .venv
.venv\Scripts\activate     # Windows
source .venv/bin/activate    # Linux/macOS
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar tus credenciales

Crear el archivo `.streamlit/secrets.toml` con:

```toml
OPENAI_API_KEY = "sk-..."

[google_service_account]
type = "service_account"
project_id = "..."
private_key_id = "..."
private_key = "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
client_email = "..."
client_id = "..."
...
SHEET_PUBLIC_URL = "https://docs.google.com/spreadsheets/..."
VISUALIZAR_DATOS_PASSWORD1 = "tuclave"
```

### 5. Ejecutar la app

```bash
streamlit run app.py
```

---

## 📁 Estructura del proyecto

```
NeuroTest-GENAI-V2
├── app.py                          # Lógica principal de la app
├── access/
│   └── login.py                   # Módulo de autenticación
├── utils/
│   ├── test_data.py              # Preguntas y opciones del test
│   ├── visualizacion.py          # Radar + barras con colores
│   ├── interaccion.py            # Evaluación de respuestas
│   ├── sheets.py                 # Integración con Google Sheets
│   ├── report_generator_gpt.py   # Informe redactado con GPT-4
│   └── export_pdf_streamlit.py   # Generador de PDF en memoria
├── data/
│   └── generador.py              # Dataset base (entrenamiento)
├── model/
│   └── classifier.py             # Modelo Random Forest
├── .streamlit/
│   └── secrets.toml              # Credenciales privadas
├── requirements.txt
└── README.md
```

---

## 👤 Contacto

Autor: Carlos Ezequiel Leiva  
📍 Buenos Aires, Argentina  
🔗 [LinkedIn](https://www.linkedin.com/in/carlos-ezequiel-leiva)  
📧 xc.leiva@gmail.com