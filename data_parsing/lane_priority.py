import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

pathnameSummary = './data_parsing/data/game_summary.parquet'
dfSummary = pd.read_parquet(pathnameSummary, columns=['game_urn', 'team_1_name', 'team_1_side', 'team_2_name', 'team_2_side'])

pathname = './data_parsing/data/snapshot_player_stats.parquet'
dfRaw = pd.read_parquet(pathname, columns=['game_urn', 'game_time', 'team', 'player', 'pos_x', 'pos_y'])

df_c9 = dfRaw[dfRaw['game_urn'] == 'live:lol:riot:map:esportstmnt01-3373466']
# df_c9 = dfRaw[(dfRaw['team'] == 'C9') & ((dfRaw['game_time'] > 60000) & (dfRaw['game_time'] < 840000))]

def getSide(game, team):
  team_1 = dfSummary.loc[dfSummary['game_urn'] == game, 'team_1_name'].iloc[0]
  team_1_side = dfSummary.loc[dfSummary['game_urn'] == game, 'team_1_side'].iloc[0]
  team_2 = dfSummary.loc[dfSummary['game_urn'] == game, 'team_2_name'].iloc[0]
  team_2_side = dfSummary.loc[dfSummary['game_urn'] == game, 'team_2_side'].iloc[0]

  if team_1 == team:
    return team_1_side
  if team_2 == team:
    return team_2_side

count = 0
total = 0

grouped_by_game_and_player = df_c9.groupby(['game_urn', 'player'])
for (game_urn, player), game_player_data in grouped_by_game_and_player:
  side = getSide(game_urn, 'C9')
  if player == 'Fudge':
    # < 0 red side | > 0 blue side | = 0 is on the line, we will consider this prio
    value = 16000 * (game_player_data['pos_y'] - 16000) - game_player_data['pos_x'] * (-16000)
    # TODO: i realized everything only runs once because of how pandas data is structured LOL
    if side == 'blue':
      if (value).any() < 0: count -= 1
      else: count += 1
    elif side == 'red':
      print(value)
      if (value).any() > 0: count -= 1
      else: count += 1
    total += 1

print(count/total)