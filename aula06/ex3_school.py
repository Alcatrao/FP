# Complete o programa!

# a)
import os


def loadFile(fname, lst):
    directory="C:/Users/joaoa/OneDrive/Ambiente de Trabalho/FP/aula06"+"/"
    with open(directory+fname) as ficheiro:
        while True:
            linha = ficheiro.readline().split('\t')
            #print(linha)
            if linha[0]=='':
                break
            try:
                #print(linha[7])
                linha[7]=linha[7][:-1]      #retirar o \n do final que faz com que haja newline neste valor
                #print(linha[7])
                lst.append( (int(linha[0]), linha[1], float(linha[5]), float(linha[6]), float(linha[7])) )
            except:
                continue


    
# b) Crie a função notaFinal aqui...
def notaFinal(tuplo):
    return (tuplo[2] + tuplo[3] + tuplo[4])/3

# c) Crie a função printPauta aqui...
def printPauta(lst, file=0):
    if file==0:
        print("{:>6} {:^50} {:>5}". format("Número", "Nome", "Nota"))
        for tuplo in lst:
            print("{:>6} {:^50} {:>5.1f}". format(tuplo[0], tuplo[1], notaFinal(tuplo)))
    else:
        directory="C:/Users/joaoa/OneDrive/Ambiente de Trabalho/FP/aula06"+"/"
        ficheiro = open(directory + file, 'w')
        print("{:>6} {:^50} {:>5}". format("Número", "Nome", "Nota"), file=ficheiro)
        for tuplo in lst:
            print("{:>6} {:^50} {:>5.1f}". format(tuplo[0], tuplo[1], notaFinal(tuplo)), file=ficheiro) 

        ficheiro.close()
        

# d)
def main():
    lst = []
    # ler os ficheiros
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)

    #print(lst)
    print(notaFinal(lst[0]))


    # ordenar a lista
    lst.sort()
    
    # mostrar a pauta
    printPauta(lst, 'ex4.txt')


# Call main function
if __name__ == "__main__":
    main()


