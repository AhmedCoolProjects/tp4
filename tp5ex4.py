l = list(map(str, input('please enter a list of strings ').split()))
def remo(l):
	for x in l:
		while l.count(x)>1:
			l.remove(x)
	return l
print(remo(l))
