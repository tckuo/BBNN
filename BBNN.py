import Chess
'''
board has elements as (player, 'b or n')
'''

# step=(column, rank)

blankboard=[[(0,'0') for i in range(7)] for j in range(7)]

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


def drawb(player, step, board):
	#laststep=step
	board[step[0]][step[1]]=(player,'b')

	
def drawn(player, step, board):
	#laststep=step
	board[step[0]][step[1]]=(player,'n')


def showboard(board):   # board has elements as (player, 'b or n')
	#lastcor={(1,'b'):'  B* ',(1,'n'):'  N* ',(2,'b'):' (b)*',(2,'n'):' (n)*'}
	showcor={(0,'0'):'     ',(1,'b'):'  B  ',
			 (1,'n'):'  N  ',(2,'b'):' (b) ',(2,'n'):' (n) '}
	middle=''
	for i in range(6,1,-1):
		onerank='\t'+str(i)+'|'
		for j in range(1,7):
			onerank=onerank+showcor[board[j][i]]+'|'
		middle=(middle+'\t |'+'     |'*6+'\n'+onerank
				+'\n\t |-----+-----+-----+-----+-----+-----|\n')
	lastrank='\t1|'
	for j in range(1,7):
		lastrank=lastrank+showcor[board[j][1]]+'|'
	boardgraph=('\t .-----.-----.-----.-----.-----.-----.\n'+middle
				+'\t |'+'     |'*6+'\n'+lastrank
				+'\n\t \'-----\'-----\'-----\'-----\'-----\'-----\''
				+'\n\t    1     2     3     4     5     6    ')
	print boardgraph


def checkwin(board):
	columnocc={1:[[],[],[],[],[],[]],2:[[],[],[],[],[],[]]}
	rankocc={1:[[],[],[],[],[],[]],2:[[],[],[],[],[],[]]}
	slashocc={1:[[],[],[],[],[]],2:[[],[],[],[],[]]}
	slantocc={1:[[],[],[],[],[]],2:[[],[],[],[],[]]}
	for player in [1,2]:
		for column in range(1,7):
			for rank in range(1,7):
				if board[column][rank][0]==player:
					columnocc[player][column-1].append(rank)
					rankocc[player][rank-1].append(column)
					if column-rank>=-2 and column-rank<=2:
						slashocc[player][column-rank+2].append(column)
					if column+rank>=5 and column+rank<=9:
						slantocc[player][column+rank-5].append(column)

	for player in [1,2]:
		opponent=3-player
		for j in columnocc[player]:
			if len(j)>=4: # Check if 4 in a line
				# Check if unblocked:
				if len(columnocc[opponent][columnocc[player].index(j)])==0:
					return player
				else:
					for k in columnocc[opponent][columnocc[player].index(j)]:
						if k<max(j) and k>min(j):
							if len(j)==4:
								break
							else:
								if k==3 or k==4:
									break
								else:
									return player
					else:
						return player
		for j in rankocc[player]:
			if len(j)>=4: # Check if 4 in a line
				# Check if unblocked:
				if len(rankocc[opponent][rankocc[player].index(j)])==0:
					return player
				else:
					for k in rankocc[opponent][rankocc[player].index(j)]:
						if k<max(j) and k>min(j):
							if len(j)==4:
								break
							else:
								if k==3 or k==4:
									break
								else:
									return player
					else:
						return player
		for j in slashocc[player]:
			if len(j)>=4: # Check if 4 in a line
				# Check if unblocked:
				if len(slashocc[opponent][slashocc[player].index(j)])==0:
					return player
				else:
					for k in slashocc[opponent][slashocc[player].index(j)]:
						if k<max(j) and k>min(j):
							if len(j)==4:
								break
							else:
								if k==3 or k==4:
									break
								else:
									return player
					else:
						return player
		for j in slantocc[player]:
			if len(j)>=4: # Check if 4 in a line
				# Check if unblocked:
				if len(slantocc[opponent][slantocc[player].index(j)])==0:
					return player
				else:
					for k in slantocc[opponent][slantocc[player].index(j)]:
						if k<max(j) and k>min(j):
							if len(j)==4:
								break
							else:
								if k==3 or k==4:
									break
								else:
									return player
					else:
						return player




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
print 'NC', nowCoord
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
			inputKey=raw_input('This function is not finished. Please draw on a square: ')
		else:
			try:
				int(inputKey[0])
				int(inputKey[1])
				check = 0
			except ValueError:
				inputKey=raw_input('This function is not finished. Please draw on a square: ')

	nextStep = [int(inputKey[0]),int(inputKey[1])]
	print 'NC', nowCoord
	print 'NS', nextStep
	diff = [0, 0]
	if nowCoord == [0,0]:
		diff = [6,6]
	else:
		diff[0] = nextStep[0] - nowCoord[0]
		diff[1] = nextStep[1] - nowCoord[1]
	print 'diff', diff
	print nowdraw
	if nowdraw==0:
		nextDraw = Chess.Pieces(1, 'b', diff)
		print '0'
		if nextDraw.checkMoves():
			drawb(1, nextStep, board)
			print 'B'
			nowdraw=(nowdraw+1)%4
			nowCoord[0:] = nextStep[0:]
	elif nowdraw==1:
		nextDraw = Chess.Pieces(2, 'n', diff)
		print 1
		if nextDraw.checkMoves():
			drawn(2, nextStep, board)
			print 'n'
			nowdraw=(nowdraw+1)%4
			nowCoord[0:] = nextStep[0:]
	elif nowdraw==2:
		nextDraw = Chess.Pieces(1, 'n', diff)
		print 2
		if nextDraw.checkMoves():
			drawn(1, nextStep, board)
			print 'N'
			nowdraw=(nowdraw+1)%4
			nowCoord[0:] = nextStep[0:]
	elif nowdraw==3:
		nextDraw = Chess.Pieces(2, 'b', diff)
		print 3
		if nextDraw.checkMoves():
			drawb(2, nextStep, board)
			print 'b'
			nowdraw=(nowdraw+1)%4
			nowCoord[:] = nextStep[:]
	else:
		break
	showboard(board)
	if checkwin(board) != None:
		print 'Player',checkwin(board),'wins!'
		break
	#nowdraw=(nowdraw+1)%4
