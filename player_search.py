import numpy as np
import pandas as pd

def searchapi(data):
    player_name = data['player']
    df = pd.read_csv('player_id1.csv')
    player_list = []
    
    for i in range(len(df)):
        small_name = df['player_name'][i].lower()
        target_list = player_name.split()
        for j in range(len(target_list)):
            target_list[j] = target_list[j].lower()
        for k in range(-1,-len(target_list)-1,-1):
            small_target = target_list[k]
            if small_target in small_name:
                # print(small_name)
                player_list.append({
                    'player_name': df['player_name'][i],
                    'player_id': int(df['player_id'][i])
                })

    return player_list
