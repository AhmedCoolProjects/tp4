d = {}
def ddd(d):
	n = int(input('please enter the nbr of pairs you want to add in dictionary: '))
	for i in range(n):
		k = input('enter the key please ')
		v = input('enter the value of '+str(k)+' ')
		d[k] = v 
	m = input('enter the key for checking ')
	return m in d.keys()
print(ddd(d))
