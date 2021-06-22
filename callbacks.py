from dash.dependencies import Input, Output
import data as d
from app import app
import logging

# callbacks
@app.callback(
    Output('lov_team', 'options'),
    [Input('lov_majorLeague', 'value'), Input('lov_season', 'value') ]
    )
def set_team_from_majorleague(lov_majorLeagueId=None, lov_seasonId=None):
    fcols = { 'majorLeagueId' : lov_majorLeagueId,
              'seasonId' : lov_seasonId
            }

    df = d.filter_df( df = d.lov_specs['lov_team']['dataset'], fcols=fcols)

    lov = []

    for col in d.lov_specs['lov_team']['dataset'].columns:
        lov.append({'label': col, 'value': col })

    #lov = d.create_list_of_values( df, lcol = d.lov_specs['lov_team']['lcol'],  vcol = d.lov_specs['lov_team']['vcol'] )

    return lov
