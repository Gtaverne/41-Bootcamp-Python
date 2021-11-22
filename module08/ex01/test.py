import numpy as np
from log_pred import logistic_predict

# Example 1
x = np.array([[4]])
theta = np.array([[2], [0.5]])
r = logistic_predict(x, theta)
print(r)
#  Output:
# array([[0.98201379]])

# Example 1
x2 = np.array([[4], [7.16], [3.2], [9.37], [0.56]])
theta2 = np.array([[2], [0.5]])
r = logistic_predict(x2, theta2)
print(r)
# Output:
# array([[0.98201379],
# [0.99624161],
# [0.97340301],
# [0.99875204],
# [0.90720705]])

# Example 2
x3 = np.array([[0, 2, 3, 4], [2, 4, 5, 5], [1, 3, 2, 7]])
theta3 = np.array([[-2.4], [-1.5], [0.3], [-1.4], [0.7]])
r = logistic_predict(x3, theta3)
print(r)
# Output:
# array([[0.03916572],
# [0.00045262],
# [0.2890505 ]])