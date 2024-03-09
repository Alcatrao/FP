
def getAllStrings(obj):
   """Get a list with all the strings contained in the given object."""

   lst = []
   if isinstance(obj, str):   # if obj is a string, just store it
      lst.append(obj)
   # If obj is a list, etc., we must call recursively for each of its elements
   if isinstance(obj, set) or isinstance(obj, list) or isinstance(obj, tuple):
      for elemento in obj:
         stringsLista=getAllStrings(elemento)
         lst+=stringsLista
         
   if isinstance(obj, dict):
      for chave, valor in obj.items():
         stringsDicio=getAllStrings(chave)
         stringsValor=getAllStrings(valor)
         lst+=stringsDicio
         lst+=stringsValor

   return lst


def main():
   obj1 = ["one", 2, ["three", 4, [5, "six"]]]
   obj2 = [1, "a", ("b", [{"c", "d", 2}, 3, (4, "e")], "f")]
   obj3 = {"a": 1, "b": ["c", "d"], (2, ("x", 3)): obj1}
   print(eval(input()))


if __name__ == "__main__":
   main()
