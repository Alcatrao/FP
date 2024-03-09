def inverteNum(input):
    output=0
    while input>0:
        output = output + input%10
        input = input//10
        if input==0:
            break
        else:
            output = output*10

    return output


def inverteStr(input):
    if input == '':
        return ''
    return inverteStr(input[1:])+input[0] #Na palavra normal, a 1ª letra aparece antes da 2ª (ou a 2ª letra aparece depois da 1ª). Na palavra invertida, a 1ª letra aparece depois da 2ª (ou a 2ª antes da 1ª).


def askInput():
    lista=[]
    while True:
        n = input("Insira algo: ")
        if n=="":
            return lista
        else:
            try:
                n = int(n)
                lista.append(n)
            except:
                lista.append(n)

def main():
    lista = askInput()
    listaInvertida = []

    for valor in lista:
        if isinstance(valor, int):
            listaInvertida.append(inverteNum(valor))
        else:
            listaInvertida.append(inverteStr(valor))

    print("Lista original: ", lista)
    print("Lista invertida: ", listaInvertida)


main()