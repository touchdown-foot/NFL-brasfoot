'''
Author: Pedro G Nobrega
Date: 02/09/2023
Description: create the depth chart from the excels
'''
import os
from test_env import PATH_TO_DB, POSITIONS_OF
import pandas as pd

def create_lineup (teams_name):
    teams_path = os.path.join(PATH_TO_DB, teams_name)
    dic_lineup = {}
    for position in POSITIONS_OF:
        print("READING POSITION: %s"%position)
        df_position = pd.read_excel(teams_path, header= 0, sheet_name= position, index_col=0)
        dic_lineup[position] = df_position
        print("POSITION %s read!!"%position)
    return dic_lineup

if __name__ == "__main__":
    print(create_lineup("kc_chiefs.xlsx"))
