#!/usr/bin/python3

class actiontable:
    # 0 = error, 1 = MA, 2 = HR
    action_table = [ [ 1, 1, 1, 1, 1, 1, 0, 0],   # State S0
                     [ 1, 1, 2, 2, 2, 2, 2, 2],   # State S1
                     [ 1, 0, 0, 0, 0, 0, 0, 0],   # State S2
                     [ 1, 2, 1, 2, 2, 2, 1, 2],   # State S3
                     [ 2, 2, 2, 2, 2, 2, 2, 2],   # State S4
                     [ 2, 2, 2, 2, 2, 2, 2, 2],   # State S5
                     [ 2, 2, 2, 2, 2, 2, 2, 2],   # State S6
                     [ 1, 2, 2, 2, 2, 2, 2, 2],   # State S7
                     [ 1, 0, 1, 0, 0, 0, 1, 0] ]  # State S8
    def gettable(new_state, new_char):
        return actiontable.action_table[new_state][new_char]
