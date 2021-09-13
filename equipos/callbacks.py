
# Dash components, html, and dash tables
from dash.dependencies import Input, Output

# Custom dependencies
from app import app
import commons.functions as f
from equipos.specs import object_specs


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

@app.callback(
    Output(component_id="fig_winPercentage", component_property="figure"),
    [
        Input(component_id="lov_majorLeague", component_property="value"),
        Input(component_id="lov_season", component_property="value"),
        Input(component_id="lov_team", component_property="value"),
        Input(component_id="lov_teamType", component_property="value"),
        Input(component_id="lov_gameType2", component_property="value"),
    ],
)
def fig_winPercentage(
    lov_majorLeague, lov_season=None, lov_team=None, lov_teamType=None, lov_gameType2=None
):
    print(f"Calling from winPercentage")
    filter_cols = {
        "majorLeagueId": lov_majorLeague,
        "seasonId": lov_season,
        "teamId": lov_team,
        "teamType": lov_teamType,
        "gameType2" : lov_gameType2,
    }
    df = f.filter_df(
        dataset_name=object_specs["fig_winPercentage"]["dataset_name"],
        filter_cols=filter_cols,
        default_filters=object_specs["fig_winPercentage"]["default_filters"],
    )
    obj = f.create_px_figure(
        df=df,
        fig_type=object_specs["fig_winPercentage"]["fig_type"],
        fig_specs=object_specs["fig_winPercentage"]["fig_specs"],
    )

    print(obj)
    return obj

@app.callback(
    Output(component_id="fig_runDifferential", component_property="figure"),
    [
        Input(component_id="lov_majorLeague", component_property="value"),
        Input(component_id="lov_season", component_property="value"),
        Input(component_id="lov_team", component_property="value"),
        Input(component_id="lov_teamType", component_property="value"),
        Input(component_id="lov_gameType2", component_property="value"),
    ],
)
def fig_runDifferential(
    lov_majorLeague=None, lov_season=None, lov_team=None, lov_teamType=None, lov_gameType2=None
):

    print(f"Calling from runDifferential")
    filter_cols = {
        "majorLeagueId": lov_majorLeague,
        "seasonId": lov_season,
        "teamId": lov_team,
        "teamType": lov_teamType,
        "gameType2" : lov_gameType2,
    }
    df = f.filter_df(
        dataset_name=object_specs["fig_runDifferential"]["dataset_name"],
        filter_cols=filter_cols,
        default_filters=object_specs["fig_runDifferential"]["default_filters"],
    )
    obj = f.create_px_figure(
        df=df,
        fig_type=object_specs["fig_runDifferential"]["fig_type"],
        fig_specs=object_specs["fig_runDifferential"]["fig_specs"],
    )

    return obj

@app.callback(
    Output(component_id="fig_wins_losses", component_property="figure"),
    [
        Input(component_id="lov_majorLeague", component_property="value"),
        Input(component_id="lov_season", component_property="value"),
        Input(component_id="lov_team", component_property="value"),
        Input(component_id="lov_teamType", component_property="value"),
        Input(component_id="lov_gameType2", component_property="value"),
    ],
)
def fig_wins_losses(
    lov_majorLeague=None, lov_season=None, lov_team=None, lov_teamType=None, lov_gameType2=None
):

    print(f"Calling from pythagoreanExp")
    filter_cols = {
        "majorLeagueId": lov_majorLeague,
        "seasonId": lov_season,
        "teamId": lov_team,
        "teamType": lov_teamType,
        "gameType2" : lov_gameType2,
    }
    df = f.filter_df(
        dataset_name=object_specs["fig_wins_losses"]["dataset_name"],
        filter_cols=filter_cols,
        default_filters=object_specs["fig_wins_losses"]["default_filters"],
    )
    obj = f.create_px_figure(
        df=df,
        fig_type=object_specs["fig_wins_losses"]["fig_type"],
        fig_specs=object_specs["fig_wins_losses"]["fig_specs"],
    )

    return obj

