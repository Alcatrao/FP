def lcm(cena, dor):
    if cena<dor:
        mau=cena
        cena=dor
        dor=mau
    if dor==0:
        return cena
    return lcm(cena%dor, dor)

def minimoDivisorComum(lst):
    if len(lst)==1:
        return lst[0]

    meio=len(lst)//2
    cena=minimoDivisorComum(lst[0:meio])
    dor=minimoDivisorComum(lst[meio:])

    mau=lcm(cena,dor)
    return mau

    return lcm(lst[0], minimoDivisorComum(lst[1:]))


lista=[29, 1996]
print(minimoDivisorComum(lista))


#############################################################################
import os
caminho = os.path.join(os.path.abspath(os.path.dirname(__file__)), "randomNumberSequence.txt")
#print(caminho)

contaDor=0

with open(caminho, 'r') as stream:
    for lineFeel in stream:
        contaDor+=1                    
        if contaDor > 994: #contar apenas o que estiver nas primeiras 900 linhas 
            break
        try:
            lista.append(int(lineFeel))
        except:
            continue


print(lista)
print(len(lista))
print(minimoDivisorComum(lista))




""" import random
lista2=[]
for i in range(0, 9000):
    x=random.randint(100000, 100000000)
        
print(lista2)
print(minimoDivisorComum(lista2)) """