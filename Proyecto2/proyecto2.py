# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division

import te2_pagerank as te
import random as random
import numpy as np
import scipy.stats as st

"""
def elegirVecino(transicion,nodo,vecinos):
    u = random.random()
    suma = 0
    result = 0
    for i in vecinos:
        suma += transicion[nodo][i]
        if u < suma:
            result = i
            break
    return result
"""
def elegirVecino(transicion,nodo,vecinos):
	U = random.random()

	i = 0
	S = transicion[nodo][i]
	while U >= S:
		i += 1
		S += transicion[nodo][i]

	return i

def randomWalk(g):
    mTransicion = te.g2p(g)
    N = len(g)
    nodo = random.randint(0,N-1)
    for _ in xrange(100):
        vecino = elegirVecino(mTransicion,nodo,g[nodo])
        nodo = vecino
    return nodo

def randomWalk2(g):
    mTransicion = te.g2p_pagerank(g,0.85)
    N = len(g)
    nodo = random.randint(0,N-1)
    for _ in xrange(100):
        vecino = elegirVecino(mTransicion,nodo,g[nodo])
        nodo = vecino
    return nodo

def potencias(g,mTransicion):
    N = len(g)
    dist = np.ones(N)
    for _ in xrange(100):
        dist = te.power_iter_one_step(dist,mTransicion)
    return [round(i,3) for i in dist]



def simular(g):
    lista = []
    nodos = []
    for _ in xrange(1000):
        lista.append(randomWalk(g))
    for i in xrange(len(g)):
        nodos.append(lista.count(i)/float(1000))

    return nodos

def simular2(g):
    lista = []
    nodos = []
    for _ in xrange(1000):
        lista.append(randomWalk2(g))
    for i in xrange(len(g)):
        nodos.append(lista.count(i)/float(1000))

    return nodos





"""
EJERCICIO 3
"""

def tiempoCubrimiento(g,mTransicion):
    N = len(g)
    nodo = random.randint(0,N-1)
    visitados = [nodo]
    pasos = 0
    while True:
        nodo = elegirVecino(mTransicion,nodo,g[nodo])
        pasos += 1
        if not nodo in visitados:
        	visitados.append(nodo)
        if len(visitados) == N:
        	return pasos

def ej3(g,mTransicion,simulaciones):
	ls = []

	for _ in xrange(simulaciones):
		ls.append(tiempoCubrimiento(g,mTransicion))
	return sum(ls)/float(simulaciones)

def ejer3(g, n, alpha):
	mTransicion = te.g2p_pagerank(g, alpha)
	N = len(g)

	tiempo = 0
	for _ in xrange(n):
		nodos = [i for i in xrange(N)]
		nodo = random.randint(0, N - 1)

		while len(nodos) != 0:
			if nodo in nodos:
				nodos.remove(nodo)
			nodo = elegirVecino(mTransicion,nodo,g[nodo])
			tiempo += 1

	return tiempo / float(n)

"""
print(ej3(te.G1,te.g2p_pagerank(te.G1,0.99),1000))
print(ej3(te.G2,te.g2p_pagerank(te.G2,0.99),100))

print(ej3(te.G1,te.g2p_pagerank(te.G1,0.85),1000))
print(ej3(te.G2,te.g2p_pagerank(te.G2,0.85),100))

print(ej3(te.G1,te.g2p_pagerank(te.G1,0.50),1000))
print(ej3(te.G2,te.g2p_pagerank(te.G2,0.50),100))

print(ej3(te.G1,te.g2p_pagerank(te.G1,0.10),1000))
print(ej3(te.G2,te.g2p_pagerank(te.G2,0.10),100))

print(ej3(te.G1,te.g2p_pagerank(te.G1,0.0005),1000))
print(ej3(te.G2,te.g2p_pagerank(te.G2,0.0005),100))
"""

"""
ejercicio 5
"""
def ej5a(K):
	G2a = list(te.G2)
	G2a.append(())
	for _ in xrange(K):
		G2a.append((100,))

	G2a = tuple(G2a)
	a = simular2(G2a)

	print (a[100])

def ej5b(K):
	G2a = list(te.G2)
	n = len(G2a)
	G2a.append(())
	print (len(G2a))
	agregados=[]
	deck = list(range(0, 100))
	for _ in xrange(K):
		
		random.shuffle(deck)
		G2a[deck[0]] += (100,)
		deck.pop()


	G2a = tuple(G2a)
	a = simular2(G2a)

	print (a[100])



#################################EJERCICIO 2###############################################

def tiempo_cruce(g, nodo, visitas, mt):

    aux = visitas
    vecino = nodo
    pasos = 0

    while 0 < aux:
            vecino = elegirVecino(mt, vecino, g[vecino])
            pasos += 1

            if vecino == nodo:
                aux -= 1

    return (pasos/float(visitas))

def simulacion_tc(g, visitas, mt):
    tiempos_cruces = []

    for i in xrange(len(g)):
        tiempos_cruces.append(float(tiempo_cruce(g, i, visitas, mt)))

    return (tiempos_cruces,sum(tiempos_cruces)/float(len(tiempos_cruces)))
"""
print("G1 comun",(simular(te.G1)))
print("G1 pr",(simular2(te.G1)))
print("G1 potencia comun",(potencias(te.G1,te.g2p(te.G1))))
print("G1 potencia pr",(potencias(te.G1,te.g2p_pagerank(te.G1,0.85))))


print("tiempo cruce, los pg con 0.85 G1 / G1 PR / G2 / G2 pr")
print (simulacion_tc(te.G1, 1000, te.g2p(te.G1)), "original")
print (simulacion_tc(te.G1, 1000, te.g2p_pagerank(te.G1, 0.85)), "pagerank")
print (simulacion_tc(te.G2, 100, te.g2p(te.G2)), "original2")
print (simulacion_tc(te.G2, 100, te.g2p_pagerank(te.G2, 0.85)), "pagerank2")

print("G1 y G2 con pagerank 0.85 cubrimiento")
print(ej3(te.G1,te.g2p_pagerank(te.G1,0.85),1000))
print(ej3(te.G2,te.g2p_pagerank(te.G2,0.85),100))


print("prob de S con G2 page rank 0.85 K=75")
ej5a(75)

ej5b(75)
"""
def asd():
	lst = []
	for _ in xrange(10):
		
		a = te.randg(30)
		lst.append(ej3(a,te.g2p_pagerank(a,0.85),100))
	print(sum(lst)/float(10))

asd()