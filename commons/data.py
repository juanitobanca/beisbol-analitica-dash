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
WITH g2 AS (
  SELECT
    homeTeamId AS teamId,
    'home' AS teamType,
    gamePk,
    gameType2,
    majorLeagueId,
    seasonId,
    gameDate,
    venueName,
    homeTeamName,
    awayTeamName,
    CONCAT(homeScore, '-', awayScore) resultadoCarreras,
    IF(homeIsWinner > 0, 'Ganado', 'Perdido') resultado,
    attendance,
    doubleHeader,
    dayNight,
    weather,
    wind,
    homeScore - awayScore runDifference
  FROM games

  UNION ALL

  SELECT
    awayTeamId AS teamId,
    'away' AS teamType,
    gamePk,
    gameType2,
    majorLeagueId,
    seasonId,
    gameDate,
    venueName,
    homeTeamName,
    awayTeamName,
    CONCAT(homeScore, '-', awayScore) resultadoCarreras,
    IF(awayIswinner > 0, 'Ganado', 'Perdido') resultado,
    attendance,
    doubleHeader,
    dayNight,
    weather,
    wind,
    awayScore - homeScore runDifference
  FROM games
), g As
(
SELECT
    gameType2,
    majorLeagueId,
    seasonId,
    teamId,
    teamType,
    gameDate,
    venueName,
    homeTeamName,
    awayTeamName,
    resultadoCarreras,
    resultado,
    attendance,
    runDifference,
                REPLACE(REPLACE(REPLACE(REPLACE( REPLACE( REPLACE( REPLACE( REPLACE( REPLACE (
        REPLACE( REPLACE( REPLACE( REPLACE(weather,'0','')
        ,'1',''),'2',''),'3',''),'4',''),'5',''),'6',''),'7',''),'8',''),'9',''), 'degrees', '' ), '.',''), ' , ', '') weather,
        wind,     CONCAT('&nbsp;&nbsp;[Boxscore](https://www.milb.com/gameday/', gamePk, '#game_state=final)') boxscoreUrl,
    CONCAT(
      '&nbsp;&nbsp;[Jugada a Jugada](https://www.milb.com/gameday/',
      gamePk,
      '#game_tab=play-by-play)'
    ) playByPlayUrl,
        CASE
      WHEN doubleHeader IN ('N', 'S') THEN ''
      ELSE 'Doble Juego'
    END doubleHeader,
    CASE
      WHEN dayNight = 'night' THEN 'Dia'
      ELSE 'Noche'
    END dayNight
FROM g2
)
Select  gameType2,
    majorLeagueId,
    seasonId,
    teamId,
    teamType,
    gameDate,
    venueName,
    homeTeamName,
    awayTeamName,
    resultadoCarreras,
    resultado,
    attendance,
    playByplayUrl,
    boxScoreUrl,
    doubleHeader,
    dayNight,
    runDifference,
    Case When weather = 'Partly Cloudy' Then 'Parcialmente Nublado'
            When weather In ( 'Overcast', 'Cloudy' ) Then 'Nublado'
            When weather = 'Snow' Then 'Nevado'
            When weather = 'Sunny' Then 'Soleado'
            When weather in ('Drizzle', 'Rain' ) Then 'Lluviado'
            When weather = 'Roof Closed' Then 'Techo Cerrado'
            When weather = ('Clear' ) Then 'Despejado'
            When weather Is Null Or weather = 'Unknown' Then 'Desconocido'
            Else weather
       End weather,
       wind
From g
Where seasonId >= 2010
ORDER BY
  gameDate
        """,
    },
}

for dataset, specs in dataset_specs.items():

    if specs["format"] == "csv":
        df = pd.read_csv(filepath_or_buffer=specs["path"])
        dataset_specs[dataset]["dataset"] = df
