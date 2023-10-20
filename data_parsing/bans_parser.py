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
                                          'bb1', 'bb2', 'bb3', 'bb4', 'bb5', 'bp1', 'bp2', 'bp3', 'bp4', 'bp5',
                                        'team_2_name', 'team_2_side',
                                          'rb1', 'rb2', 'rb3', 'rb4', 'rb5', 'rp1', 'rp2', 'rp3', 'rp4', 'rp5'])

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
  
c9_champs_picked_blue = []
c9_champs_picked_red = []

for index, row in df.iterrows():
  temp_list = []
  if row['team_1_name'] == 'C9':
    for i in range(5):
      pick_num = 'bp' + str(i + 1)
      if row[pick_num] not in c9_champs_picked_blue:
        c9_champs_picked_blue.append(row[pick_num])

  elif row['team_2_name'] == 'C9':
    for i in range(5):
      pick_num = 'rp' + str(i + 1)
      if row[pick_num] not in c9_champs_picked_red:
        c9_champs_picked_red.append(row[pick_num])

print(c9_champs_picked_blue)
print(c9_champs_picked_red)

for champ in c9_ban_freq.keys():
  if champ not in c9_champs_picked_blue and champ not in c9_champs_picked_red:
    print(champ)

c9_bp1 = {}
for index, row in df.iterrows():
  if row['team_1_name'] == 'C9':
    champ = row['bp1']
    if row['bp1'] not in c9_bp1:
      c9_bp1[champ] = 1
    else:
      c9_bp1[champ] += 1

c9_rp1_rp2 = {}

for index, row in df.iterrows():
  if row['team_2_name'] == 'C9':
    champs = row['bp1'] + ' ' + row['rp1'] + ' ' + row['rp2']
    if champs not in c9_rp1_rp2:
      c9_rp1_rp2[champs] = 1
    else:
      c9_rp1_rp2[champs] += 1

print(c9_bp1)
print()
print(c9_rp1_rp2)

#print(c9_ban_freq)