a = int(input("pour l'equation ax²+bx+c=0 entrer la valeur de a "))
b = int(input("pour l'equation ax²+bx+c=0 entrer la valeur de b "))
c = int(input("pour l'equation ax²+bx+c=0 entrer la valeur de c "))
of = open('equation.txt', 'a')
if a!=0:
	delta = (b**2)-4*a*c
	if delta > 0:
		x1 = (-b - delta**(1/2))/2*a
		x2 = (-b + delta**(1/2))/2*a
		print('les deux solutions de '+str(a)+'x²+'+str(b)+'x+'+str(c)+'= 0 dans R sont:',x1,x2,'pour delta =',delta)
		of.write('les deux solutions de '+str(a)+'x²+'+str(b)+'x+'+str(c)+'= 0 dans R sont: '+str(x1)+' '+str(x2)+' pour delta = '+str(delta)+'\n')
	elif delta == 0:
		x = -b/2*a
		print('la seule solution de '+str(a)+'x²+'+str(b)+'x+'+str(c)+'= 0 est:',x,'pour delta =',delta)
		of.write('la seule solution de '+str(a)+'x²+'+str(b)+'x+'+str(c)+'= 0 est :'+str(x)+' pour delta = '+str(delta)+'\n')
	else:
		print('pas de solutions de '+str(a)+'x²+'+str(b)+'x+'+str(c)+'= 0 dans R, pour delta =',delta)
		of.write('pas de solutions de '+str(a)+'x²+'+str(b)+'x+'+str(c)+'= 0 dans R, pour delta = '+str(delta)+'\n')
else:
	if b!=0:
		print('la solution de '+str(a)+'x²+'+str(b)+'x+'+str(c)+'= 0 est:',-c/b)
		of.write('la solution de '+str(a)+'x²+'+str(b)+'x+'+str(c)+'= 0 est: '+str(-c/b)+'\n')
	else:
		print('tous les elements de R sont des solutions de '+str(a)+'x²+'+str(b)+'x+'+str(c)+'= 0')
		of.write('tous les elements de R sont des solutions de '+str(a)+'x²+'+str(b)+'x+'+str(c)+'= 0'+'\n')
of.close()



