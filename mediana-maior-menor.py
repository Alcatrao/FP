def mediana (lista):
    assert len(lista)%2==1
    def merge_sort(lista):
        if len(lista)<=1:
            return lista
            
        meio = len(lista)//2
        cena = merge_sort(lista[0:meio])
        dor = merge_sort(lista[meio:])

        coisa=[]
        i=0
        index=0

        while index < len(cena) and i < len(dor):       
            if cena[index]<=dor[i]:
                coisa.append(cena[index])
                index+=1
            else:
                coisa.append(dor[i])
                i+=1

        if index < len(cena):
            for index2 in range(index, len(cena)):
                coisa.append(cena[index2])

        if i < len(dor):
            for i2 in range(i, len(dor)):
                coisa.append(dor[i2])

        return coisa
    
    lst = merge_sort(lista)
    return lst[len(lst)//2]




def menor(lst):
    if lst==[]:
        return lst
    if len(lst)==1:
        return lst[0]
    
    meio=len(lst)//2
    dor=menor(lst[:meio])
    ocd=menor(lst[meio:])

    if dor<ocd:
        return dor
    return ocd



def maior(lst):
    if lst==[]:
        return lst
    if len(lst)==1:
        return lst[0]
    
    meio=len(lst)//2
    dor=maior(lst[:meio])
    ocd=maior(lst[meio:])

    if dor>ocd:
        return dor
    return ocd



lst=[1,2,5,3,4,0,6,3,67,5,1,34,7,2,4,2,54,2,4,2,5,6,7,4,3,62,3]
print(mediana(lst))
print(maior(lst))
print(menor(lst))

