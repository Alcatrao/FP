import copy
import os
from time import sleep


def interface(jornada):
    #selecionar número de uma jornada válida (entre 1 e 13)
    """ while True:
        jornada = input("Jornada? ")
        try:
            jornada=int(jornada)
            if jornada<1 or jornada>13:
                #...
                print("Jornada inválida!")
            else:
                break
        except:
            #...
            print("Jornada inválida!") """

    dicio = {}

    #carregar jornadas.cvs para um dicionário, para que se possam ver todos os jogos de cada jornada (em especial, da jornada selecionada acima)
    oldPath = os.getcwd()
    newPath = os.path.dirname(os.path.abspath(__file__))
    os.chdir(newPath)

    contaDor = 1
    with open("Jornadas.csv", 'r', encoding="utf-8") as stream:
        for linha in stream:
            try:
                palavras = linha.split(",")
                if int(palavras[0])==jornada:
                    dicio[contaDor]=[palavras[1], palavras[2][:-1]]
                    contaDor+=1

            except:
                continue

    #para cada jogo da jornada selecionada, fazer uma aposta, e guardá-la no mesmo dicionário criado acima
    listaDicio=[dicio]
    for n in range(1, contaDor):
        """ while True:
            aposta = input(str(n)+" "+dicio[n][0]+" vs "+dicio[n][1]+": ")
            if aposta == "1" or aposta == "2" or aposta.upper() == "X":
                dicio[n].append(aposta.upper())
                break
            else:
                #...
                print("Aposta inválida!") """
        listaDicio=apostas(listaDicio, n)
        #print(listaDicio)


    #guardar apostas num documento jornada"n".csv
    file = "jornada"+str(jornada)+".csv"
    with open(file, 'a', encoding="utf-8") as stream:
        for n in range(1, contaDor):
            #print(dicio[n])
            for dicio in listaDicio:
                stream.write(str(n)+", "+dicio[n][2]+"\n")

    return [contaDor, listaDicio, jornada]

    
def sorte(resultado, aposta):
    resultado=resultado.split("-")
    if resultado[0]==resultado[1]:
        if aposta=="X":
            return "(CERTO)"
        else:
            return "(ERRADO)"
    if resultado[0]<resultado[1]:
        if aposta=="2":
            return "(CERTO)"
        else:
            return "(ERRADO)"
    if resultado[0]>resultado[1]:
        if aposta=="1":
            return "(CERTO)"
        else:
            return "(ERRADO)"



#criar tabela dos resultados das apostas para cada jogo
def tabela(contaDor, dicio):
    todosOsJogos = {}
    with open("Jogos.csv", 'r', encoding="utf-8") as stream:
        for linha in stream:
            palavras = linha.split(",")
            try:
                todosOsJogos[palavras[1]+" "+palavras[2]] = palavras[3]+"-"+palavras[4][:-1]
            except:
                continue

    for n in range(1, contaDor):
        if dicio[n][0]+" "+dicio[n][1] in todosOsJogos:
            resultado = todosOsJogos[dicio[n][0]+" "+dicio[n][1]]
            print("{:<d} {:>20s} {:^5s} {:<20s} : {:<3s} {:<10s}".format(n, dicio[n][0], resultado, dicio[n][1], dicio[n][2], sorte(resultado, dicio[n][2])))
#consegui fazer esta função a funcionar corretamente à primeira, S-tier
    return todosOsJogos #meti esta linha só para fazer a próxima função que até então não tinha lido (a função prize)



