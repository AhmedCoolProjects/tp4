l1 = list(map(str, input('please enter the first list ').split()))
l2 = list(map(str, input('please enter the second list ').split()))
def commun(l1,l2):
	for x in l1:
		if x in l2:
			return True
	return False
print(commun(l1,l2))
