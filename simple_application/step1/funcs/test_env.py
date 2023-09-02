'''
Author: Pedro G Nobrega
Date: 02/09/2023
Description: 
'''

PATH_TO_DB = "../../../db"

FORMATIONS = {"RUNNING_INSIDE": {"RB": 2, "TE": 2, "WR": 1},
             "RUNNING_OUTSIDE": {"RB": 1, "TE": 2, "WR": 2},
             "PASSING_SHORT": {"RB": 1, "TE": 2, "WR": 2},
             "PASSING_MID": {"RB": 1, "TE": 1, "WR": 3},
             "PASSING_LONG": {"RB": 0, "TE": 1, "WR": 4}}
POSITIONS_OF = ["QB", "OL", "RB", "WR","TE"]