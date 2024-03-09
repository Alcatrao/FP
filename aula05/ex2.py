def inputFloatList():
    lista=[]
    while True:
        try:
            n=input("Insira um número: ")
            if n=="":
                break
            else:
                n=int(n) 
                lista.append(n)
        except:
            print("Número inválido; tente novamente.")

    return lista



def countLower(lst, v):
    if lst==[]:
        return []
    if len(lst)==1:
        if lst[0]<v:
            #return [lst[0]]
            return 1
        else:
            #return []
            return 0
    
    meio=len(lst)//2

    cena=countLower(lst[0:meio], v)
    dor=countLower(lst[meio:], v)

    return cena+dor



def minmax(lst):
    if lst==[]:
        return [], []
    if len(lst)==1:
        return lst[0], lst[0]

    if len(lst)==2:
        if lst[0]>lst[1]:
            return lst[0], lst[1]
        else:
            return lst[1], lst[0]

    meio=len(lst)//2
    coisa, dor = minmax(lst[0:meio])
    cena, pior = minmax(lst[meio:])

    if coisa>cena:
        luz=coisa
    else:
        luz=cena

    if dor<pior:
        beliscao=dor
    else:
        beliscao=pior

    return luz, beliscao






def main():
    lst=inputFloatList()
    print("Lista: ",lst)

    #while True:
    #    try:
    #        v=int(input("Indique o maior valor aceitável para a lista acima: "))
    #        break
    #    except:
    #        print("Número inválido. Tenta novamente.")

    #contaDor=countLower(lst, v)
    #print("CountLower: ",contaDor)

    maior, menor = minmax(lst)
    print("Menor:", menor)
    print("Maior:", maior)


    #alínea d) (foi o que me fez comentar tudo o que está comentado acima, incluindo o funcionamento da função countLower())
    v=(maior+menor)/2
    contaDor=countLower(lst, v)
    print("Número de números na lista", lst,"inferiores a",v,": ", contaDor)

main()
