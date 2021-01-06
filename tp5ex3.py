l = list(map(str, input('please enter a list of strings ').split()))
def look(l):
	r = 0
	for x in l:
		if len(x)>= 2 and x[0]==x[-1]:
			r += 1
	return r
print(look(l))