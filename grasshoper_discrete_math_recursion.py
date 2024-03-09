def grasshoper(n):          #this function returns the number of ways a grasshoper can climb "n" stairs, considering it can jump 1, 2, or 3 steps at a time
    if n<=1:
        return 1            #only one way to climb 1 step (a single 1 step jump)
    if n==2:
        return grasshoper(1) + 1            #2 ways to climb 2 stairs: 1) make a singe 2 step jump; 2) jump 1 step twice. Both ways result in 2 steps climbed
    if n==3:
        return grasshoper(2) + grasshoper(1) + 1            #4 ways to climb 3 stairs: 1) make a single 3 step jump; [   2) jump 2 steps at once, then jump another single step; 3) jump 1 step twice, then jump another single step   ]
                            #(   4) jump 1 step, and then jump 2 steps at once     )
                            #the ways to climb 3 stairs that are in brackets above, are the same [   ways to climb 2 stairs   ], and then taking another a single step, and the same (   ways to climb 1 single
                            #stair   ), and then jumping 2 stairs at once.  
    #if n>4
    return grasshoper(n-1) + grasshoper(n-2) + grasshoper(n-3)

                            #the ways to climb 4 stairs, are the same ways to climb 3 stairs, and then jump a single step, plus the same ways to climp 2 stairs, and then jump 2 steps at once, plus the same ways
                            #to climb 1 stair, and then jump 3 steps at once. Notice that the ways to climb 4 stairs that consist of, for example, climbing 2 stairs, and then jumping 1 step twice, are already
                            #included in the ways to climb 3 stairs that end in a single step, appended with another single step. So these are already covered in the ways to climb 4 stairs above.

def askInput():
    while True:
        try:
            n = int(input("Quantos degraus tem a escada que o grilo quer subir? "))
            return n
        except:
            print("Número inválido. Tente novamente.")

def main():
    print("Um grilo quer subir umas escadas. O grilo pode saltar 1, 2, ou 3 degraus com cada salto.")
    n = askInput()
    print("O grilo pode subir uma escada com", n, "degraus de", grasshoper(n), "maneiras diferentes.")

main()