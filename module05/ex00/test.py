from vector import Vector


# Column vector of dimensions n * 1
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = v1 * 5
print(v1)
print(v2)

# Row vector of dimensions 1 * n
v1 = Vector([0.0, 1.0, 2.0, 3.0])
v2 = v1 * 5
print(v1)
print(v2)