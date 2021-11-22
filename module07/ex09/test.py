from data_splitter import data_spliter
import numpy as np


x = np.arange(15)
y = 1001 *x
x = x.reshape((-1,1))
x = np.concatenate((x, -x), axis = 1)
print(x)
print (y)

res = data_spliter(x, y, 0.8)
print(res)