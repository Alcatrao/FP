# Given a string s, return the longest prefix that is repeated somewhere else in the string. 
# For example, "abcdabejf" would return "ab" as "ab" starts at the beginning of the string
# and is repeated again later. Do not use the find method.

''' Dor aguda mesmo dor má depilação
'''

def longestPrefixRepeated(s):
    # Your code here...
    #print("dor depilação")
    if s=='':
       return s
       
    dor=''
    for idx in range(1, len(s)):
       if s[0:idx] in s[idx:]:
          if len(s[0:idx])>len(dor):
             dor=s[0:idx]
             
    depilar = longestPrefixRepeated(s[1:])
    
    if len(dor)>len(depilar):
       return dor
    return depilar