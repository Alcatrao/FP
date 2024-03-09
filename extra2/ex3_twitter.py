# Este programa demonstra a leitura e utilização de dados de um ficheiro JSON
# com mensagens do Twitter.
# Modifique-o para resolver o problema proposto.


# O módulo json permite descodificar ficheiros no formato JSON.
# São ficheiros de texto que armazenam objetos compostos que podem incluir
# números, strings, listas e/ou dicionários.
import json
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Abre o ficheiro e descodifica-o criando o objeto twits.
with open("twitter.json", encoding="utf8") as f:
    twits = json.load(f)

# Analise os resultados impressos para perceber a estrutura dos dados.
print(type(twits))       # deve indicar que é uma lista!
print(type(twits[0]))    # cada elemento da lista é um dicionário.
print(twits[0].keys())   # mostra as chaves no primeiro elemento.

# Cada elemento contém uma mensagem associada à chave "text":
print(twits[0]["text"])

# Algumas mensagens contêm hashtags:
print(twits[880]["text"])




#ex1
def allWords(twits_list):
    listaPalavrasTwits=[]

    for dicio in twits_list:
            try:
                palavras_lista=dicio["text"].split()
                for palavra in palavras_lista:
                    #print(palavra)
                    listaPalavrasTwits.append(palavra)
            except:
                continue

    return listaPalavrasTwits



#ex2
def listaContagem(palavrasTwits):
    return sorted(palavrasTwits, key=lambda x: palavrasTwits.count(x), reverse=True)

def contarOcorrenciasPalavra(palavrasTwit, palavra):
    contaDor=0
    if palavra not in palavrasTwit:
        return contaDor
    for word in palavrasTwit:
        if word==palavra:
            contaDor+=1
    return contaDor


#ex3
def hashtags(palavrasTwits):
    palavrasTwitsHashtags=[]
    for palavra in palavrasTwits:
        if palavra[0]=="#":
            palavrasTwitsHashtags.append(palavra)

    return listaContagem(palavrasTwitsHashtags)


#ex4
def cruzesGeneraDor(percentagem):
    return '+'*round((percentagem*18)/100)



def histogramTwits(palavrasTwitsOrdenadas, tamanho):
    if isinstance(tamanho, int)==False:
        print("Parâmetro de número de palavras a considerar no histograma inválido (não é um inteiro).")
    if tamanho > len(palavrasTwitsOrdenadas):
        print("Parâmetro de número de palavras a considerar no histograma inválido (é maior que a lista a analisar).")

    idx=0
    total=0
    usados=[]
    while total<tamanho:
        if palavrasTwitsOrdenadas[idx] not in usados:
            percentagem=(contarOcorrenciasPalavra(palavrasTwitsOrdenadas, palavrasTwitsOrdenadas[idx])/contarOcorrenciasPalavra(palavrasTwitsOrdenadas, palavrasTwitsOrdenadas[0]))*100
            cruzes=cruzesGeneraDor(percentagem)
            print("{:<20s} ({:3d}) {:<18s}".format(palavrasTwitsOrdenadas[idx], int(percentagem), cruzes))

            usados.append(palavrasTwitsOrdenadas[idx])
            idx+=1
            total+=1
            
        else:
            idx+=1
            continue

#check com dicionário
def dicioContaDor(twits, hashtag=False):
    dicio={}
    for palavra in twits:
        if hashtag==True:
            if palavra[0]!="#":
                continue
        if palavra not in dicio:
            dicio[palavra]=1
        else:
            dicio[palavra]+=1
    return dicio


def main():
    print()
    todasAsPalavras=allWords(twits)
    #print("Ex1: ",todasAsPalavras)

    todasAsPalavras=listaContagem(todasAsPalavras)
    #print("\nEx2: ",todasAsPalavras)

    todasAsHashtags=hashtags(todasAsPalavras)
    todasAsHashtags=listaContagem(todasAsHashtags)
    #print("Ex3: ",todasAsHashtags[0:100])

    histogramTwits(todasAsHashtags, 4)



    #check (os resultados são idênticos certo)
    #print()
    #print(dicioContaDor(todasAsPalavras, True))

main()