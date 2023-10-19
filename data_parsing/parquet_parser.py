import pandas as pd
import matplotlib.pyplot as plt

pathname = './data_parsing/data/game_summary.parquet'

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

dfRaw = pd.read_parquet(pathname, columns=['team_1_name', 'team_2_name', 'bb1', 'rb1', 'bb2', 'rb2', 'bb3', 'rb3', 'bp1', 'rp1', 'rp2', 'bp2', 'bp3', 'rp3', 'rb4', 'bb4', 'rb5', 'bb5', 'rp4', 'bp4', 'bp5', 'rp5'])

df_gg = dfRaw[(dfRaw['team_1_name'] == 'GG') | (dfRaw['team_2_name'] == 'GG')]
df_c9 = dfRaw[(dfRaw['team_1_name'] == 'C9') | (dfRaw['team_2_name'] == 'C9')]

dfRaw.to_csv('./data_parsing/parsed/raw')
df_gg.to_csv('./data_parsing/parsed/gg')
df_c9.to_csv('./data_parsing/parsed/c9')

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