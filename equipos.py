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
            html.P("Select Clinic"),
            dcc.Dropdown(
                style = {'text-align': 'center', 'font-size': '12px', 'width': '250px'},
                id='seasons-dropdown',
                options=d.lov_seasons,
                value=d.lov_teams[0]['value'],
                clearable=False,
                placeholder="Selecciona una Temporada",
                ),
            html.P("Select Team"),
            dcc.Dropdown(
                style = {'text-align': 'center', 'font-size': '12px', 'width': '250px'},
                id='teams-dropdown',
                options=d.lov_teams,
                value=d.lov_teams[0]['value'],
                clearable=False
                ),
        ]
)
