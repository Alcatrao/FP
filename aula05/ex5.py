from curses.ascii import isdigit


def digitCounter(str):
    contaDor=0
    for letter in str:
        if isdigit(letter)==True:
            contaDor+=1
    return contaDor

frase=input("Escreva uma frase, e direi-lhe quantos dígitos foram encontrados: ")
print(digitCounter(frase))