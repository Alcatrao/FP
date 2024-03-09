#def invertString(stri):
#    strInversa="a"*len(stri)
#    for i in range(0,len(stri)):
#        strInversa[i]=stri[:-i-1]
#
#    return strInversa


def askNumber():
    while True:
        try:
            n=int(input("Insira um número: "))
            return n
        except:
            print("Numero inválido. Tente novamente.")

def invertNumber(numero):
    #i=Math.log10(numero) #descobrir nº de dígitos sem recorrer ao str
    reverse=0
    while numero>0:
        resto=numero%10 #para n=27438:  27438 % 10 = 8;   27438 // 10 = 2743 (ou seja, esta operação devolve sempre o último dígito do número)
        numero=numero//10 #(esta operação devolve o resto do número, sem o "resto")
        reverse=reverse*10+resto #estava errado antes porque tinha reverse+=reverse+resto*i, onde i=1, 10, 100, 1000... (o "resto", último dígito do número, passa a a ser o 1º. A multiplicação por 10 assegura que a casa das unidades está vazia para receber outro "resto")
        #reverse+=resto*i
        #i//=10


    return reverse




numero=askNumber()
print("Reverse: ",invertNumber(numero))