import numpy as np
from loss import loss_elem_, loss_, predict_

test = np.arange(1,6)
print(test)
print(test.shape)
x1 = np.array([[0.], [1.], [2.], [3.], [4.]])
theta1 = np.array([[2.], [4.]])
print(f"{x1.shape}, {theta1.shape}")
y_hat1 = predict_(x1, theta1)
y1 = np.array([[2.], [7.], [12.], [17.], [22.]])
print(f"{y1.shape}, {y_hat1.shape}")

""" 
# Example 1:
loss_elem_(y1, y_hat1)


# Example 2:
loss_(y1, y_hat1)


x2 = np.array([0, 15, -9, 7, 12, 3, -21]).reshape(-1, 1)
theta2 = np.array(np.array([[0.], [1.]]))
y_hat2 = predict_(x2, theta2)
y2 = np.array([2, 14, -13, 5, 12, 4, -19]).reshape(-1, 1)


# Example 3:
loss_(y2, y_hat2)


# Example 4:
loss_(y2, y2)
"""