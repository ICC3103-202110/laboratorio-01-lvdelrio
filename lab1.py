# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 13:15:11 2021

@author: lucas
"""


import random
import sys

def memorama():
    
    screen()
    print('player 1´s turn')
    
    x = int(input('Enter a value from left to right as you see on screen: '))
    if x >= len(matrix[0]):
        print('ERROR')
        memorama()

    y = int(input('Enter a value from top to bottom as the values on the screen indicate: '))
    if y >= len(matrix):
        print('ERROR')
        memorama()
    elif matrix[y][x] == " ":
        print("this coordinate has already been revealed, try another position")
        memorama()

    matrix[y][x] = matrix2[y][x]

    screen()
#---------------------------------------------------------------------------|
    while True:
        
        x2 = int(input('Enter a value from left to right as you see on screen: '))
        y2 = int(input('Enter a value from top to bottom as the values on the screen indicate: '))
        if (x2,y2) != (x,y):
            if x2 >= len(matrix[0]):
                print('ERROR')
                matrix[y][x] = '-'
            elif y2 >= len(matrix):
                print('ERROR')
                matrix[y][x] = '-'
            elif matrix[y2][x2] == " ":
                print("this coordinate has already been revealed, try another position")
            else:
                break
        else:
            print("ERROR, you placed the same coordinate, try again")
#---------------------------------------------------------------------------|

    matrix[y2][x2] = matrix2[y2][x2]
    screen()
    turn=0
    condition(x,y,x2,y2,turn)

def memorama2():
    screen()
    print('player 2´s turn')

    x = int(input('Enter a value from left to right as you see on screen: '))
    if x >= len(matrix[0]):
        print('ERROR')
        memorama2()

    y = int(input('Enter a value from top to bottom as the values on the screen indicate: '))
    if y >= len(matrix):
        print('ERROR')
        memorama2()
    elif matrix[y][x] == " ":
        print("this coordinate has already been revealed, try another position")
        memorama2()

    matrix[y][x] = matrix2[y][x]
    screen()
#--------------------------------------------------------------------------|
    while True:
        
        x2 = int(input('Enter a value from left to right as you see on screen: '))
        y2 = int(input('Enter a value from top to bottom as the values on the screen indicate: '))
        if (x2,y2) != (x,y):
            if x2 >= len(matrix[0]):
                print('ERROR')
                matrix[y][x] = '-'
            elif y2 >= len(matrix):
                print('ERROR')
                matrix[y][x] = '-'
            elif matrix[y2][x2] == " ":
                print("this coordinate has already been revealed, try another position")
            else:
                break
        else:
            print("ERROR, you placed the same coordinate, try again")
#---------------------------------------------------------------------------|
    matrix[y2][x2] = matrix2[y2][x2]
    
    screen()
    turn=1
    condition(x,y,x2,y2,turn)

def condition(x,y,x2,y2,turn):
    global p1
    global p2
#----------------------------------------------------turns-------------------|
    if turn == 0:
        if matrix[y][x] != matrix[y2][x2]:
            matrix[y2][x2] = "-"
            matrix[y][x] = "-"
            memorama2()
        else:
            matrix[y2][x2] = " "
            matrix[y][x] = " "
            p1 += 1 
            print("player 1 won a point, now you have: ",p1)
            endgame(x,y,x2,y2,turn)
    elif turn == 1:
        if matrix[y][x] != matrix[y2][x2]:
            matrix[y2][x2] = "-"
            matrix[y][x] = "-"
            memorama()
        else:
            matrix[y2][x2] = " "
            matrix[y][x] = " "
            p2 += 1 
            print("player 2 won a point, now you have: ",p2)
            endgame(x,y,x2,y2,turn)

    
#------------------------------------check endgame-----------------------------------------|
def check():
    for i in range(len(matrix)):
        for j in range(len (matrix[0])):
            if matrix[i][j] != " ":
                return False
    return True


def endgame(x,y,x2,y2,turn):

    equal = check()
    
    if equal == True:
        print('the player 1 have ',p1,'pairs')
        print('the player 2 have ',p2,'pairs')
        if p1 > p2:
            print('The winner was player 1')
        elif p2 > p1:
            print('The winner was player 2')
        elif p2 == p1:
            print('it was a tie!')
        elif p1 == p2:
            print('it was a tie!')
        sys.exit() 
    else:
        if turn == 0:
            print("it's your turn again")
            memorama()
        else:
            print("it's your turn again")
            memorama2()



def screen():
    contador = 0
    for i in range(len(matrix[0])):
        print("",i,"", end = '')
    print("\n")
    for i in range(len(matrix)):
        print(contador, '', end = '')
        contador += 1
        for j in range(len(matrix[0])):
            print((matrix[i][j]),' ', end = '')

        print('\n')

def main():
    memorama()
        
#----------------------------------------global variables----------------------------------|       
x=0        
y=0
x2=0
y2=0
p1 = 0
p2 = 0
turn=0
equal=0
lista=[]
matrix = []
matrix2 = [[],[]]

cant_cartas=int(input("enter the number of the pair you want to play"))


for i in range(cant_cartas):
    lista.append(i+1)
lista=lista*2
random.shuffle(lista)
matrix2=[lista[0:int(len(lista)/2)],lista[int(len(lista)/2):int(len(lista))]]
    

lista=[]
for i in range(cant_cartas):
    lista.append("-")
lista=lista*2

matrix=[lista[0:int(len(lista)/2)],lista[int(len(lista)/2):int(len(lista))]]


main()