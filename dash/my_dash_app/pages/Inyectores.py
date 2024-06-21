# apps/Inyectores.py

from dash import html,dcc

layout = html.Div([
    html.H1('Inyectores'),
    html.P('Welcome to Page 1.'),
    dcc.Link('Go to Home', href='/'),
    html.Br(),
    dcc.Link('Go to Page Productores', href='/Productores'),
    html.Br(),
    dcc.Link('Go to Page Patrones', href='/Patrones')
])

