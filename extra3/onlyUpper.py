def onlyUpper(s):
   # NOTE: ch.isupper() -> True if ch is uppercase.
   
   if s=='':
      return ''
      
   if s[0].isupper()==True:
      return s[0]+onlyUpper(s[1:])
   return onlyUpper(s[1:])
   
   '''
   if len(s)==1:
      if s[0].isupper():
         return s[0]
      return ''
      
   meio=len(s)//2
   cena=onlyUpper(s[0:meio])
   dor=onlyUpper(s[meio:])
   
   return cena+dor
   '''




dor='Dor aguda má mesmo dOr; doR de beliscão no peito; dor de depilação às costas - cena dor'

print(onlyUpper(dor).lower())
