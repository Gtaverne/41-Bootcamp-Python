from NumPyCreator import NumPyCreator


npc = NumPyCreator()

a = npc.from_list([[1, 2,3],[6,3,4]])

print(a)

b = npc.from_tuple(("a", "b", "c"))
print (b)

c =npc.from_iterable(range(5))
print(c)

shape = (3, 5)
d = npc.from_shape(shape)
print(d)

e = npc.random(shape)
print(e)

f = npc.identity(4)
print (f)
print( 42 * f)