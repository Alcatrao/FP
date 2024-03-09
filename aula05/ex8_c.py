def mirrorMirror(n):
    if n==0 or n<0:
        return []
    return mirrorMirror(n-1)+[n]*n

def askInput():
    while True:
        try:
            n=input("Insira um número: ")
            n=int(n)
            return n
            break
        except:
            print("Número inválido. Tente outra vez.")

def main():
    n=askInput()
    print(mirrorMirror(n))

main()