
from polynomial_model import add_polynomial_features
from My_Linear_Regression import MyLinearRegression as MyLR
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(1,11).reshape(-1,1)
y = np.array([[ 1.39270298],
[ 3.88237651],
[ 4.37726357],
[ 4.63389049],
[ 7.79814439],
[ 6.41717461],
[ 8.63429886],
[ 8.19939795],
[10.37567392],
[10.68238222]])
plt.scatter(x,y)
plt.show()

# Build the model:
DIM = 5
x_ = add_polynomial_features(x, DIM)
print(x_)
my_lr = MyLR(np.zeros(DIM + 1).reshape(-1,1))
my_lr.fit_(x_, y)
print("We fit")
# Plot:
## To get a smooth curve, we need a lot of data points
continuous_x = np.arange(1,10.01, 0.001).reshape(-1,1)
continuous_x_cont = add_polynomial_features(continuous_x, DIM)
print("Shape of the _x quasicontinuous:", continuous_x_cont.shape)
y_hat = my_lr.predict_(continuous_x_cont)
plt.scatter(x, y)
plt.plot(continuous_x, y_hat, color="orange")
plt.show()