from dash.dependencies import Input, Output

# Custom dependencies
import commons.data as d
from app import app

@app.callback(
    Output('lov_team', 'options'),
    [Input('lov_majorLeague', 'value'), Input('lov_season', 'value') ]
    )
def set_team_from_majorleague(lov_majorLeagueId=None, lov_seasonId=None):
    filter_cols = { 'majorLeagueId' : lov_majorLeagueId,
              'seasonId' : lov_seasonId
            }

    df = d.filter_df( df = d.lov_specs['lov_team']['dataset'], filter_cols=filter_cols)

    lov = d.create_list_of_values( df, label_col = d.lov_specs['lov_team']['label_col'],  value_col = d.lov_specs['lov_team']['value_col'] )

    return lov
