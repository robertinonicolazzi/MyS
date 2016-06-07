from math import exp, log,floor,sqrt,factorial
from random import random,randint, choice,shuffle
from parcialVariables import binomial
import numpy as nm
import scipy.stats as st
import scipy.special as ss

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def binomialProb(n,p,k):
    comb = factorial(n) / float(factorial(k)*factorial(n-k))
    return p**k *(1-p)**(n-k) * comb

def estimarEsperanza(lst):
    """calculates mean"""
    return sum(lst) /float(len(lst))

def estimarPbinomial(lst,t):
    return estimarEsperanza(lst)/float(t)

def estimarDesviacion(lst,esperanza):
    """returns the standard deviation of lst"""
    if esperanza == 0:
        mn = estimarEsperanza(lst)
    else:
        mn = esperanza
    suma = sum([(e-mn)**2 for e in lst])
    return suma/float(len(lst)-1),sqrt(suma/float(len(lst)-1))

def estimarEsperanzaDesviacionNormal(lst,esperanza):
    if esperanza == 0:
        mn = estimarEsperanza(lst)
    else:
        mn = esperanza
    suma = sum([(e-mn)**2 for e in lst])
    return mn, suma/float(len(lst)),sqrt(suma/float(len(lst)))

def estimacionesXlista(n,lista):
    M = choice(lista)
    S2 = 0
    for i in range(2,n+1):
        X = choice(lista)
        Manterior= M
        M = M + (X - M)/float(i)
        S2 = (1 - 1/float(i-1))*S2 + (i)*((M-Manterior)**2)
    j = n
    datos = 0

    while float(sqrt(S2/float(j))) > 0.01:
        j += 1
        datos += 1
        X = choice(lista)
        Manterior = M
        M = M + (X - M)/float(j)
        S2 = (1 - 1/float(j-1))*S2 + j*((M-Manterior)**2)
    return datos, sqrt(S2), M

#print(estimacionesXlista(100,[1,2,2,3,3,3,3,4,5,6,6,7,7,7,7,7,8,8]))
#print(estimarDesviacionNormal([1,2,2,3,3,3,3,4,5,6,6,7,7,7,7,7,8,8],0))
#print(estimarDesviacion([1,2,2,3,3,3,3,4,5,6,6,7,7,7,7,7,8,8],8))
#print(estimarPbinomial([1,2,2,3,3,3,3,4,5,6,6,7,7,7,7,7,8,8],8))

"""""""""""""""""""""""""""""""""""""""""""""""
Ejercicio 1 y 2, simulacion de p valor discreto
"""""""""""""""""""""""""""""""""""""""""""""""

def ejercicio2p():
    Y = randint(1,6)
    return Y

def ejercicio1p():
    #1 blanca 2 rosa 3 roja
    U=random()
    Y=0
    if U < 0.5:
        Y = 2
    elif U < 0.75:
        Y = 1
    elif U >= 0.75:
        Y = 3
    return Y

def simularPdiscreto(n,r,t,k,prob,p):
    Ylist = []
    Nlist = []
    exitos = 0
    for _ in range(r):
        for _ in range(n):
            Ylist.append(p())

        for i in range(k):
            Nlist.append(Ylist.count(i+1))
        suma = 0
        T = 0
        for i in range(k):       
            suma = ((Nlist[i] - prob[i]*n)**2)/float(prob[i]*n)
            T += suma
        Ylist = []
        Nlist = []
        if T>=t:
            exitos +=1

    return exitos/float(r)

def ejercicio1():
    n = 564
    pBlanca = 0.25
    pRosa = 0.5
    pRoja = 0.25
    prob = [pBlanca,pRosa,pRoja]

    NBlanca = 141
    NRosa = 291
    NRoja = 132
    obs = [NBlanca,NRosa,NRoja]

    npBlanca = n* pBlanca #= 141
    npRosa = n* pRosa #= 282
    npRoja = n * pRoja #= 141

    T = ((NBlanca-npBlanca)**2/float(npBlanca)) + ((NRosa-npRosa)**2/float(npRosa)) + ((NRoja-npRoja)**2/float(npRoja))
    print " simulado",(simularPdiscreto(n,1000,T,3,[0.25,0.5,0.25],ejercicio1p))
    print " chi2",1 - st.chi2.cdf(T,2)
    print " chi (python)",st.chisquare([141,291,132], f_exp=[141,282,141])
    #T es 0.86 y de resultado es 0.65



