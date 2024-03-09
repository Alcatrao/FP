def max2(x, y):
    if x<=y:
        return y
    return x

def max3(x, y, z):
    return max2(max2(x,y), max2(y,z))

def maior_divide_and_conquer(lista):
    if len(lista)==1:
        return lista[0]

    mid=len(lista)//2
    cena=maior_divide_and_conquer(lista[0:mid])
    dor=maior_divide_and_conquer(lista[mid:])

    if cena>=dor:
        return cena
    return dor

def maior_decrease_and_conquer(lista):
    if len(lista)==1:
        return lista[0]

    if lista[0] >= maior_decrease_and_conquer(lista[1:]):
        return lista[0]
    return maior_decrease_and_conquer(lista[1:])



def main():
    while True:
        try:
            a=float(input("Insira o argumento 1: "))
            break
        except:
            print("Argumento inválido.")
            exit()

    while True:
        try:
            b=float(input("Insira o argumento 2: "))
            break
        except:
            print("Argumento inválido.")
            exit()

    while True:
        try:
            c=float(input("Insira o argumento 3: "))
            break
        except:
            print("Argumento inválido.")
            exit()

    print("max2:", max2(a,b))
    print("max3:", max3(a,b,c))

    #lista=[1,2,3,29,0]
    #print(maior_divide_and_conquer(lista))
    #print(maior_decrease_and_conquer(lista))


main()