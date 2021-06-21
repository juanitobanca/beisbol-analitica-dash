import pandas as pd

# functions
def create_list_of_values( df, scol ):

    lov = []
    unique_values = df[scol].unique()

    for v in unique_values:
        lov.append({'label': v, 'value': v })

    return lov

def filter_df( df, col_val ):

    filters = []
    sql_filter = None

    for c, v in col_val.items():
        filters.append(f"{c} == '{v}'")

    sql_filter =  'AND '.join(filters)

    df.query(sql_filter)

    return df

# datasets
agg_batting_stats = pd.read_csv('data/agg_batting_stats.csv')

# list of values
lov_team = create_list_of_values(agg_batting_stats, 'teamName')
lov_season = create_list_of_values(agg_batting_stats, 'seasonId')
lov_majorLeague = create_list_of_values(agg_batting_stats, 'majorLeague')
