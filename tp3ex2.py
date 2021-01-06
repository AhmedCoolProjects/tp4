s = str(input('please enter a phrase '))
l = []
for i in s:
	l.append(i)
l.reverse()
phrase = ''.join(l)
print(phrase)