def prize(contaDor, dicio, todosOsJogos):
    certas = 0
    for n in range(1, contaDor):
        if dicio[n][0]+" "+dicio[n][1] in todosOsJogos:
            resultado = todosOsJogos[dicio[n][0]+" "+dicio[n][1]]
            if sorte(resultado, dicio[n][2]) == "(CERTO)":
                certas+=1

    if certas<7:
        print("TEM", certas, "CERTAS. SEM PRÉMIO.")
        return 0
    elif certas<8:
        print("TEM", certas, "CERTAS. 3º PRÉMIO.")
        return 100
    elif certas<9:
        print("TEM", certas, "CERTAS. 2º PRÉMIO.")
        return 1000
    else:
        print("TEM", certas, "CERTAS. 1º PRÉMIO.")
        return 5000






def apostasPossiveis(n_letras): #complemento para a última alínea. Calcula as combinações possíveis de input de apostas, tendo em conta o nº de caractéres desse input (limites=[1;3])
    escolhas = "12X"
    possibilities = []

    if n_letras==1:
        for letra in escolhas:
            #print(letra)
            possibilities.append(letra)

    if n_letras>1 and n_letras<=3:
        possibilities=apostasPossiveis(n_letras-1)

        #print("Recursion")                                     #a recursão estava certa, nunca se entrava em recursão infinita.
        #sleep(1)
        #print(possibilities)

        for possibilidade in range(len(possibilities)):         #a linha "for possibilidade in possibilities:" cria um ciclo infinito (não recursivo; é sempre o mesmo), porque a cada iteração, adicionamos 3 novos elementos, e quando essa iteração acaba, vamos para o próximo elemento, mas já lá estarão 3 novos elementos, pelo que nunca se chega ao fim
            for letra in escolhas:
                #print(possibilidade+letra)
                #possibilities.append(possibilidade+letra)      #esta linha adicionava elementos ao ciclo acima, pelo que por cada elemento iterado, eram adicionados 3 novos elementos, o que impossibilitava a chegada ao fim. Nunca se entrava num novo nível de recusão, simplesmente adicionava-se novos elementos ao ciclo iterativo a cada iteração, pelo que ele nunca terminava.
                possibilities.append(possibilities[possibilidade]+letra)
            #sleep(1)
            #print(possibilities)
    
    return possibilities



def dicioMultiplier(listaDicio, n, letras):


    if len(letras)==1:
        listaDicioNova = copy.deepcopy(listaDicio)
        for dicio in listaDicioNova:
            dicio[n].append(letras)
        #print(listaDicioNova)
        return listaDicioNova

    lista = dicioMultiplier(listaDicio, n, letras[1:])

    listaDicioNova = copy.deepcopy(listaDicio)
    for dicio in listaDicioNova:
        dicio[n].append(letras[0])

    #print(listaDicioNova+lista)
    return listaDicioNova+lista
 
    
    


def apostas(listaDicio, n):
    while True:
            dicio=listaDicio[0]
            aposta = input(str(n)+" "+dicio[n][0]+" vs "+dicio[n][1]+": ")
            if aposta.upper() in apostasPossiveis(len(aposta)):
                listaDicio = dicioMultiplier(listaDicio, n, aposta.upper())            #adicionar 1 dicionário igual ao anterior por cada letra extra da aposta (no caso de ser só uma letra, modifica-se logo esse dicionário) 
                return listaDicio
            
            else:
                #...
                print("Aposta inválida!")






def main():
    saldo=0
    print("Interface:")
    while True:
        while True:
            jornada = input("Jornada? ")
            try:
                jornada=int(jornada)
                if jornada==0:
                    return
                if jornada<1 or jornada>13:
                    #...
                    print("Jornada inválida!")
                else:
                    #saldo-=0.4
                    break
            except:
                #...
                print("Jornada inválida!")
        [contaDor, listaDicio, jornada] = interface(jornada)

        dor=0
        for dicio in listaDicio:
            print()
            print("Jornada", jornada)
            todosOsJogos = tabela(contaDor, dicio)
            premio = prize(contaDor, dicio, todosOsJogos)
            saldo-=0.4
            saldo+=premio
            print("Saldo: {:.2f} euro".format(saldo))
            dor+=1
            print(dor)
            print()
    

main()




