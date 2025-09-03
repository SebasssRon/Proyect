import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Cargar dataset
df = pd.read_csv("dataset.csv")

# Crear la app
app = dash.Dash(__name__)

# Gráfico de histograma
histograma = px.histogram(df, x=df.columns[0])

# Gráfico de dispersión
dispersion = px.scatter(df, x=df.columns[0], y=df.columns[1])

# Layout de la app
app.layout = html.Div([
    html.H1("Mi Aplicación de Visualización", style={'textAlign': 'center'}),

    html.H3("Histograma"),
    dcc.Graph(figure=histograma),

    html.H3("Gráfico de Dispersión"),
    dcc.Graph(figure=dispersion),

    html.H3("Interacción"),
    dcc.Checklist(
        options=[
            {"label": "Opción A", "value": "A"},
            {"label": "Opción B", "value": "B"},
        ],
        value=["A"]
    ),
    html.Button("Haz clic aquí", id="boton")
])

if __name__ == "__main__":
    app.run_server(debug=True)
