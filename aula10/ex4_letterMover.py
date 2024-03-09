def letterMover(palavra, letra):
    if palavra=='':
        return ''
    if palavra[0].lower()==letra.lower():
        return letterMover(palavra[1:], letra)+palavra[0]
    return palavra[0]+letterMover(palavra[1:], letra)


palavra='dor'
letra='r'

print(letterMover(palavra, letra))
print(letterMover("XxanaDor", 'x'))