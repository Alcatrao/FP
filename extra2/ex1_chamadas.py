import os


def menu():

    listaChamadas={}

    while True:
        print("1) Registar chamada")
        print("2) Ler ficheiro")
        print("3) Lista clientes")
        print("4) Fatura")
        print("5) Terminar")

        op = input("Opção? ")

        if op=="1":
            registarChamada(listaChamadas)
        elif op=="2":
            lerFicheiro(listaChamadas)
        elif op=="3":
            listaClientes(listaChamadas)
        elif op=="4":
            fatura(listaChamadas)
        elif op=="5":
            print("Programa terminado com sucesso.")
            exit()
        else:
            print("Opção inválida. Tente novamente.")





def numberValidator(num):   #esta função retorna True apenas se o número dado for válido. Se não for, retorna False
    try:
        if num[0]=="+":
            if len(num)<4 or len(num)>12:
                return False
            digitos=int(num[1:])
            return True
        else:
            if len(num)<3 or len(num)>9:
                return False
            digitos=int(num)
            return True
    except:
        return False





def registarChamada(listaChamadas):
    while True:
        try:
            telOri=input("Telefone origem? ")
            if numberValidator(telOri)==True:
                break
        except:
            ...

    while True:
        try:
            telDes=input("Telefone destino? ")
            if numberValidator(telDes)==True:
                break
        except:
            ...

    while True:
        try:
            Dur=input("Duração (s)? ")
            Dur=int(Dur)
            break
        except:
            ...
    
    if telOri not in listaChamadas:
        listaChamadas[telOri]=[[telDes, Dur]]
    else:
        listaChamadas[telOri].append([telDes, Dur])





def lerFicheiro(listaChamadas):
    file=input("Ficheiro? ")

    caminhoAntigo=os.getcwd()
    caminhoNovo=os.path.dirname(os.path.abspath(__file__))
    os.chdir(caminhoNovo)

    if os.path.isfile(os.path.join(caminhoNovo, file))==False:
        print("Este ficheiro não existe.")
        return


    with open(file, 'r', encoding="utf-8") as stream:
        for linha in stream:
            try:
                palavras=linha.split()
                telOri=palavras[0]
                telDes=palavras[1]
                dur=palavras[2]

                if numberValidator(telOri)==False:
                    continue
                if numberValidator(telDes)==False:
                    continue
                dur=int(dur)

                if telOri not in listaChamadas:
                    listaChamadas[telOri]=[[telDes, dur]]
                else:
                    listaChamadas[telOri].append([telDes, dur])

            except:
                continue

    os.chdir(caminhoAntigo)






def listaClientes(listaChamadas):
    print("Clientes:", end=" ")
    for key in sorted(listaChamadas.keys()):
        print(key, end=" ")
    print()





def fatura(listaChamadas):
    telOri=input("Cliente? ")
    if telOri not in listaChamadas:
        print("Cliente não encontrado.")
    else:
        total=0
        print("Fatura do cliente", telOri)
        print("{:<20s} {:>10s} {:>13s}".format("Destino", "Duração", "Custo"))
        for registo in listaChamadas[telOri]:
            if registo[0][0]=="+":
                taxa=0.8/60
            elif registo[0][0]=="2":
                taxa=0.02/60
            elif registo[0][0:2]==telOri[0:2]:
                taxa=0.04/60
            else:
                taxa=0.1/60

            custo=registo[1]*taxa
            total+=custo

            print("{:<20s} {:>10d} {:>13.2f}".format(registo[0], registo[1], custo))

        print("{:>31s} {:>13.2f}".format("Total:", total))





def main():
    menu()





main()
#Meu número: 916879326
#Número Márcia: 935975688