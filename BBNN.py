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
nowDraw=0

# step=(column, rank)

#laststep=None   # laststep=(column, rank)


############################### Game starts here... ###########################


board=blankboard[:]
clearUp()
showboard(board)
print 'type \'H\' for Help'
nowDraw = 0
nowCoord = [0,0]
rook = 1
while True:
	showPlayer(nowDraw)
	inputKey=raw_input('Please draw on a square: ')
	check = 1
	while check == 1:
		if inputKey == 'S':		#Save
			inputKey=raw_input('The function \'Save\' is not finished. Please draw on a square: ')
		elif inputKey == 'R':	#change to Rook
			#inputKey=raw_input('The function \'Rook\' is not finished. Please draw on a square: ')
			nextDraw = Chess.Pieces(1, 'r', nowCoord)
			if rook==1 and nowDraw%2==0 and len(nextDraw.availMoves())!=0 and nowCoord != [0, 0]:
				inputKey = raw_input('Now player 1 plays as Rook. Please draw on a square: ')
				nowDraw += 4
			elif nowCoord==[0, 0]: #1st piece
				inputKey = raw_input('What a waste! You can not do that. Please draw on a square: ')
			elif nowDraw%2==1: #wrong player
				inputKey = raw_input('Wrong player. Please draw on a square: ')
			elif rook==0: #run out of rook
				inputKey = raw_input('You can only use Rook once per game. Please draw on a square: ')
			else:
				inputKey=raw_input('Invalid input. Please draw on a square: ')
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
	if nowDraw==0:
		nextDraw = Chess.Pieces(1, 'b', nowCoord, nextStep, board)
		cM = nextDraw.checkMove()
		if cM==1:
			nextDraw.draw()
			#drawb(1, nextStep, board)
			nowDraw=(nowDraw+1)%4
			nowCoord[:] = nextStep[:]
			clearUp()
			showboard(board)
		elif cM==0:
			nowDraw=(nowDraw+1)%4
			clearUp()
			showboard(board)
		else:
			print 'Invalid move! The available moves are:'
			print cM
	elif nowDraw==1:
		nextDraw = Chess.Pieces(2, 'n', nowCoord, nextStep, board)
		cM = nextDraw.checkMove()
		if cM==1:
			nextDraw.draw()
			#drawn(2, nextStep, board)
			nowDraw=(nowDraw+1)%4
			nowCoord[:] = nextStep[:]
			clearUp()
			showboard(board)
		elif cM==0:
			nowDraw=(nowDraw+3)%4
			clearUp()
			showboard(board)
		else:
			print 'Invalid move! The available moves are:'
			print cM
	elif nowDraw==2:
		nextDraw = Chess.Pieces(1, 'n', nowCoord, nextStep, board)
		cM = nextDraw.checkMove()
		if cM==1:
			nextDraw.draw()
			#drawn(1, nextStep, board)
			nowDraw=(nowDraw+1)%4
			nowCoord[:] = nextStep[:]
			clearUp()
			showboard(board)
		elif cM==0:
			nowDraw=(nowDraw+1)%4
			clearUp()
			showboard(board)
		else:
			print 'Invalid move! The available moves are:'
			print cM
	elif nowDraw==3:
		nextDraw = Chess.Pieces(2, 'b', nowCoord, nextStep, board)
		cM = nextDraw.checkMove()
		if cM==1:
			nextDraw.draw()
			#drawb(2, nextStep, board)
			nowDraw=(nowDraw+1)%4
			nowCoord[:] = nextStep[:]
			clearUp()
			showboard(board)
		elif cM==0:
			nowDraw=(nowDraw+3)%4
			clearUp()
			showboard(board)
		else:
			print 'Invalid move! The available moves are:'
			print cM
	elif nowDraw in [4, 6]:
		nextDraw = Chess.Pieces(1, 'r', nowCoord, nextStep, board)
		cM = nextDraw.checkMove()
		if cM==1:
			nextDraw.draw()
			if checkwin(board) == None:
				nowDraw=(nowDraw+1)%4
				nowCoord[:] = nextStep[:]
				clearUp()
				showboard(board)
				rook = 0
			else: #use Rook to win
				#Erase the Rook
				nextDraw = Chess.Pieces(0, '0', [0, 0], nextStep, board)
				nextDraw.draw()
				print 'Illigal move! You can not win the game by Rook.'
				nowDraw -= 4
		#checked before
		#elif cM==0:
		#	nowDraw=(nowDraw+1)%4
		#	clearUp()
		#	showboard(board)
		else:
			print 'Invalid move! The available moves are:'
			print cM
	else:
		break
	#clearUp()
	#showboard(board)
	if checkwin(board) != None:
		clearUp()
		showboard(board)
		print 'Player',checkwin(board),'wins!'
		break
