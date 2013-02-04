#import Chess
from Func import *

try:
	open('ss','r')
except IOError:
	open('ss','w').write('a')
print open('ss','r').read().split()

###Why??
#blankboard=[[(0,'0') for i in range(7)] for j in range(7)]
#showboard(blankboard)
#board=[]
#board[:]=blankboard[:]
#showboard(board)
#board[1][1]=(1,'r')
##Chess.Pieces(1, 'b', [0, 0], [3,3], board).draw()
#showboard(board)
#showboard(blankboard)

#f=open('t.txt','w')
#f.write('qwe')

#Chess.Pieces(0,'1',[0,0],[1,1]).draw()

#if 1 in [1]:
#	print 1
#elif 1 in [1,2]:
#	print 2
#elif 1 in [1,2,3]:
#	print 3
#else:
#	print 4

#a = Chess.Pieces()
#print a.details()
#print a.moves()
#a = Chess.Pieces(1,'b')
#print a.details()
#print a.moves()
#a = Chess.Pieces(1,'n')
#print a.details()
#print a.moves()
#a = Chess.Pieces(1,'r')
#print a.details()
#print a.moves()
#
#print type(a.move[0])==int
#
#a = Chess.Pieces(1, 'b', [3,3])
#print a.checkMove()
#a = Chess.Pieces(1, 'b', [3,6])
#print a.checkMove()
#a = Chess.Pieces(1, 'n', [2,1])
#print a.checkMove()
#a = Chess.Pieces(1, 'n', [3,6])
#print a.checkMove()
#a = Chess.Pieces(1, 'r', [3,0])
#print a.checkMove()
#a = Chess.Pieces(1, 'r', [3,6])
#print a.checkMove()
#a = Chess.Pieces(1, 'r', [6,6])
#print a.checkMove()

#a = Chess.Pieces(1, 'b', [3,3])
#print a.availMoves()
#a = Chess.Pieces(1, 'b', [2,5], [1,4])
#print a.availMoves()
#a = Chess.Pieces(1, 'n', [2,5], [1,4])
#print a.availMoves()
#a = Chess.Pieces(1, 'r', [2,5], [1,4])
#print a.availMoves()

#a = Chess.Pieces(1, 'b', [3,3])
#print a.checkMove()
#a = Chess.Pieces(1, 'b', [2,5], [3,3])
#print a.checkMove()
#a = Chess.Pieces(1, 'b', [1,5], [3,3])
#print a.checkMove()
#a = Chess.Pieces(1, 'n', [1,5], [3,3])
#print a.checkMove()
#a = Chess.Pieces(1, 'n', [2,5], [3,3])
#print a.checkMove()
#a = Chess.Pieces(1, 'r', [2,5], [3,3])
#print a.checkMove()
#a = Chess.Pieces(1, 'r', [3,5], [3,3])
#print a.checkMove()
