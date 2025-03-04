import numpy as np
from prediction import predict_

x = np.arange(1,6)
# Example 1:
theta1 = np.array([[5], [0]])
predict_(x, theta1)

# Example 2:
theta2 = np.array([[0], [1]])
predict_(x, theta2)

# Example 3:
theta3 = np.array([[5], [3]])
predict_(x, theta3)

# Example 4:
theta4 = np.array([[-3], [1]])
predict_(x, theta4)