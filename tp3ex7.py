import string as st

s = str(input('please enter a sentence lowercase that you want to crypte '))
s = s.lower()
s = list(s)
index = 0
alph = list(st.ascii_lowercase)
for i in range(0,len(s)):
	if s[i] in alph:
		index = alph.index(s[i])+1
		if index >= len(alph):
			index = 0
			s[i] = alph[index]
		else:
			s[i] = alph[index]
h = ''.join(s)
print(h)