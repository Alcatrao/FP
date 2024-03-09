#Uma função recursiva chama-se a ela própria. Isto ocorre para qualquer função/chamada recursiva, a não ser que alguma instrução anterior impeça que uma subchamada ocorra, ou algum erro ocorra, ou alguma coisa mal aconteça. Cena dor. Beliscão dor.

#Uma função que faça uma chamada recursiva em qualquer caso, que não dependa de nada (que seja a primeira instrução dentro da função, por exemplo), chama essa função sempre que é executada. O mesmo se aplica às subchamadas seguintes, chamam a função sempre, porque é o que elas fazem, em qualquer caso, a não ser que ocorra algum erro, ou alguma coisa corra mal.
#Mas se a chamada recursiva estiver dependente de uma condição, seja um if, ou dentro de um for loop, só é chamada se essa condição o permitir (se o for loop exercutar a chamada, mas não tiver nenhum elemento, o loop termina assim que começa, sem fazer nenhuma iteração/chamada).
#Na função original, a chamada recursiva dependia de 1 loop que dependia de outro. Se um deles não tivesse elementos, a chamada não era feita.
#Na nova função, a chamada só depende de um loop, pelo que só não é feita a chamada se esse loop tiver 0 elementos. Embora a função original tenha mais complexidade (2 loops em vez de 1), esta complexidade oferecia mais maneiras de evitar complexidade infinita/chamadas recursivas sem fim.
#Como o loop da 2ª função não era reduzido em cada chamada, o seu nº de elementos mantinha-se constante, nunca chegava a 0 onde o seu corpo não era executado, e a chamada recursiva era feita constantemente, pois dependia apenas deste loop.
#Na função original, o este loop também se mantinha constante, mas o seu corpo tinha um 2º loop, que diminuía em cada chamada (podendo chegar a 0, onde as instruções dentro de si não eram executadas), no qual estava a chamada recursiva. Se este loop tiver 0 elementos, o seu corpo, onde se encontra a chamada recursiva, não é executado.
#Assim, a função nova executa a ela própria sem fim, pois não há maneira de não executar a chamada recursiva, a não ser que o loop tenha 0 elementos (o nº de elementos nunca diminui de chamada para chamada, pelo que nunca chega a 0, pelo que a chamada é feita constantemente).
#A função original executa até que o 2º ciclo, que diminui de chamada para chamada, atinja 0 elementos, situação na qual a chamada recursiva não ocorre, e a chamada termina.


def amount(x):
    if x==0 or x==1:
        return 1
    if x<0:
        return 0
    
    return amount(x-200) + amount(x-100) + amount(x-50) + amount(x-20) + amount(x-10) + amount(x-5) + amount(x-2) + amount(x-1)
#"amount" = "amount-n" + "amount-200" + "amount-100" + ... + "amount-1"

print(amount(5))

def todas_as_maneiras(x):       #para a função original, só com x moedas do tipo 1 (tipoMoeda[1] = x)
    if x==0:
        return 0
    return x+x*todas_as_maneiras(x-1)   #faz x chamadas(x-1) (1 por cada moeda disponível na função, que varia (diminui por 1) de chamada para chamada), e por cada 1 dessas chamadas(x-1) faz (x-1) chamadas(x-2)

def todas_as_maneiras_nova(x, y):  #para a função nova, moedas do tipo 1 (x) 5 vezes (y) (x = tipoMoedas = [1(1),1,1,1,1(5),...,1(x)])
    if y==0:
        return 0
    return x+x*todas_as_maneiras_nova(x,y-1)                        #faz x chamadas(x, y-1) (1 por cada tipoMoeda (que não varia)), e por cada 1 dessas chamadas(x, y-1), faz x chamadas(x,y-2)



def amount_lista(x, tipoMoedas, maneira, maneiras):    #em vez de mostrar o nº de maneiras de ter "amount" com os tipos de moedas disponibilizados, mostras as combinações que correspondem a essas maneiras
    global contaDor
    contaDor+=1
    print(contaDor)
    if x == 0:
        #print("Sucesso!")
        return True
    if x < 0:
        return False

    for moeda in tipoMoedas:
        if amount_lista(x-moeda, tipoMoedas, maneira+[moeda], maneiras)==True:
            #print(maneira+[moeda])
            #print(maneiras)
            maneiras.append(maneira+[moeda])

    return maneiras

