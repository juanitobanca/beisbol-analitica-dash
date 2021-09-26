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
    "container_heatmaps": {
        "header": "HeatMaps",
        "children": [],
        "object_type": "container",
    },
    "lov_players": {
        "dataset_name": "players",
        "object_type": "lov",
        "id": "lov_players_hm",
        "label_col": "name",
        "value_col": "playerId",
        "P": "Jugador",
        "style": {"text-align": "center", "font-size": "12px", "width": "100%"},
        "value": 110029,
        "clearable": False,
        "placeholder": "Selecciona un Jugador",
        "multi": False,
        "default_filters": {},
        "callback_output": None,
        "callback_input": None,
        "container": "container_control",
        "searchable" : True
    },
    "lov_pitches": {
        "dataset_name": "pitches",
        "object_type": "lov",
        "id": "lov_pitches_hm",
        "label_col": "trajectory",
        "value_col": "trajectory",
        "P": "Trayectoria",
        "style": {"text-align": "center", "font-size": "12px", "width": "100%"},
        "value": None,
        "clearable": True,
        "placeholder": "Selecciona una Trayectoria",
        "multi": True,
        "default_filters": {},
        "callback_output": None ,
        "callback_input": None,
        "container": "container_control",
        "searchable" : False
    },
    "lov_season": {
        "dataset_name": "agg_team_performance_stats",
        "object_type": "lov",
        "id": "lov_season_hm",
        "label_col": "seasonId",
        "value_col": "seasonId",
        "P": "Temporada",
        "style": {"text-align": "center", "font-size": "12px", "width": "100%"},
        "value": None,
        "clearable": True,
        "placeholder": "Selecciona una Temporada",
        "multi": False,
        "default_filters": {
            "aggregationType": "AGGREGATED",
            "gameType2": "RS",
            "groupingDescription": "MAJORLEAGUEID_SEASONID_GAMETYPE2_TEAMID",
        },
        "callback_output": None ,
        "callback_input": None,
        "container": "container_control",
        "searchable" : False
    },
    "lov_majorLeague": {
        "dataset_name": "agg_team_performance_stats",
        "object_type": "lov",
        "id": "lov_majorLeague_hm",
        "label_col": "majorLeague",
        "value_col": "majorLeagueId",
        "P": "Liga",
        "style": {"text-align": "center", "font-size": "12px", "width": "100%"},
        "value": None,
        "clearable": True,
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
        "searchable" : False
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