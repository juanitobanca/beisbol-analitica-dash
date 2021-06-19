from dash.dependencies import Input, Output
import data as d
from app import app

# callbacks
@app.callback(
    Output('majorleagues-dropdown', 'options'),
    [Input('teams-dropdownn', 'value')])
def filter_teams_from_majorleagues(fval):
    scol = 'teamName'
    fcol = 'majorLeague'
    df = d.agg_batting_stats
    df = d.filter_dataset( df, scol, fcol, fval )
