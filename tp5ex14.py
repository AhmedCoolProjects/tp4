import string as st
l = list(map(str, input('please enter a sentence ').split()))
def pangramme(l):
	r = []
	for x in l:
		for i in x:
			r.append(i.lower())
	for i in list(st.ascii_lowercase):
		if i not in r :
			return 0 == 1
	return 0 == 0
print(pangramme(l))
