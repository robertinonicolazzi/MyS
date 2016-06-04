from parcialVariables import normalMejorada
from random import random, randint
from math import sqrt, log, exp

def ejer3Ext(n = 100):
	# sumador para los n (min {n : Sn^i > 1})
	countGeneral = 0

	for _ in xrange(n):
		# contador para U (queremos saber n tal que sn < 1).    Inicialmente 2
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

def montecarlo(n):
	# Para sumar los valores de g(xi)
	sumExp = 0
	# Numero de muestras
	for _ in xrange(n):
		# Simular variable unfirme
		X = random()

		sumExp += exp(-X/float(2))

	return sumExp / float(n)


def algoritmoProporcion(n=100,p):
    P = p
    for i in xrange(2, n+1):
        X = p
        P = P + (X-P)/float(i)
    j = 100
    datos = 0

    while float(sqrt(P*(1-P)/float(j))) > 0.001:
        j += 1
        X = p
        P = P + (X-P)/float(j)

    return P

def algoritmo(n,p):
    M = p
    S2 = 0
    for i in xrange(2, n+1):
        X = p
        Manterior= M
        M = M + (X - M)/float(i)
        S2 = (1 - 1/float(i-1))*S2 + i*((M-Manterior)**2)
    j = 100
    datos = 0

    while float(sqrt(S2)/j) > 0.001:
        j += 1
        datos += 1
        X = p
        Manterior = M
        M = M + (X - M)/float(j)
        S2 = (1 - 1/float(j-1))*S2 + j*((M-Manterior)**2)
    return M

def ejercicio1():
    print(algoritmo(100,normalMejorada))

def ejercicio2():
    print(algoritmo(100,montecarlo(10)))

def ejer3():

    N = ejer3Ext()
    # generar v.a. normal N
    S2, M = 0, N

    for i in xrange(2, 1001):
        N = ejer3Ext()
        A = M
        M = M + (N - M) / i
        S2 = (1 - 1 / float(i - 1)) * S2 + i * (M - A)**2

    S = sqrt(S2)
    IC = (M - 1.96 * (S / sqrt(1000)), M + 1.96 * (S / sqrt(1000)))

    return M, S2, IC

def ejer4Ext(ns=100):
    count = 0
    for _ in xrange(ns):
        anterior = random()
        x = random()
        n = 1
        while anterior <= x:
            anterior = x
            x = random()
            n += 1
        n +=1
        count +=n
    return float(count) / ns


def ejer4():

    N = ejer4Ext()
    print (N)
    # generar v.a. normal N
    S2, M = 0, N

    for i in xrange(2, 1001):
        N = ejer4Ext()
        A = M
        M = M + (N - M) / i
        S2 = (1 - 1 / float(i - 1)) * S2 + i * (M - A)**2

    S = sqrt(S2)
    IC = (M - 1.96 * (S / sqrt(1000)), M + 1.96 * (S / sqrt(1000)))

    return M, S2, IC

def estPi():
    U = random()
    V = random()

    X = 2 * U - 1
    Y = 2 * V - 1

    PI = 0
    if X**2 + Y**2 <= 1:
        PI = 1

    return float(4 * PI)

def ejer5():
    N = estPi()
    # generar v.a. normal N
    S2, M = 0, N

    for i in xrange(2, 30):
        N = estPi()
        A = M
        M = M + (N - M) / i
        S2 = (1 - 1 / float(i - 1)) * S2 + i * (M - A)**2

    IC = (0, 1)
    j = 30
    while IC[1] - IC[0] > 0.1: # corregirlo con la formula.
        j += 1
        N = estPi()
        A = M
        M = M + (N - M) / j
        S2 = (1 - 1 / float(j - 1)) * S2 + j * (M - A)**2
        S = sqrt(S2)
        IC = (M - 1.96 * S / sqrt(j), M + 1.96 * S / sqrt(j))

    return M, S, IC, j

def ejer6ex(muestra, B, n, a = -5, b = 5):

    exitos = 0

    mediaMuestralEmpirica = sum(muestra) / float (n)

    for _ in xrange(B):

        suma = 0
        for _ in xrange(n):
            suma += muestra[randint(0, 9)]

        media = suma / float(n)
        valor = media - mediaMuestralEmpirica

        if valor > a and valor < b:
            exitos += 1

    return exitos / float(B)

def ejer6():
    muestra = [56, 101, 78, 67, 93, 87, 64, 72, 80, 69]
    p = ejer6ex(muestra, 100000, len(muestra), a = -5, b = 5)

    return p

print ejer6()
