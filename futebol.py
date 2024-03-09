import os
import sys
    
caminho = os.path.abspath(__file__)
os.chdir(os.path.dirname(caminho))

def loadDados(ficheiro):
    lista=[]
    with open(ficheiro, 'r', encoding='utf-8') as stream:
        #stream.readline()  #mesma maneira de ignorar a 1ª linha do ficheiro que o if abaixo
        for linha in stream:
            if linha[0:4]=='rank':
                continue
            #try:    
                #palavras = tuple(linha.split(','))
                #lista.append(palavras)
            #except:
            #    print("erro em algum lado")
            #    continue
            palavras = linha.split(',')
            palavras[-1]=palavras[-1][:-1]
            lista.append(tuple(palavras))
    return lista


def dadosCountry(lista, country):
    print(" {}   {}  {}:".format("Clube", "Rank", "Score"))
    for elem in lista:
        if elem[2].lower()==country.lower():
            print("{}   {}  {}".format(elem[1], elem[0], elem[3]))


def dadosCountryWrite(lista, country, ficheiro):
    with open(ficheiro, 'w', encoding='utf-8') as stream:
        print(" {}   {}  {}:".format("Clube", "Rank", "Score"), file=stream)
        for elem in lista:
            if elem[2].lower()==country.lower():
                print("{}   {}  {}".format(elem[1], elem[0], elem[3]), file=stream)
    #sys.stdout = open("Clubes_Portugal.txt", "a")
    #dadosCountry(lista, country)
    #sys.stdout.close()     #funciona, mas o sys.stdout não volta ao default

def dictCountry_Club(lista):
    dictCountry = {}
    for tuplo in lista:
        if tuplo[2] not in dictCountry:
            dictCountry[tuplo[2]]=[]
            dictCountry[tuplo[2]].append(tuplo[1])
        else:
            dictCountry[tuplo[2]].append(tuplo[1])
    return dictCountry


def rankClimbers(lista):
    if len(lista)==1:
        return lista[0]
    meio=len(lista)//2
    metade1=rankClimbers(lista[:meio])
    metade2=rankClimbers(lista[meio:])

    #print(metade1[6]+metade1[4])
    if int(metade1[6]+metade1[4])>=int(metade2[6]+metade2[4]):
        return metade1
    return metade2


def clubInfo(lista, clube):
    dados=None
    if len(lista)==1:
        if clube==lista[0][1]:
            dados=lista
        return dados
        

    meio=len(lista)//2
    metade1=clubInfo(lista[:meio], clube)
    metade2=clubInfo(lista[meio:], clube)

    if isinstance(metade1, list):
        return metade1
    if isinstance(metade2, list):
        return metade2
    s="Erro. O clube não existe."
    return s


def meanRank(lista):
    dictCountry={}
    if len(lista)==1:
        if lista[0][3] not in dictCountry:
            dictCountry[lista[0][2]]=[int(lista[0][0])]
        else:
            dictCountry[lista[0][2]]+=[int(lista[0][0])]
        return dictCountry

    meio=len(lista)//2
    metade1=meanRank(lista[:meio])
    metade2=meanRank(lista[meio:])

    for chave in metade1.keys():
        if chave in metade2:
            metade2[chave]+=metade1[chave]
        else:
            metade2[chave]=metade1[chave]
    
    #print(metade2)
    for chave in metade2.keys():
        sum=0
        ranks=metade2[chave]
        for rank in ranks:
            sum+=rank
        sum=sum/len(metade2[chave])
        metade2[chave] = [sum]

    return metade2
    
            
def menu():
    lista=loadDados('Soccer_Football Clubs Ranking.csv')
    while True:
        while True:
            print()
            print("1 - LoadFicheiro(ficheiro)")
            print("2 - dadosCountry(lista, country)")
            print("3 - dadosCountryWrite(lista, country, ficheiro)")
            print("4 - dictCountry_club(lista)")
            print("5 - rankClimbers(lista)")
            print("6 - clubInfo(lista, clube)")
            print("7 - meanRank(lista)")
            print(" 0 - exit()")
            op = input("Que opção deseja ativar? ")
            print()

            if op=="1":
                try:
                    ficheiro=input("Indique o nome do ficheiro que pretende carregar: ")
                    lista=loadDados(ficheiro)
                    for elem in sorted(lista, key=lambda x: int(x[4])):
                        print(elem)
                    print("\n")
                    break
                except:
                    print("Ficheiro inválido.")

            if op=="2":
                while True:
                    country=input("Indique o país cujos clubes pretende saber: ")
                    dadosCountry(lista, country)
                    #print("\n")
                    break

            if op=="3":
                country=input("Indique o país cujos clubes pretende guardar num ficheiro ('país.txt'): ")
                ficheiro=country+".txt"
                dadosCountryWrite(lista, country, ficheiro)
                #print("\n")
                break
            
            if op=="4":
                dictCountry = dictCountry_Club(lista)
                #print("\n")
                break

            if op=="5":
                topClimber = rankClimbers(lista)
                print("\nTop Rank Climber:",topClimber)
                #print("\n")
                break

            if op=="6":
                clube=input("Insira o nome do clube de que pretende ver as informações: ")
                print("\nExiste o clube '"+str(clube)+"'?", clubInfo(lista, clube))
                #print("\n")
                break

            if op=="7":
                rankMed = meanRank(lista)
                for chave, valor in rankMed.items():
                    valor=valor[0]
                    rankMed[chave]=valor
                for elem in sorted(rankMed, key=lambda x: (rankMed[x], x)):
                    print(elem+":",rankMed[elem])
                print("\n")
                break

            if op=="0":
                exit()

menu()

    






""" 
def main():
    lista=loadDados('Soccer_Football Clubs Ranking.csv')
    for elem in sorted(lista, key=lambda x: int(x[4])):
        print(elem)

    #dadosCountry(lista, "Portugal")
    dadosCountryWrite(lista, "Portugal", "Portugal.txt")
    dictCountry = dictCountry_Club(lista)
    ''' for key, value in dictCountry.items():
        print(key+":")
        for valueSplit in value:
            print("     "+valueSplit) '''
    topClimber = rankClimbers(lista)
    print("\nTop Rank Climber:",topClimber)
    
    clube="Silkeborg"
    print("\nExiste o clube '"+str(clube)+"'?", clubInfo(lista, clube))

    print()
    rankMed = meanRank(lista)
    for chave, valor in rankMed.items():
        valor=valor[0]
        rankMed[chave]=valor
    for elem in sorted(rankMed, key=lambda x: (rankMed[x], x)):
        print(elem+":",rankMed[elem])
        

main()

 """