@app.callback(
    Output(component_id="fig_games", component_property="figure"),
    [
        Input(component_id="lov_majorLeague", component_property="value"),
        Input(component_id="lov_season", component_property="value"),
        Input(component_id="lov_team", component_property="value"),
        Input(component_id="lov_teamType", component_property="value"),
        Input(component_id="lov_gameType2", component_property="value"),
    ],
)
def fig_games(
    lov_majorLeague=None, lov_season=None, lov_team=None, lov_teamType=None, lov_gameType2=None
):

    print(f"Calling from games")
    filter_cols = {
        "majorLeagueId": lov_majorLeague,
        "seasonId": lov_season,
        "teamId": lov_team,
        "teamType": lov_teamType,
        "gameType2" : lov_gameType2,
    }
    df = f.filter_df(
        dataset_name=object_specs["fig_games"]["dataset_name"],
        filter_cols=filter_cols,
        default_filters=object_specs["fig_games"]["default_filters"],
    )
    obj = f.create_px_figure(
        df=df,
        fig_type=object_specs["fig_games"]["fig_type"],
        fig_specs=object_specs["fig_games"]["fig_specs"],
    )

    return obj

@app.callback(
    Output(component_id="fig_attendance", component_property="figure"),
    [
        Input(component_id="lov_majorLeague", component_property="value"),
        Input(component_id="lov_season", component_property="value"),
        Input(component_id="lov_team", component_property="value"),
        Input(component_id="lov_teamType", component_property="value"),
        Input(component_id="lov_gameType2", component_property="value"),
    ],
)
def fig_attendance(
    lov_majorLeague=None, lov_season=None, lov_team=None, lov_teamType=None, lov_gameType2=None
):

    print(f"Calling from games")
    filter_cols = {
        "majorLeagueId": lov_majorLeague,
        "seasonId": lov_season,
        "teamId": lov_team,
        "teamType": lov_teamType,
        "gameType2" : lov_gameType2,
    }
    df = f.filter_df(
        dataset_name=object_specs["fig_attendance"]["dataset_name"],
        filter_cols=filter_cols,
        default_filters=object_specs["fig_attendance"]["default_filters"],
    )
    obj = f.create_px_figure(
        df=df,
        fig_type=object_specs["fig_attendance"]["fig_type"],
        fig_specs=object_specs["fig_attendance"]["fig_specs"],
    )

    return obj

@app.callback(
    Output(component_id="table_games", component_property="data"),
    [
        Input(component_id="lov_majorLeague", component_property="value"),
        Input(component_id="lov_season", component_property="value"),
        Input(component_id="lov_team", component_property="value"),
        Input(component_id="lov_teamType", component_property="value"),
        Input(component_id="lov_gameType2", component_property="value"),
    ],
)
def table_games(
    lov_majorLeague=None, lov_season=None, lov_team=None, lov_teamType=None, lov_gameType2=None
):

    print(f"Calling from table_games")
    filter_cols = {
        "majorLeagueId": lov_majorLeague,
        "seasonId": lov_season,
        "teamId": lov_team,
        "teamType": lov_teamType,
        "gameType2" : lov_gameType2,
    }
    df = f.filter_df(
        dataset_name=object_specs["table_games"]["dataset_name"],
        filter_cols=filter_cols,
        default_filters=object_specs["table_games"]["default_filters"],
    )

    #print(df.to_dict('records'))

    return df.to_dict('records')



@app.callback(
    Output(component_id="fig_hit_distribution", component_property="figure"),
    [
        Input(component_id="lov_majorLeague", component_property="value"),
        Input(component_id="lov_season", component_property="value"),
        Input(component_id="lov_team", component_property="value"),
        Input(component_id="lov_teamType", component_property="value"),
        Input(component_id="lov_gameType2", component_property="value"),
    ],
)
def fig_hit_distribution(
    lov_majorLeague=None, lov_season=None, lov_team=None, lov_teamType=None, lov_gameType2=None
):

    print(f"Calling from fig_hit_distribution")
    filter_cols = {
        "majorLeagueId": lov_majorLeague,
        "seasonId": lov_season,
        "teamId": lov_team,
        "teamType": lov_teamType,
        "gameType2" : lov_gameType2,
    }
    df = f.filter_df(
        dataset_name=object_specs["fig_hit_distribution"]["dataset_name"],
        filter_cols=filter_cols,
        default_filters=object_specs["fig_hit_distribution"]["default_filters"],
    )
    print("Dataframe for fig_hit_distribution")
    print(df["groupingDescription"].unique())
    obj = f.create_px_figure(
        df=df,
        fig_type=object_specs["fig_hit_distribution"]["fig_type"],
        fig_specs=object_specs["fig_hit_distribution"]["fig_specs"],
    )

    return obj


