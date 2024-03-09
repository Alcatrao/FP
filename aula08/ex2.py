import os


caminho = os.path.join(os.path.dirname(os.path.abspath(__file__)), "names.txt")
#print(caminho)

def reader(caminho):
    apelidos = {}
    with open(caminho, 'r') as ficheiro:
        while True:
            linha = ficheiro.readline()
            if linha == '':
                ficheiro.close()
                return apelidos
            palavras=linha.split()
            if len(palavras)<=1:
                continue
            #print(palavras)
            if palavras[-1] not in apelidos:
                apelidos[palavras[-1]] = {palavras[0]}
            else:
                apelidos[palavras[-1]].add(palavras[0])

                
def listagem(apelidos):
    for key, value in apelidos.items():
        print("{:<10s}: {}".format(key, value))

def main():
    #global caminho         #isto só é necessário se quisermos alterar a variável "caminho"
    apelidos = reader(caminho)
    listagem(apelidos)

main()