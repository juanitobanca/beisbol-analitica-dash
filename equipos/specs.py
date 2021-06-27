# Charts
import plotly.express as px

# Custom dependencies
import commons.data as d
import commons.functions as f

# List of Values
object_specs = {
    "lov_season": {
        "dataset": d.dataset_specs["agg_team_performance_stats"]["dataset"],
        "object_type": "lov",
        "id": "lov_season",
        "label_col": "seasonId",
        "value_col": "seasonId",
        "P": "Temporada",
        "style": {"text-align": "center", "font-size": "12px", "width": "250px"},
        "value": None,
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
    },
    "lov_majorLeague": {
        "dataset": d.dataset_specs["agg_team_performance_stats"]["dataset"],
        "object_type": "lov",
        "id": "lov_majorLeague",
        "label_col": "majorLeague",
        "value_col": "majorLeagueId",
        "P": "Liga",
        "style": {"text-align": "center", "font-size": "12px", "width": "250px"},
        "value": None,
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
    },
    "lov_team": {
        "dataset": d.dataset_specs["agg_team_performance_stats"]["dataset"],
        "object_type": "lov",
        "id": "lov_team",
        "label_col": "teamName",
        "value_col": "teamId",
        "P": "Equipo",
        "style": {"text-align": "center", "font-size": "12px", "width": "250px"},
        "value": None,
        "clearable": False,
        "placeholder": "Selecciona un Equipo",
        "multi": True,
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
    "fig_winPercentage": {
        "dataset": d.dataset_specs["agg_team_performance_stats"]["dataset"],
        "object_type": "fig",
        "id": "fig_winPercentage",
        "default_filters": {
            "aggregationType": "CUMULATIVE",
            "gameType2": "RS",
            "groupingDescription": "MAJORLEAGUEID_SEASONID_GAMETYPE2_TEAMID",
        },
        "fig_type" : "scatter",
        "fig_specs": {"x":"gameDate","y:""winPercentage"},
        "callback_output": None,
        "callback_input": None,
    },
}

# Set the dataset and options spec. Abstract this
for (obj, specs) in object_specs.items():

    object_specs[obj]["dataset"] = f.filter_df(
        df=specs["dataset"], filter_cols=specs["default_filters"]
    )

    object_specs[obj]["options"] = f.create_list_of_values(
        df=specs["dataset"], label_col=specs["label_col"], value_col=specs["value_col"]
    )

    if specs["object_type"] = "fig":
         if specs["fig_type"]:
             object_specs[obj]["options"] = px.scatter( df = specs["dataset"], **kwargs(specs[fig_type]) )
