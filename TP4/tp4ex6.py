original_file = str(input('please enter the name of the original file : ')) #file.txt
of = open(original_file, 'r')
text = of.readlines()
of.close()
nf = open('lignes_paires_'+original_file, 'w')
for i in text:
	if (text.index(i)+1)%2 ==0 :
		nf.write(i)
nf.close()