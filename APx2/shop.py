# Pode correr o programa sem argumentos:
#   python3 shop
# ou passando outros ficheiros de produtos como argumento:
#   python3 shop produtos1.txt ...

import os


def loadDataBase(fname, produtos):
    """Lê dados do ficheiro fname e atualiza/acrescenta a informação num
    dicionário de produtos com o formato {código: (nome, secção, preço, iva), ...}.
    """

    original_directory = os.getcwd()                                               #vamos mudar de diretoria para poder abrir ficheiros com caminhos relativos; no final da função, mudamos de volta para a diretoria original
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    caminho = fname

    #caminho = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)   #evita problemas a abrir o ficheiro (mas impede o uso de caminhos absolutos, e suponho que haja uma possibilidade grande de que os testes mais avançados usem ficheiros alheios aos que nos deram)                                  
    
    with open(caminho, encoding='utf-8') as stream:
        while True:
            linha = stream.readline()                                           #ler linha da stream
            if linha == '':                                                     #se a linha lida for a última, podemos terminar este processo e retornar o dicionário produtos
                #print(produtos)
                os.chdir(original_directory)
                return produtos
            palavras = linha.split(';')                                         #para cada linha, vamos separá-la numa lista com várias palavras (sendo o símbolo ';' usado como separador)
            if palavras[0]=='CODIGO':                                           #a 1ª linha não é de interesse, podemos ignorá-la
                continue
            if palavras[0] not in produtos:                                     #se o código não tiver no dicionário, fazemos uma atualização a este com 1 tuplo com a restante informação correspondente a esse código (nome, categoria, preço, taxa)
                try:
                    produtos[palavras[0]] = (palavras[1], palavras[2], float(palavras[3]), float(palavras[4][:-2])/100)           #para o palavras[4], não se quer nem o símbolo '%' nem o símbolo de final de linha '\n', por isso é que uso [:-2] no final
                except:
                    continue




def registaCompra(produtos):
    """Lê códigos de produtos (ou códigos e quantidades),
    mostra nome, quantidade e preço final de cada um,
    e devolve dicionário com {codigo: quantidade, ...}
    """
    cesto={}                                                                    #dicionário que representa o cesto de compras
    while True:
            codigo = input("Code? ")
            if codigo == "":
                #print(cesto)
                return cesto


            codigo_quantidade = codigo.split()                                  #verificar se o input é um código, ou é um código e uma quantidade

            if len(codigo_quantidade)==1:
                try:
                    if codigo in produtos:
                        print(produtos[codigo][0],  1,  format(produtos[codigo][2]+produtos[codigo][2]*produtos[codigo][3], '.2f'))          #imprimir nome do produto a que o código se refere, bem como a sua quantidade e preço (com IVA)

                        if codigo not in cesto:                                     #verificar se o produto já estava presente no cesto, ou se está a ser adicionado pela 1ª vez
                            cesto[codigo]=1
                        else:
                            cesto[codigo]+=1
                except:
                    continue


            if len(codigo_quantidade)==2:
                try:
                    codigo = codigo_quantidade[0]                               #caso o input contenha 2 componentes (separadas por whitespace), a 1ª componente passa a ser o código, e a 2ª a quantidade 
                    quantidade = int(codigo_quantidade[1])
                    if quantidade < 1:
                        continue

                    if codigo in produtos:
                        print(produtos[codigo][0], quantidade, format((produtos[codigo][2]+produtos[codigo][2]*produtos[codigo][3])*quantidade, '.2f'))

                        if codigo not in cesto:                                     #verificar se o produto já estava presente no cesto, ou se está a ser adicionado pela 1ª vez
                            cesto[codigo]=quantidade
                        else:
                            cesto[codigo]+=quantidade
                except:
                    continue

            else:
                continue