""" def amount_lista(x, tipoMoedas):    #em vez de mostrar o nº de maneiras de ter "amount" com os tipos de moedas disponibilizados, mostras as combinações que correspondem a essas maneiras
    global contaDor
    contaDor+=1
    print(contaDor)

    maneiras=[]

    if x == 0:
    #    #print("Sucesso!")
        return []
    if x < 0:
        return []

    for moeda in tipoMoedas:
        #try:
        maneira1=[moeda]+amount_lista(x-moeda, tipoMoedas) #para tipoMoedas=[1]: chamada original amount_lista(5, ...) ---> (aqui) ---> amount_lista(5-1=4, ...) -> amount_lista(4-1=3, ...) -> amount_lista(3-1=2, ...) -> amount_lista(2-1=1, ...) -> amount_lista(1-1=0, ...)=return True (se fosse menor que 0, também retornava, mas era com False). 6 chamadas total
                                            #(nova função)  #para tipoMoedas=[1,2]: amount(5) :-> amount(5-1=4) -> amount(4-1=3) -> amount(3-1=2) -> amount(2-1=1) -> amount(1-1=0) = return True
                                                            #                                                                                                     -> amount(1-2=-1) = return False
                                                            #                                                                                    -> amount(2-2=0) = return True
                                                            #                                                                   -> amount(3-2=1) -> amount(1-1=0) = return True
                                                            #                                                                                    -> amount(1-2=-1) = return False
                                                            #                                                  -> amount(4-2=2) -> amount(2-1=1) -> amount(1-1=0) = return True
                                                            #                                                                                    -> amount(1-2=-1) = return False
                                                            #                                                                   -> amount(2-2=0) = return True
                                                            #                                  -> amount(5-2=3) -> amount(3-1=2) -> amount(2-1=1) -> amount(1-1=0) = return True
                                                            #                                                                                     -> amount(1-2=-1) = return False
                                                            #                                                                    -> amount(2-2=0) = return True
                                                            #                                                   -> amount(3-2=1) -> amount(1-1=0) = return True
                                                            #                                                                    -> amount(1-2=-1) = return False.   Chamadas total=25     
                                                        
                                                        #x=5; tipoMoedas=[1]: 1(5)+1(4)+1(3)+1(2)+1(1)+1(0) = 6: cada chamada faz 1 chamada com 1 valor a menos (quando x=0, a função não faz nenhuma chamada e termina)
                                                        
                                                        #para a outra função, com x=5; tipoMoedas[1]=5: 1(5)+5(4)+5*4(3)+5*4*3(2)+5*4*3*2(1)+5*4*3*2*1(0) = 326
                                                        
                                                        #x=5; tipoMoedas=[1,1]: 1(5)+2(4)+2*2(3)+2*2*2(2)+2*2*2*2(1)+2*2*2*2*2(0) = 63: cada chamada faz 2 subchamadas com 1 valor a menos
        
        #except:
            #continue
        if sum(maneira1)==x:
            print(maneira1)
            #maneiras=maneiras.append(maneira1)
        #maneira2=amount_lista(x-moeda, tipoMoedas)
        #print(maneira2)
        #if sum(maneira2)==x:
        #    maneiras.append(maneira1)
    #print("Total", maneira1)

    return maneiras     #assim também dá 37 chamadas; com a maneira2 descomentada, dá 303 ou 121 ou 415 (x=5, tipoMoedas=[1,2,5]) """





#A função original faz, se tiver tipos de moeda, e moedas para cada 1 desses tipos, 1 chamada recursiva com 1 moeda a menos e com 1 amount-esse_valor. Se não tiver moedas, nem tipos de moeda, retorna. Caso a subchamada retorne, faz outra chamada recursiva para a próxima moeda, com a outra moeda de volta mas com esta a menos, e com 1 amount-este_valor. Se não houver próxima moeda, vai para o próximo tipo de moeda. Se não houver 1 próxima moeda ou tipo de moeda, retorna.
    #Nesta função, para cada subchamada, altera-se o nº de moedas, e o amount. O tipo de moedas mantém-se igual. Se o tipo de moeda (mantém-se constante), ou o nº de moedas (diminui), ou o amount (diminui, mas sem fim) forem infinitos, a recursão pode ser infinita.
    #Nesta função, quando se escreve amount(0), o 0 refere-se ao nº de moedas, e não ao valor. O nº de iterações do ciclo é igual a este valor, pelo que se for 0, não há mais iterações, nem chamadas recursivas. 
