
# Given a list of integers, return the second-largest element.

def secondLargestElement(arr):
   def secondLargestElement2(arr):
       # Your code here...
       if len(arr)==1:
          return arr[0], arr[0]
       if len(arr)==2:
          return arr[0], arr[1]
       meio=len(arr)//2
       mau1, mau2=secondLargestElement2(arr[:meio])
       dor1, dor2=secondLargestElement2(arr[meio:])
       
       #lst={mau1, mau2, dor1, dor2}
       lst=set([mau1, mau2, dor1, dor2])
       lst=sorted(list(lst))
       
       if len(lst)==4:
          return lst[2], lst[3]
       elif len(lst)==3:
          return lst[1], lst[2]
       elif len(lst)==2:
          return lst[0], lst[1]
       else:
          return lst[0]
   return secondLargestElement2(arr)[0]