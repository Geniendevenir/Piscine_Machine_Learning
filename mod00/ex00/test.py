from matrix import Matrix


"""
TEACHINGS:
-> Ternary
-> All()
-> for _ in iter
-> Initialize empty Matrix of 0.'s:		self.matrix = [[0.] * columns for row in range(rows)]
"""

""" CHECK_INIT == SUCCESS
#m1 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]]) #good == SUCCESS
#m2 = Matrix([[4.0, 5.0]]) #good == SUCCESS
#m3 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0, 0.0]]) #Error inequal size row == SUCCESS
#m4 = Matrix([[0.0, 1.0], [2.0, 3.0], "oui"])#Error == SUCCESS
#m5 = Matrix([0.0, 1.0])#Error == SUCCESS
#m6 = Matrix("Test")#Error == SUCCESS
#m7 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, -1]])#Error == SUCCESS
#m8 = Matrix((1,2))#good == SUCCESS
#m9 = Matrix((10,2,3))#Error == SUCCESS
 """

""" CALCUL
__add__ / __radd__:
Work => SUCCESS
m1 = Matrix([[1., 1.], [1., 1.]])
m2 = Matrix([[1., 2.], [3., 4.]])
m1 + m2

Shouldnt Work => SUCCESS
m1 = Matrix([[1., 1., 1.], [1., 1., 1.]])
m2 = Matrix([[1., 2.], [3., 4.]])
m1 + m2

__sub__ / __rsub__:
Work => SUCCESS
m1 = Matrix([[1., 1.], [1., 1.]])
m2 = Matrix([[1., 2.], [3., 4.]])
m2 - m1

"""

m1 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])

m1.T()




