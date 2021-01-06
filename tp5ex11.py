l = list(map(int, input('please enter a list of numbers ').split()))
def pair(l):
	r = []
	for x in l:
		if x%2 == 0:
			r.append(x)
	return r
print(pair(l))