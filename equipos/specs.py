# Custom dependencies
import commons.data as d
import commons.functions as f

# List of Values
object_specs = {
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
        "get_groupingDescription": False,
        "default_filters": {
            "aggregationType": "AGGREGATED",
            "gameType2": "RS",
            "groupingDescription": "MAJORLEAGUEID_SEASONID_GAMETYPE2_TEAMID",
        },
        "callback_output": None,
        "callback_input": None,
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
        "get_groupingDescription": False,
        "default_filters": {
            "aggregationType": "AGGREGATED",
            "gameType2": "RS",
            "groupingDescription": "MAJORLEAGUEID_SEASONID_GAMETYPE2_TEAMID",
        },
        "callback_output": None,
        "callback_input": None,
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
        "get_groupingDescription": False,
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
        "dataset_name": "home_away",
        "object_type": "lov",
        "id": "lov_teamType",
        "label_col": "label",
        "value_col": "value",
        "P": "Local/Visitante",
        "style": {"text-align": "center", "font-size": "12px", "width": "200px"},
        "value": '',
        "clearable": False,
        "placeholder": "Selecciona un Valor",
        "multi": False,
        "get_groupingDescription": False,
        "default_filters": None,
        "callback_output": [
            {"component_id": "lov_teamType", "component_property": "options"}
        ],
    },
    "fig_winPercentage": {
        "dataset_name": "agg_team_performance_stats",
        "get_groupingDescription": True,
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
        ],
    },
    "fig_runDifferential": {
        "dataset_name": "agg_team_performance_stats",
        "get_groupingDescription": True,
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
                "runDifferential": "Diferencia de Carreras",
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
        ],
    },
}

# Set the dataset and options spec. Abstract this
for (obj, specs) in object_specs.items():

    # Set aggregation type filter
    if specs["get_groupingDescription"]:
        object_specs[obj]["default_filters"][
            "groupingDescription"
        ] = f.get_groupingDescription(specs)

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
