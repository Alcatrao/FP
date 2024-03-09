def ispalindrome(s):
    if s=='': #or len(s)==1:
        return True
    #if len(s)==2:
    #    if s[0]==s[-1]:
    #        return True

    if s[0]==s[-1]:
        return ispalindrome(s[1:-1])
    return False

def capicua(lista):
	if lista==[]:
		return True
	if lista[0]!=lista[-1]:
		return False

	dor=capicua(lista[1:-1])
	return dor

frase=input("Escreva algo para saber se é um palíndromo: ") #mau cena dor pior
print(ispalindrome(frase))