# Dash components, html, and dash tables
import dash_core_components as dcc
import dash_html_components as html
import dash_table

# Import Bootstrap components
import dash_bootstrap_components as dbc

# Import custom data.py
import data as d

# Main applicaiton menu
layout = html.Div([
    dbc.Row(
        [
            dbc.Col(dcc.Dropdown(
                style = {'text-align': 'center', 'font-size': '12px', 'width': '250px'},
                id='seasons-dropdown',
                options=d.lov_seasons,
                value=d.lov_teams[0]['value'],
                clearable=False,
                placeholder="Select a city",
                ),
                xs={'size':'auto', 'offset':0}, sm={'size':'auto', 'offset':0}, md={'size':'auto', 'offset':0},
                lg={'size':'auto', 'offset':0}, xl={'size':'auto', 'offset':0}),
            dbc.Col(html.H2(style={'text-align': 'center', 'font-size': '12px'}, children='Equipo '),
                xs={'size':'auto', 'offset':0}, sm={'size':'auto', 'offset':0}, md={'size':'auto', 'offset':3},
                lg={'size':'auto', 'offset':0}, xl={'size':'auto', 'offset':0}),
            dbc.Col(dcc.Dropdown(
                style = {'text-align': 'center', 'font-size': '12px', 'width': '250px'},
                id='teams-dropdown',
                options=d.lov_teams,
                value=d.lov_teams[0]['value'],
                clearable=False),
                xs={'size':'auto', 'offset':0}, sm={'size':'auto', 'offset':0}, md={'size':'auto', 'offset':0},
                lg={'size':'auto', 'offset':0}, xl={'size':'auto', 'offset':0}),
        ],
            justify="center",
        ),
],className = 'app-page')
