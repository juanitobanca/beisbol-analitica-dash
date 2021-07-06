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

    elif specs["object_type"] == "table":
        print("Table")
        print(specs["fig"])
        print("----------")
        object_specs[specs['container']]['children'].append(
            dbc.Col(html.Div(
                dt.DataTable(id = specs["id"], columns=[{'name': 'Fecha', 'id': 'gameDate'}], data=[{'teamId': 520, 'teamType': 'away', 'gameType2': 'PS', 'boxscoreUrl': 'https://www.milb.com/gameday/525105#game_state=final', 'playByPlayUrl': 'https://www.milb.com/gameday/525105#game_tab=play-by-play', 'majorLeagueId': 125, 'seasonId': 2017.0, 'gameDate': '2017-08-17', 'venueName': 'Estadio De Beisbol Beto Avila', 'homeTeamName': 'Tigres de Quintana Roo', 'awayTeamName': 'Pericos de Puebla', 'homeScore': 1.0, 'awayScore': 6.0, 'runDifference': 5.0, 'resultado': 'Ganado', 'attendance': 5754.0}, {'teamId': 520, 'teamType': 'away', 'gameType2': 'PS', 'boxscoreUrl': 'https://www.milb.com/gameday/525106#game_state=final', 'playByPlayUrl': 'https://www.milb.com/gameday/525106#game_tab=play-by-play', 'majorLeagueId': 125, 'seasonId': 2017.0, 'gameDate': '2017-08-18', 'venueName': 'Estadio De Beisbol Beto Avila', 'homeTeamName': 'Tigres de Quintana Roo', 'awayTeamName': 'Pericos de Puebla', 'homeScore': 0.0, 'awayScore': 2.0, 'runDifference': 2.0, 'resultado': 'Ganado', 'attendance': 5306.0}, {'teamId': 520, 'teamType': 'away', 'gameType2': 'PS', 'boxscoreUrl': 'https://www.milb.com/gameday/525122#game_state=final', 'playByPlayUrl': 'https://www.milb.com/gameday/525122#game_tab=play-by-play', 'majorLeagueId': 125, 'seasonId': 2017.0, 'gameDate': '2017-08-25', 'venueName': 'Parque Kukulkan', 'homeTeamName': 'Leones de Yucatan', 'awayTeamName': 'Pericos de Puebla', 'homeScore': 1.0, 'awayScore': 4.0, 'runDifference': 3.0, 'resultado': 'Ganado', 'attendance': 12000.0}, {'teamId': 520, 'teamType': 'away', 'gameType2': 'PS', 'boxscoreUrl': 'https://www.milb.com/gameday/525123#game_state=final', 'playByPlayUrl': 'https://www.milb.com/gameday/525123#game_tab=play-by-play', 'majorLeagueId': 125, 'seasonId': 2017.0, 'gameDate': '2017-08-26', 'venueName': 'Parque Kukulkan', 'homeTeamName': 'Leones de Yucatan', 'awayTeamName': 'Pericos de Puebla', 'homeScore': 7.0, 'awayScore': 6.0, 'runDifference': -1.0, 'resultado': 'Perdido', 'attendance': 12000.0}, {'teamId': 520, 'teamType': 'away', 'gameType2': 'PS', 'boxscoreUrl': 'https://www.milb.com/gameday/525131#game_state=final', 'playByPlayUrl': 'https://www.milb.com/gameday/525131#game_tab=play-by-play', 'majorLeagueId': 125, 'seasonId': 2017.0, 'gameDate': '2017-09-07', 'venueName': 'Estadio Gasmart', 'homeTeamName': 'Toros de Tijuana', 'awayTeamName': 'Pericos de Puebla', 'homeScore': 5.0, 'awayScore': 3.0, 'runDifference': -2.0, 'resultado': 'Perdido', 'attendance': 16231.0}, {'teamId': 520, 'teamType': 'away', 'gameType2': 'PS', 'boxscoreUrl': 'https://www.milb.com/gameday/525132#game_state=final', 'playByPlayUrl': 'https://www.milb.com/gameday/525132#game_tab=play-by-play', 'majorLeagueId': 125, 'seasonId': 2017.0, 'gameDate': '2017-09-06', 'venueName': 'Estadio Gasmart', 'homeTeamName': 'Toros de Tijuana', 'awayTeamName': 'Pericos de Puebla', 'homeScore': 8.0, 'awayScore': 2.0, 'runDifference': -6.0, 'resultado': 'Perdido', 'attendance': 15105.0}]) )
            )
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
                dbc.Col(
                    children=[
                        dbc.Row(container_winPercentage),
                        html.Br(),
                        dbc.Row(container_games),
                    ],
                    width=10,
                ),
            ],
        ),
    ],
)
