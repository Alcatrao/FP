while True:
    try:
        andares=int(input("Indique o número de andares: "))
        break
    except:
        print("Insira um número válido.")

while True:
    try:
        moradores=int(input("Indique o número de moradores: "))
        break
    except:
        print("Insira um número válido.")

#distancia_percorrida_num_dia=0
#for i in range(1,andares+1):
#    distancia_percorrida_num_dia=distancia_percorrida_num_dia + 12*i*moradores

#cada morador percorre 4 vezes 3m (subir e descer 2x) por cada andar, sendo que o número de metros percorridos pelos moradores de um andar acima é igual a 12m + o número de metros percorridos pelos moradores de baixo (sequência aritmética)
distancia_percorrida_num_dia=(3*4)*moradores*(andares/2)*(2+andares-1)
distancia_percorrida_num_ano=distancia_percorrida_num_dia*365
distancia_percorrida=distancia_percorrida_num_ano/1000

#visto que cada metro é percorrido num segundo, temos que o tempo que os moradores demoram a subir/descer andares é igual à distância que eles percorreram
segundos=distancia_percorrida_num_ano
horas=segundos/(60*60)


print("O elevador percorre", distancia_percorrida, "km num ano, num tempo de funcionamento de", horas, "horas.")
