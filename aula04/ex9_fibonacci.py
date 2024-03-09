def fibonacci(n):
    f1=0
    f2=1

    if n==0:
        return f1
    if n==1:
        return f2

    for i in range(0,n):
        fn=f1+f2

        f2=f1
        f1=fn

    return fn


while True:
    try:
        n=int(input("Indique um número: "))
        break
    except:
        print("Valor inválido. Indique outro.")


print(fibonacci(n))