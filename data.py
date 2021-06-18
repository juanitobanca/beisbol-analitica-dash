import pandas as pd

# functions

def create_list_of_values( df, col ):

    lov = []
    unique_values = df[col].unique()

    for v in unique_values:
        lov.append({'label': v, 'value': v })

    return lov

# datasets
agg_batting_stats = pd.read_csv('data/agg_batting_stats.csv')

# list of values
lov_teams = create_list_of_values(agg_batting_stats, 'teamName')
