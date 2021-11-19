
import numpy as np

def add_polynomial_features(x, power):
	vandermonde = np.ones((x.size, 1))
	if x.ndim == 1:
		tmp = x.reshape(x.size, 1)
	else:
		tmp = x
	for i in range(power):
		vandermonde = np.concatenate((vandermonde, tmp), axis = 1)
		tmp = tmp * x
	return vandermonde

