# Dash components, html, and dash tables
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table

# Import custom data.py
import data as d

# Main applicaiton menu
layout = html.Div(
    children =
        [
            html.Br(),
            html.P("Temporada"),
            dcc.Dropdown(
                style = {'text-align': 'center', 'font-size': '12px', 'width': '250px', 'display': 'inline-block'},
                id='seasons-dropdown',
                options=d.lov_seasons,
                value=None,
                clearable=False,
                placeholder="Selecciona una Temporada",
                ),
            html.Br(),
            html.P("Liga"),
            dcc.Dropdown(
                style = {'text-align': 'center', 'font-size': '12px', 'width': '250px'},
                id='majorleagues-dropdown',
                options=d.lov_majorLeagues,
                value=None,
                clearable=False,
                placeholder="Selecciona una Liga",
                ),
            html.Br(),
            html.P("Equipo"),
            dcc.Dropdown(
                style = {'text-align': 'center', 'font-size': '12px', 'width': '250px'},
                id='teams-dropdown',
                options=d.lov_teams,
                value=None,
                clearable=False,
                placeholder="Selecciona un Equipo",
                multi=True
                )
        ]
)
