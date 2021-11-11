from TinyStatistician import TinyStatistician
import random

lst = random.sample(range(101), 101)
lbis = [0, 1, 2, 10, 1000]
lter = [4, 5, 5, 6]


# print (lst)

# print("Mean")
# print(TinyStatistician.mean(lst))
# print(TinyStatistician.mean(lbis))
# print(TinyStatistician.mean(lter))

# print()
# print("median")
# print(TinyStatistician.median(lst))
# print(TinyStatistician.median(lbis))
# print(TinyStatistician.median(lter))

# print()
# print("quartile", 1 )
# print(TinyStatistician.quartiles(lst, 1))
# print(TinyStatistician.quartiles(lbis, 1))
# print(TinyStatistician.quartiles(lter, 1))
# print("quartile", 3 )
# print(TinyStatistician.quartiles(lst, 3))
# print(TinyStatistician.quartiles(lbis, 3))
# print(TinyStatistician.quartiles(lter, 3))

# print()
# print("var")
# print(TinyStatistician.var(lst))
# print(TinyStatistician.var(lbis))
# print(TinyStatistician.var(lter))

# print()
# print("std")
# print(TinyStatistician.std(lst))
# print(TinyStatistician.std(lbis))
# print(TinyStatistician.std(lter))


print("From the subject")
tstat = TinyStatistician()
a = [1, 42, 300, 10, 59]
tstat.mean(a)
tstat.median(a)
tstat.quartile(a, 25)
tstat.quartile(a, 75)
tstat.var(a)
tstat.std(a)
