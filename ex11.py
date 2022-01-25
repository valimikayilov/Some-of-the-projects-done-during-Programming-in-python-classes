"""
Author: Vali Mikayilov
Matr.Nr.: K12037083
Exercise 11
"""
import numpy as np

def __get_next_state__(state):
    state2 = np.zeros(shape=(len(state),len(state[0])), dtype=np.int32)
    def adjacent(state, x, y):
        def notcorner(x, y):
            return 0 <= x < len(state) and 0 <= y < len(state[x]) and state[x,y]
        on = 0
        nearby = [[x-1,y-1],[x-1,y],[x-1,y+1],[x,y-1],[x,y+1],[x+1,y-1],[x+1,y],[x+1,y+1]]
        for x in nearby:
            if notcorner(x[0], x[1]) != 0:
                on +=1
        return on

    for index, value in np.ndenumerate(state):
        if value == 1:
            if 2 > adjacent(state, index[0], index[1]):
                state2[index[0], index[1]] = 0
        if value == 1:
            if 2 <= adjacent(state, index[0], index[1]):
                state2[index[0], index[1]] = 1
        if value == 1:
            if 3 < adjacent(state, index[0], index[1]):
                state2[index[0], index[1]] = 0
        if value == 0:
            if 3 == adjacent(state, index[0], index[1]):
                state2[index[0], index[1]] = 1
    return state2
