
# Constantes para indexar os tuplos:
import os

NAME,DATE,OPEN,MAX,MIN,CLOSE,VOLUME = 0,1,2,3,4,5,6

def main():
    lst = loadStockFile("nasdaq.csv")
    # Show just first and last tuples:
    print("first:", lst[1])
    print("last:", lst[-1])
    
    print("a) totVol=", totalVolume(lst))

    print("b) maxVal=", maxValorization(lst))
    
    stocksDic = stocksByDateByName(lst)
    print("c) CSCO@11:", stocksDic['2020-10-12']['CSCO'])
    print("c) AMZN@22:", stocksDic['2020-10-22']['AMZN'])

    port = {'NFLX': 100, 'CSCO': 80}
    print("d) portfolio@01:", portfolioValue(stocksDic, port, "2020-10-01"))
    print("d) portfolio@30:", portfolioValue(stocksDic, port, "2020-10-30"))

def loadStockFile(filename):
    #este programa não tinha estas 2 linhas, mas precisa delas para abrir o ficheiro
    diretoria = os.path.realpath(os.path.dirname(__file__))
    filename = os.path.join(diretoria, filename)

    lst = []
    with open(filename) as f:
        for line in f:
            parts = line.strip().split('\t')
            name = parts[NAME]
            date = parts[DATE]
            tup = (name, date, float(parts[OPEN]), float(parts[MAX]),
                float(parts[MIN]), float(parts[CLOSE]), int(parts[VOLUME]))
            lst.append(tup)
    return lst

def totalVolume(lst):
    totVol = {}
    # Complete ...
    for tup in lst:
        if tup[NAME] not in totVol:
            totVol[tup[NAME]] = tup[VOLUME]
        totVol[tup[NAME]] += tup[VOLUME]

    return totVol

def maxValorization(lst):
    vMax = {}
    # Complete ...
    for tup in lst:
        if tup[DATE] not in vMax:
            vMax[tup[DATE]] = (tup[NAME], (tup[OPEN]/tup[CLOSE] * 100))
        else:
            if (tup[OPEN]/tup[CLOSE] - 100) > vMax[tup[DATE]][1]:
                vMax[tup[DATE]] = (tup[NAME], (tup[OPEN]/tup[CLOSE] * 100))

    return vMax

def stocksByDateByName(lst):
    dic = {}
    # Complete ...
    for tup in lst:
        if tup[DATE] not in dic:
            dic[tup[DATE]] = {tup[NAME] : (tup[OPEN], tup[MAX], tup[MIN], tup[CLOSE], tup[VOLUME])}
        else:
            dic[tup[DATE]][tup[NAME]] = (tup[OPEN], tup[MAX], tup[MIN], tup[CLOSE], tup[VOLUME])


    return dic

def portfolioValue(stocks, portfolio, date):
    assert date in stocks
    val = 0.0
    # Complete ...
    for stock in portfolio:
        if stock in stocks[date]:
            val += stocks[date][stock][3] * portfolio[stock]

    return val

if __name__ == "__main__":
    main()
