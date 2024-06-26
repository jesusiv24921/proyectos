# index.py
# Manejador de de navegaciòn entre las diferentes paginas

# index.py
from dash import html, dcc
from dash.dependencies import Input, Output
from app import app
from pages import home, Inyectores, Productores, Patrones

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/Inyectores':
        return Inyectores.layout
    elif pathname == '/Productores':
        return Productores.layout
    elif pathname == '/Patrones':
        return Patrones.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(debug=True)
