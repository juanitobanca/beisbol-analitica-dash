from dash.dependencies import Input, Output

# Custom dependencies
from app import data as d
from app import data import app

@app.callback(
    Output('lov_team', 'options'),
    [Input('lov_majorLeague', 'value'), Input('lov_season', 'value') ]
    )
def set_team_from_majorleague(lov_majorLeagueId=None, lov_seasonId=None):
    fcols = { 'majorLeagueId' : lov_majorLeagueId,
              'seasonId' : lov_seasonId
            }

    df = d.filter_df( df = d.lov_specs['lov_team']['dataset'], fcols=fcols)

    lov = d.create_list_of_values( df, lcol = d.lov_specs['lov_team']['lcol'],  vcol = d.lov_specs['lov_team']['vcol'] )

    return lov
