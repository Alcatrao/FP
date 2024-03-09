#def pior(j):
#    dor=j+1
#    return dor


def pior(lista, dor):
    #print("cena")
    if(lista==[]):
        return dor
    if lista[0]>dor:
        return pior(lista[1:], lista[0])
    return pior(lista[1:], dor)

def sentir(lista):
    #if lista==[]:
    #    #print(lista)
    #    return []
    if len(lista)==1:
        return lista[0]

    #print(lista[0:len(lista)//2])
    #print(lista[len(lista)//2:])
    #print()
    cena=sentir(lista[0:len(lista)//2]) #sentir([29]) invoca cena=sentir([]) e dor=sentir([29]). Cena=sentir([]) invoca sentir([]), faz print e retorna []. Dor=sentir([29]) invoca sentir([29]), que invoca
    dor=sentir(lista[len(lista)//2:])   #cena=sentir([]) e dor=sentir([29]). dor=sentir([29]) invoca dor=sentir([29]), o que se traduz num bottomless pit of pain. Cena dor

    if cena>dor:
        return cena
    return dor


lista=[0, 1, 2, 3, 5, 7, 19, 13, 14, 10, 29, 17, 19]
print(sentir(lista))