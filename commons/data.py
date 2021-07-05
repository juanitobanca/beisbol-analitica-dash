import pandas as pd

# datasets
dataset_specs = {
    "agg_batting_stats": {
        "path": "datasets/agg_batting_stats.csv",
        "format": "csv",
        "query": None,
    },
    "agg_team_performance_stats": {
        "path": "datasets/agg_team_performance_stats.csv",
        "format": "csv",
        "query": None,
    },
    "teamType": {
        "path": None,
        "format": "hardcode",
        "dataset": pd.DataFrame(
            {"label": ["Local", "Visitante", "Ambos"], "value": ["home", "away", ""]}
        ),
    },
    "gameType": {
        "path": None,
        "format": "hardcode",
        "dataset": pd.DataFrame(
            {"label": ["Temporada Regular", "Post-Temporada"], "value": ["RS", "PS"]}
        ),
    },
    "games": {
        "path": "datasets/games.csv",
        "format": "csv",
        "query": """
        WITH g AS (
        SELECT
            majorLeagueId,
            seasonId,
            gameDate,
            gameType2,
            'home' teamType,
            venueId,
            venueName,
            homeTeamId AS teamId,
            homeTeamName AS teamName,
            homeScore runs,
            awayScore runsAllowed,
            attendance
        FROM games

        UNION ALL

        SELECT
            majorLeagueId,
            seasonId,
            gameDate,
            gameType2,
            'away' teamType,
            venueId,
            venueName,
            awayTeamId AS teamId,
            awayTeamName AS teamName,
            awayScore runs,
            homeScore runsAllowed,
            attendance
        FROM games
        )
        SELECT
        *
        FROM g
        """,
    },
}

for dataset, specs in dataset_specs.items():

    if specs["format"] == "csv":
        df = pd.read_csv(filepath_or_buffer=specs["path"])
        dataset_specs[dataset]["dataset"] = df
