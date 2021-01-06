d = {0:10,1:20}
print('the actule dictionary is ',d)
def kk(d):
	k = input('please enter the key ')
	v = input('please enter the value of '+str(k)+' ')
	d[k] = v
	print(d)
	l = input('do you want to add more pairs ? y / n : ')
	if l == 'y':
		kk(d)
	else:
		print('okay ')
kk(d)
