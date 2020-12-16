original_file = str(input('please enter the name of the original file : ')) #file.txt
of = open(original_file, 'r')
text = of.readlines()
of.close()
new_file = str(input('please enter the new file name without extention : '))
nf = open(new_file+'.txt', 'w')
for i in text:
	if i[0] != '#':
		nf.write(i)
nf.close()