from math import exp, log
from random import random

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

def simularPdiscreto(n,r,t,k,prob):
    Ylist = []
    Nlist = []
    exitos = 0
    for _ in range(r):
        for _ in range(n):
            Ylist.append(ejercicio1p())

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

    NBlanca = 141
    NRosa = 291
    NRoja = 132

    npBlanca = n* pBlanca #= 141
    npRosa = n* pRosa #= 282
    npRoja = n * pRoja #= 141

    T = ((NBlanca-npBlanca)**2/float(npBlanca)) + ((NRosa-npRosa)**2/float(npRosa)) + ((NRoja-npRoja)**2/float(npRoja))
    print(simularPdiscreto(n,100,T,3,[0.25,0.5,0.25]))
    #T es 0.86 y de resultado es 0.65
    print (T)

def ejercicio2():
    n = 1000
    pHonesto = 1/float(6)

    N1 = 158
    N2 = 172
    N3 = 164
    N4 = 181
    N5 = 160
    N6 = 165

    npHonesto = n* pHonesto #= 141

    T = ((N1-npHonesto)**2 + (N2-npHonesto)**2 + (N3-npHonesto)**2+ (N4-npHonesto)**2+ (N5-npHonesto)**2+ (N6-npHonesto)**2)/float(npHonesto)

    #chi de 5 libertad de 2.18 es 0.82372
    print (T)

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
        for U in valores:
            valoresD.append(j/float(n) - U)
            valoresD.append(U - (j-1)/float(n))
            j += 1

        D = max(valoresD)
        print(D)
        if D >= d:
            exitos += 1
        valores = []
        valoresD = []
    return exitos/float(r)

def ejercicio4(alfa):
    valoresD = []
    valores = [86,133,75,22,11,144,78,122,8,146,33,41,99]
    valores.sort()

    j = 1
    n = 13
    for i in valores:
        valoresD.append(j/float(n) - acumulada(i,0.02))
        valoresD.append(acumulada(i,0.02) - (j-1)/float(n))
        j += 1
        
    D = max(valoresD)



    #D = d calcular p = Pf(D>=d)
    p = simularP(10,len(valores), D)
    print("p y D")
    print(D)
    print(p)
    if p < alfa :
        print("Rechaza H0")
    else:
        print("No rechaza H0")

def exponencial(lamb):
    U= random()
    return (- log(U)/float(lamb))

def ejercicio6(alfa):
    valoresD = []
    valores = []
    for _ in range(10):
        valores.append(exponencial(1))
    valores.sort()

    j = 1
    n = 13
    for i in valores:
        valoresD.append(j/float(n) - acumulada(i,1))
        valoresD.append(acumulada(i,1) - (j-1)/float(n))
        j += 1
        
    D = max(valoresD)


    print(valoresD)
    #D = d calcular p = Pf(D>=d)
    p = simularP(1,len(valores), D)
    print("p y D")
    print(D)
    print(p)
    if p < alfa :
        print("Rechaza H0")
    else:
        print("No rechaza H0")

def estMedia(lista):
    return sum(lista)/float(len(lista))
    

def ejercicio7(alfa):
    valoresD = []
    valores = [1.6,10.3,3.5,13.5,18.4,7.7,24.3,10.7,8.4,4.9,7.9,12,16.2,6.8,14.7]
    valores.sort()
    lamb= 1/float(estMedia(valores))
    j = 1
    n = 13
    for i in valores:
        valoresD.append(j/float(n) - acumulada(i,lamb))
        valoresD.append(acumulada(i,lamb) - (j-1)/float(n))
        j += 1
        
    D = max(valoresD)


    print(valoresD)
    #D = d calcular p = Pf(D>=d)
    p = simularP(10,len(valores), D)
    print("p y D")
    print(D)
    print(p)
    if p < alfa :
        print("Rechaza H0")
    else:
        print("No rechaza H0")

ejercicio1()
