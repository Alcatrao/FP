
# Convert a telephone number into corresponding name, if on list.
# (If not on list, just return the number itself.)
def telToName(tel, telList, nameList):
    # your code here
    try:
        number = telList.index(tel)
        name = nameList[number]
        return name
    except:
        return tel


# Return list of telephone numbers corresponding to names containing partName.
def nameToTels(partName, telList, nameList):
    # your code here
    listaFiltrada=[]
    tels=[]
    for name in nameList:
        if partName in name:
            listaFiltrada.append(name)
    for name in listaFiltrada:
        tels.append(telList[nameList.index(name)])

    return tels

def main():
    # Lists of telephone numbers and names
    telList = ['975318642', '234000111', '777888333', '911911911']
    nameList = ['Angelina', 'Brad',      'Claudia',   'Bruna']

    # Test telToName:
    while True: #isto serve para forçar o utilizador a inserir um número válido
        try:
            tel = input("Tel number? ")
            tel_number=int(tel) #só para ver se o número inserido é, de facto, um número
            break
        except:
            print("Invalid number. Try again.")

    print( telToName(tel, telList, nameList) )
    print( telToName('234000111', telList, nameList) == "Brad" )
    print( telToName('222333444', telList, nameList) == "222333444" )

    # Test nameToTels:
    name = input("Name? ")
    print( nameToTels(name, telList, nameList) )
    print( nameToTels('Clau', telList, nameList) == ['777888333'] )
    print( nameToTels('Br', telList, nameList) == ['234000111', '911911911'] )


if __name__ == "__main__":
    main()
