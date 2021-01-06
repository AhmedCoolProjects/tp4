l = list(map(str, input('please enter a sentence ').split()))
def calc(l):
	m = 0
	M = 0
	for i in l:
		for x in i:
			if x == x.upper():
				M += 1
			else:
				m += 1
	return('Majuscules ',M,',','miniscules ',m)
print(calc(l))
