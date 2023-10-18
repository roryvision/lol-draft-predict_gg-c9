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


C9RolePicks = {}
GGRolePicks = {}

C9ChampPriority = {}
GGChampPriority = {}

for index, row in df.iterrows():
    if (row['team_1_name'] == 'C9'):
        team_1_name = row['team_1_name']
        roles = ['top', 'jng', 'mid', 'bot', 'sup']

        for role in roles:
            role_column = 'team_1_' + role
            role_pick_num_column = 'team_1_' + role + '_pick_num'

            role_name = row[role_column]
            role_pick_num = row[role_pick_num_column]

            if role_name not in C9RolePicks:
                C9RolePicks[role_name] = 1
                C9ChampPriority[role_name] = role_pick_num
            else:
                C9RolePicks[role_name] += 1
                C9ChampPriority[role_name] += role_pick_num

    if (row['team_2_name'] == 'GG'):
        team_2_name = row['team_2_name']
        roles = ['top', 'jng', 'mid', 'bot', 'sup']

        for role in roles:
            role_column = 'team_2_' + role
            role_pick_num_column = 'team_2_' + role + '_pick_num'

            role_name = row[role_column]
            role_pick_num = row[role_pick_num_column]

            if role_name not in GGRolePicks:
                GGRolePicks[role_name] = 1
                GGChampPriority[role_name] = role_pick_num
            else:
                GGRolePicks[role_name] += 1
                GGChampPriority[role_name] += role_pick_num

for key in C9ChampPriority:
    C9ChampPriority[key] /= C9RolePicks[key]

for key in GGChampPriority:
    GGChampPriority[key] /= GGRolePicks[key]

C9_sorted_priority = sorted(C9ChampPriority.items(), key=lambda x:x[1])
C9_converted_dict = dict(C9_sorted_priority)

GG_sorted_priority = sorted(GGChampPriority.items(), key=lambda x:x[1])
GG_converted_dict = dict(GG_sorted_priority)

print("C9 Priorities:", C9_converted_dict)
print("GG Priorities:", GG_converted_dict)

#Drafting Algorithm - Scale of 0 - 1.0 