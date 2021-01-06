l = list(map(str, input('please enter a list ').split()))
def mini(l):
	r = []
	for x in l:
		if x not in r:
			r.append(x)
	return r
print(mini(l))

	