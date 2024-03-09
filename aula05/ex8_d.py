def positionOfFirstLargest(lista): #adicionado só por causa do codecheck

    def indexMaior(lista, idx=0):
        if len(lista)==1:
            return lista[0], idx

        meio=len(lista)//2
        dor, coisa=indexMaior(lista[0:meio], idx)
        pior, cena=indexMaior(lista[meio:], idx+meio)

        if dor>=pior:
            return dor, coisa
        else:
            return pior, cena

    def indexRetriever(numeroIndex):
        return numeroIndex[1]

    return indexRetriever(indexMaior(lista))

lista=[0, 1, 10, 3, 29, 6, 29]
#print(indexRetriever(indexMaior(lista)))
print(positionOfFirstLargest(lista))