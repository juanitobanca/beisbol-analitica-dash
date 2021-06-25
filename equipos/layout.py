# Dash components, html, and dash tables
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_table

# Custom dependencies
import app.data as d

# Main application menu
layout = html.Div(
    children =
        [
            html.Br(),
            html.P("Temporada"),
            # TODO: Move all of this to the lov spec
            dcc.Dropdown(
                style = {'text-align': 'center', 'font-size': '12px', 'width': '250px'},
                id='lov_season',
                options=d.lov_specs['lov_season']['options'],
                value=None,
                clearable=False,
                placeholder="Selecciona una Temporada",
                ),
            html.Br(),
            html.P("Liga"),
            dcc.Dropdown(
                style = {'text-align': 'center', 'font-size': '12px', 'width': '250px'},
                id='lov_majorLeague',
                options=d.lov_specs['lov_majorLeague']['options'],
                value=None,
                clearable=False,
                placeholder="Selecciona una Liga",
                ),
            html.Br(),
            html.P("Equipo"),
            dcc.Dropdown(
                style = {'text-align': 'center', 'font-size': '12px', 'width': '250px'},
                id='lov_team',
                options=d.lov_specs['lov_team']['options'],
                value=None,
                clearable=False,
                placeholder="Selecciona un Equipo",
                multi=True
                )
        ]
)
