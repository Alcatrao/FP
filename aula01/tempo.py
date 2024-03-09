while True:
    try:
        segundos=int(input("Segundos a converter: "))
        break
    except:
        print("Insira um número válido")

s=segundos%60
m=(segundos//60)%60
h=segundos//(60*60)

print("{:02d}:{:02d}:{:02d}".format(h, m, s))