from random import random, shuffle
from math import log, exp
from parcialVariables import varianzaEsperanza, poisson

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
ejercicio 1
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def ejer1ex():
    '''
    EJERCICIO CON METODO DE LA INVERSA
    '''
    # simulo U~u(0,1)
    U = random()
    if U > 1/float(4):
        X = 6 - 6 * sqrt((1-U)/ 3.0)

    else:
        X = 2 + 2 * sqrt(U)

    return X

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
ejercicio 2 / metodo inversa
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def ejer2ex1(alpha, beta):
    '''
    EJERCICIO CON METODO 1
    '''
    # simulamos U~u(0,1)
    U = random()
    X = -log(U) / alpha

    return X**(1 / float(beta))

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
ejercicio 6
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def ejer6a(n):
    # lis of uniforms
    uniforms = [random() for _ in xrange(n)]
    return max(uniforms)

def ejer6b(n):
    # simulate a uniform
    while U >= n*(X**(n - 1)):
        U = random()
        X = random()

    X = U
    return X

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
ejercicio 7
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def ejer7a():
    # constantes
    e = exp(1)

    while True:
        # Generar V ~ exp
        Z = random()
        X = -2 * log(Z)
        # Generar U
        U = random()

        if U < (e * X * exp(-X / 2)) / 2:
            break

    return X

print (varianzaEsperanza(ejer7a,100))