def ejercicio2():
    n = 1000
    pHonesto = 1/float(6)
    
    N1 = 158
    N2 = 172
    N3 = 164
    N4 = 181
    N5 = 160
    N6 = 165
    obs = [N1,N2,N3,N4,N5,N6]
    npHonesto = n* pHonesto #= 141
    esp = [npHonesto,npHonesto,npHonesto,npHonesto,npHonesto,npHonesto]
    T = (
    (N1-npHonesto)**2 +
    (N2-npHonesto)**2 + 
    (N3-npHonesto)**2+ 
    (N4-npHonesto)**2+ 
    (N5-npHonesto)**2+ 
    (N6-npHonesto)**2)/float(npHonesto)
    print " simulado",(simularPdiscreto(n,1000,T,6,[pHonesto,pHonesto,pHonesto,pHonesto,pHonesto,pHonesto],ejercicio2p))
    print " chi2",1 - st.chi2.cdf(T,5)
    print " chi (python)",st.chisquare(obs, f_exp=esp)
    #chi de 5 libertad de 2.18 es 0.82372


print (bcolors.OKGREEN + "---------------ejercicio1-----------------"+ bcolors.ENDC)
ejercicio1()
print (bcolors.HEADER + "---------------ejercicio2-----------------"+ bcolors.ENDC)
ejercicio2()

"""""""""""""""""""""""""""""""""""""""""""""""
Ejercicio 4, 6 , 7,,8 usan kogomolov simulacion de p valor discreto
"""""""""""""""""""""""""""""""""""""""""""""""

def acumulada(y,lamb):
    return 1 - exp(-lamb*y)


def simularP(r,n,d):
    valores = []
    valoresD = []

    exitos = 0
    for _ in range(r):
        for _ in range(n):
            valores.append(random())
        j = 1
        valores.sort()
        for U in valores:
            valoresD.append(j/float(n) - U)
            valoresD.append(U - (j-1)/float(n))
            j += 1

        D = max(valoresD)
        if D >= d:
            exitos += 1
        valores = []
        valoresD = []
    return exitos/float(r)

def ejercicio3(alfa):
    valoresD = []
    valores = [0.12,0.18,0.06,0.33,0.72,0.83,0.36,0.27,0.77,0.74]
    valores.sort()

    j = 1
    n = len(valores)
    for i in valores:
        valoresD.append(j/float(n) - st.uniform.cdf(i))
        valoresD.append(st.uniform.cdf(i) - (j-1)/float(n))
        j += 1
        
    D = max(valoresD)



    #D = d calcular p = Pf(D>=d)
    p = simularP(100,len(valores), D)
    print("D:"),D,"| p-valor:",p
    print "kstest (python)", st.kstest(valores,lambda x: st.uniform.cdf(x))
    if p < alfa :
        print("Rechaza H0")
    else:
        print("No rechaza H0")

def ejercicio4(alfa):
    valoresD = []
    valores = [86,133,75,22,11,144,78,122,8,146,33,41,99]
    valores.sort()

    j = 1
    n = len(valores)
    for i in valores:
        valoresD.append(j/float(n) - acumulada(i,0.02))
        valoresD.append(acumulada(i,0.02) - (j-1)/float(n))
        j += 1
        
    D = max(valoresD)



    #D = d calcular p = Pf(D>=d)
    p = simularP(100,len(valores), D)
    print("D:"),D,"| p-valor:",p
    print "kstest (python)", st.kstest(valores,lambda x: st.expon.cdf(x, scale=1/float(0.02)))
    if p < alfa :
        print("Rechaza H0")
    else:
        print("No rechaza H0")

print("--------------ejercicio3------------")
ejercicio3(0.5)

print("--------------ejercicio4------------")
ejercicio4(0.5)




def exponencial(lamb):
    U= random()
    return (- log(U)/float(lamb))


"""

"""
def binomial2(x, n, p):
    return factorial(n) / float (factorial(n - x) * factorial(x)) * p**x * (1-p)**(n - x)




def probabilidadBinomial(n, p, i):
    combinatorio = factorial(n)/float(factorial(i) * factorial(n-i))

    return combinatorio*(p**i)*((1 - p)**(n-i))

