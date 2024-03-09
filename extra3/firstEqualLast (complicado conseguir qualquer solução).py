# Given a sequence lst, return the longest n so that 
# the first n elements equal the last n elements (with no overlapping).

# Dada uma sequência lst, devolva o maior n tal que
# os primeiros n elementos igualam os últimos n elementos (sem sobreposição).

def firstEqualLast(lst):
   if len(lst)==0:
      return 0
   
   
   longestN=0
   
   meio=len(lst)//2
   

   for n in range(1, meio+1):
      #print(lst[:n])
      #print(lst[-n:], "\n")
      
      
      if lst[:n]==lst[-n:]:
         longestN=n
      else:
         continue
      
   return longestN

''' #Recursiva; funciona
# Given a sequence lst, return the longest n so that 
# the first n elements equal the last n elements (with no overlapping).

# Dada uma sequência lst, devolva o maior n tal que
# os primeiros n elementos igualam os últimos n elementos (sem sobreposição).

def firstEqualLast(lst):

   if len(lst)<=1:
      return 0
      
      
   meio=len(lst)//2
   metade1=lst[:meio]
   if len(lst)%2!=0:
      metade2=lst[meio+1:]
   else:
      metade2=lst[meio:]
      
      
   #print(metade1)
   #print(metade2)
   #print()
      
   #if lst[:meio]==lst[meio:]:
   if metade1==metade2:
      return len(lst[:meio])
   else:
      cena=lst[:meio-1]
      dor=lst[meio+1:] #devia de ser igual a metade2.pop(), porque assim, aquele detalhe de aumentar o início da lista2 quando a lista original tem tamanho ímpar é ignorado. De qualquer modo, mesmo que estas 2 listas tenham tamanhos diferentes, a próxima chamada à função corríge isso.
      
      #print(cena)
      #print(dor)
      #print()
      
      lstPior=cena+dor
      return firstEqualLast(lstPior)
'''    
   
