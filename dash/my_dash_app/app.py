#Configuración Principal de la aplicación

# app.py
from dash import Dash

app = Dash(__name__, suppress_callback_exceptions=True)
app.title = "My Multi-Page App"




