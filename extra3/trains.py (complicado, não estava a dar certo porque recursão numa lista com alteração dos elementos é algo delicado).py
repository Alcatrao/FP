   #for vagao in range(len(t)-1:-1:-1):
   #   if t[vagao][0]==m:


   if q==0:
      return 0
   if t==[]:
      return q
   
   if t[-1][0]==m:
      if t[-1][1]>q:
         t[-1][1]-=q
         return unload(t, m, 0)
      elif t[-1][1]==q:
         t.pop()
         return unload(t, m, 0)
      else:
         parcial=t[-1][1]
         t.pop()
         return unload(t, m, q-parcial)
         
   last=t.pop()
   next=unload(t,m,q)
   t.append(last)
   return next
   #last = t.pop()
   #return unload(t, m, q), t.append(last)
         