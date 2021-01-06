l = list(map(str, input('please enter a sentence ').split()))
def palindrome(l):
	r = []
	for x in l:
		for i in x:
			r.append(i)
	r2 = r[::-1]
	#r2 = list(reversed(r))
	return r == r2
print('is ',''.join(str(e) for e in l),' palindrome ? ',palindrome(l))