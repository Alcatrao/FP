def mediana(lista):
    lst = merge_sort(lista)
    meio = len(lista)//2 # == len(lst)//2
    if len(lista)%2 != 0:
        return lst[meio]
    return (lst[meio]+lst[meio+1])/2


def merge_sort(lista):
    if len(lista)==1:
        return lista
        
    meio = len(lista)//2
    cena = merge_sort(lista[0:meio])
    dor = merge_sort(lista[meio:])

    coisa=[]
    i=0
    """ contaDor = 0

    for index in range(0, len(cena)):       #o ciclo for deve funcionar aqui como funciona no exercício das moedas (em que só percorre o nº de iterações específicadas ao início, e diminuir o valor do "index" para prolongar o ciclo não o prolonga além desse nº estabelecido)
        if i<len(dor):
            if cena[index]<=dor[i]:
                coisa.append(cena[index])
                contaDor = 0
            else:
                coisa.append(dor[i])
                i+=1
                contaDor +=1
                index-=contaDor         #update: todas as linhas com o contaDor foram adicionadas posteriormente à função estar corretamente acabada, e esta linha era index-=1. Isto foi uma tentativa de ultrapassar o facto de o index não se manter constante por mais de 1 else sucessivo (6-1=5, mas depois 7-1=6; o valor não é conservado entre iterações). De qualquer modo, o limite acima mantém-se, pelo que não se consegue assegurar o correto funcionamento do programa com este for.
            #print("index: ",index)
            #print("i: ",i)
    index+=1 """

    index=0
    while index < len(cena) and i < len(dor):       #o while aqui funciona na perfeição, e supostamente faz o mesmo que o ciclo for comentado acima (mas aqui, o nº de iterações máximo não é limitado/fixo)
        if cena[index]<=dor[i]:
            coisa.append(cena[index])
            index+=1
        else:
            coisa.append(dor[i])
            i+=1
        #print("index: ",index)
        #print("i: ",i)


    if index < len(cena):
        for index2 in range(index, len(cena)):
            coisa.append(cena[index2])
            #print("index2: ",index2)

    if i < len(dor):
        for i2 in range(i, len(dor)):
            coisa.append(dor[i2])
            #print("i2: ",i2)

    return coisa


lista = [29, 1, 0, -1, 3, -2, 4, 5, 1996, 10]
lista = [29, 1, 1996]
#lista = [1996, 29, 1, 0, -1]
print(merge_sort(lista))

print(mediana(lista))