def tabla():
	l = [6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7]
	n = len(l) # numero de muestra
	intervalos = [[0,1,2],[3,4,5],[6,7,8]]
	pMuestra = estimarPbinomial(l, 8)
	N=[]
	for i in intervalos:
		suma = 0
		for x in l:
			suma += i.count(x)
		N.append(suma)


	binomial1 = []

	for i in xrange(0,9):
		binomial1.append(probabilidadBinomial(8,pMuestra,i))

	Np= []
	Np.append(binomial1[0]+binomial1[1]+binomial1[2])
	Np.append(binomial1[3]+binomial1[4]+binomial1[5])
	Np.append(binomial1[6]+binomial1[7]+binomial1[8])

	fexp = [18*x for x in Np]

	T = 0
	for j in xrange(len(intervalos)):
		denomi = n * Np[j]
		T += (N[j] - denomi)**2 / denomi
	return T,N,fexp



#esto funciona bien no tocar
def tabla2():
	l = [6,7,3,4,7,2,6,3,7,8,2,1,3,5,8,7]
	n = len(l) # numero de muestra
	intervalos = [[0,1,2,3],[4],[5],[6],[7,8]]
	pMuestra = estimarPbinomial(l,8)

	N=[]
	for i in intervalos:
		suma = 0
		for x in l:
			suma += i.count(x)
		N.append(suma)


	binomial1 = []
	for i in xrange(0,9):
		binomial1.append(probabilidadBinomial(8,pMuestra,i))


	Np= []
	Np.append(binomial1[0]+binomial1[1]+binomial1[2]+binomial1[3])
	Np.append(binomial1[4])
	Np.append(binomial1[5])
	Np.append(binomial1[6])
	Np.append(binomial1[7]+binomial1[8])

	T = 0
	for j in xrange(len(intervalos)):
		denomi = n * Np[j]
		T += (N[j] - denomi)**2 / float(denomi)
	return T


def ejercicio5b():
    val1 = [6,1,1,2,6]
    valores = [6,7,3,4,7,3,7,2,6,3,7,8,2,1,3,5,8,7]
    p = estimarPbinomial(valores,8)
    val2 = [st.binom.cdf(x,8,p)*18 for x in val1]
    print " chi (python)",st.chisquare(val1, f_exp=[2.37,3.49,4.5,3.62,2.01],ddof=1)
    print " chi2", 1 - st.chi2.cdf(tabla2(),3)





print("------------ejercicio5b------------")
ejercicio5b()

def ejer5ext1(r):
	'''
	k = numero de intervalos
	r = numero de iteraciones
	'''
	l = [6,7,3,4,7,3,7,2,6,3,7,8,2,1,3,5,8,7]
	l = [6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7]
	n = len(l) # numero de muestra
	t, x, y = tabla()
	intervalos = [[0,1,2],[3,4,5],[6,7,8]]
	pMuestra = estimarPbinomial(l, 8) # obtener la estimacion de la muestra
	exitos = 0
	for _ in xrange(r):
		Y = []
		for i in xrange(n):
			# generamos los Y de la F propuesta con parametro p y n = 8
			Y.append(binomial(pMuestra, 8))

		N = []
		for i in intervalos:
			suma = 0
			for x in Y:
				suma += i.count(x)
			N.append(suma)

		p = estimarPbinomial(Y, 8)

		binomial1 = []
		for i in xrange(0,9):
			binomial1.append(probabilidadBinomial(8,p,i))


		Np= []
		Np.append(binomial1[0]+binomial1[1]+binomial1[2])
		Np.append(binomial1[3]+binomial1[4]+binomial1[5])
		Np.append(binomial1[6]+binomial1[7]+binomial1[8])

		T = 0

		for j in xrange(len(intervalos)):
			denomi = n * Np[j]
			T += (N[j] - denomi)**2 / denomi

		if T >= t:
			exitos += 1

	return exitos / float(r), t

def ejercicio5():
    T,N,fexp = tabla()
    print " chi (python)",st.chisquare(N, f_exp=fexp,ddof=1)
    print " chi2", 1 - st.chi2.cdf(T,1)  
    simulado, t = ejer5ext1(10000)
    print "simulado es", simulado, t


print("------------ejercicio5------------")
ejercicio5()


