l = list(map(str, input('please enter a sentence ').split()))
n = int(input('please enter the size of words you want to collect '))
def coll(l,n):
	l2 = []
	for x in l:
		if len(x)>= n:
			l2.append(x)
	return l2
print(coll(l,n))