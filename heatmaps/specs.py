# Custom dependencies
import commons.data as d
import commons.functions as f

# List of Values.
object_specs = {
    "container_control": {
        "header": "Centro de Control",
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
        "style": {"text-align": "center", "font-size": "12px", "width": "100%"},
        "value": 562,
        "clearable": False,
        "placeholder": "Selecciona un Equipo",
        "multi": False,
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
}
