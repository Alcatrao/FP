# Exercise 5 on "How to think like a computer scientist", ch. 11.

import turtle

t = turtle.Turtle()

# Use t.up(), t.down() and t.goto(x, y)

# Put your code here


def turtle_actions():
    with open('C:/Users/joaoa/OneDrive/Ambiente de Trabalho/FP/aula06/drawing.txt', 'r') as actions:
        for action in actions:
            try:
                coordinates = action.split()
                #print(coordinates)
                t.goto(int(coordinates[0]), int(coordinates[1]))        #as coordenadas têm que ser ints
                #print("Try successful")
            except:
                #print("Try failed")
                #print(action)                                          #tem sempre uma linha nova por baixo; nunca iguala "UP" ou "Down"
                coordinates = action.split()
                action = coordinates[0]
                if action == '':
                    break
                elif action == 'UP':
                    t.up()                                              #os t.up() e t.down() nunca chegavam a ocorrer antes da inserção da linha de .split(), porque action tinha sempre newline por baixo (pelo que nunca igualava "UP" ou "DOWN")
                    #print("Up!")
                elif action == 'DOWN':
                    t.down()
                    #print("Down!")
     
                



turtle_actions() #tem que estar antes do turtle.Screen(); caso contrário, não há "canvas" para a tartaruga pintar (o que resulta em erro)
# wait
turtle.Screen().exitonclick()



