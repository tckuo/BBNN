
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
