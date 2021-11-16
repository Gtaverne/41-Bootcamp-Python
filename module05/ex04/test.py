import numpy as np
from tools import add_intercept


x = np.arange(1,12)
res = add_intercept(x)
print(res)


x1 = np.arange(0,100).reshape(20,5)
res = add_intercept(x1)
print(res)