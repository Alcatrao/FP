while True:
    try:
        livros=int(input("Indique o número de livros para obter uma estimativa do valor da totalidade da sua venda: "))
        break
    except:
        print("Insira um número válido")

#24.95=20+Lucro + (20+Lucro)*0.23 + 0.2 <==> 24.75 = 1.23(20+Lucro) <==> 24.75 = 24.6 + 1.23*Lucro <==> 0.15 = 1.23*Lucro <==> Lucro = 0.15/1.23

Lucro=0.15/1.23
Imp=0.23*(20+Lucro)

Total_Lucro=livros*Lucro
Total_Imp=livros*Imp

print("O lucro total da venda de {:d} livros é de {:3.2f} euros, e o total de imposto é de {:3.2f} euros.".format(livros, Total_Lucro, Total_Imp)) #parece pouco, mas é o que dá usando a fórmula acima

#ex9
#06:52h + 10min = 07:02h
#07:02h + 6*3 min (min/km * km) = 07:20h
#07:20h + 4*10 (km * min/km ) = 08:00h