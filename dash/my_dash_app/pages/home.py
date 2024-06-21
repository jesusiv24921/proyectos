from dash import html, dcc

layout = html.Div([
    # Primera sección con nombre del proyecto y pestañas
    html.Div([
        html.Div('Nombre del Proyecto', style={'color': 'white', 'font-size': '20px', 'padding': '5px'}),
        html.Div([
            html.Div(className='dropdown', style={'margin': '10px', 'color': 'white', 'cursor': 'pointer', 'zIndex': '1000'}, children=[
                html.Span('Apps', className='dropbtn', style={'font-size': '18px'}),
                html.Div([
                    dcc.Link('Inyectores', href='/Inyectores', style={'display': 'block', 'padding': '12px 16px', 'color': 'black'}),
                    dcc.Link('Productores', href='/Productores', style={'display': 'block', 'padding': '12px 16px', 'color': 'black'}),
                    dcc.Link('Patrones', href='/Patrones', style={'display': 'block', 'padding': '12px 16px', 'color': 'black'})
                ], className='dropdown-content', style={'position': 'absolute', 'top': '100%', 'left': '0'})
            ]),
            dcc.Link('About', href='/about', style={'margin': '10px', 'color': 'white'}),
            dcc.Link('ML', href='/ml', style={'margin': '10px', 'color': 'white'}),
            
        ], style={'display': 'flex', 'alignItems': 'center', 'gap': '20px'})
    ], style={'backgroundColor': '#202536', 'overflow': 'visible', 'position': 'relative', 'padding': '20px', 'display': 'flex', 'justifyContent': 'space-between'}),
    
    # Segunda sección con título y texto
    html.Div([
        html.H1('Título Principal', style={'color': 'black', 'font-size': '36px'}),
        html.P('Este es un texto de ejemplo debajo del título principal.', style={'color': 'black', 'font-size': '18px'})
    ], style={'backgroundColor': '#323D61', 'padding': '80px', 'text-align': 'center'}),

    # Bloque de Inyectores
    html.Div([
        html.Div([
            html.H2('Inyectores', style={'color': 'black', 'font-size': '30px'}),
            html.P('Texto descriptivo para la sección de Inyectores.', style={'color': 'black', 'font-size': '18px'})
        ], style={'width': '70%', 'display': 'inline-block', 'verticalAlign': 'top'}),
        html.Div([
            html.Img(src='path/to/image1.png', style={'width': '45%', 'padding': '10px'}),
            html.Img(src='path/to/image2.png', style={'width': '45%', 'padding': '10px'})
        ], style={'width': '30%', 'display': 'inline-block', 'text-align': 'right'})
    ], style={'backgroundColor': 'white', 'padding': '100px', 'borderBottom': '1px solid gray'}),
    
    # Bloque de Productores
    html.Div([
        html.Div([
            html.H2('Productores', style={'color': 'black', 'font-size': '30px'}),
            html.P('Texto descriptivo para la sección de Productores.', style={'color': 'black', 'font-size': '18px'})
        ], style={'width': '70%', 'display': 'inline-block', 'verticalAlign': 'top'}),
        html.Div([
            html.Img(src='path/to/image1.png', style={'width': '45%', 'padding': '10px'}),
            html.Img(src='path/to/image2.png', style={'width': '45%', 'padding': '10px'})
        ], style={'width': '30%', 'display': 'inline-block', 'text-align': 'right'})
    ], style={'backgroundColor': 'white', 'padding': '100px', 'borderBottom': '1px solid gray'}),
    
    # Bloque de Patrones
    html.Div([
        html.Div([
            html.H2('Patrones', style={'color': 'black', 'font-size': '30px'}),
            html.P('Texto descriptivo para la sección de Patrones.', style={'color': 'black', 'font-size': '18px'})
        ], style={'width': '70%', 'display': 'inline-block', 'verticalAlign': 'top'}),
        html.Div([
            html.Img(src='path/to/image1.png', style={'width': '45%', 'padding': '10px'}),
            html.Img(src='path/to/image2.png', style={'width': '45%', 'padding': '10px'})
        ], style={'width': '30%', 'display': 'inline-block', 'text-align': 'right'})
    ], style={'backgroundColor': 'white', 'padding': '100px', 'borderBottom': '1px solid gray'})
], style={'font-family': 'Arial', 'overflowY': 'scroll', 'height': '100vh'})
