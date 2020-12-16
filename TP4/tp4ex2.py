file_name = str(input('Enter the file name you want to create : '))
f = open(file_name+'.txt', 'w')
for p in range(1,13):
	f.write('*'*4+' '+str(p)+' '+'*'*4+'\n')
	for i in range(0,11):
		x = i*p
		content = str(p)+' x '+str(i)+' = '+ str(x)
		f.write(content+'\n')
f.close()