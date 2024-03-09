import os


def sizeFinder(dir, soma_default=0):
    if os.path.isdir(dir)==False:
        print("The inserted directory path could not be found.")
        exit()

    lista = os.listdir(dir)
    soma = soma_default

    for name in lista:
        #print(name)
        if os.path.isfile(os.path.join(dir,name))==True:
            soma+=os.stat(os.path.join(dir,name)).st_size

        elif os.path.isdir(os.path.join(dir,name))==True:
            soma+=sizeFinder(os.path.join(dir,name), soma)
            #print("Dor size (",os.path.join(dir,name),"):  ",soma)

    return soma


print(sizeFinder("C:\\Users\\joaoa\\OneDrive\\Ambiente de Trabalho\\"))