numeros=[x for x in range(994)]
digitos=[0, 1, 7, 9]

def hasDigits(listaDeNumeros, listaDeDigitos):
    listaRevisionada=[]
    for x in listaDeNumeros:
        y=str(x)
        #x="x"
        count=0
        for i in y:
            #print(i)
            count+=1
            if(int(i) not in listaDeDigitos): #o "i" é um char da string "y", pelo que é necessário convertê-lo para int antes de comparar com os valores (ints) em "digitos"
                break
            if(count==len(y)):
                listaRevisionada.append(y)
    print("Números que contém apenas os dígitos requiridos: ", len(listaRevisionada))
    return listaRevisionada

                
print(hasDigits(numeros, digitos))



######################################
######################################
######################################


numeros=[x for x in range(994)]
contador=0
digito=0

def lastDigit(listaDeNumeros, digito, contaDor): #ultrapassa o limite de profundidade de recursão a partir do range(997)
    if(listaDeNumeros==[]):
        print("\nNúmeros que acabam com o dígito requirido: ", contaDor) #com a variável contaDor, o limite de profundidade de recursão é alcançado a partir do range(994)
        return []
    letras=str(listaDeNumeros[0])
    if(int(letras[-1])==digito):
        return [listaDeNumeros[0]]+lastDigit(listaDeNumeros[1:], digito, contaDor+1)
    else:
        return lastDigit(listaDeNumeros[1:], digito, contaDor)


print(lastDigit(numeros, digito, contador))



######################################
######################################
######################################


numeros=[x for x in range(994)]
digitos=[0]
numeroOcorrencias=2


def presenceDigits(listaDeNumeros, listaDeDigitos, numeroOcorrencias, peloMenos="=="):
    cena=0
    listaRevisionada=[]
    ocorrencias={}
    for digito in listaDeDigitos:
        ocorrencias[digito]=0
    for numero in listaDeNumeros:
        numeroValido=True
        letras=str(numero)
        for algarismo in letras:
            if(int(algarismo) in listaDeDigitos):
                ocorrencias[int(algarismo)]+=1
        for digito in listaDeDigitos:
            valorOcorrencia=ocorrencias[digito]
            ocorrencias[digito]=0

            if(peloMenos=="=="):
                if(valorOcorrencia!=numeroOcorrencias):
                    numeroValido=False
            if(peloMenos==">="):
                if(valorOcorrencia<numeroOcorrencias):
                    numeroValido=False
                    #print("dor")

        if(numeroValido==True):
            listaRevisionada.append(numero)
            cena+=1
    print("\nNúmeros com exatamente "+str(numeroOcorrencias)+" de "+str(listaDeDigitos)+": "+str(cena))
    return listaRevisionada



def presenceDigitsRecursive(listaDeNumeros, listaDeDigitos, numeroOcorrencias, dor, peloMenos="=="):
    if(listaDeNumeros==[]):
        print("\nNúmeros com exatamente "+str(numeroOcorrencias)+" de "+str(listaDeDigitos)+": "+str(dor))
        return []
    ocorrencias={}
    for digito in listaDeDigitos:
        ocorrencias[digito]=0
    letras=str(listaDeNumeros[0])
    for algarismo in letras:
        if(int(algarismo) in listaDeDigitos):
            ocorrencias[int(algarismo)]+=1
    for digito in listaDeDigitos:

        if(peloMenos=="=="):
            if(ocorrencias[digito]!=numeroOcorrencias):
                return presenceDigitsRecursive(listaDeNumeros[1:], listaDeDigitos, numeroOcorrencias, dor, peloMenos)

        else:
            if(ocorrencias[digito]<numeroOcorrencias):
                return presenceDigitsRecursive(listaDeNumeros[1:], listaDeDigitos, numeroOcorrencias, dor, peloMenos)

    return [listaDeNumeros[0]]+presenceDigitsRecursive(listaDeNumeros[1:], listaDeDigitos, numeroOcorrencias, dor+1, peloMenos)



#print(presenceDigits(numeros, digitos, numeroOcorrencias, ">="))
print(presenceDigitsRecursive(numeros, digitos, numeroOcorrencias, 0, ">="))



######################################
######################################
######################################



numeros=[x for x in range(994)]
digito=0
lugar=2



def hasDigitAt(listaDeNumeros, digito, lugar, contaDor=0):
    if(listaDeNumeros==[]):
        print("\nNúmeros com o dígito requirido na determinada posição: "+str(contaDor))
        return []
    if(len(str(listaDeNumeros[0]))<=lugar):
        return hasDigitAt(listaDeNumeros[1:], digito, lugar, contaDor)
    if(str(listaDeNumeros[0])[-lugar]==str(digito)):
        return [listaDeNumeros[0]]+hasDigitAt(listaDeNumeros[1:], digito, lugar, contaDor+1)
    return hasDigitAt(listaDeNumeros[1:], digito, lugar, contaDor)



print(hasDigitAt(numeros, digito, lugar, 0))



######################################
######################################
######################################
print("\nTodos os números entre 0 e 100000 que contém apenas os digítos 0, 1, 3, sendo que contém o número 0 exatamente 2x, acabam com o dígito 1, e que o digíto 3 se encontre na casa das dezenas:")

numeros=[x for x in range(0,100000)]

numeros=hasDigits(numeros, [0,1,3])
numeros=lastDigit(numeros, 1, contador)
numeros=presenceDigitsRecursive(numeros, [0], 2, contador)
numeros=hasDigitAt(numeros, 3, 2, contador)
print(numeros)


######################################
######################################
######################################
print("\nConsidere todos os números naturais de sete algarismos que se podem escrever utilizando dois algarismos 5, quatro algarismos 6 e um algarismo 7")
print("Determine quantos destes números são ímpares e maiores do que seis milhões.")

def oddNumber(numero):
    if(numero%2!=0):
        return True
    else:
        return False

def biggerThan(numero1, numero2):
    if(numero1>numero2):
        return True
    else:
        return False


numeros=[x for x in range(1000000,9999999)]

numeros=presenceDigits(numeros, [5], 2)
numeros=presenceDigits(numeros, [6], 4)
numeros=presenceDigits(numeros, [7], 1)

lista=[]
for x in numeros:
    if(oddNumber(x)==True and biggerThan(x,6000000)==True):
        lista.append(x)
print(lista)
print("\nResposta: "+str(len(lista)))