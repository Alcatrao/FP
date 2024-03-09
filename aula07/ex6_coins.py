# A set of functions to deal with bags of money.
#
# JMR 2017


# Face values of coins (in cents):
from copy import deepcopy


COINS = [200, 100, 50, 20, 10, 5, 2, 1]

def value(bag):
    """Return total amount in a bag."""
    valor = 0
    for coinType in bag:                #para cada tipo de moeda na carteira
        if coinType in COINS:           #verificar se o tipo de moeda é válido
            valor += coinType * bag[coinType]   #ao valor acrescenta-se o nº de moedas, cada uma com o valor coinType
    return valor


def transfer1coin(bag1, c, bag2):
    """Try to transfer one coin of value c from bag1 to bag2.
    If possible, transfer coin and return True, otherwise return False."""
    try:
        if c in bag1 and bag1[c]>0:                         #verificar que se este tipo de moeda exista na carteira1, e que há moedas deste tipo lá
            bag1[c] -= 1
            if c not in bag2:
                bag2[c] = 1
            else:
                bag2[c] += 1
            return True                                     #se o acima for verdadeiro, a transferência é possível
        return False                                        #caso contrário, não é
    except:
        return False                                        #dor, mau mesmo mau

def transfer(bag1, amount, bag2):       
    """Try to transfer an amount from bag1 to bag2.
    If possible, transfer coins and return True,
    otherwise, return False and leave bags with same values."""
    if amount == 0:
        #print("Sucesso!")
        return True
    if value(bag1) < amount:
        return False

    #Tentativa 1: começar pelas moedas maiores (tal como fazemos na vida real). Porquê? Porque nos deixa mais perto do valor desejado mais rapidamente, e conserva as moedas mais pequenas para cobrir restos menores.
    #Questão: começar com as moedas grandes pode limitar de alguma algumas possibilidades de resolver o problema? (Eu creio que não, simplesmente parece ser uma forma mais rápida de o conseguir) <- Errado
    #A questão abaixo, de transferir 60 moedas da carteira 1 para a carteira 2, mostra que ao usar a moeda de 50, o problema não é possível, porque não há moedas de 10, 5, 2, e 1 suficientes para cobrir as 10
    #moedas restantes. Mas se usarmos 3 moedas de 20, chegamos logo ao valor 60.



    '''
    bag1_clone = deepcopy(bag1)
    bag2_clone = deepcopy(bag2)


    valor = 0
    for tipoMoeda in dict(sorted(bag1.items(), reverse=True)):
        #if tipoMoeda > amount:             #estas linhas não são necessárias; o programa faz backtracking ao ultrapassar o valor desejado
        #    continue

        while valor < amount and bag1_clone[tipoMoeda]>0:
            valor += tipoMoeda
            transfer1coin(bag1_clone, tipoMoeda, bag2_clone)

            if valor == amount:
                bag1.clear()
                bag1.update(bag1_clone)
                bag2.clear()
                bag2.update(bag2_clone)
                return True

            if valor > amount:
                valor -= tipoMoeda
                transfer1coin(bag2_clone, tipoMoeda, bag1_clone)
                break

    return False
    '''


    #Tentativa 2: usar recursão e backtracking, bem como a função transfer1coin() para tentar solucionar a coisa
    bag1_clone = deepcopy(bag1)
    bag2_clone = deepcopy(bag2)


    valor = 0
    for tipoMoeda in dict(sorted(bag1.items(), reverse=True)):
        if tipoMoeda > amount:             #estas linhas não são necessárias; o programa faz backtracking ao ultrapassar o valor desejado. Update: são necessárias agora, mas não sei bem porquê
            continue

        for moeda in range(bag1[tipoMoeda]):
        #while bag1[tipoMoeda]>0:                           #o while não funciona, porque sempre que há um trackback para este tipo de moedas, a mesma moeda que foi recebida é reenviada de volta, constantemente. No ciclo for, se uma moeda não funcionar e houver trackback, essa moeda é devolvida, mas já não é reenviada de novo.
            #valor += tipoMoeda
            #if valor > amount:
            #    valor -= tipoMoeda
            #    continue
            valor = tipoMoeda                                           #é indiferente estar esta linha descomentada ou as 4 acima; os resultados são idênticos

            #print("Moeda de Ida: ", tipoMoeda, "\t fica a faltar: ",amount-valor)
            transfer1coin(bag1, tipoMoeda, bag2)
            if transfer(bag1, amount-valor, bag2) == True:
                return True

            #print("Moeda de Volta: ", tipoMoeda, "\t fica a faltar: ",amount)
            transfer1coin(bag2, tipoMoeda, bag1)

            #if transfer(bag1, amount-valor, bag2) == True:             #este transfer aqui repetiria o mesmo processo que o transfer acima; assim, se o transfer acima não der em nada (a moeda incluida não é ideal), é feito transfer para a próxima moeda (sem esta que não é ideal e cuja inclusão numa transfer não resultou) na próxima iteração desta mesma chamada à função
            #    return True                                                #Update: troquei bag1 e bag2, e o programa funciona mesmo assim. só entra em recursão infinita quando o input de amount é amount apenas - mas o programa também consegue concluir com o caso base com ele, para vários inputs de amount (amount, amount-valor, amount-tipoMoeda, ...), mas os balanços das carteiras não são bag1-amount e bag2+amount, como o pretendido (mas os resultados aparentam ser consistentes com o balanço total das 2 carteiras, pelo que creio que a sua inclusão não fosse errada ou má)


    #print("Não é possível.")
    #bag1.update(bag1_clone)                                             #caso uma transfer falhe quer com a inclusão ou não de uma moeda, é porque o erro vem de trás. Pensei ser necessário incluir este reset, mas a integridade das carteiras é assegurada pelas transfer1coin opostas que são feitas até chegar aqui
    #bag2.update(bag2_clone)
    return False        #beliscão peito, dor, cena dor, mau mesmo mau; cena coisa
    


    
                


    #usar recorrência de Matemática Discreta para solucionar o problema
    #Nº total de maneiras de ter uma quantia igual a "amount" com os diferentes tipos de moedas:
    #para "amount" = 0: nenhuma moeda serve (1 maneira)
    #para "amount" = 1: "amount-1" com 1 moeda de 1 (1 maneira)
    #"amount" = 2: 1 moeda de 2; "amount-1" com 1 moeda de 1 (2 maneiras: 1 moeda de 2; 2 moedas de 1)
    #"amount" = 3: "amount-2" com 1 moeda de 2; "amount-1" com 1 moeda de 1 (1+2 maneiras) ["amount-2" com 2 moedas de 1 já está incluído no "amount-1" com 1 moeda de 1][aqui a ordem importa: 1 moedas de 1 e 1 moeda de 2, ou 1 moeda de 2 e 1 moeda de 1 contam como 2 maneiras distintas]
    #"amount" = 4: "amount-2" com 1 moeda de 2; "amount-1" com 1 moeda de 1 (2+3 maneiras)
    #"amount" = 5: 1 moeda de 5; "amount-2" com 1 moeda de 2; "amount-1" com 1 moeda de 1 (1+3+5 maneiras)  
    #"amount" = n: "amount-n" com 1 moeda de n; "amount-200" com 1 moeda de 200; ... "amount-1" com 1 moeda de 1
    #"amount" = "amount-n" + "amount-200" + "amount-100" + ... + "amount-1"

    
            

