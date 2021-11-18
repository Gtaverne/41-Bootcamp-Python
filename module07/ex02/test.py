import numpy as np
from loss import loss_

X = np.array([0, 15, -9, 7, 12, 3, -21])
Y = np.array([2, 14, -13, 5, 12, 4, -19])
# Example 0:
print(loss_(X, Y))
# Output:
# 2.1428571428571436


# Example 1:
print(loss_(X, X))
# Output:
0.0