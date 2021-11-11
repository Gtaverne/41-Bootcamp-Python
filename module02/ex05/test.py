from TinyStatistician import TinyStatistician
import random

lst = random.sample(range(101), 101)
lbis = [0, 1, 2, 10, 1000]
lter = [4, 5, 5, 6]

tstat = TinyStatistician()

print (lst)

("Mean")
tstat.mean(lst)
tstat.mean(lbis)
tstat.mean(lter)

print()
("median")
tstat.median(lst)
tstat.median(lbis)
tstat.median(lter)

print()
("quartile", 1 )
tstat.quartile(lst, 1)
tstat.quartile(lbis, 1)
tstat.quartile(lter, 1)
print("quartile", 3 )
tstat.quartile(lst, 3)
tstat.quartile(lbis, 3)
tstat.quartile(lter, 3)

print()
("var")
tstat.var(lst)
tstat.var(lbis)
tstat.var(lter)

print()
("std")
tstat.std(lst)
tstat.std(lbis)
tstat.std(lter)


print("From the subject")
a = [1, 42, 300, 10, 59]
tstat.mean(a)
tstat.median(a)
tstat.quartile(a, 25)
tstat.quartile(a, 75)
tstat.var(a)
tstat.std(a)
