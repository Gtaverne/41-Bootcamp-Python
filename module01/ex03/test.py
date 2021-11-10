from matrix import Matrix

a = Matrix([0,1,2,3], [4,5,6,7], [8,9,10,11])
b = Matrix([10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120])

print("Wrongmat:")
wrongmat = Matrix([0,1,2,3], [4,5,6,7], [8,9,10,11, 12])


vecmat = Matrix([0], [5], [10])

print ("a: ", a, "\n")
print ("a.lines: ", a.lines, "\n")
print ("b: ", b, "\n")
print ("vecmat", vecmat, "lines: ", vecmat.lines, "columns: ", vecmat.columns, "\n")
print("a + a", a+a, "\n")
print("a + 7", a+7, "\n")
print("7 + a", 7 + a, "\n")
print("vecmat + vecmat", vecmat + vecmat, "\n")

print("a - a", a-a, "\n")
print("a - 7", a-7, "\n")
print("7 - a", 7 - a, "\n")
print("vecmat - vecmat", vecmat - vecmat, "\n")

print("a / a", a/a, "\n")
print("a / 5", a/5, "\n")
print("7 / a", 7 / a, "\n")
print("vecmat / vecmat", vecmat / vecmat, "\n")