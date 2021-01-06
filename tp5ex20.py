n = int(input('please enter a nbr '))
def ff(n):
	d = {}
	for i in range(1,n+1):
		d[i] = i**2
	return d
print(ff(n))
	