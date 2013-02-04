#bbnn.sv2 > bbnn.sav to test R to stop opponent
#bbnn.sv3 > bbnn.sav to test R when B, N can not be used

import Chess
from Func import *

##Why??
blankboard=[[(0,'0') for i in range(7)] for j in range(7)]
board=blankboard[:]
Chess.Pieces(1, 'b', [0, 0], [3,3], board).draw()
showboard(board)
showboard(blankboard)
