# Complete the code to make the HiLo game...

import random
import string

#def cena(dor):
#    while True:
#        try:
#            number = int(input(dor))
#            return number
#        except:
#            print("Invalid number. Try again.")

def cena():
   while True:
        try:
            number = int(input("Choose a number: "))
            return number
        except:
            print("Invalid number. Try again.")


def main():
    # Pick a random number between 1 and 100, inclusive
    secret = random.randrange(1, 101);
    print("Can you guess my secret?")
    # put your code here
    
    #number=cena("Try to find it! \n")
    while True:
        number=cena()
        if number < secret:
            #number=cena("The chosen number is too small, try again: \n")
            print("The chosen number is too small, try again.")
        elif number > secret:
            #number=cena("The chosen number is too big, try again: \n")
            print("The chosen number is too big, try again.")
        elif number == secret:
            print("You have correctly guessed the secret!")
            break
        else:
            print("Something dark and ominous is at play here. Is is well beyond the known horrors of this world. Do not feel it, for it is far worse than any pain you have experienced. Cena dor.")
            exit(29)




main()
