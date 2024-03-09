def primesUpTo(n):
    conjunto = {n for n in range(2,n+1)}
    p=2
    usado = [p]
    while True:
        eratostenes = {n for n in conjunto if n%p==0 and n >= p**2}
        #print(p, eratostenes)
        if p >= n//2:
            return conjunto
        conjunto.difference_update(eratostenes)
        usado.append(p)
        p = min([n for n in conjunto if n not in usado])

        
def askInput():
    while True:
        try:
            n = int(input("Quer os números primos até que número? "))
            return n
        except:
            print("Número inválido. Tenta outra vez.")

def main():
    n = askInput()
    print(primesUpTo(n))

main()
