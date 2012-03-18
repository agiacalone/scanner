#!/usr/bin/python3

class statetable:
    # -1 = no state, all others = move state
    state_table =  [ [ 1, 2, 3, 4, 5, 6,-1,-1],   # State S0
                     [ 1, 7,-1,-1,-1,-1,-1,-1],   # State S1
                     [ 7,-1,-1,-1,-1,-1,-1,-1],   # State S2
                     [ 3,-1, 3,-1,-1,-1, 8,-1],   # State S3
                     [-1,-1,-1,-1,-1,-1,-1,-1],   # State S4
                     [-1,-1,-1,-1,-1,-1,-1,-1],   # State S5
                     [-1,-1,-1,-1,-1,-1,-1,-1],   # State S6
                     [ 7,-1,-1,-1,-1,-1,-1,-1],   # State S7
                     [ 3,-1, 3,-1,-1,-1, 8,-1] ]  # State S8
    def gettable(new_state, new_char):
        return statetable.state_table[new_state][new_char]
