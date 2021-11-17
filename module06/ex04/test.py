

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from my_linear_regression import MyLinearRegression as MyLR


data = pd.read_csv("are_blue_pills_magics.csv")
Xpill = np.array(data["Micrograms"]).reshape(-1,1)
Yscore = np.array(data["Score"]).reshape(-1,1)

# Example 1:
linear_model1 = MyLR(np.array([[89.0], [-8]]))
Y_model1 = linear_model1.predict_(Xpill)
print(linear_model1.loss_(Yscore, Y_model1))
print(mean_squared_error(Yscore, Y_model1))
# Output:
# 57.60304285714282
# 57.60304285714282
linear_model1.plot(Xpill,Yscore)
linear_model1.lossplot(Xpill, Yscore)


# Example 2:
linear_model2 = MyLR(np.array([[89.0], [-6]]))
Y_model2 = linear_model2.predict_(Xpill)
print(linear_model2.loss_(Yscore, Y_model2))
print(mean_squared_error(Yscore, Y_model2))
# Output:
# 232.16344285714285
# 232.16344285714285
#linear_model2.plot(Xpill,Yscore)
linear_model2.plot(Xpill,Yscore)
linear_model2.lossplot(Xpill, Yscore)
