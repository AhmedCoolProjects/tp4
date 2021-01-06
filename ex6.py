import numpy as np
x = int(input('De quelle primitive voulez-vous calculer le volume ? Tapez :1 pour une sphere.2 pour un parallélépipède rectangle.3 pour un cylindre :'))
if x == 1:
	r = float(input('Entrer le rayon de la sphere '))
	print('the volume of the sphere is : ',(4/3)*np.pi*r**3)
elif x == 2:
	h = float(input('Entrer the height '))
	l = float(input('Entrer the large '))
	w = float(input('Entrer the width '))
	print('the volume of the  parallélépipède rectangle is : ',h*l*w)
elif x == 3:
	h = float(input('Entrer the height of the cylindre '))
	r = float(input('Entrer the rayon of the base '))
	print('the volume of the cylindre is : ',r*r*np.pi*h)
else:
	print('svp Tapez :1 pour une sphere.2 pour un parallélépipède rectangle.3 pour un cylindre')

