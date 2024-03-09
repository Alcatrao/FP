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

def todas_as_maneiras_nova(x, y):  #para a função nova, moedas do tipo 1 5 vezes (tipoMoedas = [1(1),1,1,1,1(5),...,1(x)])
    if y==0:
        return 0
    return x+x*todas_as_maneiras_nova(x,y-1)                        #faz x chamadas(x, y-1) (1 por cada tipoMoeda (que não varia)), e por cada 1 dessas chamadas(x, y-1), faz x chamadas(x,y-2)


""" 
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
 """
def amount_lista(x, tipoMoedas):    #em vez de mostrar o nº de maneiras de ter "amount" com os tipos de moedas disponibilizados, mostras as combinações que correspondem a essas maneiras
    global contaDor
    contaDor+=1
    print(contaDor)

    maneiras=[]

    if x == 0:
        #print("Sucesso!")
        return []
    if x < 0:
        return []

    for moeda in tipoMoedas:
        #try:
        maneira1=[moeda]+amount_lista(x-moeda, tipoMoedas) #para tipoMoedas=[1]: chamada original amount_lista(5, ...) ---> (aqui) ---> amount_lista(5-1=4, ...) -> amount_lista(4-1=3, ...) -> amount_lista(3-1=2, ...) -> amount_lista(2-1=1, ...) -> amount_lista(1-1=0, ...)=return True (se fosse menor que 0, também retornava, mas era com False). 6 chamadas total
                                                            #para tipoMoedas=[1,2]: amount(5) :-> amount(5-1=4) -> amount(4-1=3) -> amount(3-1=2) -> amount(2-1=1) -> amount(1-1=0) = return True
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

    return maneiras     #assim também dá 37 chamadas; com a maneira2 descomentada, dá 303 ou 121 ou 415 (x=5, tipoMoedas=[1,2,5])




x=5
tipo_moedas=[1, 1, 1]
maneira = []
maneiras = []
contaDor=0

#print(amount_lista(x, tipo_moedas, maneira, maneiras))
print(amount_lista(x, tipo_moedas))
print("Todas as maneiras: ",todas_as_maneiras(5)+1)
print("Todas as maneiras nova: ",todas_as_maneiras_nova(3, 5)+1)