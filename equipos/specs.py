# Custom dependencies
import commons.data as d
import commons.functions as f

# List of Values
object_specs = {
    "container_control": {
        "header": "Centro de Control",
        "children": [],
        "object_type": "container",
    },
    "container_winPercentage": {
        "header": "Carreras y Porcentajes de Victoria",
        "children": [],
        "object_type": "container",
    },
    "container_games": {
        "header": "Partidos",
        "children": [],
        "object_type": "container",
    },
    "container_games_row1": {
        "children": [],
        "object_type": "row",
        "container": "container_games",
    },
    "container_games_row2": {
        "children": [],
        "object_type": "row",
        "container": "container_games",
    },
    "container_batting": {
        "header": "Estadisticas de Bateo",
        "children": [],
        "object_type": "container",
    },
    "container_batting_row1": {
        "children": [],
        "object_type": "row",
        "container": "container_batting",
    },
    "lov_season": {
        "dataset_name": "agg_team_performance_stats",
        "object_type": "lov",
        "id": "lov_season",
        "label_col": "seasonId",
        "value_col": "seasonId",
        "P": "Temporada",
        "style": {"text-align": "center", "font-size": "12px", "width": "100%"},
        "value": 2017,
        "clearable": False,
        "placeholder": "Selecciona una Temporada",
        "multi": False,
        "default_filters": {
            "aggregationType": "AGGREGATED",
            "gameType2": "RS",
            "groupingDescription": "MAJORLEAGUEID_SEASONID_GAMETYPE2_TEAMID",
        },
        "callback_output": None,
        "callback_input": None,
        "container": "container_control",
    },
    "lov_majorLeague": {
        "dataset_name": "agg_team_performance_stats",
        "object_type": "lov",
        "id": "lov_majorLeague",
        "label_col": "majorLeague",
        "value_col": "majorLeagueId",
        "P": "Liga",
        "style": {"text-align": "center", "font-size": "12px", "width": "100%"},
        "value": 131,
        "clearable": False,
        "placeholder": "Selecciona una Liga",
        "multi": False,
        "default_filters": {
            "aggregationType": "AGGREGATED",
            "gameType2": "RS",
            "groupingDescription": "MAJORLEAGUEID_SEASONID_GAMETYPE2_TEAMID",
        },
        "callback_output": None,
        "callback_input": None,
        "container": "container_control",
    },
    "lov_team": {
        "dataset_name": "agg_team_performance_stats",
        "object_type": "lov",
        "id": "lov_team",
        "label_col": "teamName",
        "value_col": "teamId",
        "P": "Equipo",
        "style": {"text-align": "center", "font-size": "12px", "width": "100%"},
        "value": [668],
        "clearable": False,
        "placeholder": "Selecciona un Equipo",
        "multi": True,
        "container": "container_control",
        "default_filters": {
            "aggregationType": "AGGREGATED",
            "gameType2": "RS",
            "groupingDescription": "MAJORLEAGUEID_SEASONID_GAMETYPE2_TEAMID",
        },
        "callback_output": [
            {"component_id": "lov_team", "component_property": "options"}
        ],
        "callback_input": [
            {
                "component_id": "lov_majorLeague",
                "component_property": "value",
                "filter_col": "majorLeagueId",
            },
            {
                "component_id": "lov_season",
                "component_property": "value",
                "filter_col": "seasonId",
            },
        ],
    },
    "lov_teamType": {
        "dataset_name": "teamType",
        "object_type": "lov",
        "id": "lov_teamType",
        "label_col": "label",
        "value_col": "value",
        "P": "Local/Visitante",
        "style": {"text-align": "center", "font-size": "12px", "width": "100%"},
        "value": "",
        "clearable": False,
        "placeholder": "Selecciona un Valor",
        "multi": False,
        "default_filters": None,
        "callback_output": None,
        "callback_input": None,
        "container": "container_control",
        "callback_output": [
            {"component_id": "lov_teamType", "component_property": "options"}
        ],
    },
    "lov_gameType2": {
        "dataset_name": "gameType2",
        "object_type": "lov",
        "id": "lov_gameType2",
        "label_col": "label",
        "value_col": "value",
        "P": "Tipo de Partido",
        "style": {"text-align": "center", "font-size": "12px", "width": "100%"},
        "value": "RS",
        "clearable": False,
        "placeholder": "Selecciona un Valor",
        "multi": False,
        "default_filters": None,
        "callback_output": None,
        "callback_input": None,
        "container": "container_control",
        "callback_output": [
            {"component_id": "lov_gameType2", "component_property": "options"}
        ],
    },
    "fig_winPercentage": {
        "dataset_name": "agg_team_performance_stats",
        "config": {"displayModeBar": False, "responsive": True},
        "fig": {},
        "object_type": "fig",
        "id": "fig_winPercentage",
        "default_filters": {
            "aggregationType": "CUMULATIVE",
        },
        "fig_type": "line",
        "fig_specs": {
            "melt_by": ["gameDate"],
            "metrics": ["winPercentage", "pythagoreanExpectation"],
            "title": "Porcentaje de Victoria",
            "color": "teamName",
            "color_discrete_map": {},
            "labels": {
                "winPercentage": "% de Victoria",
                "gameDate": "Fecha",
                "teamName": "Equipo",
            },
            "showlegend": False,
            "height" : 350,
        },
        "container": "container_winPercentage",
        "callback_output": [
            {"component_id": "fig_winPercentage", "component_property": "figure"}
        ],
        "callback_input": [
            {
                "component_id": "lov_majorLeague",
                "component_property": "value",
                "filter_col": "majorLeagueId",
            },
            {
                "component_id": "lov_season",
                "component_property": "value",
                "filter_col": "seasonId",
            },
            {
                "component_id": "lov_team",
                "component_property": "value",
                "filter_col": "teamId",
            },
            {
                "component_id": "lov_teamType",
                "component_property": "value",
                "filter_col": "teamType",
            },
            {
                "component_id": "lov_gameType2",
                "component_property": "value",
                "filter_col": "gameType2",
            },
        ],
    },
    "fig_runDifferential": {
        "dataset_name": "agg_team_performance_stats",
        "container": "container_winPercentage",
        "config": {"displayModeBar": False, "responsive": True},
        "fig": {},
        "object_type": "fig",
        "id": "fig_runDifferential",
        "default_filters": {
            "aggregationType": "CUMULATIVE",
        },
        "fig_type": "line",
        "fig_specs": {
            "melt_by": ["gameDate"],
            "metrics": ["runDifferential", "runsAllowed", "runs"],
            "title": "Diferencial de Carreras(RS-RA)",
            "color": "teamName",
            "color_discrete_map": {},
            "labels": {
                "runDifferential": "Diferencial de Carreras(RS-RA)",
                "gameDate": "Fecha",
                "teamName": "Equipo",
            },
            "showlegend": False,
            "height" : 350,
        },
        "callback_output": [
            {"component_id": "fig_runDifferential", "component_property": "figure"}
        ],
        "callback_input": [
            {
                "component_id": "lov_majorLeague",
                "component_property": "value",
                "filter_col": "majorLeagueId",
            },
            {
                "component_id": "lov_season",
                "component_property": "value",
                "filter_col": "seasonId",
            },
            {
                "component_id": "lov_team",
                "component_property": "value",
                "filter_col": "teamId",
            },
            {
                "component_id": "lov_teamType",
                "component_property": "value",
                "filter_col": "teamType",
            },
            {
                "component_id": "lov_gameType2",
                "component_property": "value",
                "filter_col": "gameType2",
            },
        ],
    },
    "fig_pythagoreanExp": {
        "dataset_name": "agg_team_performance_stats",
        "container": "container_winPercentage",
        "config": {"displayModeBar": False, "responsive": True},
        "fig": {},
        "object_type": "fig",
        "id": "fig_pythagoreanExp",
        "default_filters": {
            "aggregationType": "CUMULATIVE",
        },
        "fig_type": "line",
        "fig_specs": {
            "x": "gameDate",
            "y": "pythagoreanExpectation",
            "title": "Expectativa Pitagorica",
            "color": "teamName",
            "color_discrete_map": {},
            "labels": {
                "pythagoreanExpectation": "Expectativa Pitagorica",
                "gameDate": "Fecha",
                "teamName": "Equipo",
            },
            "showlegend": False,
            "height" : 350,
        },
        "callback_output": [
            {"component_id": "fig_pythagoreanExp", "component_property": "figure"}
        ],
        "callback_input": [
            {
                "component_id": "lov_majorLeague",
                "component_property": "value",
                "filter_col": "majorLeagueId",
            },
            {
                "component_id": "lov_season",
                "component_property": "value",
                "filter_col": "seasonId",
            },
            {
                "component_id": "lov_team",
                "component_property": "value",
                "filter_col": "teamId",
            },
            {
                "component_id": "lov_teamType",
                "component_property": "value",
                "filter_col": "teamType",
            },
            {
                "component_id": "lov_gameType2",
                "component_property": "value",
                "filter_col": "gameType2",
            },
        ],
    },
    "fig_games": {
        "dataset_name": "games",
        "container": "container_games_row1",
        "config": {"displayModeBar": False, "responsive": True},
        "fig": {},
        "object_type": "fig",
        "id": "fig_games",
        "default_filters": {},
        "fig_type": "bar",
        "fig_specs": {
            "x": "gameDate",
            "y": "runDifference",
            "title": "Resultados de Partidos",
            "color": "resultado",
            "color_discrete_map": {"Ganado": "#00cc96", "Perdido": "#ee563b"},
            "labels": {
                "resultado": "Resultado",
                "runDifference": "Diferencia de Carreras",
                "gameDate": "Fecha",
            },
            "showlegend": True,
            "height" : 350,
        },
        "callback_output": [
            {"component_id": "fig_games", "component_property": "figure"}
        ],
        "callback_input": [
            {
                "component_id": "lov_majorLeague",
                "component_property": "value",
                "filter_col": "majorLeagueId",
            },
            {
                "component_id": "lov_season",
                "component_property": "value",
                "filter_col": "seasonId",
            },
            {
                "component_id": "lov_team",
                "component_property": "value",
                "filter_col": "teamId",
            },
            {
                "component_id": "lov_teamType",
                "component_property": "value",
                "filter_col": "teamType",
            },
            {
                "component_id": "lov_gameType2",
                "component_property": "value",
                "filter_col": "gameType2",
            },
        ],
    },
    "fig_attendance": {
        "dataset_name": "games",
        "container": "container_games_row1",
        "config": {"displayModeBar": False, "responsive": True},
        "fig": {},
        "object_type": "fig",
        "id": "fig_attendance",
        "default_filters": {},
        "fig_type": "bar",
        "fig_specs": {
            "x": "gameDate",
            "y": "attendance",
            "title": "Asistencia del Publico",
            "color": None,
            "color_discrete_map": {},
            "labels": {
                "attendance": "Asistencia",
                "gameDate": "Fecha",
            },
            "showlegend": False,
            "height" : 350,
        },
        "callback_output": [
            {"component_id": "fig_attendance", "component_property": "figure"}
        ],
        "callback_input": [
            {
                "component_id": "lov_majorLeague",
                "component_property": "value",
                "filter_col": "majorLeagueId",
            },
            {
                "component_id": "lov_season",
                "component_property": "value",
                "filter_col": "seasonId",
            },
            {
                "component_id": "lov_team",
                "component_property": "value",
                "filter_col": "teamId",
            },
            {
                "component_id": "lov_teamType",
                "component_property": "value",
                "filter_col": "teamType",
            },
            {
                "component_id": "lov_gameType2",
                "component_property": "value",
                "filter_col": "gameType2",
            },
        ],
    },
    "fig_hit_distribution": {
        "dataset_name": "agg_batting_stats",
        "container": "container_batting_row1",
        "config": {"displayModeBar": False, "responsive": True},
        "fig": {},
        "object_type": "fig",
        "id": "fig_hit_distribution",
        "fig_type": "pie",
        "default_filters": {
            "aggregationType": "AGGREGATED",
        },
        "fig_specs": {
            "title": "Distribucion de Hits",
            "melt_by": ["teamName"],
            "metrics": [
                "X1B",
                "X2B",
                "X3B",
                "HR",
            ],
            "labels": {
                "metric": "Metrica",
                "value": "Total",
            },
            "showlegend": True,
            "height" : 300,
        },
        "callback_output": [
            {"component_id": "fig_hit_distribution", "component_property": "figure"}
        ],
        "callback_input": [
            {
                "component_id": "lov_majorLeague",
                "component_property": "value",
                "filter_col": "majorLeagueId",
            },
            {
                "component_id": "lov_season",
                "component_property": "value",
                "filter_col": "seasonId",
            },
            {
                "component_id": "lov_team",
                "component_property": "value",
                "filter_col": "teamId",
            },
            {
                "component_id": "lov_teamType",
                "component_property": "value",
                "filter_col": "teamType",
            },
            {
                "component_id": "lov_gameType2",
                "component_property": "value",
                "filter_col": "gameType2",
            },
        ],
    },
    "fig_plate_appearance_distribution": {
        "dataset_name": "agg_batting_stats",
        "container": "container_batting_row1",
        "config": {"displayModeBar": False, "responsive": True},
        "fig": {},
        "object_type": "fig",
        "id": "fig_plate_appearance_distribution",
        "fig_type": "pie",
        "default_filters": {
            "aggregationType": "AGGREGATED",
        },
        "fig_specs": {
            "title": "Distribucion de Apariciones al Plato",
            "melt_by": ["teamName"],
            "metrics": ["SO", "H", "BB", "HBP"],
            "labels": {
                "metric": "Metrica",
                "value": "Total",
            },
            "showlegend": True,
            "height" : 300,
        },
        "callback_output": [
            {
                "component_id": "fig_plate_appearance_distribution",
                "component_property": "figure",
            }
        ],
        "callback_input": [
            {
                "component_id": "lov_majorLeague",
                "component_property": "value",
                "filter_col": "majorLeagueId",
            },
            {
                "component_id": "lov_season",
                "component_property": "value",
                "filter_col": "seasonId",
            },
            {
                "component_id": "lov_team",
                "component_property": "value",
                "filter_col": "teamId",
            },
            {
                "component_id": "lov_teamType",
                "component_property": "value",
                "filter_col": "teamType",
            },
            {
                "component_id": "lov_gameType2",
                "component_property": "value",
                "filter_col": "gameType2",
            },
        ],
    },
    "fig_fb_ab_distribution": {
        "dataset_name": "agg_batting_stats",
        "container": "container_batting_row1",
        "config": {"displayModeBar": False, "responsive": True},
        "fig": {},
        "object_type": "fig",
        "id": "fig_fb_ab_distribution",
        "fig_type": "pie",
        "default_filters": {
            "aggregationType": "AGGREGATED",
        },
        "fig_specs": {
            "title": "Distribucion de FlyBalls y Groundballs",
            "melt_by": ["teamName"],
            "metrics": [
                "PU",
                "GB",
                "LD",
                "FB",
            ],
            "labels": {
                "metric": "Metrica",
                "value": "Total",
            },
            "showlegend": True,
            "height" : 300,
        },
        "callback_output": [
            {"component_id": "fig_fb_ab_distribution", "component_property": "figure"}
        ],
        "callback_input": [
            {
                "component_id": "lov_majorLeague",
                "component_property": "value",
                "filter_col": "majorLeagueId",
            },
            {
                "component_id": "lov_season",
                "component_property": "value",
                "filter_col": "seasonId",
            },
            {
                "component_id": "lov_team",
                "component_property": "value",
                "filter_col": "teamId",
            },
            {
                "component_id": "lov_teamType",
                "component_property": "value",
                "filter_col": "teamType",
            },
            {
                "component_id": "lov_gameType2",
                "component_property": "value",
                "filter_col": "gameType2",
            },
        ],
    },
    "table_games": {
        "dataset_name": "games",
        "container": "container_games_row2",
        "object_type": "table",
        "fig_type": "table",
        "id": "table_games",
        "fig": {},
        "fig_specs": {
            "id": "table_games",
            "sort_action": "native",
            "style_cell": {
                "fontSize": 11,
                "font-family": "sans-serif",
                "textAlign": "center",
                "vertical-align": "top",
            },
            "page_size": 7,
            "columns": {
                "Fecha": {"id": "gameDate", "type": "text", "presentation": "text"},
                "Boxscore": {
                    "id": "boxscoreUrl",
                    "type": "any",
                    "presentation": "markdown",
                },
                "Jugada a Jugada": {
                    "id": "playByPlayUrl",
                    "type": "any",
                    "presentation": "markdown",
                },
                "Estadio": {"id": "venueName", "type": "text", "presentation": "text"},
                "Equipo Local": {
                    "id": "homeTeamName",
                    "type": "text",
                    "presentation": "text",
                },
                "Marcador": {
                    "id": "resultadoCarreras",
                    "type": "text",
                    "presentation": "text",
                },
                "Equipo Visitante": {
                    "id": "awayTeamName",
                    "type": "text",
                    "presentation": "text",
                },
                "Resultado": {
                    "id": "resultado",
                    "type": "text",
                    "presentation": "text",
                },
                "Asistencia": {
                    "id": "attendance",
                    "type": "text",
                    "presentation": "text",
                },
                "Doble Juego": {
                    "id": "doubleHeader",
                    "type": "text",
                    "presentation": "text",
                },
                "Dia/Noche": {"id": "dayNight", "type": "text", "presentation": "text"},
                "Clima": {"id": "weather", "type": "text", "presentation": "text"},
            },
            "style_table": {"width": "100%"},
            "fill_width": False,
            "css": [{"selector": "table", "rule": "width: 100%;"}],
        },
        "default_filters": {},
        # "container": "container_games",
        "callback_output": [
            {"component_id": "table_games", "component_property": "data"}
        ],
        "callback_input": [
            {
                "component_id": "lov_majorLeague",
                "component_property": "value",
                "filter_col": "majorLeagueId",
            },
            {
                "component_id": "lov_season",
                "component_property": "value",
                "filter_col": "seasonId",
            },
            {
                "component_id": "lov_team",
                "component_property": "value",
                "filter_col": "teamId",
            },
            {
                "component_id": "lov_teamType",
                "component_property": "value",
                "filter_col": "teamType",
            },
            {
                "component_id": "lov_gameType2",
                "component_property": "value",
                "filter_col": "gameType2",
            },
        ],
    },
}

# Set the dataset and options spec. Abstract this
for (obj, specs) in object_specs.items():

    # Set lov specs
    if specs["object_type"] == "lov":
        df = f.filter_df(
            dataset_name=specs["dataset_name"],
            filter_cols=specs["default_filters"],
            default_filters=specs["default_filters"],
        )
        object_specs[obj]["options"] = f.create_list_of_values(
            df=df,
            label_col=specs["label_col"],
            value_col=specs["value_col"],
        )
