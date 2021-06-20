# dash and bootstrap components
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

# app, navbar, layouts, callbacks
import app from app, server
import callbacks
from navbar import Navbar

# equipos, juadores etc
import equipos as e

navbar = Navbar()

content = html.Div([
    dcc.Location(id='url'),
    html.Div(id='page-content')
])

container = dbc.Container([
    content,
])

# Menu callback, set and return
@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return html.Div([dcc.Markdown('''
            ### Beisbol Analitica

        ''')],className='home')
    elif pathname == '/equipos':
        return e.layout
    else:
        return 'ERROR 404: Page not found!'

app.layout = html.Div([
            navbar,
            container
        ])
