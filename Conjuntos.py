def conjuntos(lista):
    if lista==[]:
        return [[]]

    '''
    #subconjunto1 = [lista[0]] + conjuntos(lista[1:])    #adiciona só este valor à lista de todos os subconjuntos, em vez de o adicionar a cada subconjunto individualmente

    subconjunto1 = []
    for conjunto in conjuntos(lista[1:]):               #também não funciona se o caso base for [], pois não ocorre iteração alguma no [] (porque tem 0 elementos). Este [] fica assim presente em todas as chamadas recursivas, e não só na penúltima. Mas ocorre em [[]] (porque tem 1 elemento, logo ocorre 1 iteração)
        subconjunto1.append([lista[0]] + conjunto)

    subconjunto2 = conjuntos(lista[1:])                 #lista de todos os subconjuntos sem o primeiro valor de lista

    return [subconjunto1] + [subconjunto2]
    '''
    
    conjunto = []

    for subconjunto in conjuntos(lista[1:]):
        conjunto.append([lista[0]]+subconjunto)
        conjunto.append(subconjunto)

    return conjunto
    


lista = [29, 1, 1996]
print(conjuntos(lista))