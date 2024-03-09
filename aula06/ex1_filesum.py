from tkinter import filedialog

def main():
    # 1) Pedir nome do ficheiro (experimente cada alternativa):
    #name = input("File? ")                                  #A    #É preciso meter o caminho absoluto
    name = filedialog.askopenfilename(title="Choose File") #B       #Abre uma janela no explorador de ficheiros
    #print(name)
    
    # 2) Calcular soma dos números no ficheiro:
    total = fileSum(name)
    
    # 3) Mostrar a soma:
    print("Sum:", total)


def fileSum(filename):
    ficheiro = open(filename, 'r')
    soma = 0
    while True:
        linha = ficheiro.readline()
        if linha == "":
            ficheiro.close()
            return soma

        soma += float(linha)

if __name__ == "__main__":
    main()

