# Given a string s, return the longest prefix that is repeated somewhere else in the string. 
# For example, "abcdabejf" would return "ab" as "ab" starts at the beginning of the string
# and is repeated again later. Do not use the find method.

def longestPrefixRepeated(s):
    # Your code here...
    start=0
    end=0
    longestPattern=''
    while True:
       pattern=s[start:end]
       if pattern in s[end:] and len(pattern)>len(longestPattern):
          longestPattern=pattern
       end+=1
       if end>len(s):
          start+=1
          end=start+1
          
       if start>=len(s):
          return longestPattern
       

''' #ciclo while e implementação manual com função idêntica à do "in"

# Given a string s, return the longest prefix that is repeated somewhere else in the string. 
# For example, "abcdabejf" would return "ab" as "ab" starts at the beginning of the string
# and is repeated again later. Do not use the find method.

def longestPrefixRepeated(s):
    # Your code here...
    start=0
    end=0
    longestPattern=''
    while True:
       pattern=s[start:end]
       length=end-start
       for i in range(end, len(s)+29): #não dá erro
         if pattern == s[i:i+length] and len(pattern)>len(longestPattern):
            longestPattern=pattern
       end+=1
       if end>len(s):
          start+=1
          end=start+1
          
       if start>=len(s):
          return longestPattern
       
'''


''' #com ciclo for e implementação manual com função idêntica à do "in"
def longestPrefixRepeated(s):
    # Your code here...
    start=0
    end=0
    longestPattern=''
    for start in range(0, len(s)):
       for end in range(start+1, len(s)):
          length=end-start
          for portions in range(end, len(s)):
             if s[start:end] == s[portions:portions+length] and len(s[start:end])>len(longestPattern):
                longestPattern=s[start:end]
                
    return longestPattern
'''


''' #tentativa de divide and conquer; não funciona
def longestPrefixRepeated(s):
    # Your code here...
    
    if s=='':
       return ''
    if len(s)==1:
       return s
    
    meio=len(s)//2
    
    cena=longestPrefixRepeated(s[0:meio])
    dor=longestPrefixRepeated(s[meio:])
    
    longestPattern=''
    
    lst={cena, dor, cena+dor}
    for letter1 in range(0, len(cena)):
       for letter2 in range(0, len(dor)):
          lst.add(cena[letter1:]+dor[letter2:])

    
    for pattern in lst:
       repeat=0
       for i in range(0, len(s)):
          if pattern==s[i:i+len(pattern)]:
             repeat+=1
             if pattern>longestPattern and repeat>=2:
               longestPattern=pattern
             
    return longestPattern
'''

'''#recursiva, com método "in" alterado/transmutado, e funciona. Dor aguda depilação a cera às minhas costas com pêlo

# Given a string s, return the longest prefix that is repeated somewhere else in the string. 
# For example, "abcdabejf" would return "ab" as "ab" starts at the beginning of the string
# and is repeated again later. Do not use the find method.

def longestPrefixRepeated(s):
    # Your code here...
    
    if s=='':
       return s
       
    longestPattern=''
    for idxLetter in range(1, len(s)):
       for portion in range(idxLetter, len(s)):
          repeat=0
          length=len(s[0]+s[1:idxLetter])
          if s[0]+s[1:idxLetter] == s[portion:portion+length] or s[portion:portion+length]==s[portion+idxLetter:portion+idxLetter+length]:
             repeat+=1
          if repeat>=1 and len(s[0]+s[1:idxLetter])>=len(longestPattern):
             longestPattern=s[0]+s[1:idxLetter]
             
    longestPattern2=longestPrefixRepeated(s[1:])
    if len(longestPattern)>=len(longestPattern2):
      return longestPattern
    return longestPattern2
       
'''



''' Recursivo, e funciona. Dor

# Given a string s, return the longest prefix that is repeated somewhere else in the string. 
# For example, "abcdabejf" would return "ab" as "ab" starts at the beginning of the string
# and is repeated again later. Do not use the find method.

def longestPrefixRepeated(s):
    # Your code here...
    
    if s=='':
       return s
       
    longestPattern=''
    for idxLetter in range(1, len(s)):
       pattern=s[0]+s[1:idxLetter]
       if pattern in s[len(pattern):] and len(pattern)>len(longestPattern):
          longestPattern=pattern
          
             
    longestPattern2=longestPrefixRepeated(s[1:])
    if len(longestPattern)>len(longestPattern2):
      return longestPattern
    return longestPattern2
       

'''