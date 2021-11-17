from vec_gradient import gradient
import numpy as np


x = np.array([12.4956442, 21.5007972, 31.5527382, 48.9145838, 57.5088733])
y = np.array([37.4013816, 36.1473236, 45.7655287, 46.6793434, 59.5585554])
# Example 0:
theta1 = np.array([2, 0.7])
res1 = gradient(x, y, theta1)
print(res1, type(res1))
# Output:
#array([-19.0342574 -586.66875564])

# Example 1:
theta2 = np.array([1, -0.4])
res2 = gradient(x, y, theta2)
print(res2, type(res2))
# Output:
#array([-57.86823748 -2230.12297889])