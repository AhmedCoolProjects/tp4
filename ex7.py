y = int(input('please enter the year '))
if y%4 == 0 and y%100 == 0:
	if y%400 == 0:
		print('this year is bissextile')
	else :
		print('this year is not bissextile')
elif y%4 == 0 and y%100 != 0:
	print('this year is bissextile')
else :
	print('this year is not bissextile')