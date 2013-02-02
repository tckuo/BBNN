class Pieces:
	def __init__(self, player=0, nextKind='0',\
				 nextStep=[0, 0], nowCoord=[0, 0],\
				 board=[[(0,'0') for i in range(7)] for j in range(7)]):
		self.player = player
		self.nextKind = nextKind
		self.nowCoord = nowCoord
		self.move = [nextStep[0]-nowCoord[0], nextStep[1]-nowCoord[1]]
		self.nextStep = nextStep[:]
		self.board = board
#	def details(self):
#		#return [self.player, self.nextKind, self.nowCoord, self.nextStep]
#		return "Now playing: Player %d with piece %s"%(self.player, self.nextKind)
	def availMoves(self):
		'''
		list all available moves
		'''
		moveList = []
		if self.nowCoord == [0, 0]: #1st move
			for i in range(1,7):
				for j in range(1,7):
					moveList.append([i, j])
		else:			
			if self.nextKind == 'b':
				x0, y0 = self.nowCoord[0], self.nowCoord[1]
				i = 1
				while i < 6: #I
					x, y = x0 + i, y0 + i
					if 0 < x < 7 and 0 < y < 7:
						if self.board[x][y][0] == 0:
							moveList.append([x, y])
						else:
							break
					else:
						break
					i += 1
				i = 1
				while i < 6: #II
					x, y = x0 - i, y0 + i
					if 0 < x < 7 and 0 < y < 7:
						if self.board[x][y][0] == 0:
							moveList.append([x, y])
						else:
							break
					else:
						break
					i += 1
				i = 1
				while i < 6: #III
					x, y = x0 - i, y0 - i
					if 0 < x < 7 and 0 < y < 7:
						if self.board[x][y][0] == 0:
							moveList.append([x, y])
						else:
							break
					else:
						break
					i += 1
				i = 1
				while i < 6: #IV
					x, y = x0 + i, y0 - i
					if 0 < x < 7 and 0 < y < 7:
						if self.board[x][y][0] == 0:
							moveList.append([x, y])
						else:
							break
					else:
						break
					i += 1
			elif self.nextKind == 'n':
				x0, y0 = self.nowCoord[0], self.nowCoord[1]
				for s1 in [-1, 1]:
					for s2 in [-1, 1]:
						x1, y1 = x0 + s1, y0 + s2*2
						x2, y2 = x0 + s1*2, y0 + s2
						if 0 < x1 < 7 and 0 < y1 < 7:
							if self.board[x1][y1][0] == 0:
								moveList.append([x1, y1])
						if 0 < x2 < 7 and 0 < y2 < 7:
							if self.board[x2][y2][0] == 0:
								moveList.append([x2, y2])
			elif self.nextKind == 'r':
				x0, y0 = self.nowCoord[0], self.nowCoord[1]
				i = 1
				while i < 6: #+x dir
					x, y = x0 + i, y0
					if 0 < x < 7 and 0 < y < 7:
						if self.board[x][y][0] == 0:
							moveList.append([x, y])
						else:
							break
					else:
						break
					i += 1
				i = 1
				while i < 6: #+y-dir
					x, y = x0, y0 + i
					if 0 < x < 7 and 0 < y < 7:
						if self.board[x][y][0] == 0:
							moveList.append([x, y])
						else:
							break
					else:
						break
					i += 1
				i = 1
				while i < 6: #-x dir
					x, y = x0 - i, y0
					if 0 < x < 7 and 0 < y < 7:
						if self.board[x][y][0] == 0:
							moveList.append([x, y])
						else:
							break
					else:
						break
					i += 1
				i = 1
				while i < 6: #-y dir
					x, y = x0, y0 - i
					if 0 < x < 7 and 0 < y < 7:
						if self.board[x][y][0] == 0:
							moveList.append([x, y])
						else:
							break
					else:
						break
					i += 1
			else:
				return None	
		return moveList

	def checkMove(self):
		'''
		check next step can be placed or not
		if yes: return 1
		if not: return a list available moves
		if no available move: return 0
		'''
		aMoves = self.availMoves()
		if len(aMoves) == 0:
			return 0
		elif self.nextStep in aMoves:
			return 1
		else:
			return aMoves
	def draw(self):
		self.board[self.nextStep[0]][self.nextStep[1]] = (self.player, self.nextKind)
