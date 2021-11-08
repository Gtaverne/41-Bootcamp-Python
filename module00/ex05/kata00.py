t = (19, 42, 21, 184 ,31, 68,4, 351)

print("The", len(t), "numbers are:", end = " ")
for x in t[0:-1:]:
    print (x, end=", ")
if (len(t) != 0):
    print(t[-1])
else:
    print("none. It's an empty tuple")