def generVAbinomial(p, n):
    '''
    Generar variable aleatoria binomial con parametros p y n
    '''
    U = random()
    i = 0
    c = p/(1 - p)
    pr = (1 - p)**n
    F = pr

    while U >= F:
        pr = (c * (n - i) / (i + 1)) * pr
        F += pr
        i += 1

    return i

def ejer5ext2(r):
	'''
	k = numero de intervalos
	r = numero de iteraciones
	'''

	l = [6,7,3,4,7,2,6,3,7,8,2,1,3,5,8,7]
	n = len(l) # numero de muestra
	t = tabla2()
	intervalos = [[0,1,2,3],[4],[5],[6],[7,8]]
	pMuestra = estimarPbinomial(l, 8) # obtener la estimacion de la muestra
	exitos = 0
	for _ in xrange(r):
		Y = []
		for i in xrange(n):
			# generamos los Y de la F propuesta con parametro p y n = 8
			Y.append(generVAbinomial(pMuestra, 8))

		N = []
		for i in intervalos:
			suma = 0
			for x in Y:
				suma += i.count(x)
			N.append(suma)


		p = estimarPbinomial(Y, 8)

		binomial1 = []
		for i in xrange(0,9):
			binomial1.append(probabilidadBinomial(8,p,i))


		Np= []
		Np.append(binomial1[0]+binomial1[1]+binomial1[2]+binomial1[3])
		Np.append(binomial1[4])
		Np.append(binomial1[5])
		Np.append(binomial1[6])
		Np.append(binomial1[7]+binomial1[8])

		T = 0

		for j in xrange(len(intervalos)):
			denomi = n * Np[j]
			T += (N[j] - denomi)**2 /float(denomi)

		if T >= t:
			print("asd")
			exitos += 1

	return exitos / float(r), t





def ejercicio6(alfa):
    valoresD = []
    valores = []
    for _ in range(10):
        valores.append(exponencial(1))
    valores.sort()

    j = 1
    n = len(valores)
    for i in valores:
        valoresD.append(j/float(n) - acumulada(i,1))
        valoresD.append(acumulada(i,1) - (j-1)/float(n))
        j += 1
        
    D = max(valoresD)



    #D = d calcular p = Pf(D>=d)
    p = simularP(100,len(valores), D)
    print("D:"),D,"| p-valor:",p
    print " kstest (python)",st.kstest(valores,'expon')
    if p < alfa :
        print("Rechaza H0")
    else:
        print("No rechaza H0")

print("------------ejercicio6------------")
ejercicio6(0.5)

def estMedia(lista):
    return sum(lista)/float(len(lista))
    

def cdfExpKstest(y):
    return 1 - exp(-0.0932256059664*y)

def ejercicio7(alfa):

    valoresD = []
    valores = [1.6,10.3,3.5,13.5,18.4,7.7,24.3,10.7,8.4,4.9,7.9,12,16.2,6.8,14.7]
    valores.sort()
    lamb= 1/float(estMedia(valores))
    j = 1
    n = len(valores)
    for i in valores:
        valoresD.append(j/float(n) - acumulada(i,lamb))
        valoresD.append(acumulada(i,lamb) - (j-1)/float(n))
        j += 1
        
    D = max(valoresD)



    #D = d calcular p = Pf(D>=d)
    p = simularP(100,len(valores), D)
    print("D:"),D,"| p-valor:",p
    print " kstest (python)",st.kstest(valores,lambda x: st.expon.cdf(x, scale=1/float(lamb)))
    if p < alfa :
        print("Rechaza H0")
    else:
        print("No rechaza H0")

print("------------ejercicio7------------")
ejercicio7(0.5)

#print "ejercicio 4 = ",(ejercicio4(0.5))
#print "ejercicio 6 = ",(ejercicio6(0.5))
#print "ejercicio 7 = ",(ejercicio7(0.5))

def ejercicio8(alfa):
    valoresD=[]
    valores = [91.9,97.8,111.4,122.3,105.4,95,103.8,99.6,119.3,104.8,101.7]
    valores.sort()
    E,V,DV = estimarEsperanzaDesviacionNormal(valores,0)
    j = 1
    n = len(valores)
    for i in valores:
        valoresD.append(j/float(n) - st.norm(E, DV).cdf(i))
        valoresD.append(st.norm(E, DV).cdf(i) - (j-1)/float(n))
        j += 1
        
    D = max(valoresD)



    #D = d calcular p = Pf(D>=d)
    p = simularP(10000,len(valores), D)
    print("D:"),D,"| p-valor:",p
    print " kstest (python)",st.kstest(valores,lambda x: st.norm.cdf(x, loc = E, scale=DV))
    if p < alfa :
        print("Rechaza H0")
    else:
        print("No rechaza H0")

