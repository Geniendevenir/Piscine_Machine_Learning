import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

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

def plot(x, y, theta):		#(x / y): Points coordinates,  theta(theta1, theta2)
	X = add_intercept(x)	#Add 1 Column Trick to x ndarray
	y_hat = X @ theta		#Numpy Matrix Multiplication => gives prediction
	print(y_hat)
	plt.scatter(x, y, color='blue', label='Data Points')		#Plot the point (x/y)
	plt.plot(x, y_hat, color="red", label="Prediction Line")	#Plot the Prediction Line
	plt.xlabel("Power Engine")
	plt.ylabel("Price")
	plt.title("Scatter Plot of Data Points")
	plt.legend()
	plt.show()