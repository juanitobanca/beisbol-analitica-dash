
# Dash components, html, and dash tables
from dash.dependencies import Input, Output

# Custom dependencies
from app import app
import commons.functions as f
from heatmaps.specs import object_specs


@app.callback(
    Output(component_id="lov_team", component_property="options"),
    [
        Input(component_id="lov_majorLeague", component_property="value"),
        Input(component_id="lov_season", component_property="value"),
    ],
)
def lov_team(lov_majorLeague=None, lov_season=None):
    filter_cols = {"majorLeagueId": lov_majorLeague, "seasonId": lov_season}
    df = f.filter_df(
        dataset_name=object_specs["lov_team"]["dataset_name"],
        filter_cols=filter_cols,
        default_filters=object_specs["lov_team"]["default_filters"],
    )
    obj = f.create_list_of_values(
        df=df,
        label_col=object_specs["lov_team"]["label_col"],
        value_col=object_specs["lov_team"]["value_col"],
    )

    return obj
