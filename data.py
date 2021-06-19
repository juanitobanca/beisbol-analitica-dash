import pandas as pd

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

    return df

# datasets
agg_batting_stats = pd.read_csv('data/agg_batting_stats.csv')

# list of values
lov_teams = create_list_of_values(agg_batting_stats, 'teamName')
lov_seasons = create_list_of_values(agg_batting_stats, 'seasonId')
lov_majorLeagues = create_list_of_values(agg_batting_stats, 'majorLeague')
