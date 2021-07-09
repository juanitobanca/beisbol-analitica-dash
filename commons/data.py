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
With g As
(
            SELECT
                homeTeamId AS teamId,
                'home' AS teamType,
                gameType2,
                CONCAT('[Boxscore](https://www.milb.com/gameday/', gamePk, '#game_state=final)') boxscoreUrl,
                CONCAT('[Jugada a Jugada](https://www.milb.com/gameday/', gamePk, '#game_tab=play-by-play)') playByPlayUrl,
                majorLeagueId,
                seasonId,
                gameDate,
                venueName,
                homeTeamName,
                awayTeamName,
                Concat( homeScore, '-', awayScore ) resultadoCarreras,
                If( homeIsWinner > 0, 'Ganado', 'Perdido' ) resultado,
                attendance,
                doubleHeader,
                dayNight,
                weather,
                wind
            FROM games

            UNION ALL

            SELECT
                awayTeamId AS teamId,
                'away' AS teamType,
                gameType2,
                CONCAT('[Boxscore](https://www.milb.com/gameday/', gamePk, '#game_state=final)') boxscoreUrl,
                CONCAT('[Jugada a Jugada](https://www.milb.com/gameday/', gamePk, '#game_tab=play-by-play)') playByPlayUrl,
                majorLeagueId,
                seasonId,
                gameDate,
                venueName,
                homeTeamName,
                awayTeamName,
                Concat( homeScore, '-', awayScore ) resultadoCarreras,
                If( awayIswinner > 0, 'Ganado', 'Perdido' ) resultado,
                attendance,
                doubleHeader,
                dayNight,
                weather,
                wind
            FROM games
            )
            SELECT
            *
            FROM g
            Order By gameDate Asc;
        """,
    },
}

for dataset, specs in dataset_specs.items():

    if specs["format"] == "csv":
        df = pd.read_csv(filepath_or_buffer=specs["path"])
        dataset_specs[dataset]["dataset"] = df
