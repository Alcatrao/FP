# A set of functions to deal with bags of money.
#
# JMR 2017


# Face values of coins (in cents):
from copy import deepcopy
import sys


COINS = [200, 100, 50, 20, 10, 5, 2, 1]
#contaDor = 0

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
            return True
        else:                                                 #se o acima for verdadeiro, a transferência é possível
            return False                                        #caso contrário, não é
    except:
        return False                                        #dor, mau mesmo mau

def transfer(bag1, amount, bag2, iteration=0):
    #global contaDor
    #contaDor+=1
    #print(contaDor)
    """Try to transfer an amount from bag1 to bag2.
    If possible, transfer coins and return True,
    otherwise, return False and leave bags with same values."""
    if amount == 0:
        print("Atualização (", iteration,") : ", "Sucesso!")
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
    for tipoMoeda in dict(sorted(bag1_clone.items(), reverse=True)):
        if tipoMoeda > amount:             #estas linhas não são necessárias; o programa faz backtracking ao ultrapassar o valor desejado. Update: são necessárias agora, mas não sei bem porquê. Update: não são necessárias; simplesmente diminuem a dimensão do problema ao contar apenas algumas moedas, em vez de literalmente todas em todas as iterações.
            continue

        for moeda in range(bag1_clone[tipoMoeda],  0, -1):
        #while bag1[tipoMoeda]>0:                           #o while não funciona, porque sempre que há um trackback para este tipo de moedas, a mesma moeda que foi recebida é reenviada de volta, constantemente. No ciclo for, se uma moeda não funcionar e houver trackback, essa moeda é devolvida, mas já não é reenviada de novo.
            #valor += tipoMoeda
            #if valor > amount:
            #    valor -= tipoMoeda
            #    continue
            valor = tipoMoeda                                           #é indiferente estar esta linha descomentada ou as 4 acima; os resultados são idênticos

            #print("Moeda de Ida: ", tipoMoeda, "\t fica a faltar: ",amount-valor)
            print("Atualização (", iteration,") : ", strbag(bag1), "(vai mandar uma moeda de:", tipoMoeda, ")")
            transfer1coin(bag1, tipoMoeda, bag2)
            #transfer1coin(bag1_clone, tipoMoeda, bag_dor)
            
            if transfer(bag1, amount-valor, bag2, iteration+1) == True:     #os resultados aparentemente repetidos, devem-se a moedas de volta a serem contadas na próxima chamada da função que não eram as últimas moedas desse tipo a serem dadas. Ao voltarem, será feita outra chamada a essas moedas (em que o nº de moedas é o mesmo), mas já será na última/próxima iteração da função que faz essa chamada, e não na penúltima/mesma, como antes (por isso é que não ocorre recursão infinita).
                #print(tipoMoeda, "  ", moeda, " ",strbag(bag1))
                n=input("More? ")
                if n == '':
                    return True
                #return True

            #print("Moeda de Volta: ", tipoMoeda, "\t fica a faltar: ",amount)
            transfer1coin(bag2, tipoMoeda, bag1)
            print("Atualização (", iteration,") (de volta) : ", strbag(bag1), "(recebeu de volta a moeda de:", tipoMoeda, ")")

            #if transfer(bag1, amount-valor, bag2) == True:             #este transfer aqui repetiria o mesmo processo que o transfer acima; assim, se o transfer acima não der em nada (a moeda incluida não é ideal), é feito transfer para a próxima moeda (sem esta que não é ideal e cuja inclusão numa transfer não resultou) na próxima iteração desta mesma chamada à função
            #    return True                                                #Update: troquei bag1 e bag2, e o programa funciona mesmo assim. só entra em recursão infinita quando o input de amount é amount apenas - mas o programa também consegue concluir com o caso base com ele, para vários inputs de amount (amount, amount-valor, amount-tipoMoeda, ...), mas os balanços das carteiras não são bag1-amount e bag2+amount, como o pretendido (mas os resultados aparentam ser consistentes com o balanço total das 2 carteiras, pelo que creio que a sua inclusão não fosse errada ou má)


    #print("Não é possível.")
    #bag1.update(bag1_clone)                                             #caso uma transfer falhe quer com a inclusão ou não de uma moeda, é porque o erro vem de trás. Pensei ser necessário incluir este reset, mas a integridade das carteiras é assegurada pelas transfer1coin opostas que são feitas até chegar aqui
    #bag2.update(bag2_clone)
    return False        #beliscão peito, dor, cena dor, mau mesmo mau; cena coisa
    
    #tirando as moedas de 50 para irmos logo para as de 20, sucede-se o procedimento seguinte: a 1ª chamada da função tem 3 moedas de 20, manda a 1º (1/3); a 2ª chamada da função tem 2 moedas de 20 (1/2), manda a 1ª;
    #a 3ª chamada da função tem 1 moeda de 20, manda a 1ª e única (1/1). A 4º chamada à função é para o amount 60-20-20-20 = 0, pelo que retorna imediatamente com True. Volta-se para a 3ª chamada da função, que pede
    #input; ao inserir algo, a função procede como se não tivesse recebido True da chamada que fez à função (4ª), pelo que recebe 1 moeda de 20, mas já mandou a única moeda de 20 que inicialmente tinha no ciclo for
    #para mandar, pelo que não manda outra vez a moeda de 20 (mandaria 2/1 moedas; o denominador mostra quantas vezes pode mandar dor), e manda ao invés a próxima moeda disponível, 1 moeda de 5. 
    #Algumas chamadas são feitas a partir daqui, até exaustar todas as moedas possíveis (inferiores aos amounts que essas chamadas receberam), sem nunca chegar ao amount=0, que só se consegue com 3 moedas de 20. As chamadas da função com 0 moedas a percorrer, seja por
    #não haver moedas disponíveis para percorrer, quer por haverem, mas já terem sido todas percorridas no ciclo for, terminam com um return False.
    #Todas as chamadas feitas a partir da 3ª chamada, que após mandar o seu 20, e este ter sido recusado e reenviado de volta, enviou 1 moeda de 5 (e não a de 20 outra vez), retornam após percorrerem todos os seus
    #elementos válidos (moedas com valor inferior ao amount) e não encontraram amount=0. A 3ª chamada também já percorreu todas as moedas que devia no seu ciclo for, e também retorna, devolvendo a última moeda que usou (1 moeda de 1).
    #A 2ª chamada, que inicialmente tinha mandado 1 moeda de 20 de 2 disponíveis no seu ciclo for (1/2) e feito uma 3ª chamada que inicialmente deu 20 (e o 1º amount=0) e depois o retornou e percorreu a função até ao
    #fim (e retornou False), recebe de volta o seu 20, e agora manda a 2ª moeda de 20 (2/2) (tendo recebido a moeda de 20 da 3ª chamada logo após o input desta ter sido usado para recusar a moeda). É invocada uma nova 3ª chamada, que tem 1 moeda
    #de 20 para usar, e usa, o que origina um prompt de input, que novamente é usado para recusar a moeda de 20 (que resultou no 2º amount=0). A moeda de 20 é devolvida, e várias chamadas surgem a partir da 3ª chamada e das suas chamadas e das
    #chamadas destas, mas todas retornam False. Após percorrer todos os seus elementos, a 3ª chamada também retorna False.
    #A 2ª chamada recebe novamente de volta a moeda de 20 que enviou, ficando agora outra vez com 2 moedas de 20. No entanto, já atingiu o limite de moedas de 20 que podia mandar com base no seu ciclo for (2/2), e mesmo
    #tendo 2 moedas de 20, não envia nenhuma destas, e envia a próxima que está prevista no seu ciclo for (1 moeda de 5). Nenhuma das chamadas feitas a partir do envio desta moeda conseguem atingir amount=0, pelo que todas
    #retornam, e a moeda de 5 é devolvida, e a 2ª chamada envia 1 moeda de 1. De igual modo, todas estas retornam, e após enviar todas as suas moedas de 1, a 2ª chamada também retorna (Falso).
    #A 1º chamada, que enviou 1 moeda de 20 de um limite de 3 (1/3), vê essa moeda a ser devolvida logo após a 2ª chamada retornar Falso. Com 3 moedas de 20 disponíveis, manda a 2ª (2/3), pois já tinha mandado a 1ª no seu ciclo
    #for e não o pode fazer novamente. A partir desta 2ª moeda de 20, é feita outra 2ª chamada, que tem 2 moedas de 20 para usar, e esta chama ainda outra 3ª chamada, que tem 1 moeda de 20 para usar, e usa, dando origem
    #ao 3º prompt de input (3ª amount=0). Recusado este resultado, novamente, a moeda de 20 usada na 3ª chamada é devolvida, e esta chamada eventualmente percorre a sua última moeda e termina (retorna Falso).
    #A 2ª chamada, utiliza então a sua 2ª e última moeda de 20 (2/2), e é invocada logo uma 3ª chamada com 1 moeda de 20 para usar, e usa, originando o 4ª prompt (4º amount=0). Doloroso este resultado, é rejeitado,
    #e eventualmente a 3ª chamada termina, e à 2ª chamada é devolvida a moeda de 20 que mandou, e após percorrer todos os outros elementos que pode usar, a 2ª chamada também termina.
    #A 1ª chamada, logo após a 2ª retornar com Falso, recebe a moeda de 20 que tinha mandado, ficando agora com 3 moedas de 20, mas só pode enviar uma última moeda de 20 (3/3), e faz-o. Surge uma 2ª chamada que usa
    #uma das 2 moedas de 20 (1/2) que pode usar e invoca uma outra 3ª chamada, que usa a única moeda de 20 (1/1) que pode usar, o que origina o 5º prompt (5º amount=0). Recusa-se, (com muita dor mesmo má e dor),
    #este resultado obtido, pelo que a moeda de 20 usada pela 3ª chamada é devolvida. Esta chamada eventualmente retorna, e logo após o fazer, a 2ª chamada recebe a moeda de 20 que enviou e manda a outra (2/2),
    #e logo a seguir chama ainda outra 3ª chamada, que pode usar 1 moeda de 20 1 única vez, e que ao usá-lo, origina imediatamente a seguir o 6º e último amount=0. Rejeitado este resultado, a moeda de 20 da 3ª
    #chamda é devolvida. Esta chamada percorre todos os outros elementos para pouco efeito, e termina, o que causa a 2ª chamada receber de volta a moeda de 20 que enviou e a percorrer todos os outros elementos diferentes
    #de 20, visto que já não pode usar mais este tipo de moedas. A 2ª chamada também termina (return Falso) após percorrer todos os seus elementos, o que faz com que a 1ª chamada receba a última moeda de 20 que mandou,
    #tendo agora 3 moedas de 20 na sua posse. No entanto, o seu ciclo for já atingiu a última iteração de moedas de 20, pelo que passa para o próximo tipo de moedas a percorrer (a moeda de 5), e não envia mais nenhuma
    #moeda de 20. Como não envia mais nenhuma moeda de 20, todas as chamadas seguintes não terão fruto, resultando apenas em dor mesmo dor, e após percorrer todos os seus elementos, a 1ª chamada termina, e com ela
    #termina todo este procedimento.
    #No caso de algum dos prompts ser aceite, 1 das moedas de 20 passa para o saco2 e não é mais devolvida, pelo que ficam só 2 moedas de 20 na caso1, pelo que não é possível haver outra combinação de 3 moedas de 20 
    #para dar amount=0. Os ciclos for têm isto em conta, e passam à frente de iterações que já não podem realizar devido à remoção de elementos. 
    #Beliscão no peito direito, dor mesmo dor, cena dor; cena coisa e outra cena e cena e não e coisa, dor.


    
                


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
    bag1 = {1: 4, 2: 0, 5:1, 10: 0, 20: 5, 50: 0, 100: 2, 200: 1}
    bag2 = {}
    

    global bag_dor
    bag_dor={}



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

    #print(transfer(bag1, 157, bag2))        # True (should be easy)
    #print("bag1:", strbag(bag1))    # bag1: 1x200+1x100+3x50+3x20+2x1=512
    #print("bag2:", strbag(bag2))    # bag2: 1x100+1x50+2x20+1x5+2x1=197

    print(transfer(bag1, 60, bag2)) # not easy, but possible...
    print("bag1:", strbag(bag1))
    print("bag2:", strbag(bag2))

    return

if __name__ == "__main__":
    main()

