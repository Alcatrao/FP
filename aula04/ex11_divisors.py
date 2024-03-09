def askInput():
    while True:
        try:
            n=int(input("Insira um número para saber se é primo: "))
            return n
        except:
            print("Argumento inválido. Tente novamente.")

def divisors(n):
    print("Divisores de",n,":")
    for i in range(1,n//2+1):
        if n%i==0:
            print(i)

def deficiencia(n):
    soma=0
    for i in range(1,n//2+1):
        if n%i==0:
            soma+=i
    if soma<n:
        print("O número",n,"é deficiente.")
    elif soma==n:
        print("O número", n,"é perfeito.")
    elif soma>n:
        print("O número", n,"é abundante.")
    else:
        print("Something dark and ominous is at play here. Is is well beyond the known horrors of this world. Do not feel it, for it is far worse than any pain you have experienced. Cena dor.")
        exit(29)

def main():
    n=askInput()
    divisors(n)
    print()
    deficiencia(n)
main()
