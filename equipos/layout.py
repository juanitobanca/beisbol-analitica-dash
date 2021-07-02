# Dash components, html, and dash tables

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

# Custom dependencies
from equipos.specs import object_specs

# Children
control_children = []
chart_children = []


for (lov, specs) in object_specs.items():

    """
    Abstract This
    """
    if specs["object_type"] == "lov":
        # Set component
        control_children.append(html.Br())
        control_children.append(html.P(specs["P"]))
        control_children.append(
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

    elif specs["object_type"] == "fig":
        chart_children.append(dcc.Graph(id=specs["id"], figure=specs["fig"], config={'displayModeBar': False }))

control_container = dbc.Card(
    children = [ dbc.CardHeader("Centro de Control"),
                 dbc.CardBody( children = control_children )
               ]
    )

chart_container = dbc.Card(
    children = [ dbc.CardHeader("Porcentajes de Victoria"),
                 dbc.CardBody( children = chart_children )
               ]
    )

# Main application menu
layout =  dbc.Container(
        fluid = True,
        children = [ dbc.Row( children=[
                    dbc.Col(control_container, width=3,  align="left"),
                    dbc.Col(chart_container, width = 9)
                    ]
                ) ],

        )
