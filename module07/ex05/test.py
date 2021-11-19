

import numpy as np
from mylinearregression import MyLinearRegression as MyLR
X = np.array([[1., 1., 2., 3.], [5., 8., 13., 21.], [34., 55., 89., 144.]])
Y = np.array([[23.], [48.], [218.]])
mylr = MyLR([[1.], [1.], [1.], [1.], [1]])


# Example 0:
res = mylr.predict_(X)
print("mylr.predict_(X)\n", res)
# Output:
# array([[8.], [48.], [323.]])


# Example 1:
res = mylr.loss_elem_(X,Y)
print("mylr.loss_elem_(X,Y)\n", res)
# Output:
# array([[225.], [0.], [11025.]])


# Example 2:
res =  mylr.loss_(X,Y)
print("mylr.loss_(X,Y)", res)
# Output:
# 1875.0


# Example 3:
mylr.alpha = 1.6e-4
mylr.max_iter = 200000
print("mylr.fit_(X, Y)", mylr.fit_(X, Y))
mylr.theta
# Output:
# array([[18.188..], [2.767..], [-0.374..], [1.392..], [0.017..]])


# Example 4:
mylr.predict_(X)
# Output:
# array([[23.417..], [47.489..], [218.065...]])


# Example 5:
mylr.loss_elem_(X,Y)
# Output:
# array([[0.174..], [0.260..], [0.004..]])


# Example 6:
mylr.loss_(X,Y)
# Output:
# 0.0732..