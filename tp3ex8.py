import numpy as np
n = np.random.randint(0,100)
a = np.random.randint(0,100)
b = np.random.randint(0,100)
c = np.random.randint(0,100)
d = np.random.randint(0,100)
print('looking for ',n,', choices ',n,a,b,c,d)
ll = [n,a,b,c,d]
def rr(ll):
	n = ll[0]
	x = int(input('which number you think is true ! '))
	l = [abs(ll[1]-n),abs(ll[2]-n),abs(ll[3]-n),abs(ll[4]-n)]
	l.sort()
	if x in ll:
		if x == n:
			print('gooood')
		elif abs(x-n) in [l[0],l[1]]:
			print('so cloooose, try again ')
			return rr(ll)
		else:
			print('faaar, try again ')
			return rr(ll)
	else:
		print('no number such ',x,' in choices, try again please with available choice ')
		return rr(ll)
rr(ll)