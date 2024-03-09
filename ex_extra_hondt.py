def hondt(votes, numseats):
   Q=[0]*len(votes)
   N=[0]*len(votes)
   while True:
      if sum(N)>=numseats:
         return N
      top = 0
      partido=0
      for i in range(len(votes)):
         Q[i] = votes[i]/(N[i]+1)
         if Q[i] > top:
            top = Q[i]
            partido=i
         
      for j in range(len(Q)): #desempate
         for k in range(j+1,len(Q)):
            if Q[j]==Q[k]:
               if Q[j]==top:
                  if votes[j]<votes[k]:
                     if votes[j]<=votes[i]:
                        partido=j
                  else:
                     if votes[k]<=votes[i]:
                        partido=k
         
            
      N[partido]+=1