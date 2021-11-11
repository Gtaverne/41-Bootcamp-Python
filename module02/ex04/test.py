from ai42 import log

import time



@log
def test(tp = 1):
	time.sleep(tp)
	print (tp)


test()
test(4)
