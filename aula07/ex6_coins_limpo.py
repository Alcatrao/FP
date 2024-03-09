# A set of functions to deal with bags of money.
#
# JMR 2017


# Face values of coins (in cents):
from copy import deepcopy


COINS = [200, 100, 50, 20, 10, 5, 2, 1]
contaDor=0

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
        return False                                        


def transfer(bag1, amount, bag2):       
    """Try to transfer an amount from bag1 to bag2.
    If possible, transfer coins and return True,
    otherwise, return False and leave bags with same values."""
    global contaDor
    contaDor+=1
    print(contaDor)

    if amount == 0:
        #print("Sucesso!")
        return True
    if value(bag1) < amount:
        return False
        
    for tipoMoeda in dict(sorted(bag1.items(), reverse=True)):
        if tipoMoeda > amount:                         
            continue

        for moeda in range(bag1[tipoMoeda]):
            transfer1coin(bag1, tipoMoeda, bag2)

            if transfer(bag1, amount-tipoMoeda, bag2) == True:
                print(strbag(bag1))
                n = input("Mais soluções? ")
                if n == "":
                    return True

            transfer1coin(bag2, tipoMoeda, bag1)
            break                                                           #este break faz com que todas as permutações das moedas que constituem a solução não sejam feitas a partir da 1ª (e torna esta função idêntica à nova)

    return False        

def transfer_infinite_coins(bag1, amount, bag2):      #caso uma saca tenha algum tipo de moedas infinitas, haveria pelo menos um ciclo for infinito, pelo que o programa nunca terminaria. No entanto, o amount a seria transferido poderia ser finito, e nunca haveria solução. Esta nova versão do programa tenta corrigir isso, usando todas as maneiras que esse amount pode ser alcançado, considerando que não há limite ao nº de moedas de cada tipo a utilizar. Update: é também imposto limite ao nº de moedas a utilizar, com auxílio da função transfer. Caso contrário, haveria infinitas soluções iguais. Update: com o break na função acima, ambas passam a ser idênticas, visto que só a 1ª moeda de cada tipo em cada chamada é contabilizada (pelo que moedas infinitas deixam de ser problema na 1ª função, desde que haja limite ao amount, tal como na 2ª função (o problema tem de ser reduzido com sentido (isto é, para parâmetros que possam impedir que uma chamada recursiva ocorra) em cada chamada para que não haja recursão infinita) ) 
        global contaDor
        contaDor+=1
        print(contaDor)
        if amount == 0:
            print(strbag(bag1))
            return True
        if amount < 0:
            return False

        for tipoMoeda in dict(sorted(bag1.items(), reverse=True)):
            if tipoMoeda > amount:                         
                continue
            
            if transfer1coin(bag1, tipoMoeda, bag2)==False:
                continue
            

            if transfer_infinite_coins(bag1, amount-tipoMoeda, bag2) == True:
                print(strbag(bag1))
                n = input("Mais soluções (2)? ")
                if n == "":
                    return True
                transfer1coin(bag2, tipoMoeda, bag1)
                
            else:
                transfer1coin(bag2, tipoMoeda, bag1)

            #transfer1coin(bag2, tipoMoeda, bag1)

        return False


    
            
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

    #print(transfer(bag1, 157, bag2))        # True (should be easy)
    #print("bag1:", strbag(bag1))    # bag1: 1x200+1x100+3x50+3x20+2x1=512
    #print("bag2:", strbag(bag2))    # bag2: 1x100+1x50+2x20+1x5+2x1=197

    print(transfer(bag1, 60, bag2)) # not easy, but possible...
    print("bag1:", strbag(bag1))
    print("bag2:", strbag(bag2))

    #print(transfer_infinite_coins(bag1, 60, bag2))
    #print("bag1:", strbag(bag1))
    #print("bag2:", strbag(bag2))

    return

if __name__ == "__main__":
    main()

