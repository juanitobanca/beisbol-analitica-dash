# Dash components, html, and dash tables

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
        control_children.append(html.Hr())
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
        chart_children.append(dcc.Graph(id=specs["id"], figure=specs["fig"]))

control_container = html.Div(
    id="left-column",
    className="four columns",
    children = control_children,
)

chart_container = html.Div(
    id="right-column",
    className="eight columns",
    children = chart_children,
)


# Main application menu
layout = html.Div(children=[ control_container, chart_container] )
