from random import random
from math import exp, log, floor
from parcialVariables import poisson, poissonExt, varianzaEsperanza, PPoissonNH


def ejer10(lamb, T):
    n = poissonExt(lamb * T)
    arrival = [random() * T for _ in xrange(n)]
    arrival.sort()

    return arrival

"""""""""""""""""
--Ejercicio 10-- 
"""""""""""""""""

def generaEventos(lamb,T):
    t = 0
    I = 0
    S = []
    while True:
        U = random()

        lamb = 1/float(lamb)
        if t - lamb*log(U) > T:
            break
        else:
            t = t -lamb*log(U)
            I += 1
            S.append(t)
    return S



"""""""""""""""""""""""""""""""""
--Lambda = 5 -----Ejercicio 11---
"""""""""""""""""""""""""""""""""
def Poisson(lamb,t):
    suma = random()
    i = 0
    # N(T)=min(n|x1,x2...,xn < e^-lambda*t) - 1
    while suma > exp(-lamb*t):
        i += 1
        suma *= random()
    # i es la cantidad de variables a generar (bondis)
    return i

def ejercicio11(T):
    n = Poisson(5,T)
    S = []
    for i in range(n):
        u = random()
        temp = u*T
        S.append(temp)
    S.sort()
    return S


print (PPoissonNH(5,1))
print("----------------")
print (ejercicio11(1))

def esperanza(n = 100):
	X = 0
	Y = 0
	Z = 0
	for _ in xrange(n):
		X += Poisson(5, 12)
		Y += poisson(5*12)
		Z += poissonExt(5*12)

	return X / float(n), Y / float(n), Z / float(n)

