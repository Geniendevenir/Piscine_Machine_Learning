import numpy as np

def loss_elem_(y, y_hat):
	if not isinstance(y, np.ndarray) or not isinstance(y_hat, np.ndarray):
		return print("y and y_hat should be of type ndarray")
	elif y.shape != y_hat.shape:
		return print("y and y_hat should haev the same lengh")
	

def loss_(y, y_hat):
	""""""

def predict_(x, theta):
	if theta is None or x is None:
		return print("x and Theta should not be empty")
	if not isinstance(x, np.ndarray) or not isinstance(theta, np.ndarray):
		return print("x and Theta should be of type ndarray")
	if len(theta) != 2:
		return print("Theta should have 2 int values")
	X = add_intercept(x)
	print(f"X = {X}\nX.shape ={X.shape}\ntheta = {theta}\ntheta.shape = {theta.shape}")
	matr_mult = X @ theta
	y_hat = matr_mult.astype(float).tolist()
	print(y_hat)
	return y_hat

def add_intercept(x):
	if not isinstance(x, np.ndarray) or x is None:
		return None
	if x.ndim == 1:
		rows = 1
		columns = x.shape[0]
	else:
		rows, columns = x.shape
	rev_x = x.reshape((columns, rows))
	X = np.insert(rev_x, 0, 1., 1)
	return X