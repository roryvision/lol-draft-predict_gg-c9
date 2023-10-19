import pandas as pd
import matplotlib.pyplot as plt

pathname = 'data/game_summary.parquet'

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#dfRaw = pd.read_parquet(pathname, columns=['team_1_name', 'team_2_name', 'bb1', 'rb1', 'bb2', 'rb2', 'bb3', 'rb3', 'bp1', 'rp1', 'rp2', 'bp2', 'bp3', 'rp3', 'rb4', 'bb4', 'rb5', 'bb5', 'rp4', 'bp4', 'bp5', 'rp5'])

#df_c9 = dfRaw[(dfRaw['team_1_name'] == 'C9') | (dfRaw['team_2_name'] == 'C9')]
#df_c9_2 = dfRaw[dfRaw['team_2_name'] == 'C9']
#print(df_c9_2)
#df_gg = dfRaw[(dfRaw['team_1_name'] == 'GG') | (dfRaw['team_2_name'] == 'GG')]

#dfRaw.to_csv('parsed/raw.csv')
#df_c9.to_csv('parsed/c9.csv')
#df_gg.to_csv('parsed/gg.csv')

df = pd.read_parquet(pathname, columns=['team_1_name', 'team_1_side', 
                                          'bb1', 'bb2', 'bb3', 'bb4', 'bb5',
                                        'team_2_name', 'team_2_side',
                                          'rb1', 'rb2', 'rb3', 'rb4', 'rb5'])

c9_bans = df[(df['team_1_name'] == 'C9') | (df['team_2_name'] == 'C9')]
gg_bans = df[df['team_2_name'] == 'GG']

c9_ban_freq = {}

for index, row in c9_bans.iterrows():
  if row['team_1_name'] == 'C9':
    champion = row['bb1']
    if champion in c9_ban_freq:
      c9_ban_freq[champion] += 1
    else:
      c9_ban_freq[champion] = 1

    champion = row['bb2']
    if champion in c9_ban_freq:
      c9_ban_freq[champion] += 1
    else:
      c9_ban_freq[champion] = 1

    champion = row['bb3']
    if champion in c9_ban_freq:
      c9_ban_freq[champion] += 1
    else:
      c9_ban_freq[champion] = 1

    champion = row['bb4']
    if champion in c9_ban_freq:
      c9_ban_freq[champion] += 1
    else:
      c9_ban_freq[champion] = 1

    champion = row['bb5']
    if champion in c9_ban_freq:
      c9_ban_freq[champion] += 1
    else:
      c9_ban_freq[champion] = 1
  elif row['team_2_name'] == 'C9':
    champion = row['rb1']
    if champion in c9_ban_freq:
      c9_ban_freq[champion] += 1
    else:
      c9_ban_freq[champion] = 1
  
    champion = row['rb2']
    if champion in c9_ban_freq:
      c9_ban_freq[champion] += 1
    else:
      c9_ban_freq[champion] = 1

    champion = row['rb3']
    if champion in c9_ban_freq:
      c9_ban_freq[champion] += 1
    else:
      c9_ban_freq[champion] = 1

    champion = row['rb4']
    if champion in c9_ban_freq:
      c9_ban_freq[champion] += 1
    else:
      c9_ban_freq[champion] = 1

    champion = row['rb5']
    if champion in c9_ban_freq:
      c9_ban_freq[champion] += 1
    else:
      c9_ban_freq[champion] = 1
  

print(c9_ban_freq)