import Chess
from Func import *
'''
board has elements as (player, 'b or n')
'''
###
# step=(column, rank)
#board as global mem?
board=[[(0,'0') for i in range(7)] for j in range(7)]
order=('B','n','N','b')
'''
blankborad has elements as (player, 'b or n')
'''
nowDraw=0

# step=(column, rank)

#laststep=None   # laststep=(column, rank)


############################### Game starts here... ###########################


gameSave=[]
nowDraw = 0
nowCoord = [0,0]
rook = 1

clearUp()
showAll(nowDraw, nowCoord, board)
print 'type \'H\' for Help'

while True:
	inputKey=raw_input('Please draw on a square: ')
	check = 1
	while check == 1:
		if inputKey == 'S':		#Save
			f = open("bbnn.sav", "w")
			for i in range(len(gameSave)):
				f.write('%s\n'%gameSave[i])
			f.close()
			clearUp()
			showAll(nowDraw, nowCoord, board)
			inputKey=raw_input('Game saved. Please draw on a square: ')
		elif inputKey == 'L':		#Load, not finished
			try:
				open("bbnn.sav", "r")
			except IOError:
				open("bbnn.sav", "w")

			f = open("bbnn.sav", "r")
			savList = f.read().split()
			f.close()

			#init
			for i in range(1,7):
				for j in range(1,7):
					Chess.Pieces(0, '0', [0, 0], [i, j], board).draw()
			gameSave=[]

			#for the case that no record
			move='2b00'
			#load
			for i in range(len(savList)):
				move = savList[i]
				if move[1]=='r': #use rook
					rook = 0
				nextDraw = Chess.Pieces(int(move[0]), move[1], [0, 0], [int(move[2]), int(move[3])], board)
				nextDraw.draw()
				nextDraw.save(gameSave)

			nowCoord = [int(move[2]), int(move[3])]
			if move[1] == 'r':
				move = savList[-2]
				if move[0:2] == '1b': #nowDraw =  move's nd + 2
					nowDraw = 2
				elif move[0:2] == '2n':
					nowDraw = 3
				elif move[0:2] == '1n':
					nowDraw = 0
				elif move[0:2] == '2b':
					nowDraw = 1

			elif move[0:2] == '1b': #nowDraw = last move's nd + 1
				nowDraw = 1
			elif move[0:2] == '2n':
				nowDraw = 2
			elif move[0:2] == '1n':
				nowDraw = 3
			elif move[0:2] == '2b':
				nowDraw = 0
			clearUp()
			showAll(nowDraw, nowCoord, board)

			del move
			del savList
			inputKey=raw_input('Game Loaded. Please draw on a square: ')		
		elif inputKey == 'R':	#change to Rook
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
			if len(gameSave)==0:
				inputKey=raw_input('Invalid input. Please draw on a square: ')
			elif len(gameSave)==1:
				movel1 = gameSave[-1]
				rmCoord = [int(movel1[2]), int(movel1[3])]
				nowCoord = [0, 0]
				if movel1[0:2] == '1b': #nowDraw = last move's nd + 1
					nowDraw = 0
				elif movel1[0:2] == '2n':
					nowDraw = 1
				elif movel1[0:2] == '1n':
					nowDraw = 2
				elif movel1[0:2] == '2b':
					nowDraw = 3
				#erase last move
				del movel1
				Chess.Pieces(0, '0', [0, 0], rmCoord, board).draw()
				gameSave.pop()

				clearUp()
				showAll(nowDraw, nowCoord, board)
				inputKey=raw_input('Please draw on a square: ')
			else:
				movel1 = gameSave[-1]
				movel2 = gameSave[-2]
				rmCoord = [int(movel1[2]), int(movel1[3])]
				nowCoord = [int(movel2[2]), int(movel2[3])]
				if movel1[1] == 'r':
					rook = 1
					if movel2[0:2] == '1b':
						nowDraw = 1
					elif movel2[0:2] == '2n':
						nowDraw = 2
					elif movel2[0:2] == '1n':
						nowDraw = 3
					elif movel2[0:2] == '2b':
						nowDraw = 0
				elif movel1[0:2] == '1b': #nowDraw = last move's nd + 1
					nowDraw = 0
				elif movel1[0:2] == '2n':
					nowDraw = 1
				elif movel1[0:2] == '1n':
					nowDraw = 2
				elif movel1[0:2] == '2b':
					nowDraw = 3
				#erase last move
				del movel1
				del movel2
				Chess.Pieces(0, '0', [0, 0], rmCoord, board).draw()
				gameSave.pop()

				clearUp()
				showAll(nowDraw, nowCoord, board)
				inputKey=raw_input('Please draw on a square: ')
		elif inputKey == 'C':	#clear up
			clearUp()
			showAll(nowDraw, nowCoord, board)
			inputKey=raw_input('Please draw on a square: ')
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
			nextDraw.save(gameSave)
			nowDraw=(nowDraw+1)%4
			nowCoord[:] = nextStep[:]
			clearUp()
			showAll(nowDraw, nowCoord, board)
		elif cM==0:
			nowDraw=(nowDraw+1)%4
			clearUp()
			showAll(nowDraw, nowCoord, board)
		else:
			print 'Invalid move! The available moves are:'
			print cM
	elif nowDraw==1:
		nextDraw = Chess.Pieces(2, 'n', nowCoord, nextStep, board)
		cM = nextDraw.checkMove()
		if cM==1:
			nextDraw.draw()
			nextDraw.save(gameSave)
			nowDraw=(nowDraw+1)%4
			nowCoord[:] = nextStep[:]
			clearUp()
			showAll(nowDraw, nowCoord, board)
		elif cM==0:
			nowDraw=(nowDraw+3)%4
			clearUp()
			showAll(nowDraw, nowCoord, board)
		else:
			print 'Invalid move! The available moves are:'
			print cM
	elif nowDraw==2:
		nextDraw = Chess.Pieces(1, 'n', nowCoord, nextStep, board)
		cM = nextDraw.checkMove()
		if cM==1:
			nextDraw.draw()
			nextDraw.save(gameSave)
			nowDraw=(nowDraw+1)%4
			nowCoord[:] = nextStep[:]
			clearUp()
			showAll(nowDraw, nowCoord, board)
		elif cM==0:
			nowDraw=(nowDraw+1)%4
			clearUp()
			showAll(nowDraw, nowCoord, board)
		else:
			print 'Invalid move! The available moves are:'
			print cM
	elif nowDraw==3:
		nextDraw = Chess.Pieces(2, 'b', nowCoord, nextStep, board)
		cM = nextDraw.checkMove()
		if cM==1:
			nextDraw.draw()
			nextDraw.save(gameSave)
			nowDraw=(nowDraw+1)%4
			nowCoord[:] = nextStep[:]
			clearUp()
			showAll(nowDraw, nowCoord, board)
		elif cM==0:
			nowDraw=(nowDraw+3)%4
			clearUp()
			showAll(nowDraw, nowCoord, board)
		else:
			print 'Invalid move! The available moves are:'
			print cM
	elif nowDraw in [4, 6]:
		nextDraw = Chess.Pieces(1, 'r', nowCoord, nextStep, board)
		cM = nextDraw.checkMove()
		if cM==1:
			nextDraw.draw()
			nextDraw.save(gameSave)
			if checkwin(board) == None:
				nowDraw=(nowDraw+1)%4
				nowCoord[:] = nextStep[:]
				clearUp()
				showAll(nowDraw, nowCoord, board)
				rook = 0
			else: #use Rook to win
				##Erase the Rook on the board
				Chess.Pieces(0, '0', [0, 0], nextStep, board).draw()
				gameSave.pop()
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
	if checkwin(board) != None:
		clearUp()
		showboard(board)
		print 'Player',checkwin(board),'wins!'
		break
