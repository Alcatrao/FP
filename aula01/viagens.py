while True:
    try:
        #v1=float(input("Insira velocidade 1: "))
        v1=float(input("v1? "))
        break
    except:
        print("Insira um valor válido.")


while True:
    try:
        #v2=float(input("Insira velocidade 2: "))
        v2=float(input("v2? "))
        break
    except:
        print("Insira um valor válido.")

#d/t1 e d/t2. t1=d/v1 e t2=d/v2. vres=2*d/(t1+t2) -> vres=(2*d) / (d/v1 + d/v2)
d=1 #placeholder para as contas. Provavelmente poderia ser retirado da esquação, pois é irrelevante
vres=(2*d)/(d/v1 + d/v2)

print("v1:", v1, "v2:", v2, "vm:", vres)