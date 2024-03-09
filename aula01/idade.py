Nome=input("Como te chamas? ")
while True:
    try:
        Nascimento=int(input("Em que ano nasceste? "))
        break
    except:
        print("Insira um número.")

idade=2030-Nascimento
print(Nome, "fará", idade, "anos em 2030")
