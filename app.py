# import dash and bootstrap components
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

# Navbar, layouts, custom callbacks
from navbar import Navbar

import equipos as e

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


# set app variable with dash, set external style to bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[external_stylesheets,
        meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'},],)

# set app server to variable for deployment
server = app.server

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

# set app callback exceptions to true
app.config.suppress_callback_exceptions = True

# set applicaiton title
app.title = 'Béisbol Analítica'
