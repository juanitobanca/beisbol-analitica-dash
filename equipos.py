# Dash components, html, and dash tables
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table

# Import custom data.py
import data as d

# Main application menu
layout = html.Div(
    children =
        [
            html.Br(),
            html.P("Temporada"),
            dcc.Dropdown(
                style = {'text-align': 'center', 'font-size': '12px', 'width': '250px', 'display': 'inline-block'},
                id='lov_season',
                options=d.lov_season,
                value=None,
                clearable=False,
                placeholder="Selecciona una Temporada",
                ),
            html.Br(),
            html.P("Liga"),
            dcc.Dropdown(
                style = {'text-align': 'center', 'font-size': '12px', 'width': '250px'},
                id='lov_majorLeague',
                options=d.lov_majorLeague,
                value=None,
                clearable=False,
                placeholder="Selecciona una Liga",
                ),
            html.Br(),
            html.P("Equipo"),
            dcc.Dropdown(
                style = {'text-align': 'center', 'font-size': '12px', 'width': '250px'},
                id='lov_team',
                options=d.lov_team,
                value=None,
                clearable=False,
                placeholder="Selecciona un Equipo",
                multi=True
                )
        ]
)
