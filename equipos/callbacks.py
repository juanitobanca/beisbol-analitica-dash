from dash.dependencies import Input, Output

# Custom dependencies
import commons.functions as f
import equipos.specs as es

from app import app

@app.callback(
    Output('lov_team', 'options'),
    [Input('lov_majorLeague', 'value'), Input('lov_season', 'value') ]
    )
def set_team_from_majorleague(lov_majorLeagueId=None, lov_seasonId=None):
    filter_cols = { 'majorLeagueId' : lov_majorLeagueId,
              'seasonId' : lov_seasonId
            }

    df = f.filter_df( df = es.lov_specs['lov_team']['dataset'], filter_cols=filter_cols)

    lov = f.create_list_of_values( df, label_col = es.lov_specs['lov_team']['label_col'],  value_col = es.lov_specs['lov_team']['value_col'] )

    return lov
