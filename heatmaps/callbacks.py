# Dash components, html, and dash tables
from dash.dependencies import Input, Output

# Custom dependencies
from app import app
import commons.functions as f
from heatmaps.specs import object_specs


@app.callback(
    Output(component_id="fig_contour", component_property="figure"),
    [
        Input(component_id="lov_majorLeague_hm", component_property="value"),
        Input(component_id="lov_season_hm", component_property="value"),
        Input(component_id="lov_player_hm", component_property="value"),
        Input(component_id="lov_trajectory_hm", component_property="value"),
    ],
)
def fig_contour(
    lov_majorLeague_hm=None,
    lov_season_hm=None,
    lov_player_hm=None,
    lov_trajectory_hm=None,
):

    filter_cols = {
        "majorLeagueId": lov_majorLeague_hm,
        "seasonId": lov_season_hm,
        "batterId": lov_player_hm,
        "trajectory": lov_trajectory_hm,
    }
    df = f.filter_df(
        dataset_name=object_specs["fig_contour"]["dataset_name"],
        filter_cols=filter_cols,
        default_filters=object_specs["fig_contour"]["default_filters"],
    )
    obj = f.create_px_figure(
        df=df,
        fig_type=object_specs["fig_contour"]["fig_type"],
        fig_specs=object_specs["fig_contour"]["fig_specs"],
    )

    print(f"Calling from dataset fig_contour. Length of dataset:{len(df)}")
    print(obj)
    return obj


@app.callback(
    Output(component_id="fig_batting_hm8", component_property="figure"),
    [
        Input(component_id="lov_majorLeague_hm", component_property="value"),
        Input(component_id="lov_season_hm", component_property="value"),
        Input(component_id="lov_player_hm", component_property="value"),
        Input(component_id="lov_trajectory_hm", component_property="value"),
    ],
)
def fig_batting_hm8(
    lov_majorLeague=None, lov_season=None, lov_team=None, lov_teamType=None, lov_gameType2=None
):

    print(f"Calling from fig_batting_hm8")

    obj = f.create_px_figure(
        df=None,
        fig_type=object_specs["fig_batting_hm8"]["fig_type"],
        fig_specs=object_specs["fig_batting_hm8"]["fig_specs"],
    )

    return obj


@app.callback(
    Output(component_id="fig_batting_hm4", component_property="figure"),
    [
        Input(component_id="lov_majorLeague_hm", component_property="value"),
        Input(component_id="lov_season_hm", component_property="value"),
        Input(component_id="lov_player_hm", component_property="value"),
        Input(component_id="lov_trajectory_hm", component_property="value"),
    ],
)
def fig_batting_hm4(
    lov_majorLeague=None, lov_season=None, lov_team=None, lov_teamType=None, lov_gameType2=None
):

    print(f"Calling from fig_batting_hm4")

    obj = f.create_px_figure(
        df=None,
        fig_type=object_specs["fig_batting_hm4"]["fig_type"],
        fig_specs=object_specs["fig_batting_hm4"]["fig_specs"],
    )

    return obj
