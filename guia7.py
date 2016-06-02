from math import exp, log,floor,sqrt,factorial
from random import random,randint, choice,shuffle
import scipy.stats as st

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
    f = math.factorial
    comb = f(n) / float(f(k)*f(n-k))
    return p**k *(1-p)**(n-k) * comb

def estimarEsperanza(lst):
    """calculates mean"""
    return sum(lst) / len(lst)

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

def ejercicio5():
    val1 = [0,1,2,4,1,1,2,5,2]
    valores = [6,7,3,4,7,3,7,2,6,3,7,8,2,1,3,5,8,7]
    p = estimarPbinomial(valores,8)
    val2 = [st.binom.cdf(x,8,p)*18 for x in val1]
    print " chi (python)",st.chisquare(val1, f_exp=val2)

print("------------ejercicio5------------")
ejercicio5()

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

#a = aproxNormal(5,10,55) esto funciona bien !!!!!!!!!!
#print(a)

# print(recursivoPvalor(5,10,55)) pValor recursivo tmb funciona!!!!!!!

def simularPvalor(n,m,r,t):
    Rmenor = 0
    Rmayor = 0
    var = list(range(1,n+m))
    for _ in range(t):
        
        
        total = 0
        shuffle(var)
        for i in range(n):
            total += var[i]
    
        if total < r:
            Rmenor += 1
        else:
            Rmayor += 1
    return Rmenor/float(t), Rmayor/float(t)

#print(simularPvalor(5,10,55,1000)) esto anda mall 
