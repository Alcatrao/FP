from curses.ascii import isupper

def askInput():
    frase = input("Insira uma frase: ")
    return frase

def primeLength(str):
    fraseOutput=''
    listaPalavras = str.split()
    for palavra in listaPalavras:
        for numero in range(2, len(palavra)//2+1):
            if len(palavra)%numero == 0:
                break
        else:
            fraseOutput=fraseOutput+" "+palavra
            #if numero == len(palavra)-1:
            #    fraseOutput=fraseOutput+" "+palavra
            #    break

    return fraseOutput









def evenUpper(str):
    output=[]
    vogais=['A', 'E', 'I' 'O', 'U']
    for index in range(0, len(str)):
        if index % 2 != 0:
            continue
        if isupper(str[index]):
            for vogal in vogais:
                if str[index] == vogal:
                    output.append(index)
                    break

    return output


def main():
    #frase = askInput()

    frase = "The quick brown fox jumps over the lazy dog."
    #frase = "Omicron Effect: Foreign Flights Won't Resumo on Dec 15, Decision Later."

    #print(evenUpper(frase))

    fraseNova = primeLength(frase)
    print(fraseNova)


main()
