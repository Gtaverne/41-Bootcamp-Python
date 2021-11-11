class Evaluator():
	def zip_evaluate(coefs, words):
		if len(coefs) == len(words):
			return sum([len(w) * c for w, c in zip(words, coefs)])
		else:
			return -1


	def enumerate_evaluate(coefs, words):
		if len(coefs) == len(words):
			s = 0
			for cf, wrd in enumerate(words):
				s += coefs[cf] * len(wrd)
			return s
		else:
			return -1