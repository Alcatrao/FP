def isPrime(n):
    if n<=1 or n==4: #para bem, abaixo deveria estar n//2+1, para que a metade de um número par possa estar incluida 
        return False
    for i in range(2,n//2):
        if n%i==0:
            return False
    return True

def askInput():
    while True:
        try:
            n=int(input("Insira um número para saber se é primo: "))
            return n
        except:
            print("Argumento inválido. Tente novamente.")

def main():
    n=askInput()
    for i in range(1,n+1):
        print("isPrime(",i,"): ",isPrime(i))

main()