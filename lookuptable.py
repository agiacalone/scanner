#!/usr/bin/python3

class lookuptable:
    # 0 = error & MA, 1 = int, 2 = id, 3 = eq, 4 = plus, 5 = semi, 6 = real
    lookup_table = [ [ 0, 0, 0, 0, 0, 0, 0, 0],   # State S0
                     [ 0, 0, 1, 1, 1, 1, 1, 1],   # State S1
                     [ 0, 0, 0, 0, 0, 0, 0, 0],   # State S2
                     [ 0, 2, 0, 2, 2, 2, 2, 2],   # State S3
                     [ 3, 3, 3, 3, 3, 3, 3, 3],   # State S4
                     [ 4, 4, 4, 4, 4, 4, 4, 4],   # State S5
                     [ 5, 5, 5, 5, 5, 5, 5, 5],   # State S6
                     [ 0, 6, 6, 6, 6, 6, 6, 6],   # State S7
                     [ 0, 0, 0, 0, 0, 0, 0, 0] ]  # State S8
    def gettable(new_state, new_char):
        return lookuptable.lookup_table[new_state][new_char]
