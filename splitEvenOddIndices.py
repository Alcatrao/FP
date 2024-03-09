# Given a list of integers, return a list of length 2, 
# each being a list. The first one holds the elements with even 
# positions, and the second one holds the elements with odd 
# positions of the original list.

def evenIndices(arr):
   if arr==[]:
      return [[], []]
   par1, impar1 = [arr[0]], []
   par2, impar2 = oddIndices(arr[1:])
   return [par1+par2, impar1+impar2]
   
def oddIndices(arr):
   if arr==[]:
      return [[], []]
   par1, impar1 = [], [arr[0]]
   par2, impar2 = evenIndices(arr[1:])
   return [par1+par2, impar1+impar2]

def splitEvenOddIndices(arr):
    return evenIndices(arr)