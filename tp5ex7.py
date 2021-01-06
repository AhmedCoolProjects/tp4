l1 = list(map(str, input('please enter the first list ').split()))
l2 = list(map(str, input('please enter the second list ').split()))
def look_for_commun(l1,l2):
	r = []
	for x in l1:
		if x in l2:
			if x not in r:
				r.append(x)
	return r
print(look_for_commun(l1,l2))