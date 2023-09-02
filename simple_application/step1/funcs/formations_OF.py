'''
Author: Pedro G Nobrega
Date: 02/09/2023
Description: create the offensive formation for the game
'''
from test_env import FORMATIONS
from lineups_OF import create_lineup
def create_formation (dic_offensive_lineups, position):
    df_qb = dic_offensive_lineups.get("QB")
    df_ol = dic_offensive_lineups.get("OL")
    l_formation = [df_qb, df_ol]
    dic_formations = FORMATIONS.get(position)
    for formation_position in dic_formations:
        qtd = dic_formations.get(formation_position)
        if qtd > 0:
            skill_position = dic_offensive_lineups.get(formation_position).head(qtd)
            l_formation.append(skill_position)
    return l_formation

def show_lformation (formation):
    for position in formation:
        print(position)

if __name__ == "__main__":
    chiefs_lineup = create_lineup("kc_chiefs.xlsx")
    formation = create_formation(chiefs_lineup, "PASSING_LONG")
    show_lformation(formation)

