weight = float(input('enter your weight in Kg '))
height = float(input('enter your height by m '))
IMC = weight/(height**2)
p = 'j'
if IMC < 18.5:
	p = 'Malnutrition' 
elif IMC< 25 and IMC >= 18.5 :
	p = 'Poids ideal'
elif IMC< 30 and IMC >= 25:
	p = 'Embonpoint'
elif IMC>= 30:
	p = 'Obesite'
print('your IMC is :', IMC)
print(p)