def fatura(produtos, compra):
    """Imprime a fatura de uma dada compra."""
    dicioFatura={}              #inicializar um dicionário para fazer a separação dos items pela categoria. Este dicionário vai ter todos os items da compra passada como argumento, mas estarão dependentes da sua secção (cada entrada do dicionário será uma secção, cujo valor será constituído por todos os items (e as suas informações respetivas) que lhe correspondem).
    totalBruto=0
    totalLiquido=0
    totalIva=0


    for item in compra.keys():
        if produtos[item][1] not in dicioFatura:
            dicioFatura[produtos[item][1]] = [[compra[item], produtos[item][0], produtos[item][3], (produtos[item][2]+produtos[item][2]*produtos[item][3])*compra[item]]]   #cada entrada no dicionário é 1 lista de listas, em que cada lista tem a quantidade de cada item no cesto de compras, o seu nome, a sua taxa, e o preço total (quantidade * (preço + IVA))  
            
            #print(dicioFatura[produtos[item][1]])
            
            totalBruto += produtos[item][2]*compra[item]
            totalIva += (produtos[item][2]*compra[item]) * produtos[item][3]

        else:
            dicioFatura[produtos[item][1]].append([compra[item], produtos[item][0], produtos[item][3], (produtos[item][2]+produtos[item][2]*produtos[item][3])*compra[item]]) #compra[item]: quantidade do item; produtos[item][0]: nome do item; produtos[item][3]: taxa do item; o último parâmetro: preço total ((preço do item + IVA) * quantidade)

            totalBruto += produtos[item][2]*compra[item]            #as atualizações do totalBruto e do totalIva são feitas aquando a adição de um novo item ao dicionário. O totalLíquido é calculado no fim, após estes valores estarem fixos 
            totalIva += (produtos[item][2]*compra[item]) * produtos[item][3]            

    for chave in dicioFatura.keys():
        print(chave)
        for valor in dicioFatura[chave]:
            print("   {:2d} {:30s} ({:>2d}%) {:>10.2f}".format(valor[0], valor[1], int(valor[2]*100), valor[3]))

    totalLiquido=totalBruto+totalIva
    print("   {:>39} {:>10.2f}".format("Total Bruto:", totalBruto))
    print("   {:>39} {:>10.2f}".format("Total IVA:", totalIva))
    print("   {:>39} {:>10.2f}".format("Total Liquido:", totalLiquido))
    



def main(args):
    # produtos guarda a informação da base de dados numa forma conveniente.
    produtos = {'p1': ('Ketchup', 'Mercearia Salgado', 1.59, 0.23)}
    # Carregar base de dados principal
    loadDataBase("produtos.txt", produtos)
    # Juntar bases de dados opcionais (Não altere)
    for arg in args:
        loadDataBase(arg, produtos)
    
    
    # Use este código para mostrar o menu e ler a opção repetidamente
    MENU = "(C)ompra (F)atura (S)air ? "

    dicioCompras={}         #as diferentes compras serão os valores deste dicionário (e as chaves serão o nº da compra, que começa em 1 e é incrementado sempre que se faz uma nova compra)
    contaDor=1              #Número da 1º compra

    repetir = True
    while repetir:
        # Utilizador introduz a opção com uma letra minúscula ou maiúscula
        op = input(MENU).upper()
        # Processar opção
        if op == "C":
            # Esta opção regista os produtos de uma compra
            compra = registaCompra(produtos)
            # Aqui pode acrescentar a compra a uma estrutura de dados adequada...
            dicioCompras[contaDor]=compra
            contaDor+=1

        # Acrescente outras opções aqui...

        if op == "F":
            try:
                numero_compra = int(input("Numero compra? "))
                fatura(produtos, dicioCompras[numero_compra])
            except:
                print("Algo de errado aconteceu. Tente novamente.")
                continue
            
            

        if op == "S":
            break

    print("Obrigado!")


# Não altere este código / Do not change this code
import sys
if __name__ == "__main__":
    main(sys.argv[1:])

