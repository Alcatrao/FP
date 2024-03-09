# Complete este programa como pedido no guião da aula.

def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {:^30s} : {:<10s}".format("Numero", "Nome", "Morada"))
    for num in dic:
        print("{:>12s} : {:^30s} : {:<10s}".format(num, dic[num][0], dic[num][1]))

def filterPartName(contacts, partName):
    dicio = {}
    """Returns a new dict with the contacts whose names contain partName."""
    for key, value in contacts.items():
        if partName.lower() in value[0].lower():
            dicio[key] = value
    return dicio
        


def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op


def main():
    """This is the main function containing the main loop."""

    # The list of contacts (it's actually a dictionary!):
    contactos = {"234370200": ("Universidade de Aveiro", "Santiago, Aveiro"),
        "727392822": ("Cristiano Aveiro", "Aveiro"),
        "387719992": ("Maria Matos", "Algures"),
        "887555987": ("Marta Maia", "Coimra"),
        "876111333": ("Carlos Martins", "Porto"),
        "433162999": ("Ana Bacalhau", "Algarve")
        }

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contactos:")
            listContacts(contactos)
        elif op == "P":
            nome = input("Insira uma palavra para filtrar a lista de contactos: ")
            lista = filterPartName(contactos, nome)
            print("Contactos filtrados por '", nome, "' :")
            listContacts(lista)
        elif op == "A":
            while True:
                try:
                    numero = input("Insira um número: ")
                    assert len(numero) == 9
                    for digito in numero:
                        assert int(digito)
                    break
                except:
                    print("Número inválido. Tente novamente.")
            nome = input("Insira um nome: ")
            morada = input("Insira uma morada: ")
            contactos[numero] = (nome, morada)
            print("Contacto adicionado com sucesso.")
        elif op=="R":
            numero = input("Insira o número que deseja remover: ")
            try:
                contactos.pop(numero)
                print("Contacto removido com sucesso.")
            except:
                print("Número não encontrado.")
        elif op=="N":
            numero = input("Insira o número do contacto que deseja encontrar: ")
            try:
                print(contactos.get(numero))
            except:
                print(numero)


        else:
            print("Opção inválida.")
    

# O programa começa aqui
main()

