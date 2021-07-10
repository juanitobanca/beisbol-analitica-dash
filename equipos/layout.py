# Dash components, html, and dash tables

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt


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
            html.Div(dcc.Dropdown(
                style=specs["style"],
                id=specs["id"],
                options=specs["options"],
                value=specs["value"],
                clearable=specs["clearable"],
                placeholder=specs["placeholder"],
                multi=specs["multi"],
            ), style = {'width': '100%'})
        )

    elif specs["object_type"] == "fig":
        object_specs[specs['container']]['children'].append(
            dbc.Col(html.Div(dcc.Graph(
                id=specs["id"], figure=specs["fig"], config = specs['config']
            )), style = {'width': '30%'})
        )

    elif specs["object_type"] == "table":
        object_specs[specs['container']]['children'].append(
            dbc.Col(html.Div(
                dt.DataTable(id = specs["id"],
                             columns = [ {"name" : name, "id" : specs["id"], "presentation" : specs["presentation"] } for name, specs in specs['fig_specs']["columns"].items() ],
                             style_cell = specs['fig_specs']["style_cell"],
                             page_size = specs['fig_specs']["page_size"],
                             sort_action = specs['fig_specs']["sort_action"],
                             style_table = specs['fig_specs']['style_table'],
                             #fill_width = specs['fig_specs']['fill_width']
                             #css = specs['fig_specs']['css']
                            )
            ), style = {'width': '100%'}
        ))

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
            children= [ dbc.Row(
                children=object_specs["container_games_row1"]["children"]
            ),
            dbc.Row(
                children=object_specs["container_games_row2"]["children"]
            ) ]
        ),
    ]
)

# Main application menu.
layout = dbc.Container(
    fluid=True,
    children=[
        dbc.Row(children=[html.Br()]),
        dbc.Row(
            children=[
                dbc.Col(container_control, md=2),
                dbc.Col(
                    children=[
                        #dbc.Row(container_winPercentage),
                        html.Br(),
                        dbc.Row(container_games),
                    ],
                   md=10
                ),
            ],
        ),
    ],
)
