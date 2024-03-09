import math


def findZero(func, a, b, tol):          #este é o método da bissecção estudado em Métodos Numéricos e Estatísticos
    if abs(a - b) < tol:
        return a, b
    
    meio = (a+b)/2
    dor = func(meio)

    if func(a) < 0 and dor >=0 or func(a) >= 0 and dor < 0:
        mau, pior = findZero(func, a, meio, tol)
    elif func(b) < 0 and dor >=0 or func(b) >= 0 and dor < 0:       #poderia ser um else:
        mau, pior = findZero(func, meio, b, tol)
    
    return mau, pior



func = lambda x: x + math.sin(10*x)
print(findZero(func, 0.2, 0.4, 0.000000000000001))
