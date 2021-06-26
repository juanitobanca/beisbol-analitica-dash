import pandas as pd

# functions
def create_list_of_values(df, lcol, vcol):

    lov = []
    unique_values = df.drop_duplicates([lcol, vcol])

    for idx, row in unique_values.iterrows():
        lov.append({"label": row[lcol], "value": row[vcol]})

    return lov


def filter_df(df, fcols):

    filters = []

    for column, value in fcols.items():

        if value:
            df = df[df[column] == value]

    return df


# datasets
dataset_specs = {
    "agg_batting_stats": {
        "path": "data/agg_batting_stats.csv",
    },
    "agg_team_performance_stats": {
        "path": "data/agg_team_performance_stats.csv",
    },
}

for dataset, specs in dataset_specs.items():
    df = pd.read_csv(filepath_or_buffer=specs["path"])
    dataset_specs[dataset]["dataset"] = df
