def tax(r):
    if r<=1000:
        return r*0.1
    elif r>1000 and r <= 2000:
        return r*0.2 - 100
    else:
        return 0.3*r - 300

def main():

    while True:
        try:
            x=float(input("Insira um valor para a variável r: "))
            break
        except:
            print("Argumento inválido.")
            exit()

    print("Resultado: {:.3f}".format(tax(x)))

main()