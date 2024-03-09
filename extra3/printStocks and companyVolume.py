def printStocks(stocks):
   #for tuple in stocks:
   #   valor=float((tuple[3]-tuple[2])/tuple[2])*100
   #   #if tuple[3]>tuple[2]:
   #   #   valor=-valor
   #   print("{:<10s}{:<10s}{:>10.2f}{:>10.2f}{:>10d}{:>10.1f}%".format(tuple[0], tuple[1], float(tuple[2]), float(tuple[3]), int(tuple[4]), valor))
   
   if stocks==[]:
      return
   tuple=stocks[0]
   valor=float((tuple[3]-tuple[2])/tuple[2])*100
   print("{:<10s}{:<10s}{:>10.2f}{:>10.2f}{:>10d}{:>10.1f}%".format(tuple[0], tuple[1], float(tuple[2]), float(tuple[3]), int(tuple[4]), valor))
   printStocks(stocks[1:])


def companyVolume(stocks, city):
   #lista=[]
   #for tuple in stocks:
   #   if tuple[1]==city:
   #      lista.append((tuple[0], tuple[4]))
   #return lista
   
   if stocks==[]:
      return []
      
   tuple=stocks[0]
   if tuple[1]==city:
      return [(tuple[0], tuple[4])] + companyVolume(stocks[1:], city)
   return companyVolume(stocks[1:], city)