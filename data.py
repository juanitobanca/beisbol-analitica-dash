import pandas as pd
from dash.dependencies import Input, Output

# functions
def create_list_of_values( df, scol ):

    lov = []
    unique_values = df[scol].unique()

    for v in unique_values:
        lov.append({'label': v, 'value': v })

    return lov

def filter_dataset( df, scol, fcol, fval ):

    df = df[df[fcol] == fval]
    df = create_list_of_values( df, scol )

# datasets
agg_batting_stats = pd.read_csv('data/agg_batting_stats.csv')

# list of values
lov_teams = create_list_of_values(agg_batting_stats, 'teamName')
lov_seasons = create_list_of_values(agg_batting_stats, 'seasonId')
lov_majorLeagues = create_list_of_values(agg_batting_stats, 'majorLeague')

# callbacks
@app.callback(
    Output('majorleagues-dropdown', 'options'),
    [Input('teams-dropdownn', 'value')])
def filter_teams_from_majorleagues(fval):
    scol = 'teamName'
    fcol = 'majorLeague'
    df = agg_batting_stats
    df = filter_dataset( df, scol, fcol, fval )
