# You throw a dart that hits coordinates (x, y) on a dartboard.
# Create a program that gives you the score.
# See:
#   https://en.wikipedia.org/wiki/Darts#Dartboard
#   https://www.dimensions.com/element/dartboard

import math


print("Enter the coordinates in mm from the center of the board.")
x = float(input("x? "))
y = float(input("y? "))

# Points of the sectors, clockwise from the top
# Example: the sector right from the center is POINTS[5] == 6.
POINTS = (20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5)

# COMPLETE...

distancia=math.sqrt(x**2 + y**2)

if x==0:
    angulo=90
else:
    angulo=math.degrees(math.atan(y/x))

#print(angulo)

if (x<0 and y<0):       #para poder ter um ângulo a variar entre 0 e 360, tendo como referência o semi-eixo positivo dos xx e andando em contra-relógio 
    angulo=angulo+180
elif (x<0 and y>0):
    angulo=-angulo+90
elif (x>0 and y<0):
    angulo=-angulo+270
else:
    angulo=angulo

#print(angulo)



index=5 #pontuação no ângulo 0
pontos=[0] * 20
pontuation=0

j=0
#atribuir pontação em função do ângulo:
for i in range(0, 360, 18): #360/20 = 18
    pontos[j]=POINTS[index]
    if (angulo)>=i and (angulo)<=i+18: #se o ângulo estiver nesta gama, atribuir pontuação
        #print(i,"    ", angulo)
        pontuation=pontos[j]

    index-=1
    j+=1
    if index<=-1:
        index=19 #mexer a pontuação conforme o ângulo (e como o ângulo sobe em contra-relógio e começa em 0 sobre o eixo das abcissas, e a lista dada cresce no sentido do relógio e começa nos 90º, isto é necessário)



if distancia > 170:
    score=0
elif distancia <= 170 and distancia >=(170-8):
    score = pontuation*2
elif distancia < (170-8) and distancia > 107:
    score = pontuation
elif distancia <= 107 and distancia >= (107-8):
    score = pontuation*3
elif distancia < (107-8) and distancia > 32:
    score = pontuation
elif distancia <= 32 and distancia > 12.7:
    score = 25
else:
    score=50 


print(score)
