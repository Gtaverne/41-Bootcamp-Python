import numpy as np
from fit import fit_
from prediction import predict

x = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
y = np.array([[19.6], [-2.8], [-25.2], [-47.6]])
theta2 = np.array([[42.], [1.], [1.], [1.]])


# Example 0:
theta2 = fit_(x, y, theta2, alpha = 0.0005, max_iter=42000)
print(theta2)
# Output:
# array([[41.99..],[0.97..], [0.77..], [-1.20..]])


# Example 1:

print(predict(x, theta2))
# Output:
# array([[19.5992..], [-2.8003..], [-25.1999..], [-47.5996..]])