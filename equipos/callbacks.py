
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
    ],
)
def fig_winPercentage(
    lov_majorLeague=None, lov_season=None, lov_team=None, lov_teamType=None
):
    print(f"Calling from winPercentage")
    filter_cols = {
        "majorLeagueId": lov_majorLeague,
        "seasonId": lov_season,
        "teamId": lov_team,
        "teamType": lov_teamType,
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

    return obj

'''
@app.callback(
    Output(component_id="fig_runDifferential", component_property="figure"),
    [
        Input(component_id="lov_majorLeague", component_property="value"),
        Input(component_id="lov_season", component_property="value"),
        Input(component_id="lov_team", component_property="value"),
        Input(component_id="lov_teamType", component_property="value"),
    ],
)
def fig_runDifferential(
    lov_majorLeague=None, lov_season=None, lov_team=None, lov_teamType=None
):

    print(f"Calling from runDifferential")
    filter_cols = {
        "majorLeagueId": lov_majorLeague,
        "seasonId": lov_season,
        "teamId": lov_team,
        "teamType": lov_teamType,
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
    Output(component_id="fig_pythagoreanExp", component_property="figure"),
    [
        Input(component_id="lov_majorLeague", component_property="value"),
        Input(component_id="lov_season", component_property="value"),
        Input(component_id="lov_team", component_property="value"),
        Input(component_id="lov_teamType", component_property="value"),
    ],
)
def fig_pythagoreanExp(
    lov_majorLeague=None, lov_season=None, lov_team=None, lov_teamType=None
):

    print(f"Calling from pythagoreanExp")
    filter_cols = {
        "majorLeagueId": lov_majorLeague,
        "seasonId": lov_season,
        "teamId": lov_team,
        "teamType": lov_teamType,
    }
    df = f.filter_df(
        dataset_name=object_specs["fig_pythagoreanExp"]["dataset_name"],
        filter_cols=filter_cols,
        default_filters=object_specs["fig_pythagoreanExp"]["default_filters"],
    )
    obj = f.create_px_figure(
        df=df,
        fig_type=object_specs["fig_pythagoreanExp"]["fig_type"],
        fig_specs=object_specs["fig_pythagoreanExp"]["fig_specs"],
    )

    return obj
'''

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
