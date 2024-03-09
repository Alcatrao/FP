def askInput():
    while True:
        try:
            n=input("Indique um valor: ")
            if n=="":
                return n
            else:
                n=float(n)
                return n
        except:
            print("Valor inválido; tente novamente.")


n=0
sum=0
number=-1

while n!="":
    sum=sum+n
    number=number+1
    n=askInput()

mean=sum/number
print("Média: ", mean)