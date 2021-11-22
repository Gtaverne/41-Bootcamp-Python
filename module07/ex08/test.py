import numpy as np
from My_Linear_Regression import MyLinearRegression as MyLR
from polynomial_model import add_polynomial_features
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("are_blue_pills_magics.csv")
X = np.array(data[["Micrograms"]])
Y = np.array(data[["Score"]])

plt.scatter(X,Y)

theta1 = np.array([-20, 160]).reshape(-1,1)
theta2 = np.array([-20, 160, -80]).reshape(-1,1)
theta3 = np.array([-20, 160, -80, 10]).reshape(-1,1)
theta4 = np.array([-20, 160, -80, 10, -1]).reshape(-1,1)
theta5 = np.array([1140, -1850, 1110, -305, 40, -2]).reshape(-1,1)
theta6 = np.array([9110, -18015, 13400, -4935, 966, -96.4, 3.86]).reshape(-1,1)

thetarray = [theta1, theta2, theta3, theta4, theta5, theta6]

continuous_x = np.arange(1,7.01, 0.001).reshape(-1,1)

for i in range (6):
	print("Training model: theta", i + 1)
	x_= add_polynomial_features(X, i+1)
	my_lr = MyLR(thetarray[i])
	my_lr.fit_(x_, Y)
	continuous_x_cont = add_polynomial_features(continuous_x, i+1)
	y_hat = my_lr.predict_(continuous_x_cont)
	plt.plot(continuous_x, y_hat, color="orange")


#Behold the bad overfitting
plt.show()
