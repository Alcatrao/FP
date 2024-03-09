def dor(x):
    cena = x
    for i in range(x):
        cena += dor(x-1)
    return cena

print(dor(3))