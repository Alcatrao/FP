def noAdjacentDuplicates(s, letra=''):
    if s == '':
        return ''

    if s[0]==letra:
        return noAdjacentDuplicates(s[1:], letra)
    return s[0]+noAdjacentDuplicates(s[1:], s[0])


frase=input("Insira uma frase para obter uma frase idêntica, mas sem caratéres adjacentes duplicados: ")
print(noAdjacentDuplicates(frase, ''))