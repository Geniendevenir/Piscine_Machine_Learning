import numpy as np

def simple_predict(x, theta):
	if theta is None or x is None:
		return print("x and Theta should not be empty")
	if not isinstance(x, np.ndarray) or not isinstance(theta, np.ndarray):
		return print("x and Theta should be of type ndarray")
	if len(theta) != 2:
		return print("Theta should have 2 int values")
	y_hat = np.zeros(x.shape)
	for i, _ in enumerate(y_hat):
		y_hat[i] = theta[0] + theta[1] * x[i]
	print(y_hat)
	return y_hat