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
    "gameType2": {
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
                homeTeamId AS teamId,
                CONCAT('https://www.milb.com/gameday/', gamePk, '#game_state=final') boxscoreUrl,
                CONCAT('https://www.milb.com/gameday/', gamePk, '#game_tab=play-by-play') playByPlayUrl,
                majorLeagueId,
                seasonId,
                gameDate,
                gameType2,
                venueName,
                homeTeamName,
                awayTeamName,
                homeScore,
                awayScore,
                homeScore - awayScore runDifference,
                If( homeScore - awayScore > 0, 'Ganado', 'Perdido' ) resultado,
                attendance
            FROM games

            UNION ALL

            SELECT
                awayTeamId AS teamId,
                CONCAT('https://www.milb.com/gameday/', gamePk, '#game_state=final') boxscoreUrl,
                CONCAT('https://www.milb.com/gameday/', gamePk, '#game_tab=play-by-play') playByPlayUrl,
                majorLeagueId,
                seasonId,
                gameDate,
                gameType2,
                venueName,
                homeTeamName,
                awayTeamName,
                homeScore,
                awayScore,
                awayScore - homeScore runDifference,
                If( awayScore - homeScore > 0, 'Ganado', 'Perdido' ) resultado,
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
