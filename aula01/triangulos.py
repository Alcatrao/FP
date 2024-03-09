import math


while True:
    try:
        cateto1=float(input("Indique o comprimento do cateto 1: "))
        break
    except:
        print("Insira um número válido")

while True:
    try:
        cateto2=float(input("Indique o comprimento do cateto 2: "))
        break
    except:
        print("Insira um número válido")


hipotenusa=math.sqrt(cateto1**2 + cateto2**2)
print("Hipotenusa tem comprimento ", hipotenusa)

angulo=math.acos((cateto2**2 + hipotenusa**2 - cateto1**2)/(2*cateto2*hipotenusa))*(180/math.pi)
print("O ângulo entre o cateto 1 e a hipotenusa é de", angulo, "graus")