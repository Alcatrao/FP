def replaceCharactersWithUnderscores(s, t):
    # Your code here...
   if s=='':
      return ''
   if len(s)==1:
      if s[0] in t:
         return '_'
      return s[0]
      
   meio=len(s)//2
   cena = replaceCharactersWithUnderscores(s[:meio], t)
   dor = replaceCharactersWithUnderscores(s[meio:], t)
   
   return cena+dor

def replaceCharactersWithUnderscores(s, t):
    # Your code here...
   if s=='':
      return ''
   
   if s[0] in t:
      return '_'+replaceCharactersWithUnderscores(s[1:], t)
   return s[0]+replaceCharactersWithUnderscores(s[1:], t)
       