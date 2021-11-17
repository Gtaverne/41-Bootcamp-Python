import numpy as np
from fit import fit_, predict


x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]])
y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]])
theta = np.array([1, 1])
# Example 0:
theta1 = fit_(x, y, theta, alpha=5e-6, max_iter=15000)

print(theta1)
# Output:
# array([[1.40709365],
# [1.1150909 ]])

# Example 1:
res = predict(x, theta1)
print(res)
# Output:

# array([[15.3408728 ],
# [25.38243697],
# [36.59126492],
# [55.95130097],
# [65.53471499]])