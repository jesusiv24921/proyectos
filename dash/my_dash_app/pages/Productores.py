# apps/Productores.py

from dash import html,dcc

layout = html.Div([
    html.H1('Page 2'),
    html.P('Welcome to Page 2.'),
    dcc.Link('Go to Home', href='/'),
    html.Br(),
    dcc.Link('Go to Page 1', href='/Inyectores')
])

