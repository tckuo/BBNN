class Pieces:
	def __init__(self, player=0, nextKind='0',\
				 nowCoord=[0, 0], nextStep=[0, 0],\
				 board=[[(0,'0') for i in range(7)] for j in range(7)]):
		self.player = player
		self.nextKind = nextKind
		self.move = [nextStep[0]-nowCoord[0], nextStep[1]-nowCoord[1]]
		self.nextStep = []
		self.nextStep[:] = nextStep[:]
		self.board = board
	def details(self):
		return [self.player, self.nextKind]
	def moves(self):
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
	def checkMoves(self):
		'''
		to be finished!!!!!!!!!!!!!!!!
		check type==int? , len==2?, move==0?, etc
		or it can check out of the class
		'''
		if self.move == [6, 6]:
			return True
		absMove = sorted([abs(self.move[0]), abs(self.move[1])])
		if self.nextKind == 'b':
			if absMove[0] == absMove[1]:
				return True
			else:
				return False
		elif self.nextKind == 'n':
			if absMove[0] * absMove[1] == 2:
				return True
			else:
				return False
		elif self.nextKind == 'r':
			if absMove in [[0, y] for y in range(1,6)]:
				return True
			else:
				return False
		else:
			return  False
