def askInput():
    while True:
        try:
            n=int(input("Indique um número inteiro: "))
            return n
            break
        except:
            print("Argumento inválido; o programa terminará.")
            exit()

def leibnizPi(n):
    soma=0
    for i in range(0, n+1):
        soma+= ((-1)**i)/(2*i +1)

    return soma

def main():
    n=askInput()
    print("leibnizPi(",n,"): ",leibnizPi(n))

main()