def strbag(bag):
    """Return a string representing the contents of a bag.""" 
    # You may want to change this to produce a more user-friendly
    # representation such as "4x200+3x50+1x5+3x1=958".
    #return str(bag)
    str1=''
    for coinType in dict(sorted(bag.items(), reverse=True)):
        str2 = str(coinType)+"*"+str(bag[coinType])+" + "
        str1 = str1+str2
    str1=str1[:-3]
    str1+=" = "+str(value(bag))
    return str1



def main():
    # A bag of coins is represented by a dict of {coin: number} items
    bag1 = {1: 4, 2: 0, 5:1, 10: 0, 20: 5, 50: 4, 100: 2, 200: 1}
    bag2 = {}

    # Test the value function.
    assert value({}) == 0
    assert value({1:7, 5:2, 20:4, 100:1}) == 197

    # Test the strbag function.
    print( strbag({1:7, 5:2, 20:4, 100:1}) )        # 1x100+4x20+2x5+7x1=197
    print( strbag({1:7, 5:2, 10:0, 20:4, 100:1}) )  # 1x100+4x20+2x5+7x1=197

    print("bag1:", strbag(bag1))    # bag1: 1x200+2x100+4x50+5x20+1x5+4x1=709
    print("bag2:", strbag(bag2))    # bag2: =0
    
    print(transfer1coin(bag1, 10, bag2))    # False!
    print("bag1:", strbag(bag1))    # bag1: 1x200+2x100+4x50+5x20+1x5+4x1=709
    print("bag2:", strbag(bag2))    # bag2: =0

    print(transfer1coin(bag1, 20, bag2))    # True
    print("bag1:", strbag(bag1))    # bag1: 1x200+2x100+4x50+4x20+1x5+4x1=689
    print("bag2:", strbag(bag2))    # bag2: 1x20=20

    print(transfer1coin(bag1, 20, bag2))    # True
    print("bag1:", strbag(bag1))    # bag1: 1x200+2x100+4x50+3x20+1x5+4x1=669
    print("bag2:", strbag(bag2))    # bag2: 2x20=40

    #print("\nTransfers:\n")

    print(transfer(bag1, 157, bag2))        # True (should be easy)
    print("bag1:", strbag(bag1))    # bag1: 1x200+1x100+3x50+3x20+2x1=512
    print("bag2:", strbag(bag2))    # bag2: 1x100+1x50+2x20+1x5+2x1=197

    print(transfer(bag1, 60, bag2)) # not easy, but possible...
    print("bag1:", strbag(bag1))
    print("bag2:", strbag(bag2))

    return

if __name__ == "__main__":
    main()

