import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


pathname = 'data/snapshot_player_stats.parquet'

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df = pd.read_parquet(pathname, columns=['game_urn', 'player', 'team', 'pos_x', 'pos_y'])
game_1 = df[df['game_urn'] == 'live:lol:riot:map:esportstmnt01-3408908']
game_1_c9 = game_1[game_1['team'] == 'C9']
#plt.plot(120, 1500, 'ro')
#plt.show()
x = []
y = []
for index, row in game_1_c9.iterrows():
    if row['player'] == 'Fudge':
        x.append(row['pos_x'])
        y.append(row['pos_y'])

#for row in game_1:
#    if row['player'] == 'Fudge':
#        print('fudge')
        #plt.plot(row['pos_x'], row['pos_y'])
        #plt.show()        


#print(df)
