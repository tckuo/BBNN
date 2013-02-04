import Chess
from Func import *
'''
board has elements as (player, 'b or n')
'''
###
# step=(column, rank)
#board as global mem?
board=[[(0,'0') for i in range(7)] for j in range(7)]
#order=('B','n','N','b')
##order: draw: (player, piece, skip-add-num)
order={0: (1, 'b', 1), 1:(2, 'n', 3),
	   2: (1, 'n', 1), 3:(2, 'b', 3),
	   4: (1, 'r', 1), 6:(1, 'r', 3)}
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
game = True

showAll(nowDraw, nowCoord, board)
print 'type \'H\' for Help'

while game:
	#check: have available move or not
	if Chess.Pieces(order[nowDraw][0], order[nowDraw][1], nowCoord, [0, 0], board).checkMove()==0:
		#for P1 still has R and can move with R, make a choice
		if rook==1 and nowDraw in [0, 2]:
			if Chess.Pieces(1, 'r', nowCoord, [0, 0], board).checkMove()==0:
				print 'No available move. Skip this turn.'
				nowDraw = (nowDraw+order[nowDraw][2])%4
				showPlayer(nowDraw)
			else:
				inputKey = raw_input('Enter \'Y\' to use Rook, else key to give up.')
				if inputKey=='Y':
					nowDraw += 4
					showPlayer(nowDraw)
				else:
					print 'No available move. Skip this turn.'
					nowDraw = (nowDraw+order[nowDraw][2])%4
					showPlayer(nowDraw)
		else: #if no R to use
			print 'No available move. Skip this turn.'
			nowDraw = (nowDraw+order[nowDraw][2])%4
			showPlayer(nowDraw)

		#After skip once, if still has no available moves => This game is drawn
		if Chess.Pieces(order[nowDraw][0], order[nowDraw][1], nowCoord, [0, 0], board).checkMove()==0:
			#for P1 still has R and can move with R, make a choice
			if rook==1 and nowDraw in [0, 2]:
				if Chess.Pieces(1, 'r', nowCoord, [0, 0], board).checkMove()==0:
					print 'Still no available move. Skip this turn.'
					print 'This game is drawn.'
					break
				else:
					inputKey = raw_input('Enter \'Y\' to use Rook, else key to give up.')
					if inputKey=='Y':
						nowDraw += 4
						showPlayer(nowDraw)
					else:
						print 'Still no available move. Skip this turn.'
						print 'This game is drawn.'
						break
			else: #if no R to use
				print 'Still no available move. Skip this turn.'
				print 'This game is drawn.'
				break
	
	inputKey=raw_input('Please draw on a square: ')
	check = 1
	while check == 1:
		if inputKey == 'B':	#take Back
			if len(gameSave)==0:
				inputKey=raw_input('Invalid input. Please draw on a square: ')
			elif len(gameSave)==1:
				movel1 = gameSave[0]
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

				showAll(nowDraw, nowCoord, board)
				inputKey=raw_input('Please draw on a square: ')
		elif inputKey == 'C':	#clear up
			showAll(nowDraw, nowCoord, board)
			inputKey=raw_input('Please draw on a square: ')
		elif inputKey == 'E':	#Exit
			game = False
			break
			#inputKey=raw_input('The function \'Exit\' is not finished. Please draw on a square: ')
		elif inputKey == 'H':	#Help
			print "'B': take Back"
			print "'C': Clear up the screen"
			print "'E': Exit the game"
			print "'L': Load the game"
			print "'R': For player 1 to use the Rook"
			print "'S': Save the game"
			inputKey=raw_input('Please draw on a square: ')
		elif inputKey == 'L':		#Load, not finished
			#!!!!!!!!!!!!
			#There is a defect that when the loaded game's last move will skip the next move
			#But still can play
			try: #still can not handle all the exception
				f = open("bbnn.sav", "r")
				test = f.read().split()
				temp = [[0 for i in range(6)] for j in range(6)]
				showcor={(1,'b'):'  B  ', (1,'n'):'  N  ',(1,'r'):'  R  ',
			 			 (2,'b'):' (b) ', (2,'n'):' (n) ',(0,'0'):'     ',}
				for i in range(len(test)):
					showcor[(int(test[i][0]), test[i][1])]
					temp[int(test[i][2])-1][int(test[i][2])-1]
				f.close()
				del temp
				del test
				del showcor
			except IOError:
				open("bbnn.sav", "w")
			except KeyError:
				open("bbnn.sav", "w")
			except IndexError:
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
			showAll(nowDraw, nowCoord, board)

			del move
			del savList
			inputKey=raw_input('Game Loaded. Please draw on a square: ')		
		elif inputKey == 'R':	#change to Rook
			if nowDraw==4:		#change back to B
				nowDraw -= 4
				inputKey = raw_input('Now player 1 plays as Bishop. Please draw on a square: ')
			elif nowDraw==6:	#change back to N
				nowDraw -= 4
				inputKey = raw_input('Now player 1 plays as Knight. Please draw on a square: ')
			else:
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
		elif inputKey == 'S':		#Save
			f = open("bbnn.sav", "w")
			for i in range(len(gameSave)):
				f.write('%s\n'%gameSave[i])
			f.close()
			showAll(nowDraw, nowCoord, board)
			inputKey=raw_input('Game saved. Please draw on a square: ')
		##BONUS!!!
		elif inputKey == 'WIN':
			game = 0
			print "Player %d wins!"%(nowDraw%2+1)
			break
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
	
	##Exit part 2
	if not game:
		print 'Thanks for your playing'
		break

	nextStep = [int(inputKey[0]),int(inputKey[1])]
	if nowDraw==0:
		nextDraw = Chess.Pieces(1, 'b', nowCoord, nextStep, board)
		cM = nextDraw.checkMove()
		if cM==1:
			nextDraw.draw()
			nextDraw.save(gameSave)
			nowDraw=(nowDraw+1)%4
			nowCoord[:] = nextStep[:]
			showAll(nowDraw, nowCoord, board)
		elif cM==0:
			nowDraw=(nowDraw+1)%4
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
			showAll(nowDraw, nowCoord, board)
		elif cM==0:
			nowDraw=(nowDraw+3)%4
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
			showAll(nowDraw, nowCoord, board)
		elif cM==0:
			nowDraw=(nowDraw+1)%4
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
			showAll(nowDraw, nowCoord, board)
		elif cM==0:
			nowDraw=(nowDraw+3)%4
			showAll(nowDraw, nowCoord, board)
		else:
			print 'Invalid move! The available moves are:'
			print cM
	elif nowDraw in [4, 6]:
		nextDraw = Chess.Pieces(1, 'r', nowCoord, nextStep, board)
		cM = nextDraw.checkMove()
		if cM==1:
			nextDraw.draw()
			#nextDraw.save(gameSave)
			if checkwin(board) == None:##not use R to win
				nowDraw=(nowDraw+1)%4
				#nowCoord[:] = nextStep[:]
				#showAll(nowDraw, nowCoord, board)
				#rook = 0

				##if use R to stop p2
				if Chess.Pieces(order[nowDraw][0], order[nowDraw][1], nextStep, [0, 0], board).checkMove()==0:
					Chess.Pieces(0, '0', [0, 0], nextStep, board).draw()
					#gameSave.pop()
					nowDraw -= 1
					showAll(nowDraw, nowCoord, board)
					print 'Illigal move! You can not stop your opponent by Rook.'
				else: #else: right move
					nowCoord[:] = nextStep[:]
					nextDraw.save(gameSave)
					showAll(nowDraw, nowCoord, board)
					rook = 0
			else: #use Rook to win
				##Erase the Rook on the board
				Chess.Pieces(0, '0', [0, 0], nextStep, board).draw()
				#gameSave.pop()
				nowDraw -= 4
				showAll(nowDraw, nowCoord, board)
				print 'Illigal move! You can not win the game by Rook.'
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
