from copy import deepcopy
from math import sqrt

class TinyStatistician ():
	def __init__(self):
		pass

	def mean(self, a, nostfu = 1):
		l = len(a)
		if l == 0:
			return
		sm = sum(a)
		if nostfu:
			print(sm/l)
		return sm / l

	def median(self, a):
		l = len(a)
		if l == 0:
			return
		srt = deepcopy(a)
		srt.sort()
		if l%2 == 0:
			print((srt[ int(l / 2 - 1)] + srt[ int(l / 2)]) /2)
			return (srt[ int(l / 2 - 1)] + srt[ int(l / 2)]) /2
		else:
			print(srt[int((l - 1) /2 )])
			return (srt[int((l - 1) /2 )])

	def quartile(self, a, percentile):
		l = len(a)
		if l == 0:
			return
		if percentile == 25 or percentile == 1:
			srt = deepcopy(a)
			srt.sort()
			print(srt[int((l - 1) /4)])
			return srt[int((l - 1) /4)]
		if percentile == 75 or percentile == 3:
			srt = deepcopy(a)
			srt.sort()
			print(srt[int((l - 1) *3 /4)])
			return srt[int((l - 1) *3 /4)]
		return None

	def var(self, a, nostfu = 1):
		l = len(a)
		if l == 0:
			return
		res = 0
		for x in a:
			res += (x - TinyStatistician.mean(self, a,nostfu= 0)) * (x - TinyStatistician.mean(self, a, nostfu=0)) / l
		#res = sum([(x - self.mean(a)) * (x - self.mean(a)) / l for x in a])
		if nostfu:
			print(res)
		return res

	def std(self, a):
		l = len(a)
		if l == 0:
			return
		res = sqrt(TinyStatistician.var(self, a, nostfu = 0))
		print (res)
		return (res)

