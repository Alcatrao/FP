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

def champion(stats):
    topPoints = 0
    champs = []
    for team in stats:
        if stats[team][5]>topPoints:
            topPoints = stats[team][5]
            champs=[]
            champs.append(team)
        elif stats[team][5]==topPoints:
            champs.append(team)

    if len(champs)==1:
        return champs[0]
    else:
        def desempatador(dicio1, dicio2): #em caso de empate pontual entre 2 equipas, esta função é invocada
            if dicio1[list(dicio1.keys())[0]] == []:
                return list(dicio1.keys())[0] #caso não haja mais nada para comparar, é campeão o primeiro a entrar como argumento na função (escolha aleatória)

            if dicio1[list(dicio1.keys())[0]][0] > dicio2[list(dicio2.keys())[0]][0]:
                return list(dicio1.keys())[0]

            if dicio1[list(dicio1.keys())[0]][0] < dicio2[list(dicio2.keys())[0]][0]:
                return list(dicio2.keys())[0]

            dicio1[list(dicio1.keys())[0]].pop(-1)
            dicio2[list(dicio2.keys())[0]].pop(-1)
            return desempatador(dicio1, dicio2)

        #confronto direto, diferença de golos, golos marcados, golos sofridos, sorte?
        l1 = {champs[0] : [stats[champs[0]][3] - stats[champs[0]][4], stats[champs[0]][0], stats[champs[0]][1]   ]}
        for t in champs:
            l2={t : [stats[t][3] - stats[t][4], stats[t][0], stats[t][1]   ]}
            campeao = desempatador(l1, l2)
            if campeao == l1.keys():
                pass
            else:
                l1 = {campeao : [stats[campeao][3] - stats[campeao][4], stats[campeao][0], stats[campeao][1]   ]}

        return campeao

def printTabela(stats):
    print("{:<10s} {:<15s} {:<15s} {:<15s} {:<15s} {:<15s} {:<15s}". format("Equipa", "Vitórias", "Empates", "Derrotas", "Golos marcados", "Golos sofridos", "Pontos"))
    for t in stats:
        print("{:<10s} {:<15n} {:<15n} {:<15n} {:<15n} {:<15n} {:<15n}". format(t, stats[t][0], stats[t][1], stats[t][2], stats[t][3], stats[t][4], stats[t][5]))

    print("The champion: ", champion(stats))
            
def main():
    equipas = askTeams()
    jogos = all_matches(equipas)
    resultados = all_scorelines(jogos)
    estatisticas = all_stats(resultados)
    printTabela(estatisticas)

main()