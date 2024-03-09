def firstRepeatedWord(s):
    # Your code here...
    if s=='':
       return s
    palavras=s.split()
    for i in range(1, len(palavras)):
       if palavras[0]==palavras[i]:
          return palavras[0]
    return firstRepeatedWord(s[1:])

    '''Dor depilação  
    '''