import numpy as np
from my_linear_regression import MyLinearRegression as MyLR


x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]])
y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]])
lr1 = MyLR([2, 0.7])


# Example 0.0:
r1 = lr1.predict_(x)
print('r1', r1)
# Output:
# array([[10.74695094],
# [17.05055804],
# [24.08691674],
# [36.24020866],
# [42.25621131]])


# Example 0.1:
r2 = lr1.loss_elem_(lr1.predict_(x),y)
print("r2", r2)
# Output:
# array([[710.45867381],
# [364.68645485],
# [469.96221651],
# [108.97553412],
# [299.37111101]])


# Example 0.2:
r3 = lr1.loss_(lr1.predict_(x),y)
print("r3", r3)
# Output:
# 195.34539903032385

# Example 1.0:
lr2 = MyLR([1, 1], 5e-8, 1500000)


lr2.fit_(x, y, verbose=True)
r4 = lr2.thetas
print('r4', r4)
# Output:
# array([[1.40709365],
# [1.1150909 ]])


# Example 1.1:
r5 = lr2.predict_(x)
print('r5', r5)
# Output:
# array([[15.3408728 ],
# [25.38243697],
# [36.59126492],
# [55.95130097],
# [65.53471499]])


# Example 1.2:
r6 = MyLR.loss_elem_(lr2.predict_(x), y)
print('r6', r5)
# Output:
# array([[486.66604863],
# [115.88278416],
# [ 84.16711596],
# [ 85.96919719],
# [ 35.71448348]])


# Example 1.3:
r7 = MyLR.loss_(lr2.predict_(x),y)
print('r7', r7)
# Output:
# 80.83996294128525