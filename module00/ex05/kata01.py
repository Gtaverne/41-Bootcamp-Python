languages = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

if (len(languages) != 0):
	for x in languages:
		print (x, "was created by", languages[x])