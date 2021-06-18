# import dash and bootstrap components
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

# Navbar, layouts, custom callbacks
from navbar import Navbar


# set app variable with dash, set external style to bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SANDSTONE],
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

app.layout = html.Div([
            navbar,
            container
        ])

# set app callback exceptions to true
app.config.suppress_callback_exceptions = True

# set applicaiton title
app.title = 'Béisbol Analítica'