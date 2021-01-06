d = {}
def dff(d):
	m = input('enter the value you want to get its first key ')
	if m in list(d.values()):
		for x in list(d.keys()):
			if d[x] == m:
				print(x)
	else:
		print("dosn't exist")
def dd(d):
	x = int(input('print 1 if you have a key, 2 for value '))
	if x == 1:
		m = str(input('enter the key you want to get its value '))
		print(d.get(m,"dosn't exist"))
	elif x == 2:
		dff(d)
def ddd(d):
	n = int(input('please enter the nbr of pairs you want to add in dictionary: '))
	for i in range(n):
		k = input('enter the key please ')
		v = input('enter the value of '+str(k)+' ')
		d[k] = v 
	dd(d)
ddd(d)