print("------------ejercicio8------------")
ejercicio8(0.5)

import sys
sys.setrecursionlimit(3000)
"""""""""""""""""""""""""""""""""""
 ejercicio 9 y 10
"""""""""""""""""""""""""""""""""""

def P(n,m,r):
    if n == 1 and m == 0:
        if r <= 0:
            return 0
        else:
            return 1
    if n == 0 and m == 1:
        if r < 0:
            return 0
        else:
            return 1
    a = 0
    b = 0
    if not n == 0:
        a = n*P(n-1,m,r-n-m)/float(n+m)
    if not m == 0:
        b = m*P(n,m-1,r)/float(n+m)
    return a + b

def recursivoPvalor(n,m,r):
    return 2*min(P(n,m,r),1- P(n,m,r-1))



def aproxNormal(n,m,r):
    E = n*(n+m+1)/float(2)
    V = n*m*(n+m+1)/float(12)
    DV = sqrt(V)

    rPrima = (r - E)/float(DV)

    if r <= E:
        return 2*st.norm(0, 1).cdf(rPrima)
    else:
        return 2*(1 - st.norm(0, 1).cdf(rPrima))

print("------------P valor normal------------")
a = aproxNormal(5,10,55)
print(a)
print("------------P recursivo------------")

print(recursivoPvalor(5,10,55))

def rangoR(muestra1, nmMuestras):
    nmMuestras.sort()

    R = []
    for valor in muestra1:
    	suma = 0
    	if nmMuestras.index(valor) != len(nmMuestras) -1 and nmMuestras[nmMuestras.index(valor) + 1] == valor:
    		i=1
    		suma = nmMuestras.index(valor) + 1
    		count = 1
	    	while nmMuestras[nmMuestras.index(valor) + i] == valor:
	    		suma += nmMuestras.index(valor) + i + 1
	    		count +=1
	    		i +=1
	    	R.append(suma/float(count))
    	else:
        	R.append(nmMuestras.index(valor) + 1)

    return sum(R)

def pValorSimu(muestra1, muestra2, simula):
    '''
    CALCULO p-valor SIMULADO
    '''
    nmMuestras = muestra1 + muestra2
    n = len(muestra1)
    r = rangoR(muestra1, nmMuestras)
    Rmin = 0
    Rmax = 0

    copyMuestra = list(nmMuestras)
    for _ in xrange(simula):
        shuffle(copyMuestra)
        remuestreo = copyMuestra[0:n]
        R = rangoR(remuestreo, copyMuestra)

        if R >= r:
            Rmax += 1

        else:
            Rmin += 1

    return 2 * min(Rmax / float(simula), Rmin / float(simula))

print ("----------simular P valor------ ")
print(pValorSimu([132,104,162,171,129],[107,94,136,99,114,122,108,130,106,88],10000))

"""
multiples muestras, m muestras
H0: todas las var IMP y igual dist => Todos los ordeanmientos igualmentte probables

E(Ri) = n(i) * (n+1)/2 n= cantidad total de var
R = 12/n*(n+1)* [ sum (1 to m) (Ri - E(Ri))**2
									/n(i)

para valores no tan grandes
p valor = P(R>=y)

para valores gnrandes de n(i)
valor p = P(X(m-1) >= y)
"""
print ("----------multiples colas------ ")
def espRango(ni,n):
	return ni*(n+1)/float(2)


m1= [121,144,158,169,194,211,242]
m2= [99,128,165,193,242,265,302]
m3= [129,134,137,143,152,159,170]

def ejercicio15(m1,m2,m3):

	m4 = m1+ m2 + m3
	m4.sort()
	R1 = rangoR(m1,m4)
	#print "python test",st.mstats.kruskalwallis(m1,m2,m3)
	R2 = rangoR(m2,m4)
	R3 = rangoR(m3,m4)
	listaRangos = []
	listaRangos.append(R1)
	listaRangos.append(R2)
	listaRangos.append(R3)

	listaNi = []
	listaNi.append(len(m1))
	listaNi.append(len(m2))
	listaNi.append(len(m3))

	n = len(m4)
	a = 12/float(n*(n+1))

	b = 0
	for i in xrange(3):
		b += ((listaRangos[i] - espRango(7,21))**2)/float(7)

	R = a*b
	#print "R",R
	#c = 1 - st.chi2.cdf(R,2)
	return R



