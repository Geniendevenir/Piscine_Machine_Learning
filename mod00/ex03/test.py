import numpy as np
from tools import add_intercept
# Example 1:
x = np.arange(1,6)
print(x)
add_intercept(x)

# Example 2:
y = np.arange(1,10).reshape((3,3))
print(y)
add_intercept(y)
