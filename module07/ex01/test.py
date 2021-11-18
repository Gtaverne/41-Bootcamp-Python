from prediction import simple_predict
import numpy as np

x = np.arange(1,13).reshape((4,-1))
# Example 0:
theta1 = np.array([5, 0, 0, 0])
tmp = simple_predict(x, theta1)
print(tmp)
# Ouput:
# array([5., 5., 5., 5.])
# Do you understand why y_hat contains only 5’s here?


# Example 1:
theta2 = np.array([0, 1, 0, 0])
tmp = simple_predict(x, theta2)
print(tmp)
# Output:
# array([ 1., 4., 7., 10.])
# Do you understand why y_hat == x[:,0] here?


# Example 2:
theta3 = np.array([-1.5, 0.6, 2.3, 1.98])
tmp = simple_predict(x, theta3)
print(tmp)
# Output:
# array([ 9.64, 24.28, 38.92, 53.56])


# Example 3:
theta4 = np.array([-3, 1, 2, 3.5])
tmp = simple_predict(x, theta4)
print(tmp)
# Output:
# array([12.5, 32. , 51.5, 71. ])