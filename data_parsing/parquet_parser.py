import pandas as pd

#pathname = 'eg_hackathon-main/Data/game_summary.parquet'
pathname = 'eg_hackathon-main/Data/player_game_stats.parquet'

#dataframe = pd.read_parquet(pathname)
dataframe = pd.read_parquet(pathname, columns=['game_urn', 'player', 'kills', 'champion'])


print(dataframe)
print(dataframe.columns)