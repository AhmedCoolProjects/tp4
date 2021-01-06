m = int(input('please enter the nbr of dictionaries you want to concatinate : '))
d = {}
def ddd(m,d):
	for x in range(m):
		n = int(input('please enter the nbr of pairs you want to add in dictionary nbr '+str(x+1)+': '))
		for i in range(n):
			k = input('enter the key please ')
			v = input('enter the value of '+str(k)+' ')
			d[k] = v 
	return d
print(ddd(m,d))