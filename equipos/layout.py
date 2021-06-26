#!/usr/bin/python
# Dash components, html, and dash tables

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_table

from dash.dependencies import Input, Output

# Custom dependencies

import data as d

# Layout Children
children = []

# List of Values

lov_specs = {
    "lov_team": {
        "dataset": dataset_specs["agg_team_performance_stats"]["dataset"],
        "id": "lov_team",
        "lcol": "teamName",
        "vcol": "teamId",
        "label": "Equipo",
        "style": {"text-align": "center", "font-size": "12px", "width": "250px"},
        "value": None,
        "clearable": False,
        "placeholder": "Selecciona un Equipo",
        "multi": True,
        "callback_output": Output("lov_team", "options"),
        "callback_input": [
            Input("lov_majorLeague", "value"),
            Input("lov_season", "value"),
        ],
    },
    "lov_season": {
        "dataset": dataset_specs["agg_team_performance_stats"]["dataset"],
        "id": "lov_season",
        "lcol": "seasonId",
        "vcol": "seasonId",
        "label": "Temporada",
        "style": {"text-align": "center", "font-size": "12px", "width": "250px"},
        "value": None,
        "clearable": False,
        "placeholder": "Selecciona una Temporada",
        "multi": True,
    },
    "lov_majorLeague": {
        "dataset": dataset_specs["agg_team_performance_stats"]["dataset"],
        "id": "lov_majorLeague",
        "lcol": "majorLeague",
        "vcol": "majorLeagueId",
        "label": "Liga",
        "style": {"text-align": "center", "font-size": "12px", "width": "250px"},
        "value": None,
        "clearable": False,
        "placeholder": "Selecciona una Liga",
        "multi": True,
    },
}

for (lov, specs) in lov_specs.items():

    # Set options
    lov_specs[lov]["options"] = create_list_of_values(
        df=specs["dataset"], lcol=specs["lcol"], vcol=specs["vcol"]
    )

    # Set component
    children.append(html.Br())
    children.append(html.P(specs["label"]))
    children.append(
        dcc.Dropdown(
            style=specs["style"],
            id=specs["id"],
            options=specs["options"],
            value=specs["value"],
            clearable=specs["clearable"],
            placeholder=specs["placeholder"],
            multi=specs["multi"],
        )
    )

# Main application menu
layout = html.Div(children=children)
