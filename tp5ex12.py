n = int(input('please enter a number to check if it is perfect '))
def perfect(n):
	s = 0
	for i in range(1,(n//2)+1):
		if n%i == 0:
			s += i
	return s == n
print('is ',n,' perfect ? ',perfect(n))
