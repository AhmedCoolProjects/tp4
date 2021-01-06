print('password : 0321')
p = str(input('enter the password please '))
c = '0321'
if p != c:
	p = str(input('wrong password for the first time, enter the password please '))
	if p != c:
		p = str(input('wrong password for the second time, enter the password please '))
		if p != c:
			print('wrong password for the third time. Sorry, Carte bancaire retenue ')
		else:
			print('correct password ')
	else:
		print('correct password ')
else:
	print('correct password ')
