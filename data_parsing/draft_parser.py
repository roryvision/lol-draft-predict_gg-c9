import pandas as pd
import matplotlib.pyplot as plt

pathname = '.\lol-draft-predict_gg-c9\data_parsing\data\game_summary.parquet'

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

dfRaw = pd.read_parquet(pathname, columns=['team_1_name', 'team_2_name', 'bb1', 'rb1', 'bb2', 'rb2', 'bb3', 'rb3', 'bp1', 'rp1', 'rp2', 'bp2', 'bp3', 'rp3', 'rb4', 'bb4', 'rb5', 'bb5', 'rp4', 'bp4', 'bp5', 'rp5'])

df_c9 = dfRaw[dfRaw['team_1_name'] == 'C9']
df_gg = dfRaw[dfRaw['team_2_name'] == 'GG']

dfRaw.to_csv('./lol-draft-predict_gg-c9\data_parsing\parsed/raw')
df_gg.to_csv('./lol-draft-predict_gg-c9\data_parsing\parsed/gg')
df_c9.to_csv('./lol-draft-predict_gg-c9\data_parsing\parsed/c9')

df = pd.read_parquet(pathname, columns=['team_1_name', 
                                          'team_1_top', 'team_1_top_pick_num',
                                          'team_1_jng', 'team_1_jng_pick_num',
                                          'team_1_mid', 'team_1_mid_pick_num',
                                          'team_1_bot', 'team_1_bot_pick_num',
                                          'team_1_sup', 'team_1_sup_pick_num',
                                        'team_2_name', 
                                          'team_2_top', 'team_2_top_pick_num',
                                          'team_2_jng', 'team_2_jng_pick_num',
                                          'team_2_mid', 'team_2_mid_pick_num',
                                          'team_2_bot', 'team_2_bot_pick_num',
                                          'team_2_sup', 'team_2_sup_pick_num'])


C9TopLanePicks = {}
GGTopLanePicks = {}

for index, row in df.iterrows():
  if (row['team_1_name'] == 'C9'):
    team_1_name = row['team_1_name']
    team_1_top = row['team_1_top']

    # Check if the team_1_name is already in the dictionary, if not, add it
    if team_1_name not in C9TopLanePicks:
        C9TopLanePicks[team_1_name] = {}

    # Check if the team_1_top is already in the nested dictionary, if not, add it
    if team_1_top not in C9TopLanePicks[team_1_name]:
        C9TopLanePicks[team_1_name][team_1_top] = 0

    # Increment the count for the current team_1_top
    C9TopLanePicks[team_1_name][team_1_top] += 1

for index, row in df.iterrows():
  if (row['team_2_name'] == 'GG'):
    team_2_name = row['team_2_name']
    team_2_top = row['team_2_top']

    # Check if the team_1_name is already in the dictionary, if not, add it
    if team_2_name not in GGTopLanePicks:
        GGTopLanePicks[team_2_name] = {}

    # Check if the team_1_top is already in the nested dictionary, if not, add it
    if team_2_top not in GGTopLanePicks[team_2_name]:
        GGTopLanePicks[team_2_name][team_2_top] = 0

    # Increment the count for the current team_1_top
    GGTopLanePicks[team_2_name][team_2_top] += 1


print(C9TopLanePicks)
print(GGTopLanePicks)