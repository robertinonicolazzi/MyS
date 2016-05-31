from variables import normalMejorada
from random import random
from math import sqrt, log, exp

def ej4(n = 100):
	# sumador para los n (min {n : Sn^i > 1})
	countGeneral = 0

	for _ in xrange(n):
		# contador para U (queremos saber n tal que sn < 1). Inicialmente 2
		countU = 2
		# simula Sn
		S = random() + random()

		while S <= 1:
			S += random()
			countU += 1

		countGeneral += countU

	return float(countGeneral) / n

def calculaProm(lista):
    return sum(lista)/float(len(lista))

def montecarloEj2(n):
	# Para sumar los valores de g(xi)
	sumExp = 0
	# Numero de muestras
	for _ in xrange(n):
		# Simular variable unfirme
		X = random()

		sumExp += exp(X**2)

	return sumExp / float(n)


def espepranza(n):
    suma = 0
    for _ in xrange(n):
        suma += ejercicio1(30)
    return suma/float(n)

def algoritmo(n,g,p):
    M = g(p)
    S2 = 0
    for i in xrange(n-1):
        X = g(p)
        Manterior= M
        M = M + (X - M)/float(i+2)
        S2 = (1 - 1/float(i+2-1))*S2 + (i+2)*((M-Manterior)**2)
    j = n
    datos = 0

    while float(sqrt(S2/float(j))) > 0.01:
        j += 1
        datos += 1
        X = g(p)
        Manterior = M
        M = M + (X - M)/float(j)
        S2 = (1 - 1/float(j-1))*S2 + j*((M-Manterior)**2)
    return datos, sqrt(S2), M

def ejercicio1():
    print(algoritmo(100,normalMejorada))

def ejercicio2():
    print(algoritmo(100,montecarloEj2,10))

ejercicio2()


