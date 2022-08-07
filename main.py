import copy


class Game:
	def __init__(self):
		self.fieldDim = int(input("field-dimmensions (1-9): ")) # stores the field's dimmension 
		self.field = [[0 for i in range(self.fieldDim)]for j in range(self.fieldDim)] # stores the field
		self.solutions = []

	def checkForSolved(self):
		# checks whether the current field is solved
		count = 0
		for i in range(self.fieldDim):
			for j in range(self.fieldDim):
				if self.field[i][j] == "D":
					self.field[i][j] = 0
					if self.is_square_free(i,j):
						count += 1
					self.field[i][j] = "D"
		if count == self.fieldDim:
			return True
			
	def printSolutions(self, field):
		# prints a given field array (format f.e. [[x, x], [x, x]]) to the screen
		print("-" * (2*self.fieldDim-1))
		for row in field:
			for num in row:
				print(str(num), end = " ")
			print("")
		print("-" * (2*self.fieldDim-1))
	
	def saveField(self):
		# checks whether the current field has already been saved.
		# If not the field gets stored in the solutions array.
		self.solutions.append(copy.deepcopy(self.field)) # creates a copy of the given field, necessary because of the mutable nature of python-arrays.
		if len(self.solutions) > 1:
			for i in self.solutions[:-1]:
				if i == self.solutions[-1]:
					self.solutions.pop()
					return False
		return True	

	def is_square_free(self, x, y):
		# checks whether a figure can be placed in the specific field
		directions = [(1,1), (-1,1), (1,-1), (-1,-1)]
		for direct in directions:
			for i in range(self.fieldDim):
				row = x + direct[0]*i
				col = y + direct[1]*i
				if row >= 0 and row < self.fieldDim and col >=0 and col < self.fieldDim:
					if self.field[row][col] == "D":
						return False
		for c in range(self.fieldDim):
			if self.field[x][c] == "D" or self.field[c][y] == "D": 
				return False
		return True

	def solve(self):
		# solves the problem via backtracking and recursion
		for i in range(self.fieldDim):
			for j in range(self.fieldDim):
					if self.field[i][j] == 0 and self.is_square_free(i, j):
						self.field[i][j] = "D"
						self.solve()
						self.field[i][j] = 0
						
		if self.checkForSolved() and self.saveField():
			self.printSolutions(self.field)


if __name__ == "__main__":
	game = Game()
	game.solve()
	if not game.solutions:
		print(f"no solutions for {game.fieldDim}x{game.fieldDim} field!")
	else:
		print(f"there are {len(game.solutions)} solutions for this problem")
	#if input("show all solutions?: ").lower() == "y":
		#for field in game.solutions:
			#game.printSolutions(field)