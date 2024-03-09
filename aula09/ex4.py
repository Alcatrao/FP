import bisect
import os

ficheiro = os.path.join(os.path.dirname(os.path.abspath(__file__)), "wordlist.txt")

def ficheiroParaLista(ficheiro):
    stream = open(ficheiro, 'r', encoding='utf-8')
    lista = []
    while True:
        linha = stream.readline()
        if linha == '':
            stream.close()
            return lista
        lista.append(linha)

        



def binary_search(lista, elemento): #1º update: havia um 3º parâmetro "idx=0", que era devolvido como era no caso base e na 1ª chamada recursiva, e era devolvido como era + meio na 2ª chamada. Os returns de baixo não tinham somas. Esta maneira sem esse parâmetro, funciona igual
    if len(lista)==1:
        if lista[0]==elemento:
            return lista[0], 0, 1   #2º update: agora também devolve um contaDor do nº de ocorrências de "elemento" na "lista"
        return lista[0], 0, 0
    
    meio = len(lista)//2
    cena, dor, contaDor1 = binary_search(lista[0:meio], elemento)
    mau, pior, contaDor2 = binary_search(lista[meio:], elemento)

    if cena == elemento:
        return cena, dor+0, contaDor1+contaDor2
    if mau == elemento:
        return mau, pior+meio, contaDor2
    return None, None, 0    #devolve o elemento encontrado (se encontrado), o menor índice onde foi encontrado (se encontrado), e o nº de ocorrências do elemento registadas 





def merge_sort(lista):
    if len(lista)==1:
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





#lista = [29, 1, 1996]
#print(binary_search(lista, 29))

#1) minha maneira, com as minhas funções merge_sort(lista) [não usada] e binary_search(lista, elemento):
""" lista = ficheiroParaLista(ficheiro)
for idx in range(len(lista)):
    if len(lista[idx])>2:
        lista[idx] = lista[idx][0:2]

#print(lista)

print(binary_search(lista, "ea"))

print(binary_search(lista, "eb")[1] - binary_search(lista, "ea")[1]) """






#2) maneira pedida:
lista = ficheiroParaLista(ficheiro)

idx_ea = bisect.bisect_left(lista, "ea")
#print(idx_ea)
idx_eb = bisect.bisect_left(lista, "eb")
#print(idx_eb)

palavras_ea = idx_eb - idx_ea
print("a)",palavras_ea)

print("b)", bisect.bisect_left(lista, "tc") - bisect.bisect_left(lista, "tb"))
print("c)", lista[bisect.bisect_left(lista, "tc")])


print("--Insira o vazio (dar Enter só) para terminar o programa--")
while True:
    prefixo = input("Insira um prefixo: ")
    if prefixo == '':
        break
    letras_possiveis = set()
    for idx in range(bisect.bisect_left(lista, prefixo), bisect.bisect_left(lista, prefixo+'{')):   #todos os índices desde o prefixo até prefixo+'{' (antes tinha prefixo+'z', mas as palavras com z não eram incluídas, pois o range pára onde encontra o z ou onde ele devia estar. '{' é o símbolo logo a seguir ao 'z' em utf-8)
        try:
            if lista[idx][len(prefixo):-1] not in letras_possiveis:
                letras_possiveis.add(lista[idx][len(prefixo):-1])
        except:
            continue

    print((sorted(letras_possiveis)))
