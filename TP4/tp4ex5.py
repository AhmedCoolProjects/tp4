original_file = str(input('please enter the name of the original file ')) #file.txt
of = open(original_file, 'r')
text = of.readlines()
of.close()
nf = open('copie_'+original_file, 'w')
for i in text:
	nf.write(str(text.index(i)+1)+'/ '+i)
nf.close()