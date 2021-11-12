from ScrapBooker import ScrapBooker
import numpy as np

scr = ScrapBooker()
a = np.arange(20).reshape(5, 4)
print(a)

print("Crop")
b = scr.crop(a, (3, 2), (1,1))
print(b)

print("axis 0")
tmp = np.arange(20).reshape(5, 4)
print ("Start", tmp)
b = scr.thin(tmp, 3, 0)
print("End", b)

print()
print("Axis 1")
tmp = np.arange(20).reshape(5, 4)
print (tmp)
b = scr.thin(tmp, 2, 1)
print()
print(b)

print()
print("Juxtapose")
tmp = np.arange(20).reshape(5, 4)
print (tmp)
b = scr.juxtapose(tmp, 3)
print(b)

print()
print("Juxtapose vert")
tmp = np.arange(20).reshape(5, 4)
print (tmp)
print()

b = scr.juxtapose(tmp, 3, 1)
print(b)


print()
print("Mosaic vert")
tmp = np.arange(20).reshape(5, 4)
print (tmp)
print()
b = scr.mosaic(tmp, (3, 5))
print(b)