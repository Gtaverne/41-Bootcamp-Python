from ai42 import log
from ai42 import loopfunc

import time



@log
def test(tp = 1):
	time.sleep(tp)
	print (tp)


test()
test(4)

loopfunc(time.sleep, 0.01, cycles = 200)