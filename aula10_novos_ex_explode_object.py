def explodeObject(name, obj):
   """Print the name and representation (repr) of an object,
   followed by the name and representation of each of its elements,
   if the object is a list, tuple or dict.
   """
   print(f"{name} = {obj!r}")       # !r converts object to its repr!
   #print("{} = {!r}".format(name, obj))    # equivalent

   if isinstance(obj, list) or isinstance(obj, set) or isinstance(obj, tuple):   # if obj is a list...
      # call recursively for each of its elements
   # Then do something similar for tuples and dicts
      idx=0
      for elemento in obj:
         newName=name+"["+str(idx)+"]"
         explodeObject(newName, elemento)
         idx+=1
         
   if isinstance(obj, dict):
      for chave, valor in obj.items():
         newName=name+"['"+str(chave)+"']"
         explodeObject(newName, valor)
         
   


def main():
   obj1 = [1, ["a", ["b", 2], 3], 4]
   obj2 = [1, "ola", (2, [[3, 4], 5, ("adeus", 6)], 7)]
   obj3 = [1, {"ola": "hello", "adeus": ["bye", "adieu"]}, (2, [[3, 4], 5], 6)]
   eval(input())


if __name__ == "__main__":
   main()
