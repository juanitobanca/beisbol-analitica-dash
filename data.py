import pandas as pd

# functions
def create_list_of_values( df, lcol, vcol ):

    lov = []
    unique_values = df.drop_duplicates([lcol, vcol])

    for idx, row  in unique_values.iterrows():
        lov.append({'label': row[lcol], 'value': row[vcol] })

    return lov

def filter_df( df, fcols ):

    filters = []

    for column, value in fcols.items():

        if value:
            df = df[df[column] == value]

    return df

# datasets
dataset_specs = {
    'agg_batting_stats' : { 'path' :'data/agg_batting_stats.csv',
                          }
    'cum_team_performance_stats' : { 'path' :'data/agg_team_performance_stats.csv',
                                    }
}

for dataset, specs in dataset_specs.items():
    df = pd.read_csv( filepath_or_buffer = specs['path'] )
    dataset_specs[dataset]['dataset'] = df

# list of values specs
lov_specs = {
    'lov_team' : { 'dataset' : dataset_specs['agg_team_performance_stats']['dataset'],
                   'id' : 'lov_team',
                   'lcol' : 'teamName',
                   'vcol' : 'teamId',
    },
    'lov_season' : { 'dataset' : dataset_specs['agg_team_performance_stats']['dataset'],
                   'id' : 'lov_season',
                   'lcol' : 'seasonId',
                   'vcol' : 'seasonId',
    },
    'lov_majorLeague' : { 'dataset' : dataset_specs['agg_team_performance_stats']['dataset'],
                          'id' : 'lov_majorLeague',
                          'lcol' : 'majorLeague',
                          'vcol' : 'majorLeagueId',
                        }
}

for lov, specs in lov_specs.items():
    lov_specs[lov]['options'] = create_list_of_values( df = specs['dataset'], lcol = specs['lcol'], vcol = specs['vcol'])
