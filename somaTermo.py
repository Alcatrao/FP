def somaTermo(num_termos, termo):
    resultado=0
    termo_inicial=termo
    i=1
    termo=0
    while num_termos > 0:

        termo=termo+termo_inicial*i #está correto 0+2=2; 2+20=22; 22+200=222...
        resultado = resultado + termo #0+2=2; 2+22=24; 24+222= 246 (estava errado antes porque tinha resultado += resultado + termo)
        print(resultado)
        
        i*=10
        num_termos-=1
        

    print(resultado)

numero=int(input("Indique o número de termos: "))
termo=int(input("Indique o termo: "))

somaTermo(numero, termo)