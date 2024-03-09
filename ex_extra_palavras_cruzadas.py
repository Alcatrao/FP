"""
Imagine que está a fazer palavras cruzadas (em Inglês) e falta-lhe uma
palavra com o padrão "?YS???Y", onde os "?" representam letras por preencher.
Complete este programa para o ajudar a descobrir a palavra.
O programa já inclui instruções para ler uma lista de palavras inglesas a
partir do ficheiro wordlist.txt.
"""

# This function reads words from a file.
import os


def load(fname):
   with open(fname) as f:
      lst = []
      for line in f:
         words = line.strip().split()
         lst.extend(words)
   return lst


""" a)
Complete a função matchesPattern(s, pattern) para devolver
True se s corresponder ao padrão fornecido e False, no caso contrário.
Uma string s corresponde ao padrão se e só se tiver os mesmos carateres
que o padrão nas mesmas posições, exceto onde o padrão tem ?.
Nas posições dos ?, não importa que carateres estão na string s.
A correspondência não deve fazer distinção entre maiúsculas e minúsculas.
"""
def matchesPattern(s, pattern):
   
   #if len(s)<len(pattern):
   #   return False
   #for i in range(len(pattern)):
   #   #print(s[i], pattern[i])
   #   if s[i].lower() == pattern[i].lower() or pattern[i] == '?':
   #      if i == len(pattern)-1:
   #         return True
   #   else:
   #      #break
   #      return False
   #return matchesPattern(s[1:], pattern)
   
   if len(s)!=len(pattern):
      return False
   for i in range(len(s)):
      if s[i].lower()==pattern[i].lower() or pattern[i]=='?':
         if i == len(pattern)-1:
            return True
      else:
         return False
   

""" b)
Complete a função filterPattern(lst, pattern) para extrair duma lista de strings
as strings que têm o padrão dado.
Sugestão: use a função matchesPattern para testar cada palavra.
"""
def filterPattern(lst, pattern):
   # Complete ...
   lst_filtrada=[]
   for palavra in lst:
      if matchesPattern(palavra, pattern) == True:
         lst_filtrada.append(palavra)
   return lst_filtrada
   


def main():
   print("a)")
   print( matchesPattern("secret", "s?c??t") )  #-> True
   print( matchesPattern("secreta", "s?c??t") ) #-> False
   print( matchesPattern("socket", "s?c??t") )  #-> True
   print( matchesPattern("soccer", "s?c??t") )  #-> False
   print( matchesPattern("SEcrEt", "?ecr?t") )  #-> True
   print( matchesPattern("SEcrET", "?ecr?t") )  #-> True
   print( matchesPattern("SecrEt", "?ECR?T") )  #-> True

   words = load(os.path.join(os.path.dirname(os.path.abspath(__file__)),"wordlist.txt"))

   print("b)")
   # Solution to "S?C??T"
   lst = filterPattern(words, "s?c??t")
   print(lst)

   assert isinstance(lst, list),  "result lst should be a list"
   assert "secret" in lst,  "result should contain 'secret'"

   # Solution to "?YS???Y"
   lst = filterPattern(words, "?ys???y")
   print(lst)


# Call main function:
if __name__ == "__main__":
   main()