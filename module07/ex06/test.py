

import pandas as pd
import numpy as np
from multivariate_linear_model import MyLinearRegression as MyLR

data = pd.read_csv("spacecraft_data.csv")
X = np.array(data[["Age"]])
Y = np.array(data[["Sell_price"]])
#print(X)
myLR_age = MyLR(theta = [[1000.0], [-1.0]], alpha = 2.5e-5, max_iter = 150000)

myLR_age.plot(X, Y)


print("Thetas (of the fit)", myLR_age.fit_(X[:,0].reshape(-1,1), Y))

print("MSE after fit", myLR_age.mse_(X[:,0].reshape(-1,1),Y))

myLR_age.plot(X, Y)



#NEW TEST
data = pd.read_csv("spacecraft_data.csv")
X = np.array(data[["Age","Thrust_power","Terameters"]])
Y = np.array(data[["Sell_price"]])
my_lreg = MyLR(theta = [1.0, 1.0, 1.0, 1.0], alpha = 1e-5, max_iter = 600000)


# Example 0:
print("raw MSE", my_lreg.mse_(X,Y))

# Output:
# 144044.877...


# Example 1:
my_lreg.fit_(X,Y)
my_lreg.thetas
# Output:
# array([[334.994...],[-22.535...],[5.857...],[-2.586...]])


# Example 2:
print("MSE after fit", my_lreg.mse_(X,Y))
# Output:
# 586.896999...