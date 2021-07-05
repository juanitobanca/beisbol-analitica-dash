# Dash components, html, and dash tables

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

# Custom dependencies
from equipos.specs import object_specs

# Set Container Children Specs
# TODO: Abstract This
for (obj, specs) in object_specs.items():

    if specs["object_type"] == "lov":

        # Set component
        object_specs[specs['container']]['children'].append(html.Br())
        object_specs[specs['container']]['children'].append(html.P(specs["P"]))
        object_specs[specs['container']]['children'].append(
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
        object_specs[specs['container']]['children'].append(
            dbc.Col(html.Div(dcc.Graph(
                id=specs["id"], figure=specs["fig"], config = specs['config']
            )))
        )

container_control = dbc.Card(
    children=[
        dbc.CardHeader(object_specs['container_control']['header']),
        dbc.CardBody(children=object_specs['container_control']['children']),
    ]
)

container_winPercentage = dbc.Card(
    children=[
        dbc.CardHeader(object_specs["container_winPercentage"]["header"]),
        dbc.CardBody(
            children=dbc.Row(
                children=object_specs["container_winPercentage"]["children"]
            )
        ),
    ]
)

container_games = dbc.Card(
    children=[
        dbc.CardHeader(object_specs["container_games"]["header"]),
        dbc.CardBody(
            children=dbc.Row(
                children=object_specs["container_games"]["children"]
            )
        ),
    ]
)

# Main application menu..
layout = dbc.Container(
    fluid=True,
    children=[
        dbc.Row(children=[html.Br()]),
        dbc.Row(
            children=[
                dbc.Col(container_control, width=2),
                dbc.Col(dbc.Row(container_winPercentage), width=10),
            ],
        )
    ],
)
