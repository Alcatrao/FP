def shorten(str):
    abreviation=""
    contaDor=0
    while True:
        if contaDor>=len(str):
            break
        if str[contaDor].isupper():
            #if contaDor==0 and contaDor+1<=len(str) and str[contaDor+1].isupper()==False:
            #    abreviation=abreviation+str[contaDor]
            #elif contaDor>0 and contaDor+1<=len(str) and str[contaDor+1].isupper()==False and str[contaDor-1].isupper()==False:
            #    abreviation=abreviation+str[contaDor]
            #elif contaDor>0 and contaDor==len(str) and str[contaDor-1].isupper()==False:
            #    abreviation=abreviation+str[contaDor]
            #else:
            #    contaDor+=1
            #    continue
            abreviation=abreviation+str[contaDor]


        contaDor+=1
    return abreviation

#ideia de frase: Dou beliscões ao meu peito para O meu Ritual 
print(shorten(input("Insira uma frase para que seja abreviada: ")))