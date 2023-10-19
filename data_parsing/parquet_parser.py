import pandas as pd
import matplotlib

#pathname = 'eg_hackathon-main/Data/game_summary.parquet'
#pathname = 'eg_hackathon-main/Data/player_game_stats.parquet'
#pathname = 'eg_hackathon-main/Data/wards_placed.parquet'

#dataframe = pd.read_parquet(pathname)``
#dataframe = pd.read_parquet(pathname, columns=['game_urn', 'player', 'kills', 'champion']) # filer by columns
#df = pd.read_parquet(pathname, columns=['game_urn', 'game_time', 'placer_team', 'ward_type', 'placer'])

#emenes = df[(df['placer'] == 'EMENES') & (df['ward_type'] != 'unknown')]
#filtered_df = df[(df['placer'] == 'EMENES') & (df['game_urn'] == 'live:lol:riot:map:esportstmnt01-3373466')]
#print(filtered_df) # print resulting dataframe
#print(filtered_df.shape) # print columns in dataframe

pathname = 'eg_hackathon-main/Data/player_game_stats.parquet'

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)#

#dfRaw = pd.read_parquet(pathname)
df = pd.read_parquet(pathname, columns=['game_start_datetime', 'player', 'champion', 'solo_kills', 'iso_deaths', 'gold_diff_at_15m'])
filtered_df = df[df['player'] == 'Palafox']
print(filtered_df)
print(filtered_df['solo_kills'].sum())
#df = pd.read_parquet(pathname, columns=['team_1_name', 'team_2_name', 'bb1', 'rb1', 'bb2', 'rb2', 'bb3', 'rb3', 'bp1', 'rp1', 'rp2', 'bp2', 'bp3', 'rp3', 'rb4', 'bb4', 'rb5', 'bb5', 'rp4', 'bp4', 'bp5', 'rp5'])

#df_c9 = dfRaw[dfRaw['team'] == 'C9']
#df_gg = dfRaw[dfRaw['team'] == 'GG']

#dfRaw.to_csv('parsed/raw_stat.csv')
#df_gg.to_csv('parsed/gg_stat.csv')
#df_c9.to_csv('parsed/c9_stat.csv')
