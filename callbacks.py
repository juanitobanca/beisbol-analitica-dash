from dash.dependencies import Input, Output
import data as d
from app import app
import logging

# callbacks
@app.callback(
    Output('lov_team', 'options'),
    [Input('lov_majorLeague', 'value'), Input('lov_season', 'value') ]
    )
def set_team_from_majorleague(lov_majorLeague=None, lov_season=None):
    scol = 'teamName'
    col_val = { 'majorLeague' : lov_majorLeague,
                'seasonId' : lov_season
              }

    df = d.filter_df(d.agg_batting_stats, col_val)
    lov = d.create_list_of_values( df, scol )

    logging.debug(lov)

    return [{'label': 'a', 'value': 'b' }]
