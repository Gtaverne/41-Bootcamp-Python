from vector import Vector

a = Vector([0,1,2,3])
b = Vector([0,1,2,3,4])

print("a >> ", a)
print("a + a >> ",a + a)
print ("a + 3 >> ", a + 3)
print ("3 + a >> ", 3 + a)
print("a + b >> ",a + b)


print("a - a >> ",a - a)
print ("a - 3 >> ", a - 3)
print ("3 - a >> ", 3 - a)
print("a - b >> ",a - b)

print("a / a >> ",a / a)
print ("a / 3 >> ", a / 3)
print ("a / 0 >> ", a / 0)
print ("3 / a >> ", 3 / a)
print("a / b >> ",a / b)

print("a * a >> ",a * a)
print ("a * 3 >> ", a * 3)
print ("a * 0 >> ", a * 0)
print ("3 * a >> ", 3 * a)
print("a * b >> ",a * b)

print("repr(b) >> ", repr(b))