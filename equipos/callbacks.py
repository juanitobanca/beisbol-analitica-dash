
# Dash components, html, and dash tables
from dash.dependencies import Input, Output

# Custom dependencies
from app import app
import commons.functions as f
from equipos.specs import object_specs

"""
for fun in f.create_callback_functions_from_specs(object_specs=object_specs):
    exec(fun, locals())
"""

@app.callback(
    Output(component_id="lov_team", component_property="options"),
    [
        Input(component_id="lov_majorLeague", component_property="value"),
        Input(component_id="lov_season", component_property="value"),
    ],
)
def lov_team(lov_majorLeague=None, lov_season=None):
    filter_cols = {"majorLeagueId": lov_majorLeague, "seasonId": lov_season}
    df = f.filter_df(df=object_specs["lov_team"]["dataset"], filter_cols=filter_cols)
    obj = f.create_list_of_values(
        df=df,
        label_col=object_specs["lov_team"]["label_col"],
        value_col=object_specs["lov_team"]["value_col"],
    )

    return obj



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