def pValorSimuM(simula):
	'''
	CALCULO p-valor SIMULADO
	'''

	m1= [121,144,158,169,194,211,242]
	m2= [99,128,165,193,242,265,302]
	m3= [129,134,137,143,152,159,170]
	m4 = m1+ m2 + m3
	lista = []
	lista.append(len(m1))
	lista.append(len(m2))
	lista.append(len(m3))
	nmMuestras = m4

	pvalor = []
	Rmin = 0
	Rmax = 0

	n = choice(lista)
	r = ejercicio15(m1,m2,m3)

	copyMuestra = list(nmMuestras)
	for _ in xrange(simula):
		shuffle(copyMuestra)
		remuestreo = copyMuestra[0:n]
		remuestreo2 = copyMuestra[n:2*n]
		remuestreo3 = copyMuestra[2*n:3*n]
		R = ejercicio15(remuestreo, remuestreo2,remuestreo3)

		if R >= r:
			Rmax += 1

		else:
			Rmin += 1
	#pvalor es P (R>Y)
	pvalor=min(Rmax / float(simula), Rmin / float(simula))
	print "p valor simu", pvalor


pValorSimuM(10000)
r = ejercicio15(m1,m2,m3)
print 1 - st.chi2.cdf(r,2)

"""poissson no homogeneo


T = S2/Nbarra valor p = 2*min[P(T<t),P(T>t)]
"""
def poissonNo(simulaciones):
	m = [18,24,16,19,25]
	EX = estimarEsperanza(m)
	V,DV = estimarDesviacion(m,EX)
	T = V/float(EX)
	Rmax = 0
	Rmin = 0
	for _ in xrange(simulaciones):
		r=[]
		r = [nm.random.poisson(EX) for _ in xrange(len(m))]
		print(r)
		E = estimarEsperanza(r)
		V,DV = estimarDesviacion(r,E)
		t = V/float(E)

		if t >= T:
			Rmax += 1

		else:
			Rmin += 1

	return 2*min(Rmax / float(simulaciones), Rmin / float(simulaciones))

print "poisssssosn"
print(poissonNo(1000))

#luego de esto usar el wacho de muchas muestras kruskal
# si p valor pequeño se rechaza la hipotesis

#valor P = 2 min { R<=Y, R>=y}
#		   2 min {Xr-1} r = cantidad muestras
"""
estiamr lambda(t)
ordenar los N tiempos de llegada
en el tiempo Yj-1 Yj ocurrio llegada en el total de r dias
en un dia hay promedio 1/r llegadas
lambda(t) = 1 / (Yj-Y(j-1) * r) Yj-1 < t Yj


homogeneo
validar como no homogeneo que sea de poisson
Xr,Nr r = cantidad muestras
N = N1 + N2 + .. Nr , total lelgadas
H0 Los N tiempos de llegada estan distribuiods uniformemente en un dia, o intervalo (0,T)

"""
"""

BOOTSTRAP
Ai: tiempo de arribo del cliente i.
Si: tiempo de servicio del cliente i.
Vi: tiempo de salida del cliente i.
Vi = max{Ai, Vi−1} + Si, V0 = 0

Wi: tiempo que pasa el cliente i en el sistema,
Wi = Vi − Ai = max{Ai, Vi−1} + Si − A


Ni ← número de clientes el día i:
Di ← suma de tiempos que permanecen los clientes en el sistema el
día i:
D1 = W1 + · · · + WN1
D2 = WN1+1 + · · · + WN1+N2
.
.
.
Di = WN1+···+Ni−1+1 + · · · + WN1+···+Ni
I Notar: los tiempos Di y los números Ni son independientes e
idénticamente distribuidos.

µ = W1 + · · · + Wn/n
= limm→∞
D1 + · · · + Dm
N1 + · · · + Nm
= limm→∞
(D1 + · · · + Dm)/m
(N1 + · · · + Nm)/m
=
E[D]
E[N]


ECM(D/N) = E"P
P
i Di
i Ni
− µ
2
#
.