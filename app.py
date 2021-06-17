# import dash and bootstrap components
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

# set app variable with dash, set external style to bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SANDSTONE],
        meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'},],)
# set app server to variable for deployment
server = app.server

app.layout = html.Div([
    html.H2('Hello World'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='display-value')
])

# set app callback exceptions to true
app.config.suppress_callback_exceptions = True

# set applicaiton title
app.title = 'MLB Historical Data Visualization'
