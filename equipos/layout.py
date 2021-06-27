#!/usr/bin/python
# Dash components, html, and dash tables

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_table

# Custom dependencies
from equipos.specs import lov_specs

# Layout Children
children = []

for (lov, specs) in lov_specs.items():

    # Set component
    children.append(html.Br())
    children.append(html.P(specs["P"]))
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
