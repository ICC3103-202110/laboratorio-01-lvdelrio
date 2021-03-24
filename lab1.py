# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 13:15:11 2021

@author: lucas
"""

import scipy
import numpy as np
import random
import sys

def memorama():
    
    imprimir()
    print('Turno de Jugador 1')
    
    x = int(input('Ingresa un valor de izquierda a derecha como ve en pantalla: '))
    if x >= len(matrix[0]):
        print('ERROR')
        memorama()

    y = int(input('Ingresa un valor de arriba hasta abajo como indican los valores en la pantalla: '))
    if y >= len(matrix):
        print('ERROR')
        memorama()
    print(x,y,matrix[y][x],matrix2[y][x])
    matrix[y][x] = matrix2[y][x]

    imprimir()
#---------------------------------------------------------------------------|
    while True:
        
        x2 = int(input('Ingresa un valor de izquierda a derecha como ve en pantalla: '))
        y2 = int(input('Ingresa un valor de arriba hasta abajo como indican los valores en la pantalla: '))
        if (x2,y2) != (x,y):
            if x2 >= len(matrix[0]):
                print('ERROR')
                matrix[y][x] = '-'
            if y2 >= len(matrix):
                print('ERROR')
                matrix[y][x] = '-'
            break
        else:
            print("aweonao qlo te crei muy chistoso maricon hazlo bien")
#---------------------------------------------------------------------------|

    matrix[y2][x2] = matrix2[y2][x2]
    imprimir()
    turno=0
    print(matrix)
    condiciones(x,y,x2,y2,turno)

def memorama2():
    imprimir()
    print('Turno de Jugador 2')

    x = int(input('Ingresa un valor de izquierda a derecha como ve en pantalla: '))
    if x >= len(matrix[0]):
        print('ERROR')
        memorama2()

    y = int(input('Ingresa un valor de arriba hasta abajo como indican los valores en la pantalla: '))
    if y >= len(matrix):
        print('ERROR')
        memorama2()

    matrix[y][x] = matrix2[y][x]
    imprimir()
#--------------------------------------------------------------------------|
    while True:
        
        x2 = int(input('Ingresa un valor de izquierda a derecha como ve en pantalla: '))
        y2 = int(input('Ingresa un valor de arriba hasta abajo como indican los valores en la pantalla: '))
        if (x2,y2) != (x,y):
            if x2 >= len(matrix[0]):
                print('ERROR')
                matrix[y][x] = '-'
            if y2 >= len(matrix):
                print('ERROR')
                matrix[y][x] = '-'
            break
        else:
            print("aweonao qlo te crei muy chistoso maricon hazlo bien")
#---------------------------------------------------------------------------|
    matrix[y2][x2] = matrix2[y2][x2]
    
    imprimir()
    turno=1
    print(matrix)
    condiciones(x,y,x2,y2,turno)

def condiciones(x,y,x2,y2,turno):
    global p1
    global p2
#----------------------------------------------------turnos-------------------|
    if turno == 0:
        if matrix[y][x] != matrix[y2][x2]:
            matrix[y2][x2] = "-"
            matrix[y][x] = "-"
            memorama2()
        else:
            matrix[y2][x2] = " "
            matrix[y][x] = " "
            p1 += 1 
            print("player 1 ganaste un punto ahora tienes ",p1)
            fin_del_juego(x,y,x2,y2,turno)
            print("te vuelve a tocar")
            memorama()
    elif turno == 1:
        if matrix[y][x] != matrix[y2][x2]:
            matrix[y2][x2] = "-"
            matrix[y][x] = "-"
            memorama()
        else:
            matrix[y2][x2] = " "
            matrix[y][x] = " "
            p2 += 1 
            print("player 2 ganaste un punto ahora tienes ",p2)
            fin_del_juego(x,y,x2,y2,turno)

    
#-----------------------------------------------------------------------------|
def recorre():
    for i in range(len(matrix)):
        for j in range(len (matrix[0])):
            if matrix[i][j] != " ":
                return False
    return True


def fin_del_juego(x,y,x2,y2,turno):

    equal = recorre()
    
    if equal == True:
        print('El jugador tiene',p1,'pares')
        print('El jugador tiene',p2,'pares')
        if p1 > p2:
            print('El ganador fue el jugador 1')
        elif p2 > p1:
            print('El ganador fue el jugador 2')
        elif p2 == p1:
            print('Fue un empate!')
        elif p1 == p2:
            print('Fue un empate!')
        sys.exit() 
    else:
        if turno == 0:
            print("te vuelve a tocar")
            memorama()
        else:
            print("te vuelve a tocar")
            memorama2()



def imprimir():
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
        
#----------------------------------------variables globales----------------------------------|       
x=0        
y=0
x2=0
y2=0
p1 = 0
p2 = 0
turno=0
equal=0
lista=[]
matrix = []
matrix2 = [[],[]]

cant_cartas=int(input("cantidad de cartas individuales? luego yo agregare su par y las revolvere"))


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

print(lista,matrix2,matrix)
main()