@app.callback(
    Output(component_id="fig_plate_appearance_distribution", component_property="figure"),
    [
        Input(component_id="lov_majorLeague", component_property="value"),
        Input(component_id="lov_season", component_property="value"),
        Input(component_id="lov_team", component_property="value"),
        Input(component_id="lov_teamType", component_property="value"),
        Input(component_id="lov_gameType2", component_property="value"),
    ],
)
def fig_plate_appearance_distribution(
    lov_majorLeague=None, lov_season=None, lov_team=None, lov_teamType=None, lov_gameType2=None
):

    print(f"Calling from fig_plate_appearance_distribution")
    filter_cols = {
        "majorLeagueId": lov_majorLeague,
        "seasonId": lov_season,
        "teamId": lov_team,
        "teamType": lov_teamType,
        "gameType2" : lov_gameType2,
    }
    df = f.filter_df(
        dataset_name=object_specs["fig_plate_appearance_distribution"]["dataset_name"],
        filter_cols=filter_cols,
        default_filters=object_specs["fig_plate_appearance_distribution"]["default_filters"],
    )
    print("Dataframe for fig_plate_appearance_distribution")
    print(df["groupingDescription"].unique())
    obj = f.create_px_figure(
        df=df,
        fig_type=object_specs["fig_plate_appearance_distribution"]["fig_type"],
        fig_specs=object_specs["fig_plate_appearance_distribution"]["fig_specs"],
    )

    return obj


@app.callback(
    Output(component_id="fig_fb_ab_distribution", component_property="figure"),
    [
        Input(component_id="lov_majorLeague", component_property="value"),
        Input(component_id="lov_season", component_property="value"),
        Input(component_id="lov_team", component_property="value"),
        Input(component_id="lov_teamType", component_property="value"),
        Input(component_id="lov_gameType2", component_property="value"),
    ],
)
def fig_fb_ab_distribution(
    lov_majorLeague=None, lov_season=None, lov_team=None, lov_teamType=None, lov_gameType2=None
):

    print(f"Calling from fig_fb_ab_distribution")
    filter_cols = {
        "majorLeagueId": lov_majorLeague,
        "seasonId": lov_season,
        "teamId": lov_team,
        "teamType": lov_teamType,
        "gameType2" : lov_gameType2,
    }
    df = f.filter_df(
        dataset_name=object_specs["fig_fb_ab_distribution"]["dataset_name"],
        filter_cols=filter_cols,
        default_filters=object_specs["fig_fb_ab_distribution"]["default_filters"],
    )
    print("Dataframe for fig_fb_ab_distribution")
    print(df["groupingDescription"].unique())
    obj = f.create_px_figure(
        df=df,
        fig_type=object_specs["fig_fb_ab_distribution"]["fig_type"],
        fig_specs=object_specs["fig_fb_ab_distribution"]["fig_specs"],
    )

    return obj

@app.callback(
    Output(component_id="fig_lob_distribution", component_property="figure"),
    [
        Input(component_id="lov_majorLeague", component_property="value"),
        Input(component_id="lov_season", component_property="value"),
        Input(component_id="lov_team", component_property="value"),
        Input(component_id="lov_teamType", component_property="value"),
        Input(component_id="lov_gameType2", component_property="value"),
    ],
)
def fig_lob_distribution(
    lov_majorLeague=None, lov_season=None, lov_team=None, lov_teamType=None, lov_gameType2=None
):

    print(f"Calling from fig_lob_distribution")
    filter_cols = {
        "majorLeagueId": lov_majorLeague,
        "seasonId": lov_season,
        "teamId": lov_team,
        "teamType": lov_teamType,
        "gameType2" : lov_gameType2,
    }
    df = f.filter_df(
        dataset_name=object_specs["fig_lob_distribution"]["dataset_name"],
        filter_cols=filter_cols,
        default_filters=object_specs["fig_lob_distribution"]["default_filters"],
    )
    print("Dataframe for fig_lob_distribution")
    print(df["groupingDescription"].unique())
    obj = f.create_px_figure(
        df=df,
        fig_type=object_specs["fig_lob_distribution"]["fig_type"],
        fig_specs=object_specs["fig_lob_distribution"]["fig_specs"],
    )

    return obj


