import numpy as np
from log_gradient import log_gradient

# Example 1:
y1 = np.array([[1]])
x1 = np.array([[4]])
theta1 = np.array([[2], [0.5]])
r = log_gradient(x1, y1, theta1)
print(r)
# Output:
# array([[-0.01798621],
# [-0.07194484]])

# Example 2:
y2 = np.array([[1], [0], [1], [0], [1]])
x2 = np.array([[4], [7.16], [3.2], [9.37], [0.56]])
theta2 = np.array([[2], [0.5]])
r = log_gradient(x2, y2, theta2)
print(r)
# Output:
# array([[0.3715235 ],
# [3.25647547]])

# Example 3:
y3 = np.array([[0], [1], [1]])
x3 = np.array([[0, 2, 3, 4], [2, 4, 5, 5], [1, 3, 2, 7]])
theta3 = np.array([[-2.4], [-1.5], [0.3], [-1.4], [0.7]])
r = log_gradient(x3, y3, theta3)
print(r)
# Output:
# array([[-0.55711039],
# [-0.90334809],
# [-2.01756886],
# [-2.10071291],
# [-3.27257351]])