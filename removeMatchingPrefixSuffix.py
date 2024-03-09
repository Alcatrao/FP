
# Given a string s, find the longest prefix that also occurs at the end 
# (so that s = p + t + p), and return t, the string without the 
# beginning and the end. Do not use the find method.

def removeMatchingPrefixSuffix(s):
   
   def removeMatchingPrefixSuffix_depilar(s): #devolve maior prefixo que for igual ao suxifo do mesmo tamanho
      if s=='':
         return s
      p=''
      p1=removeMatchingPrefixSuffix_depilar(s[0:len(s)//2-1]+s[len(s)//2+len(s)%2+1:])
      cena=s[0:len(s)//2]
      dor=s[len(s)//2+len(s)%2:]
      if cena==dor:
         p=cena
         
      if len(p1)>len(p):
         return p1
      return p
      
   if removeMatchingPrefixSuffix_depilar(s)=='':
      return s
   return s[len(removeMatchingPrefixSuffix_depilar(s)):-len(removeMatchingPrefixSuffix_depilar(s))]

''' #depilação cu dor
def removeMatchingPrefixSuffix(s):  #devolve maior substring em porções espelhadas da string 
    # Your code here...
    if s=='':
       return s
    pior=''
    meio=len(s)//2
    cena=s[0:meio]
    dor=s[meio+len(s)%2:]
    
    if cena==dor:
       pior=cena
    
    transmuteDorDepilar=removeMatchingPrefixSuffix(cena[:-1]+dor[1:])
    cenaDor=removeMatchingPrefixSuffix(cena[1:]+dor[:-1])
    
    if len(transmuteDorDepilar)>len(cenaDor):
       dorDepilation=transmuteDorDepilar
    else:
       dorDepilation=cenaDor
    
    if len(dorDepilation)>len(pior):
       return dorDepilation
    return pior
'''