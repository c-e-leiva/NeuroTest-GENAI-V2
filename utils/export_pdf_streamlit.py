# export_pdf_streamlit.py
# Este módulo genera un informe PDF en memoria a partir de texto generado por IA (GPT),
# optimizado para su descarga directa desde una app hecha con Streamlit.

from io import BytesIO  # Para trabajar con archivos en memoria (sin escribir en disco)
from reportlab.lib.pagesizes import letter  # Tamaño de página estándar para PDF (carta)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle  # Estilos de texto para el PDF
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer  # Componentes del layout del PDF

def generar_pdf_streamlit(texto_gpt, nombre="reporte_neurotest"):
    """
    Genera un PDF en memoria a partir del texto GPT.
    
    Parámetros:
        texto_gpt (str): Texto generado por GPT-4.
        nombre (str): Nombre del archivo (sin extensión).

    Retorna:
        BytesIO: PDF listo para usar con st.download_button.
    """

    # Crear buffer de memoria para almacenar el PDF generado (no se guarda en disco)
    buffer = BytesIO()

    # Crear documento PDF con márgenes definidos
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,       # Formato carta
        rightMargin=40,        # Margen derecho
        leftMargin=40,         # Margen izquierdo
        topMargin=40,          # Margen superior
        bottomMargin=40        # Margen inferior
    )

    # Obtener estilos predefinidos y agregar uno personalizado para el informe
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Informe", fontName="Helvetica", fontSize=11, leading=15))

    elements = []  # Lista de elementos (párrafos, espacios, etc.) que formarán el PDF

    # Agregar título del reporte
    elements.append(Paragraph("🧠 Reporte NeuroTest", styles["Title"]))
    elements.append(Spacer(1, 20))  # Espaciado después del título

    # Separar el texto en líneas y convertir cada una en un párrafo
    for linea in texto_gpt.strip().split("\n"):
        if linea.strip():  # Ignorar líneas vacías
            elements.append(Paragraph(linea.strip(), styles["Informe"]))
            elements.append(Spacer(1, 12))  # Espaciado entre párrafos

    # Construir el PDF con todos los elementos
    doc.build(elements)

    # Mover el cursor al inicio del buffer para poder descargarlo desde Streamlit
    buffer.seek(0)

    # Retornar el PDF en formato BytesIO (ideal para usar con st.download_button)
    return buffer
