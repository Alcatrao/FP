def allMatches(lst):
    matches=[]
    if lst==[]:
        #return []
        return [], 0
    
    #if len(lst)==1:
    #    return [lst[0]]

    #if len(lst)==2:
    #    matches=[[lst[0]]+allMatches(lst[1:])]
    #    return matches                             #estas 2 secções podem ser (des)comentadas e o resultado será o mesmo

    for i in range(1,len(lst)): #este ciclo for é ignorado quando o tamanho da lista é igual a 1
        matches.append([lst[0], lst[i]])
        matches.append([lst[i], lst[0]])

    otherMatches = allMatches(lst[1:])
    return matches + otherMatches[0], len(matches) + otherMatches[1]
    #return matches + allMatches(lst[1:])



equipas=["Eu", "Tu", "Ela", "Nós", "Vós", "Eles"] #nº total de jogos é igual ao número de arranjos n 2 a 2: n!/(n-2)!
print(allMatches(equipas))




#def allMatches_divide_and_conquer(lst):
#    matches=[]
#    
#    if len(lst)==1:
#        return [lst[0]]
#
#    meio=len(lst)//2
#    cena=allMatches_divide_and_conquer(lst[0:meio])
#    dor=allMatches_divide_and_conquer(lst[meio:])
#
#    for match1 in cena:
#        for match2 in dor:
#            matches.append(match1+match2)
#
#    return matches
    
