import copy


def askTeams():
    teams = []
    while True:
        team = input("Insert a team (Enter nothing to exit): ")
        if team == "":
            return teams
        teams.append(team)


def all_matches(teams):
    matches = []
    for team1 in teams:
        for team2 in teams:
            if team1 != team2:
                matches.append((team1, team2))
    print(matches)
    return matches


def all_scorelines(matches):
    scorelines = {}
    for match in matches:
        while True:
            try:
                frase="Número de golos de "+str(match[0])+":"
                n1 = int(input(frase))
            except:
                print("Número de golos tem de ser um inteiro. Tente novamente.")

            try:
                frase="Número de golos de "+str(match[1])+":"
                n2 = int(input(frase))
                
            except:
                print("Número de golos tem de ser um inteiro. Tente novamente.")

            scorelines[match] = (n1, n2)
            
            #stats[match[0]][3]+=n1
            #stats[match[0]][4]+=n2

            #stats[match[1]][3]+=n2
            #stats[match[1]][4]+=n1

            #if n1>n2:
            #    stats[match[0]][0]+=1
            #    stats[match[0]][5]+=3
            
            #    stats[match[1]][2]+=1
            
            #if n1<n2:
            #    stats[match[0]][2]+=1

            #    stats[match[1]][5]+=3
            #    stats[match[1]][0]+=1

            #if n1==n2:
            #    stats[match[0]][1]+=1
            #    stats[match[0]][5]+=1

            #    stats[match[1]][1]+=1
            #    stats[match[1]][5]+=1

            break

    return scorelines

def all_stats(scorelines):
    stats = {}
    for match in scorelines.keys():
        
        if match[0] not in stats:
            stats[match[0]] = [0,0,0,0,0,0]
        if match[1] not in stats:
            stats[match[1]] = [0,0,0,0,0,0]


        n1, n2 = scorelines[match]

        stats[match[0]][3]+=n1
        stats[match[0]][4]+=n2

        stats[match[1]][3]+=n2
        stats[match[1]][4]+=n1

        if n1>n2:
            stats[match[0]][0]+=1
            stats[match[0]][5]+=3
            
            stats[match[1]][2]+=1
            
        if n1<n2:
            stats[match[0]][2]+=1

            stats[match[1]][5]+=3
            stats[match[1]][0]+=1

        if n1==n2:
            stats[match[0]][1]+=1
            stats[match[0]][5]+=1

            stats[match[1]][1]+=1
            stats[match[1]][5]+=1

    return stats

def confronto_direto(team1, team2, scorelines):
    t1_goals=0
    t2_goals=0
    for match in list(scorelines.keys()):
        if (team1, team2) == match:
            t1_goals+=scorelines[match][0]
            t2_goals+=scorelines[match][1]
        if (team2, team1) == match:
            t1_goals+=scorelines[match][1]
            t2_goals+=scorelines[match][0]
    if t1_goals == t2_goals:
        return ""

    print("(Fator de desempate entre {:s} e {:s}: confronto direto)".format(team1, team2))
    if t1_goals > t2_goals:
        return team1
    return team2



def champion(stats, scorelines):
    topPoints = 0
    champs = []
    for team in stats:
        if stats[team][5]>topPoints:
            topPoints = stats[team][5]
            champs=[]
            champs.append(team)
        elif stats[team][5]==topPoints:
            champs.append(team)

    if champs==[]:
        return []

    if len(champs)==1:
        return champs[0]
    else:
        def desempatador(dicio1, dicio2, contaDor=0, lista=["diferença de golos", "golos a favor", "golos contra", "sorte"]): #em caso de empate pontual entre 2 equipas, esta função é invocada
            if dicio1[list(dicio1.keys())[0]] == []:
                print("(Fator de desempate entre {:s} e {:s}: {:s})".format(list(dicio1.keys())[0], list(dicio2.keys())[0], lista[contaDor]))
                return list(dicio1.keys())[0] #caso não haja mais nada para comparar, é campeão o primeiro a entrar como argumento na função (escolha aleatória)

            if dicio1[list(dicio1.keys())[0]][0] > dicio2[list(dicio2.keys())[0]][0]:
                print("(Fator de desempate entre {:s} e {:s}: {:s})".format(list(dicio1.keys())[0], list(dicio2.keys())[0], lista[contaDor]))
                return list(dicio1.keys())[0]

            if dicio1[list(dicio1.keys())[0]][0] < dicio2[list(dicio2.keys())[0]][0]:
                print("(Fator de desempate entre {:s} e {:s}: {:s})".format(list(dicio1.keys())[0], list(dicio2.keys())[0], lista[contaDor]))
                return list(dicio2.keys())[0]

            #dicio1_clone={ list(dicio1.keys())[0] : list(dicio1.values())[1:]}
            dicio1_clone=copy.deepcopy(dicio1)
            dicio1_clone[list(dicio1_clone.keys())[0]].pop(0)
            #dicio2_clone={ list(dicio2.keys())[0] : list(dicio2.values())[1:]}
            dicio2_clone=copy.deepcopy(dicio2)
            dicio2_clone[list(dicio2_clone.keys())[0]].pop(0)
            #print(dicio2_clone, "desemparator")
            return desempatador(dicio1_clone, dicio2_clone, contaDor+1)


        #Confronto direto
        t1=0
        for t in range (0, len(champs)):
            resultado = confronto_direto(champs[t1], champs[t], scorelines)
            if resultado == champs[t1]:
                champs.pop(t)
                t=t1
            elif resultado == champs[t]:
                champs.pop(t1)
                t1=t


        #Diferença de golos, golos marcados, golos sofridos, sorte?
        l1 = {champs[0] : [stats[champs[0]][3] - stats[champs[0]][4], stats[champs[0]][0], stats[champs[0]][1]   ]}
        campeao=champs[0]
        #champs.remove(list(l1.keys())[0])
        for t in champs:
            if t == campeao:
                continue
            l2={t : [stats[t][3] - stats[t][4], stats[t][0], stats[t][1]   ]}
            #print(l1)
            #print(l2)
            campeao = desempatador(l1, l2)
            if campeao == list(l1.keys())[0]:
                pass
            else:
                l1 = {campeao : [stats[campeao][3] - stats[campeao][4], stats[campeao][0], stats[campeao][1]   ]}
                #champs.remove(list(l1.keys())[0])

        return campeao

def printTabela(stats, scorelines):
    print("{:<10s} {:<15s} {:<15s} {:<15s} {:<15s} {:<15s} {:<15s}". format("Equipa", "Vitórias", "Empates", "Derrotas", "Golos marcados", "Golos sofridos", "Pontos"))
    for t in stats:
        print("{:<10s} {:<15n} {:<15n} {:<15n} {:<15n} {:<15n} {:<15n}". format(t, stats[t][0], stats[t][1], stats[t][2], stats[t][3], stats[t][4], stats[t][5]))

    print("The champion: ", champion(stats, scorelines))
            
def main():
    equipas = askTeams()
    jogos = all_matches(equipas)
    resultados = all_scorelines(jogos)
    estatisticas = all_stats(resultados)
    printTabela(estatisticas, resultados)

main()