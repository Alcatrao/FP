import os

def ler_ficheiro(nome):
    try:
        print("Fist attempt:")
        with open(nome, 'r', encoding='utf-8') as ficheiro:
            lst=[]
            for linha in ficheiro:
                try:
                    palavras=linha.split()
                    lst.append(palavras)
                except:
                    continue
    except:
        print("Second attempt:")
        with open(nome, 'r') as ficheiro:
            lst=[]
            for linha in ficheiro:
                try:
                    palavras=linha.split()
                    lst.append(palavras)
                except:
                    continue
    

    return lst




def baralha(lst):
    for linha in lst:
        for palavra in linha:
            palavra_baralhada=''
            for letra in palavra:
                palavra_baralhada=palavra_baralhada+






print(os.getcwd())
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(ler_ficheiro("debug.log"))