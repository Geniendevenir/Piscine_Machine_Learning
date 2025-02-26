import numpy as np

def add_intercept(x):
	if not isinstance(x, np.ndarray) or x is None:
		return None
	print(x.shape)
	if x.ndim == 1:
		rows = 1
		columns = x.shape[0]
	else:
		rows, columns = x.shape
	rev_x = x.reshape((columns, rows))
	X = np.insert(rev_x, 0, 1., 1)
	print(X)
	return X