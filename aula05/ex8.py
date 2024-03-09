def evenThenOdd(str):
    if str=='':
        return ''

    #return str[0]+evenThenOdd(str[2:2:])+evenThenOdd(str[1:]) -> retorna o input direitinho tal como é
    return str[0::2]+str[1::2]

def oddThenEven_odder(str): #2
    if str=='':
        return str
    if len(str)==1:
        return str
    oddsFirst = evenThenOdd_recursive(str, "par")
    return  oddsFirst + str[1::2]

def evenThenOdd_recursive(str, i): #a parte dos índices pares fica ordenada normalmente, mas as letras correspondentes aos índices ímpares ficam inversamente ordenados
    if str=='':
        return ''

    if i=="par":
        return str[0]+evenThenOdd_recursive(str[1:], "impar")
    else:
        return evenThenOdd_recursive(str[1:], "par") #2

        return evenThenOdd_recursive(str[1:], "par")+str[0] #para a palavra "dor": quando a função é chamada inicialmente para "dor", retorna "d" + uma chamada a ela própria com a string "or". Esta chamada devolve 
        #outra chamada a ela própria, com a string "r", e também devolve a letra "o", após essa chamada concluir. Esta chamada devolve "r" (sendo o output agora "dr"), e outra chamada a uma string vazia, que devolve
        #o vazio, não tendo efeito no output, mas parando as chamadas recursivas a partir da string vazia. Concluída esta última chamada ao vazio, a letra "o" é devolvida no output, sendo este agora igual a "dro".

        #Com 4 letras: [a]+[odd(bcd)->[even(cd)=c+[odd(d)->[even("")=""]+d]]+b]

        #Com 5 letras "abcde": a 1ª chamada retorna "a" + chamada a "bcde". Esta 2ª chamada devolve uma 3ª chamada a "cde", que retorna "c" + uma 4ª chamada a "de", ficando a 2ª chamada pendente da conclusão da
        #3ª chamada para devolver também a letra "b". Esta 4ª chamada retorna uma 5ª chamada a "e" (ficando à espera do término desta para devolver "d"; a 5ª chamada retorna primeiro que a 3ª chamada, pelo que "d"
        #será devolvido primeiro do que "b"), que retorna "e" + uma 6ª chamada a "", que retorna "" apenas. O output aqui é "ace[[[6ªchamada terminou com ""]4ª chamada por terminar]2ª chamada por terminar]".
        #O output depois torna-se em "ace""d[2ªchamada por terminar]". E depois torna-se em "acedb".

        #Com 6 letras: a+[odd(bcdef)=[even(cdef)=c+[odd(def)=[even(ef)=e+[odd(f)=[even[]='']+f]]+d]]+b]=acefdb


    

frase="abcde"
print(evenThenOdd(frase))
print(evenThenOdd_recursive(frase, "par"))

#2
print(oddThenEven_odder(frase))