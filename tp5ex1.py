l = list(map(float, input('please enter a list of numbers ').split()))
def addition_fct(l):
	x = 0
	for i in l:
		x += i
	return x
print(addition_fct(l))
