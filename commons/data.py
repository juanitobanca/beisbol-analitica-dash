import pandas as pd

# datasets
dataset_specs = {
    "agg_batting_stats": {
        "path": "../datasets/agg_batting_stats.csv",
    },
    "agg_team_performance_stats": {
        "path": "../datasets/agg_team_performance_stats.csv",
    },
}

for dataset, specs in dataset_specs.items():
    df = pd.read_csv(filepath_or_buffer=specs["path"])
    dataset_specs[dataset]["dataset"] = df