#A função nova faz, se tiver tipos de moeda, 1 chamada recursiva com 1 amount-esse_valor. Se não tiver tipos de moeda, ou o amount for <=0, retorna. Caso a subchamada retorne, passa para o próximo tipo de moeda, e faz 1 chamada com amount-este_valor. Se não houver próximo tipo de moeda, retorna. 
    #Nesta função, para cada subchamada, altera-se o amount apenas. Se o tipo de moedas (mantém-se constante), ou o amount (diminui, mas sem fim) forem infinitos, a recursão pode ser infinita.
    #Nesta função, quando se escreve amount(0), o 0 refere-se ao valor, e não ao nº de moedas. Se não houver limite ao amount, a recursão é infinita. O amount e o tipo de moedas podem tornar a recursão infinita, se não tiverem limite. Na função acima, o nº de moedas, se não for infinito, pode travar a recursão.
#Conclusão: a função original entra em recursão infinita com nº de tipos de moeda infinito (mantém-se de chamada para chamada), ou com nº de moedas infinito (que diminuem de chamada para chamada, desde que seja de um nível de recursão para um superior. No mesmo ciclo for, todas as chamadas têm o mesmo nº de moedas).
#           a função nova entra em recursão infinita com nº de tipos de moeda infinito (mantém-se de chamada para chamada; esta parte da função é igual à de cima), ou com amount sem limite (que diminui de chamada para chamada).
#               Em termos de código e funcionamento: a função original retorna quando o ciclo for das moedas acaba (se for infinito, não acaba, e a função não retorna) e o ciclo do tipo de moedas acaba (se for infinito, não acaba; o ciclo das moedas não acaba, este também não acaba, e função não retorna).
#               A função nova retorna quando o ciclo for do tipo de moedas acaba (nunca acaba, a não ser que o tipo de moedas seja 0 para começar. Se for infinito nunca acaba, se for finito, a chamada feita dentro dele terá o mesmo nº de tipos de moeda, e o problema não diminuiu neste sentido, que é o sentido que pode retornar a função. Na função acima, que também é igual em ter um ciclo destes a fazer chamadas que não diminuem este parâmetro, o ciclo dos tipos de moeda pode terminar se o nº de moedas for finito).
#                   A função original precisa de ter 1 nº de moedas finito (e 1 nº de tipos de moedas finito) para terminar.
#                   A função nova precisa de ter 1 nº de tipos de moedas finito e um limite ao amount para terminar.
#                       Se a função original tiver um break no ciclo das moedas, mesmo que estas sejam infinitas, pode terminar. E assim só o tipo de moedas for infinito é que a função não termina.
#                       Se a função nova tiver um limite ao amount, mesmo que o nº de tipos de moeda sejam infinitos, pode terminar. Só se o amount for infinito é que não termina.

x=5
#tipo_moedas=[1,1,1]    #para a 2ª versão da nova função. Embora o nº de iteraões de ambas as versão serem iguais
tipo_moedas=[1,2]
maneira = []
maneiras = []
contaDor=0

print(amount_lista(x, tipo_moedas, maneira, maneiras))
#print(amount_lista(x, tipo_moedas))        #para a 2ª versão da nova função
print("Todas as maneiras: ",todas_as_maneiras(4)+1)                 #para tipo_moedas={1: 4}: nº chamadas=1+4+4*3+4*3*2+4*3*2*1=65 (a função retorna quando o nº de moedas é 0; se não for, faz uma chamada recursiva com 1 moeda a menos (o tipo de moedas permanece igual) (no limite, por cada moeda que tem))
print("Todas as maneiras nova: ",todas_as_maneiras_nova(4, 4)+1)    #para tipo_moedas=[1,1,1,1]; amount=4: nº chamadas=1+4+4*4+4*4*4+4*4*4*4=341 (a função retorna quando o amount <= 0; se não for, faz uma chamada recursiva com amount-1 (o tipo de moedas permanece igual) (no limite, por cada tipo de moeda que tem))