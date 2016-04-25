from math import log, exp, pi, cos, sin
from random import random
'''
DISCRETAS
'''
def varianzaEsperanza(g, n = 100, p = 0.0):
	'''
	FORMULA PARA CALCULAR VARIANZA - ESPERANZA GENERAL
	'''
	# para sumar las X
	vaX = 0
	# para sumar las X^2 para la varianza
	vaX2 = 0
	for _ in xrange(n):

		# with arguments
		if not p:
			varTmp = g()
		# without arguments
		else:
			varTmp = g(p)

		vaX += varTmp
		vaX2 += varTmp**2

	esperanza =  vaX / float(n)
	varianza = vaX2 / float(n) - esperanza**2

	return esperanza, varianza


'''
DISCRETAS
'''
def uniform(a, b):
    U = random()
    X = int(U * (b - a + 1)) + a
    return X

def geometrica(q):
    # q es 1-p    p.q^i-1
    V = random()
    X = int(log(V) / log(q)) + 1
    return X

def poisson(lam):
    i, p = 0, exp(-lam)
    F = p
    # uniform in (0,1)
    U = random()

    while U >= F:
        i += 1
        p = (lam * p) / i
        F += p

    return i

def poissonExt(lamb):
    # uniform in (0, 1)
    uniforms = random()
    # constant e^-lamb
    e = exp(-lamb)
    X = 0

    while uniforms >= e:
        uniforms *= random()
        X += 1

    return X


def Fpoisson(i, lam):
    p = exp(-lam)
    F = p

    for _ in xrange(i):
        p = (lam * p) / i
        F += p

    return F

''' MAL VERLO
def poissonMejor(lam):
    i = int(lam)
    F = Fpoisson(i, lam)

    # generar uniform
    U = random()
    if U <= F:
        F = F * i / lam
        i -= 1

    else:
        F = F * lam / i
        i += 1

    return i
'''

def binomial(p, n):
    # generar U uniform(0, 1)
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

def urna(tam, digitos, vector):
    # generar uniforme (0, 1)
    U = random()
    J = int(U * 10**digitos)

    return vector[J]

'''
CONTINUAS
'''

def maxVaIndep(n):
    '''
    MULTIPLICATE V.A.I.
    '''
    # simulate n uniforms
    uniforms = [random() for _ in xrange(n)]
    X = max(uniforms)

    return X

def minVaIndep(n):
    uniforms = [random() for _ in xrange(n)]
    X = min(uniforms)

    return X

def exponential(lamb):
    # generate U~u(0,1)
    U = random()
    X = -log(U) / lamb

    return X

def gamma(lamb, n):
    # generate product of uniform
    uniforms = 1

    for _ in xrange(n):
        uniforms *= random()

    X = -log(uniforms) / lamb

    return X

def nExponential(lamb, n):
    # generates n random uniform and multiplicate
    uniforms = 1
    for _ in xrange(n):
        uniforms = uniforms * random()

    t = -log(uniforms) / lamb

    # generates n-1 v.a. uniform and order
    V = [random() for _ in xrange(n - 1)]
    V.sort()

    # n v.a. exponential
    Xvar = []
    for i in xrange(n - 1):

        if i == 0:
            Xvar.append(V[i] * t)

        elif i == (n - 1):
            Xvar.append(t - t*V[i-1])

        else:
            Xvar.append(t*(V[i] - V[i - 1]))

    return Xvar


def normal():
    V = random()
    Y = -log(V)
    U = random()
    while U >= exp(-(Y - 1)**2 / 2):
        V = random()
        Y = -log(V)
        U = random()

    return Y


def normalMejorada():
    while True:
        # simulate two uniform (0, 1)
        U = random()
        V = random()
        # simulate two exp with lam=1
        Y1 = -log(U)
        Y2 = -log(V)

        if Y2 > (Y1 - 1) ** 2 / 2:
            break

    return Y1

def normalTotal():
    while True:
        Y1 = exponential(1)
        Y2 = exponential(1)

        if Y2 > (Y1 - 1)**2 / 2:
            break

    X = Y2 - (Y1 - 1)**2 / 2
    # generate a new random variable
    U = random()

    if U < 0.5:
        Z = Y1

    else:
        Z = -Y2

    return Z

def normalPolar():
    # simulate U1 and U2 uniforms
    U1 = random()
    U2 = random()
    R = -2 * log(U1)
    tetha = 2 * pi * U2
    X = R**(1/2) * cos(tetha)
    Y = R**(1/2) * sin(tetha)

    return X, Y

def normalPolar2():
    # simular V1, V2 uniforms in (-1, 1)
    S = 1
    while S >= 1:
        U1 = random()
        U2 = random()
        V1 = 2 * U1 - 1
        V2 = 2 * U2 - 1
        S = V1**2 + V2**2

    C = (-2 * log(S) / S)
    X = C * V1
    Y = C * V2

    return X, Y


'''
PROCESO DE POISSON
'''

def PPoissonNH(lamb, T):
    S = []
    t = 0
    I = 0

    while True:
        # generamos U~ u(0, 1)
        U = random()

        if t - log(U) / lamb > T:
            break

        else:
            t = t - log(U) / lamb
            I += 1
            S.append(t)

    return S

def adelgazamiento(lamb, funden, T):
    t, i = 0, 0
    S = []

    while True:
        # generar U uniform(0, 1)
        U = random()

        if t - log(U) / lamb > T:
            break

        else:
            t = t - log(U) / lamb
            # generar V
            V = random()

            if V < funden(t) / lamb:
                i += 1
                S.append(t)

    return S

def adelgazamientoMejor(lambdas,intervalos, funden,T):
    t, i = 0, 0
    S = []
    J = 1
    while True:
        # generar U uniform(0, 1)
        U = random()
        X = - log(U)/lambdas[J]

        while t + X > intervalos[J]:
            if J == k+1:
                break
        X = (X - intervalos[J] + t)*lambdas[J]/lambdas[J+1]
        t = intervalos[J]
        J += 1

        t = t + X
        V = random()
        if V < funden(t) / lamb:
            i += 1
            S.append(t)

    return S


