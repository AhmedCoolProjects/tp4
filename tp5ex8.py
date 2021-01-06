l1 = list(map(str, input('please enter the first list ').split()))
l2 = list(map(str, input('please enter the second list you want to add ').split()))
def rep(l1,l2):
	l1.pop()
	l1.extend(l2)
	return l1
print(rep(l1,l2))