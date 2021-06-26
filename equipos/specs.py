# Dash components, html, and dash tables

from dash.dependencies import Input, Output

# Custom dependencies

import commons.data as d

# List of Values

lov_specs = {
    "lov_season": {
        "dataset": d.dataset_specs["agg_team_performance_stats"]["dataset"],
        "id": "lov_season",
        "label_col": "seasonId",
        "value_col": "seasonId",
        "P": "Temporada",
        "style": {"text-align": "center", "font-size": "12px", "width": "250px"},
        "value": None,
        "clearable": False,
        "placeholder": "Selecciona una Temporada",
        "multi": True,
    },
    "lov_majorLeague": {
        "dataset": d.dataset_specs["agg_team_performance_stats"]["dataset"],
        "id": "lov_majorLeague",
        "label_col": "majorLeague",
        "value_col": "majorLeagueId",
        "P": "Liga",
        "style": {"text-align": "center", "font-size": "12px", "width": "250px"},
        "value": None,
        "clearable": False,
        "placeholder": "Selecciona una Liga",
        "multi": True,
    },
    "lov_team": {
        "dataset": d.dataset_specs["agg_team_performance_stats"]["dataset"],
        "id": "lov_team",
        "label_col": "teamName",
        "value_col": "teamId",
        "P": "Equipo",
        "style": {"text-align": "center", "font-size": "12px", "width": "250px"},
        "value": None,
        "clearable": False,
        "placeholder": "Selecciona un Equipo",
        "multi": True,
        "default_filters": [{"aggregationType": "AGGREGATE", "gameType2": "RS"}],
        "callback_output": [{"name:": "lov_team", "value": "options"}],
        "callback_input": [
            {"name": "lov_majorLeague", "value": "value"},
            {"name": "lov_season", "value": "value"},
        ],
    },
}

for (lov, specs) in lov_specs.items():

    # Set options
    if specs["default_filters"]:
        df = d.filter_df(df=specs["dataset"], fcols=specs["default_filters"])

    lov_specs[lov]["options"] = d.create_list_of_values(
        df=df, label_col=specs["label_col"], value_col=specs["value_col"]
    )
