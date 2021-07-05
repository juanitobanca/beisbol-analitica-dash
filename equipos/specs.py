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
    "container_partidos": {
        "header": "Partidos",
        "children": [],
        "object_type": "container",
    },
    "lov_season": {
        "dataset_name": "agg_team_performance_stats",
        "object_type": "lov",
        "id": "lov_season",
        "label_col": "seasonId",
        "value_col": "seasonId",
        "P": "Temporada",
        "style": {"text-align": "center", "font-size": "12px", "width": "200px"},
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
        "style": {"text-align": "center", "font-size": "12px", "width": "200px"},
        "value": 125,
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
        "style": {"text-align": "center", "font-size": "12px", "width": "200px"},
        "value": [520, 523, 528, 532],
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
        "style": {"text-align": "center", "font-size": "12px", "width": "200px"},
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
    "lov_gameType": {
        "dataset_name": "gameType",
        "object_type": "lov",
        "id": "lov_gameType",
        "label_col": "label",
        "value_col": "value",
        "P": "Tipo de Partido",
        "style": {"text-align": "center", "font-size": "12px", "width": "200px"},
        "value": "RS",
        "clearable": False,
        "placeholder": "Selecciona un Valor",
        "multi": False,
        "default_filters": None,
        "callback_output": None,
        "callback_input": None,
        "container": "container_control",
        "callback_output": [
            {"component_id": "lov_gameType", "component_property": "options"}
        ],
    },
    "fig_winPercentage": {
        "dataset_name": "agg_team_performance_stats",
        "config": {"displayModeBar": False},
        "fig": None,
        "object_type": "fig",
        "id": "fig_winPercentage",
        "default_filters": {
            "aggregationType": "CUMULATIVE",
            "gameType2": "RS",
        },
        "fig_type": "line",
        "fig_specs": {
            "x": "gameDate",
            "y": "winPercentage",
            "title": "% de Victoria",
            "color": "teamName",
            "labels": {
                "winPercentage": "% de Victoria",
                "gameDate": "Fecha",
                "teamName": "Equipo",
            },
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
        ],
    },
    "fig_runDifferential": {
        "dataset_name": "agg_team_performance_stats",
        "container": "container_winPercentage",
        "config": {"displayModeBar": False},
        "fig": None,
        "object_type": "fig",
        "id": "fig_runDifferential",
        "default_filters": {
            "aggregationType": "CUMULATIVE",
            "gameType2": "RS",
        },
        "fig_type": "line",
        "fig_specs": {
            "x": "gameDate",
            "y": "runDifferential",
            "title": "Diferencial de Carreras",
            "color": "teamName",
            "labels": {
                "runDifferential": "Diferencial de Carreras(RS-RA)",
                "gameDate": "Fecha",
                "teamName": "Equipo",
            },
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
        ],
    },
    "fig_pythagoreanExp": {
        "dataset_name": "agg_team_performance_stats",
        "container": "container_winPercentage",
        "config": {"displayModeBar": False},
        "fig": None,
        "object_type": "fig",
        "id": "fig_pythagoreanExp",
        "default_filters": {
            "aggregationType": "CUMULATIVE",
            "gameType2": "RS",
        },
        "fig_type": "line",
        "fig_specs": {
            "x": "gameDate",
            "y": "pythagoreanExpectation",
            "title": "Expectativa Pitagorica",
            "color": "teamName",
            "labels": {
                "pythagoreanExpectation": "Expectativa Pitagorica",
                "gameDate": "Fecha",
                "teamName": "Equipo",
            },
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
