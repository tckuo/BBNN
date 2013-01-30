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
	def details(self):
		return [self.player, self.nextKind, self.nowCoord, self.nextStep]
	def moves(self):
		'''
		list all possible moves
		'''
		if self.nextKind == 'b': #bishops
			#d_moves = []
			#for i in range(5):
			#	d_moves.append([i+1, i+1])
			#	d_moves.append([i+1, -i-1])
			#	d_moves.append([-i-1, i+1])
			#	d_moves.append([-i-1, -i-1])
			#return d_moves
			##express in comprehension
			return [[sx*l, sy*l] for sx in [-1, 1] for sy in [-1, 1] for l in range(1,6)]
		elif self.nextKind == 'n': #knights
			#k_moves = []
			#for i in [-1, 1]:
			#	for j in [-1, 1]:
			#		k_moves.append([i, j*2])
			#		k_moves.append([i*2, j])
			#return k_moves
			##express in comprehension
			return [[sx*x , sy*y] for [x,y] in [[1,2],[2,1]] for sx in [-1, 1] for sy in [-1, 1]]
		elif self.nextKind == 'r': #rook
			r_moves = []
			for i in range(5):
				r_moves.append([0, i+1])
				r_moves.append([0, -i-1])
				r_moves.append([i+1, 0])
				r_moves.append([-i-1, 0])
			return r_moves
		else:
			return [[0, 0]]
	def checkMove(self):
		'''
		check the next step can be placed or not

		to be finished!!!!!!!!!!!!!!!!
		check type==int? , len==2?, move==0?, etc
		or it can check out of the class
		'''
		if self.move == [6, 6]: #the case must can place it, e.g. 1st piece
			return True
		elif self.board[self.nextStep[0]][self.nextStep[1]][0] != 0: #place on another piece
			return False
		else:
			absMove = sorted([abs(self.move[0]), abs(self.move[1])])
			if self.nextKind == 'b':
				if absMove[0] == absMove[1]:
					#check on trace
					x, y = self.nowCoord[0], self.nowCoord[1]
					moveDir = [self.move[0]/abs(self.move[0]), self.move[1]/abs(self.move[1])]
					for l in range(1, absMove[0]):
						x += moveDir[0]
						y += moveDir[1]
						if self.board[x][y][0] != 0:
							return False
					return True
				else:
					return False
			elif self.nextKind == 'n':
				if absMove[0] * absMove[1] == 2:
					return True
				else:
					return False
			elif self.nextKind == 'r':
				if absMove in [[0, yy] for yy in range(1,6)]:
					x, y = self.nowCoord[0], self.nowCoord[1]
					if self.move[0] == 0:
						moveDir=[0, self.move[1]/abs(self.move[1])]
					else:
						moveDir=[self.move[0]/abs(self.move[0]), 0]
					for l in range(1, absMove[0]):
						x += moveDir[0]
						y += moveDir[1]
						if self.board[x][y][0] != 0:
							return False
					return True
				else:
					return False
			else:
				return  False
