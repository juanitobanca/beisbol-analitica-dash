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
    "lov_player": {
        "dataset_name": "players",
        "object_type": "lov",
        "id": "lov_player_hm",
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
        "searchable": True,
    },
    "lov_trajectory": {
        "dataset_name": "trajectoryType",
        "object_type": "lov",
        "id": "lov_trajectory_hm",
        "label_col": "label",
        "value_col": "value",
        "P": "Trayectoria",
        "style": {"text-align": "center", "font-size": "12px", "width": "100%"},
        "value": None,
        "clearable": True,
        "placeholder": "Selecciona una Trayectoria",
        "multi": True,
        "default_filters": {},
        "callback_output": None,
        "callback_input": None,
        "container": "container_control",
        "searchable": False,
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
        "callback_output": None,
        "callback_input": None,
        "container": "container_control",
        "searchable": False,
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
        "searchable": False,
    },
    "fig_contour": {
        "dataset_name": "pitches",
        "config": {"displayModeBar": False, "responsive": True},
        "fig": {},
        "object_type": "fig",
        "id": "fig_contour",
        "default_filters": {},
        "fig_type": "contour",
        "fig_specs": {
            "x": "coordX",
            "y": "coordY",
            "title": "Pelotas puestas en juego",
            "color_discrete_map": {},
            "labels": {
                "x": "X",
                "y": "Y",
            },
            "showlegend": False,
            "height": 350,
            "orientation": "v",
        },
        "container": "container_heatmaps",
        "callback_output": [
            {"component_id": "fig_contour", "component_property": "figure"}
        ],
        "callback_input": [
            {
                "component_id": "lov_majorLeague_hm",
                "component_property": "value",
                "filter_col": "majorLeagueId",
            },
            {
                "component_id": "lov_season_hm",
                "component_property": "value",
                "filter_col": "seasonId",
            },
            {
                "component_id": "lov_player_hm",
                "component_property": "value",
                "filter_col": "seasonId",
            },
            {
                "component_id": "lov_trajectory_hm",
                "component_property": "value",
                "filter_col": "seasonId",
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
