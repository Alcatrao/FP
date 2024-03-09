def CowsAndBulls(guess, secret):
    if len(guess)!=len(secret):
        print("Error - mismatching lenghts.")
        exit()

    bulls=0
    cows=0

    used=''
    bullsIdx=[]

    for idx in range(0, len(guess)): #bulls
        if guess[idx] == secret[idx]:
            bulls+=1
            #used+=guess[idx]
            bullsIdx.append(idx)

    newSecret=''
    newGuess=''
    for idx in range(0, len(guess)):
        if idx not in bullsIdx:
            newSecret+=secret[idx]
            newGuess+=guess[idx]

    #for idx in range(0, len(guess)): #cows
    #    if guess[idx] in secret and guess[idx] not in used:
    #        cows+=1
    #        used+=guess[idx]

    for idx in range(0, len(newSecret)):
        if newGuess[idx] in newSecret:
            cows+=1
            used+=newGuess[idx]


    print("(bulls, cows) = ({:d}, {:d})".format(bulls, cows))
    exit()


guess="MARIA"
word="ALADA"
CowsAndBulls(guess, word)


