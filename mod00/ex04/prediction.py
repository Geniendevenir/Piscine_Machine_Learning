import numpy as np

def predict_(x, theta):
	if theta is None or x is None:
		return print("x and Theta should not be empty")
	if not isinstance(x, np.ndarray) or not isinstance(theta, np.ndarray):
		return print("x and Theta should be of type ndarray")
	if len(theta) != 2:
		return print("Theta should have 2 int values")
	X = add_intercept(x)
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