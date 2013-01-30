import Chess
from Func import *
'''
board has elements as (player, 'b or n')
'''
###
# step=(column, rank)
#board as global mem?
blankboard=[[(0,'0') for i in range(7)] for j in range(7)]
board=blankboard[:] 
order=('B','n','N','b')
'''
blankborad has elements as (player, 'b or n')
'''


#unoccupied=[]
#for i in [1,7]:
#	for j in [1,7]:
#		unoccupied.append(str(i)+str(j))
#'''
#unoccupied is ['11', '12', ...,'66'], shows unoccupied square in string
#'''


nowdraw=0

# step=(column, rank)

#laststep=None   # laststep=(column, rank)


############################### Game starts here... ###########################


board=blankboard[:]
showboard(board)
print 'type \'H\' for Help'
#x=raw_input('Please draw on a square: ')
#firststep=(int(x[0]),int(x[1]))
#board[firststep[0]][firststep[1]]=(1,'b')
#showboard(board)
#nowdraw=1
nowdraw=0
nowCoord=[0,0]
while True:
	inputKey=raw_input('Please draw on a square: ')
	check = 1
	while check == 1:
		if inputKey == 'S':		#Save
			inputKey=raw_input('The function \'Save\' is not finished. Please draw on a square: ')
		elif inputKey == 'R':	#change to Rook
			inputKey=raw_input('The function \'Rook\' is not finished. Please draw on a square: ')
		elif inputKey == 'B':	#take Back
			inputKey=raw_input('The function \'take Back\' is not finished. Please draw on a square: ')
		elif inputKey == 'E':	#Exit
			inputKey=raw_input('The function \'Exit\' is not finished. Please draw on a square: ')
		elif inputKey == 'H':	#Help
			inputKey=raw_input('The function \'Help\' is not finished. Please draw on a square: ')
		elif len(inputKey) != 2:
			inputKey=raw_input('Invalid input. Please draw on a square: ')
		else:
			try:
				int(inputKey[0])
				int(inputKey[1])
				if 0 < int(inputKey[0]) < 7 and 0 < int(inputKey[1]) < 7:
					check = 0
				else:
					inputKey=raw_input('Input out of index. Please draw on a square: ')
			except ValueError:
				inputKey=raw_input('Invalid input. Please draw on a square: ')

	nextStep = [int(inputKey[0]),int(inputKey[1])]
	if nowdraw==0:
		nextDraw = Chess.Pieces(1, 'b', nextStep, nowCoord, board)
		if nextDraw.checkMove():
			drawb(1, nextStep, board)
			nowdraw=(nowdraw+1)%4
			nowCoord[:] = nextStep[:]
	elif nowdraw==1:
		nextDraw = Chess.Pieces(2, 'n', nextStep, nowCoord, board)
		if nextDraw.checkMove():
			drawn(2, nextStep, board)
			nowdraw=(nowdraw+1)%4
			nowCoord[:] = nextStep[:]
	elif nowdraw==2:
		nextDraw = Chess.Pieces(1, 'n', nextStep, nowCoord, board)
		if nextDraw.checkMove():
			drawn(1, nextStep, board)
			nowdraw=(nowdraw+1)%4
			nowCoord[:] = nextStep[:]
	elif nowdraw==3:
		nextDraw = Chess.Pieces(2, 'b', nextStep, nowCoord, board)
		if nextDraw.checkMove():
			drawb(2, nextStep, board)
			nowdraw=(nowdraw+1)%4
			nowCoord[:] = nextStep[:]
	else:
		break
	showboard(board)
	if checkwin(board) != None:
		print 'Player',checkwin(board),'wins!'
		break
	#nowdraw=(nowdraw+1)%4
