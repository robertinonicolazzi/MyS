from random import random, shuffle
from math import log, exp
from parcialVariables import varianzaEsperanza, poisson

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
ejercicio 1
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def esperanza(n):
	#Utilizamos la ley de grandes numeros para aproximar

	Exito = 0
	cartas = range(1,101)
	shuffle(cartas)
	for _ in xrange(n):

		permutar(cartas) #mezclar las cartas

		Exito += sum([cartas[i-1] == i for i in xrange(1,101)])
	return float(Exito)/n

def varianza(n):
	suma1=0
	suma2=0
	for _ in xrange(n):
		cartas = range(1,101)
		shuffle(cartas) #mezclar las cartas

		Exito += sum([cartas[i-1] == i for i in xrange(1,101)])

		suma1 += Exito
		suma2 += Exito**2

	varianza = suma2/float(n) - (suma1/float(n))**2

	return varianza

def permutar(cartas):
	k = len(cartas)-1
	while(k>1):
		U = random()
		I = int(math.floor(k*U))
		cartas[k],cartas[I] = cartas[I], cartas[k]
		k = k - 1

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
ejercicio 2
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def ejer2(n = 100):
	# constante N
	N = 10000
	# para sumar los a(Xi)
	A = 0.0
	for _ in xrange(n):
		# simulo U en (0,1)
		U = random()
		# simulo variable aleatorea en (1, 100)
		X = int(U * N) + 1
		# para guardar los a(X)
		A += N * exp(X / float(N))

	return A / float(n)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
ejercicio 3
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def ejer3ex():
	numLanza = 0
	# lista temporal para numeros del 2 al 12
	listTmp = range(2, 13)
	while listTmp:
		# Hacemos un lanzamiento
		numLanza += 1
		# simulamos variables uniformes U1 y U2 ~ U(0, 1)
		U1 = random()
		U2 = random()
		# simulamos dados D1 y D2 ~ U(1, 6)
		D1 = int(U1 * 6) + 1
		D2 = int(U2 * 6) + 1
		# Ver el resultado de la suma de dados
		result = D1 + D2

		if result in listTmp:
			listTmp.remove(result)

	return numLanza

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
ejercicio 4 - inversa y geometrica
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def ejer4ex():
	# generar variable aleatorea U en (0, 1)
	U = random()
	if U < 0.5:

		# generamos V unif(0,1)
		V = random()
		j = 1
		# para generar X1
		P = (1 / float(2))

		while V >= P:
			j += 1
			P += 0.5**j # Es equivalente a P += 0.5**j

	else:
		# generamos V unif(0,1)
		V = random()
		j = 1

		P = (1 / float(2)) * (2 / float(3))

		while V >= P:
			j += 1
			P += (2/float(3))**j*(1 / float(2))

	return j


# otra forma de hacerlo
def ejer4ex2():
	'''
	CON GEOMETRICA
	'''
	# simular uniforme en ~(0,1)
	U = random()

	if U < 0.5:
		# generamos otra V v.a uniforme en (0,1)
		V = random()
		# X geometrica
		X = int(log(V) / log(1 / float(2))) + 1

	else:
		# generamos otra V v.a uniforme en (0,1)
		V = random()
		# X geometrica P = 1/3
		X = int(log(V) / log(2 / float(3))) + 1

	return X

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
ejercicio 5 - inversa y geometrica
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def ejer5a(lam, k):
	'''
	METODO DE TRANSFORMACION INVERSA
	'''
	# genero el denominador
	r = exp(-lam)
	denomi = r

	for j in xrange(1, k + 1):
		r = r * (lam / float(j))
		denomi += r

	# genero U~u(0,1)
	U = random()
	p = exp(-lam) / denomi
	F = p

	i = 0
	while U >= F:
		i += 1
		p *= lam / float(i)
		F += p

	return i

def ejer5b(lam, k):
	'''
	METODO DE ACEPTACION y RECHAZO
	'''
	X = poisson(lam)
	while X >= k:
		X = poisson(lam)
	return X

def ejer5c(lam, k):
	'''
	METODO DE ACEPTACION y RECHAZO
	'''
	while True:
		X = poisson(lam)
		U = random()
		if X <= k:
			break
	return X


def esperanza(n = 100):
	X = 0
	Y = 0
	for _ in xrange(n):
		X += ejer5a(1, 10)
		Y += ejer5c(1, 10)
	return X / float(n), Y / float(n)

print (esperanza(1000))