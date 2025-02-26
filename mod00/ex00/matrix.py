class Matrix:
	def __init__(self, matrix):
		self._check_matrix(matrix)
		print(self.matrix)
		print(self.shape)
	
	def _check_matrix(self, matrix):
		if not isinstance(matrix, list) and not isinstance(matrix, tuple):
			raise TypeError("Matrix must either be a list or a tuple")

		elif all(isinstance(vector, list) for vector in matrix):
			self._get_matrix_shape(matrix)
			return 0

		elif isinstance(matrix, tuple):
			if len(matrix) == 2 and all(isinstance(nbr, int) and nbr > 0 for nbr in matrix):
				rows, columns = matrix
				self.matrix = [[0.] * columns for row in range(rows)]
				self.shape = matrix
				return 0
			raise ValueError("Matrix tuple should only contain 2 positive int values")

		else:
			raise ValueError("Matrix should either be a list of list of vector or a list with one tuple")
	
	def _get_matrix_shape(self, matrix):
		row = len(matrix)
		column = 0
		for data in matrix:
			if len(data) == 0:
				raise ValueError("Matrix vector can't be empty")
			elif column == 0:
				column = len(data)
			elif column != len(data):
				raise ValueError("Matrix vector Column size should be the same")
			for nbr in data:
				if not isinstance(nbr, float):
					raise TypeError("Matrix vector should only contain floats")
		self.shape = (row, column)
		self.matrix = matrix
		return 0

	def T(self):
		rev_matrix = Matrix([list(row) for row in zip(*self.matrix)])
		return rev_matrix
	
	def __add__(self, mat2):
		if self.shape != mat2.shape:
			return print("__add__: Two Matrices must have the same shape")
		result = Matrix(self.shape)
		for i, (rows1, rows2) in enumerate(zip(self.matrix, mat2.matrix)):
			for j, (col1, col2) in enumerate(zip(rows1, rows2)):
				result.matrix[i][j] = col1 + col2
		print(result.matrix)
		return result
		
	def __radd__(self, mat2):
		self.__add__(mat2)

	def __sub__(self, mat2):
		if self.shape != mat2.shape:
			return print("__sub__: Two Matrices must have the same shape")
		result = Matrix(self.shape)
		for i, (rows1, rows2) in enumerate(zip(self.matrix, mat2.matrix)):
			for j, (col1, col2) in enumerate(zip(rows1, rows2)):
				result.matrix[i][j] = col1 - col2
		print(result.matrix)
		return result.matrix
	
		
	def __rsub__(self, mat2):
		if self.shape != mat2.shape:
			return print("__rsub__: Two Matrices must have the same shape")
		result = Matrix(self.shape)
		for i, (rows1, rows2) in enumerate(zip(self.matrix, mat2.matrix)):
			for j, (col1, col2) in enumerate(zip(rows1, rows2)):
				result.matrix[i][j] = col1 - col2
		print(result.matrix)
		return result.matrix
	
	def __truediv__(self, scalar):
		if not isinstance(scalar, (int, float)):
			return print("__truediv__: scalar must be an int or a float")
		result = Matrix(self.shape)
		for i, rows in enumerate(self.matrix):
			for j, col in enumerate(rows):
				result.matrix[i][j] = col / scalar
		print(result.matrix)
		return result.matrix

	def __rtruediv__(self, scalar):
		raise ValueError("__rtruediv__: Scalar / Matrix is not supported")

	def __mul__(self, data):
		if isinstance(data, (int, float)): #Scalar
			result = Matrix(self.shape)
			for i, rows in enumerate(self.matrix):
				for j, col in enumerate(rows):
					result.matrix[i][j] = col * data
			print(result.matrix)
			return result.matrix

		elif isinstance(data, Vector):
			""""""
		elif isinstance(data, Matrix):

			result = Matrix()
			for i, (rows1, rows2) in enumerate(zip(self.matrix, data.matrix)):
				for j, (col1, col2) in enumerate(zip(rows1, rows2)):
					result.matrix[i][j] = col1 + col2
			return print(result.matrix)
		
	def __rmul__(self, data):
		self.__mul__(data)
		
	#def __str__(self):
		""""""
		
	#def __repr__(self):
		""""""



class Vector(Matrix):
	""""""			
				