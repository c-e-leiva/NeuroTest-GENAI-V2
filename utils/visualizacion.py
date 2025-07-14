# visualizacion.py
# Este módulo genera visualizaciones interactivas para representar los resultados
# cognitivos del test. Incluye:
# - Gráfico radar: vista global del perfil cognitivo
# - Gráfico de barras horizontales: comparación clara por puntaje, con colores por riesgo

import plotly.graph_objects as go  # Librería de gráficos interactivos Plotly

def graficar_radar(respuestas, width=350, height=350):
    """
    Genera un gráfico tipo radar (polar) para visualizar de forma integral
    los puntajes obtenidos por área cognitiva.

    Parámetros:
        respuestas (dict): Áreas cognitivas como claves, puntajes como valores.
        width (int): Ancho del gráfico en píxeles.
        height (int): Alto del gráfico en píxeles.

    Retorna:
        fig (plotly.graph_objects.Figure): Objeto gráfico radar.
    """
    categorias = list(respuestas.keys())
    valores = list(respuestas.values())

    # Cierra el polígono repitiendo primer punto
    valores.append(valores[0])
    categorias.append(categorias[0])

    fig = go.Figure(
        data=[go.Scatterpolar(
            r=valores,
            theta=categorias,
            fill='toself',
            name='Puntaje por área',
            line=dict(color='#1f77b4', width=3),
            marker=dict(symbol='circle', size=8)
        )],
        layout=go.Layout(
            polar=dict(
                bgcolor="#fafafa",
                radialaxis=dict(
                    visible=True,
                    range=[0, 25],
                    showline=True,
                    linewidth=1,
                    gridcolor="lightgrey"
                )
            ),
            width=width,
            height=height,
            showlegend=False,
            margin=dict(t=20, b=20)
        )
    )

    return fig

def color_por_nivel(valor):
    """
    Asigna color según puntaje:
    - Verde: sin riesgo
    - Amarillo: leve
    - Naranja: moderado
    - Rojo: alto riesgo
    """
    if valor >= 12:
        return 'green'
    elif valor >= 9:
        return 'gold'
    elif valor >= 6:
        return 'orange'
    else:
        return 'red'

def graficar_barras(respuestas, width=350, height=350):
    """
    Genera un gráfico de barras horizontales ordenado de menor a mayor puntaje,
    y coloreado según el nivel de riesgo cognitivo.

    Parámetros:
        respuestas (dict): Áreas cognitivas como claves, puntajes como valores.
        width (int): Ancho del gráfico en píxeles.
        height (int): Alto del gráfico en píxeles.

    Retorna:
        fig (plotly.graph_objects.Figure): Objeto gráfico de barras.
    """
    ordenado = sorted(respuestas.items(), key=lambda x: x[1])
    categorias = [x[0] for x in ordenado]
    valores = [x[1] for x in ordenado]
    colores = [color_por_nivel(v) for v in valores]

    fig = go.Figure(
        data=[go.Bar(
            x=valores,
            y=categorias,
            orientation='h',
            marker_color=colores,
            text=valores,
            textposition='auto'
        )]
    )

    fig.update_layout(
        title="Puntaje por Área Cognitiva (ordenado)",
        xaxis=dict(title="Puntaje", range=[0, 25]),
        yaxis=dict(title="Área"),
        width=width,
        height=height,
        margin=dict(t=40, b=40)
    )

    return fig
