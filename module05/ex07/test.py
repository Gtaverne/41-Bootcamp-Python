from cost import cost_elem_
from cost import cost_
from cost import predict_
import numpy as np


x1 = np.array([[0.], [1.], [2.], [3.], [4.]])
theta1 = np.array([[2.], [4.]])
y_hat1 = predict_(x1, theta1)
y1 = np.array([[2.], [7.], [12.], [17.], [22.]])


# Example 1:
res = cost_elem_(y1, y_hat1)
print(res)
print(cost_(y1, y_hat1))

x2 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
theta2 = np.array([[0.05], [1.], [1.], [1.]])
y_hat2 = predict_(x2, theta2)
print(y_hat2)
y2 = np.array([[19.], [42.], [67.], [93.]])
# Example 3:
print(cost_elem_(y2, y_hat2))