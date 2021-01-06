n = int(input('enter a number please '))
l = []
while n != 0:
	l.append(n%2)
	n = n//2
l.reverse()
bn = ''.join(str(e) for e in l)
print(bn)
