a = int(input("pour l'equation ax²+bx+c=0 entrer la valeur de a"))
b = int(input("pour l'equation ax²+bx+c=0 entrer la valeur de b"))
c = int(input("pour l'equation ax²+bx+c=0 entrer la valeur de c"))
delta = 0
if a!=0:
	delta = (b**2)-4*a*c
	if delta > 0:
		x1 = (-b - delta**(1/2))/2*a
		x2 = (-b + delta**(1/2))/2*a
		print('les deux solutions dans R sont:' )
		print(x1, x2)
		print('delta :')
		print(delta)
	elif delta == 0:
		x = -b/2*a
		print('la seule solution est:' )
		print(x)
		print('delta :')
		print(delta)
	else:
		print('pas de solutions dans R')
else:
	if b!=0:
		print('la solution est:')
		print(-c/b)
	else:
		print('tous les elements de R sont des solutions')



