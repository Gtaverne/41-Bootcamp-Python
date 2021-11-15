import numpy as np
from prediction import simple_predict

x = np.arange(1,6)
# Example 1:
theta1 = np.array([5, 0])
res = simple_predict(x, theta1)
print(res)

theta2 = np.array([0, 1])
res2 = simple_predict(x, theta2)
print(res2)

theta3 = np.array([5, 3])
res3 = simple_predict(x, theta3)
print(res3)


theta4 = np.array([-3, 1, 18, 11])
res4 = simple_predict(x, theta4)
print(res4)