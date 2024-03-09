
# Given a list of integers and a value, return the position of 
# the element that is closest in value to the given value. If 
# there is more than one, return the position of the first one.
# Return -1 if the list is empty.
def findClosestValueIndex(arr, val):
   def findClosestValueIndex2(arr, val):
       # Your code here...
       if arr==[]:
          return -1, 0
       if len(arr)==1:
          if arr[0]==val:
             return 0, 29000
          return 0, abs(val-arr[0])
          
       meio=len(arr)//2
       idx1, dor=findClosestValueIndex2(arr[:meio], val)
       idx2, mau=findClosestValueIndex2(arr[meio:], val)
       
       if dor<=mau:
          return idx1, dor
       return idx2+meio, mau
       
   return findClosestValueIndex2(arr, val)[0]