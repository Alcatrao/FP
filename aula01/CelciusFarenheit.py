from curses.ascii import isdigit


#caso haja erro de "no module named '_curses'"": abrir terminal (cmd) e executar o comando "pip install windows-curses"

#celcius=input("Temperatura em Celsius: ")
celcius=input("Temperature (ºC)? ")
while celcius.replace(".","",1).isdigit()==False:
    try:
        celcius=float(celcius)
        break
    except:
        celcius=input("Insira uma temperatura válida: ")

celcius=float(celcius)

farenheit=1.8*celcius+32

print(celcius, "ºC =", farenheit, "ºF")

