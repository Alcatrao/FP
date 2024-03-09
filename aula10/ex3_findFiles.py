import os

def printDirFiles(d):
    lst = os.listdir(d)
    for fname in lst:
        path = os.path.join(d, fname)
        if os.path.isfile(path):
            ftype = "FILE"
        elif os.path.isdir(path):
            ftype = "DIR"
        else:
            ftype = "?"
        print(ftype, path)
    return


def findFiles(path, ext):
    # Complete...
    #print(os.path.isdir(os.path.join(os.getcwd(), path)))      #com path = '...', a função os.path.isdir retorna True
    #print(os.path.abspath(os.path.join(os.getcwd(), path)))    #o path com '...' é equivalente ao path absoluto do working directory sem '...'
    if os.path.isdir(os.path.join(os.getcwd(), path))==False:
        print("The inserted directory path could not be found.")
        exit()
    
    path=os.path.abspath(os.path.join(os.getcwd(), path))       #com esta linha, todos os paths se tornam absolutos (em vez de relativos, que dávam erros com inputs de path como '...')

    listaFicheiros=[]
    lst = os.listdir(path)
    for nome in lst:
        caminho = os.path.join(path, nome)
        #print(caminho)
        if os.path.isfile(caminho):
            try:
                if nome[-len(ext):]==ext:
                    listaFicheiros.append(nome)
            except:
                continue
        elif os.path.isdir(caminho):
            listaFicheiros = listaFicheiros + findFiles(caminho, ext)
        else:
            continue
    return listaFicheiros


def findFiles_dicio(path, ext):
    if os.path.isdir(os.path.join(os.getcwd(), path))==False:
        print("The inserted directory path could not be found.")
        exit()
    
    path=os.path.abspath(os.path.join(os.getcwd(), path))       #com esta linha, todos os paths se tornam absolutos (em vez de relativos, que dávam erros com inputs de path como '...')

    listaFicheiros={}
    lst = os.listdir(path)
    for nome in lst:
        caminho = os.path.join(path, nome)
        #print(caminho)
        if os.path.isfile(caminho):
            try:
                if nome[-len(ext):]==ext:
                    if path not in listaFicheiros:
                        listaFicheiros[path]=[nome]
                    else:
                        listaFicheiros[path].append(nome)
            except:
                continue
        elif os.path.isdir(caminho):
            listaFicheiros.update(findFiles_dicio(caminho, ext))
        else:
            continue
    return listaFicheiros



def main():
    print("Testing printDirFiles('..'):")
    printDirFiles("..")

    print("\nTesting findFiles('.', '.py'):")
    lst = findFiles(".", ".py")
    print(lst)
    assert isinstance(lst, list)

    print("\nTesting findFiles('..', '.csv'):")
    lst = findFiles("..", ".csv")
    print(lst)

    ###
    dicio = findFiles_dicio("..", ".py")
    for chave in dicio:
        print("DIR:",chave)
        #print(dicio[chave])
        for valor in dicio[chave]:
            print("     FILE:",valor)


if __name__ == "__main__":
    #print(os.getcwd())
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()

