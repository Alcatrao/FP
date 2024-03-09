import os
import sys


if len(sys.argv) != 2:
    print("Número de argumentos inválido.")

#print(os.path.join(os.path.abspath(__file__), sys.argv[1]))
#print(os.path.join(os.path.dirname(os.path.abspath(__file__)), sys.argv[1]))

print(sys.argv[1])

if os.path.isfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), sys.argv[1])) == False:
    print("Argumento não é um ficheiro.")
    

def countLetters():
    ficheiro = open(sys.argv[1], 'r')
    dicionario_letras = {}
    while True:
        try:
            linha = ficheiro.readline()
        except:
            continue #algumas linhas não conseguem ser lidas pela .readline(), que devolve um erro (character 549 couldn't be decoded...)
        if linha == "":
            ficheiro.close()
            break
        for palavra in linha.split():
            for letra in palavra:
                try:
                    letra = letra.lower()
                    if letra.isalpha()!=True:
                        continue
                except:
                    continue
                if letra not in dicionario_letras:
                    dicionario_letras[letra]=1
                else:
                    dicionario_letras[letra]+=1
    return dicionario_letras

def imprimir(dicionario):
    for letra in sorted(dicionario):
        print(letra, ":", dicionario[letra])

def main():
    imprimir(countLetters())

main()