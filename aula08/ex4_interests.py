
def main():
    A = "reading"
    B = "eating"
    C = "traveling"
    D = "writing"
    E = "running"
    F = "music"
    G = "movies"
    H = "programming"

    interests = {
        "Marco": {A, D, E, F},
        "Anna": {E, A, G},
        "Maria": {G, D, E},
        "Paolo": {B, D, F},
        "Frank": {D, B, E, F, A},
        "Teresa": {F, H, C, D}
        }


    print("a) Table of common interests:")

    commoninterests = {(x,y): interests[x].intersection(interests[y]) for x in interests for y in interests if x!=y}
    commoninterestsCopy = commoninterests.copy()
    for (x,y) in commoninterests: 
        if (x,y) in commoninterestsCopy:
            del commoninterestsCopy[(y,x)] 
    commoninterests = commoninterestsCopy
    
    print(commoninterests)

    print("b) Maximum number of common interests:")

    maxCI = max( (len(x) for x in list(commoninterests.values())  ) )
    print(maxCI)

    print("c) Pairs with maximum number of matching interests:")
    maxmatches = [ (x,y) for (x,y) in commoninterests if len(commoninterests[(x,y)]) == maxCI ]
    print(maxmatches)

    print("d) Pairs with low similarity:")
    lowJaccard = [ (x,y) for (x,y) in commoninterests if len(interests[x].intersection(interests[y])) / len(interests[x].union(interests[y])) <= 0.25]
    print(lowJaccard)


# Start program:
main()