@app.callback(
    Output(component_id="fig_sb_distribution", component_property="figure"),
    [
        Input(component_id="lov_majorLeague", component_property="value"),
        Input(component_id="lov_season", component_property="value"),
        Input(component_id="lov_team", component_property="value"),
        Input(component_id="lov_teamType", component_property="value"),
        Input(component_id="lov_gameType2", component_property="value"),
    ],
)
def fig_sb_distribution(
    lov_majorLeague=None, lov_season=None, lov_team=None, lov_teamType=None, lov_gameType2=None
):

    print(f"Calling from fig_sb_distribution")
    filter_cols = {
        "majorLeagueId": lov_majorLeague,
        "seasonId": lov_season,
        "teamId": lov_team,
        "teamType": lov_teamType,
        "gameType2" : lov_gameType2,
    }
    df = f.filter_df(
        dataset_name=object_specs["fig_sb_distribution"]["dataset_name"],
        filter_cols=filter_cols,
        default_filters=object_specs["fig_sb_distribution"]["default_filters"],
    )
    print("Dataframe for fig_sb_distribution")
    print(df["groupingDescription"].unique())
    obj = f.create_px_figure(
        df=df,
        fig_type=object_specs["fig_sb_distribution"]["fig_type"],
        fig_specs=object_specs["fig_sb_distribution"]["fig_specs"],
    )

    return obj

@app.callback(
    Output(component_id="table_player_batting_stats", component_property="data"),
    [
        Input(component_id="lov_majorLeague", component_property="value"),
        Input(component_id="lov_season", component_property="value"),
        Input(component_id="lov_team", component_property="value"),
        Input(component_id="lov_teamType", component_property="value"),
        Input(component_id="lov_gameType2", component_property="value"),
    ],
)
def table_player_batting_stats(
    lov_majorLeague=None, lov_season=None, lov_team=None, lov_teamType=None, lov_gameType2=None
):

    print(f"Calling from table_player_batting_stats")
    filter_cols = {
        "majorLeagueId": lov_majorLeague,
        "seasonId": lov_season,
        "teamId": lov_team,
        "teamType": lov_teamType,
        "gameType2" : lov_gameType2,
    }
    df = f.filter_df(
        dataset_name=object_specs["table_player_batting_stats"]["dataset_name"],
        filter_cols=filter_cols,
        default_filters=object_specs["table_player_batting_stats"]["default_filters"],
    )

    #print(df.to_dict('records'))

    return df.to_dict('records')

@app.callback(
    Output(component_id="fig_batting_hm4", component_property="figure"),
    [
        Input(component_id="lov_majorLeague", component_property="value"),
        Input(component_id="lov_season", component_property="value"),
        Input(component_id="lov_team", component_property="value"),
        Input(component_id="lov_teamType", component_property="value"),
        Input(component_id="lov_gameType2", component_property="value"),
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

@app.callback(
    Output(component_id="fig_batting_hm8", component_property="figure"),
    [
        Input(component_id="lov_majorLeague", component_property="value"),
        Input(component_id="lov_season", component_property="value"),
        Input(component_id="lov_team", component_property="value"),
        Input(component_id="lov_teamType", component_property="value"),
        Input(component_id="lov_gameType2", component_property="value"),
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
    Output(component_id="fig_contour_hm", component_property="figure"),
    [
        Input(component_id="lov_majorLeague", component_property="value"),
        Input(component_id="lov_season", component_property="value"),
        Input(component_id="lov_team", component_property="value"),
        Input(component_id="lov_teamType", component_property="value"),
        Input(component_id="lov_gameType2", component_property="value"),
    ],
)
def fig_contour_hm(
    lov_majorLeague=None, lov_season=None, lov_team=None, lov_teamType=None, lov_gameType2=None
):

    print(f"Calling from fig_contour_hm")

    obj = f.create_px_figure(
        df=None,
        fig_type=object_specs["fig_contour_hm"]["fig_type"],
        fig_specs=object_specs["fig_contour_hm"]["fig_specs"],
    )

    return obj


"""
for fun in f.create_callback_functions_from_specs(object_specs=object_specs):
    exec(fun, locals())
"""


'''
@app.callback(
    Output('lov_team', 'options'),
    [Input('lov_majorLeague', 'value'), Input('lov_season', 'value') ]
    )
def set_team_from_majorleague(lov_majorLeagueId=None, lov_seasonId=None):
    filter_cols = { 'majorLeagueId' : lov_majorLeagueId,
              'seasonId' : lov_seasonId
            }

    df = f.filter_df( df = es.object_specs['lov_team']['dataset'], filter_cols=filter_cols)

    lov = f.create_list_of_values( df, label_col = es.object_specs['lov_team']['label_col'],  value_col = es.object_specs['lov_team']['value_col'] )

    return lov
'''
