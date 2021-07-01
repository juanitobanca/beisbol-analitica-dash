# import dash and bootstrap components
import dash
import dash_bootstrap_components as dbc

# set app variable with dash, set external style to bootstrap theme
app = dash.Dash(__name__,
        suppress_callback_exceptions = True,
        meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'},],)

# set app server to variable for deployment
server = app.server

# set applicaiton title
app.title = "Béisbol Analítica"
