# Dash components, html, and dash tables

import dash_core_components as dcc
import dash_html_components as html

# Custom dependencies
from equipos.specs import object_specs

# Layout Children
children = []


for (lov, specs) in object_specs.items():

    """
    Abstract This
    """
    if specs["object_type"] == "lov":

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

    elif specs["object_type"] == "fig":

        children.append(dcc.Graph(id=specs["id"], figure=specs["fig"]))

# Main application menu
layout = html.Div(children=children)
