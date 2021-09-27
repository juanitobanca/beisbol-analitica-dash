import pandas as pd

# datasets.
dataset_specs = {
    "agg_batting_stats": {
        "path": "datasets/agg_batting_stats.csv",
        "format": "csv",
        "query": None,
        "column_renamings": {
            "singles": "X1B",
            "doubles": "X2B",
            "triples": "X3B",
            "homeRuns": "HR",
            "hits" : "H",
            "strikeOuts" : "SO",
            "walks" : "BB",
            "unintentionalWalks" : "UBB",
            "intentionalWalks" : "IBB",
            "hitByPitch" : "HBP",
            "sacFlies" : "SF",
            "sacBunts" : "SH",
            "popUps" : "PU",
            "lineDrives" : "LD",
            "flyBalls" : "FB",
            "groundBalls" : "GB",
            "runsBattedIn" : "RBI",
            "leftOnBase" : "LOB",
            "stolenBases" : "SB",
            "caughtStealing" : "CS",
            "games" : "G",
            "plateAppearances" :"PA",
            "atBats" :"AB",
            "runs" :"R",
            "battingAverage": "BA",
            "onBasePercentage": "OBP",
            "sluggingPercentage": "SLG",
            "onBasePlusSluggingPercentage": "OPS",
            "onBasePlusSluggingPercentagePlus": "OPS+",
            "totalBases": "TB",
            "groundedIntoDoublePlays": "GDP",
            "hitByPitch" : "HBP",
            "sacBunts" : "SH",
            "sacFlies" : "SF",
        },
    },
    "agg_team_performance_stats": {
        "path": "datasets/agg_team_performance_stats.csv",
        "format": "csv",
        "query": None,
        "column_renamings": None,
         "column_renamings": {
            "winPercentage": "W%",
            "pythagoreanExpectation": "PyExp",
            "runs": "R",
            "runsAllowed": "RA",
            "runDifferential": "RS-RA",
            "wins" : "W",
            "losses" : "L"
        },
    },
    "teamType": {
        "path": None,
        "format": "hardcode",
        "dataset": pd.DataFrame(
            {"label": ["Local", "Visitante", "Ambos"], "value": ["home", "away", ""]}
        ),
        "column_renamings": None,
    },
    "trajectoryType": {
        "path": None,
        "format": "hardcode",
        "dataset": pd.DataFrame(
            {"label": ["line_drive", "ground_ball", "popup", "fly_ball",""], "value": ["line_drive", "ground_ball", "popup", "fly_ball",""]}
        ),
        "column_renamings": None,
    },
    "gameType2": {
        "path": None,
        "format": "hardcode",
        "dataset": pd.DataFrame(
            {"label": ["Temporada Regular", "Post-Temporada"], "value": ["RS", "PS"]}
        ),
        "column_renamings": None,
    },
    "pitches": {
        "path": "datasets/pitches.csv",
        "format": "csv",
        "column_renamings": None,
        "query": """
        With p AS
        (
        Select gamePk, battingTeamId, batterId, pitchingTeamId, pitcherId, coordX, coordY, trajectory, HM4, HM8
        From pitches
        Where coordX Is Not Null
        And coordY Is Not Null
        ), g As
        (
        Select gamePk, seasonId, majorLeagueId
        From games
        Where gameType2 = 'RS'
        And seasonId > 2012
        )
        Select g.seasonId, g.majorLeagueId, p.*
        From g
        Inner Join p
        On g.gamePk = p.gamePk
        """
    },
    "players": {
        "path": "datasets/players.csv",
        "format": "csv",
        "column_renamings": None,
        "query": """
        Select Concat( lastName, ', ', firstName, ' (' , playerId, ')' ) name, playerId
        From players
        """
    },
    "games": {
        "path": "datasets/games.csv",
        "format": "csv",
        "column_renamings": None,
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
                wind,     CONCAT('[Boxscore](https://www.milb.com/gameday/', gamePk, '#game_state=final)') boxscoreUrl,
            CONCAT(
            '[Jugada a Jugada](https://www.milb.com/gameday/',
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
