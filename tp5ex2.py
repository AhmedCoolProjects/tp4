l = list(map(int, input('please enter a list of nbrs ').split()))
def max(l):
	m = l[0]
	for x in l:
		if x > m:
			m = x
	return m
print(max(l)) 
