def trainsPerMerchandise(trains):
   
   '''
   diciMercadorias={}
   
   
   for nome,comboio in trains.items():
      for vagao in comboio:
         if vagao[0] not in diciMercadorias:
            diciMercadorias[vagao[0]]=set()
            diciMercadorias[vagao[0]].add(nome)
         else:
            diciMercadorias[vagao[0]].add(nome)
            
   return diciMercadorias
   '''
            
   
   diciMercadorias={}
   
   trains_items = list(trains.items())
   
      
   
   def trainsPerMerchandise_recursion(trains_items):
      if trains_items==[]:
         return
      nome, comboio = trains_items[0]
      for vagao in comboio:
         if vagao[0] not in diciMercadorias:
            diciMercadorias[vagao[0]]=set()
            diciMercadorias[vagao[0]].add(nome)
         else:
            diciMercadorias[vagao[0]].add(nome)
      return trainsPerMerchandise_recursion(trains_items[1:])
   
   trainsPerMerchandise_recursion(trains_items)
      
      
          
   return diciMercadorias











   
   '''
   def diciFiller():
      if list(trains.keys())==[]:
         return diciMercadorias
      for mercadoria in trains[list(trains.keys())[-1]]:
         if mercadoria[0] not in diciMercadorias:
            diciMercadorias[mercadoria[0]]={list(trains.keys())[-1]}
         else:
            diciMercadorias[mercadoria[0]].add(list(trains.keys())[-1])
      
      lastNomes = list(trains.keys()).pop()
      lastComboio = list(trains.values()).pop()
      diciFiller()
      list(trains.keys()).append(lastNomes)
      list(trains.values()).append(lastComboio)

   return diciFiller()
   '''         
   
     
   
   