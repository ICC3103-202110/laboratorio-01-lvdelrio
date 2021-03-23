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
    print(len(matrix2))
    imprimir()
    print('Jugador 1')
    
    x = int(input('Ingresa un valor en la horizontal: '))
    if x >= len(matrix[0]):
        print('ERROR')
        memorama()

    y = int(input('Ingresa un valor en la vertical: '))
    if y >= len(matrix):
        print('ERROR')
        memorama()
    print(x,y,matrix[y][x],matrix2[y][x])
    matrix[y][x] = matrix2[y][x]

    imprimir()
#---------------------------------------------------------------------------|
    while True:
        
        x2 = int(input('Ingresa un valor en la horizontal: '))
        y2 = int(input('Ingresa un valor en la vertical: '))
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
    
    condiciones(x,y,x2,y2)

def memorama2():
    imprimir()
    print('Jugador 2')

    x = int(input('Ingresa un valor en la horizontal: '))
    if x >= len(matrix[0]):
        print('ERROR')
        memorama2()

    y = int(input('Ingresa un valor en la vertical: '))
    if y >= len(matrix):
        print('ERROR')
        memorama2()

    matrix[y][x] = matrix2[y][x]

    imprimir()
#--------------------------------------------------------------------------|
    while True:
        
        x2 = int(input('Ingresa un valor en la horizontal: '))
        y2 = int(input('Ingresa un valor en la vertical: '))
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
    
    condiciones2(x,y,x2,y2)

def condiciones(x,y,x2,y2):
    global p1
    if matrix[y][x] != matrix[y2][x2]:
        matrix[y2][x2] = "-"
        matrix[y][x] = "-"
        respuesta = str(input('¿Quiere seguir jugando? s/n: '))
        if respuesta == 's':
            memorama2()
        elif respuesta == 'n':
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
        p1 += 1 
        print("player 1 ganaste un punto ahora tienes ",p1)
        
        memorama()

def condiciones2(x,y,x2,y2):
    global p2
    if matrix[y][x] != matrix[y2][x2]:
        matrix[y2][x2] = "-"
        matrix[y][x] = "-"
        respuesta = str(input('¿Quiere seguir jugando? s/n: '))
        if respuesta == 's':
            memorama()

        elif respuesta == 'n':
            print(p1)
            print(p2)
            if p1 > p2:
                print('El jugador tiene',p1,'pares')
            elif p2 > p1:
                print('El jugador tiene',p2,'pares')
            elif p2 == p1:
                print('Fue un empate!')
            elif p1 == p2:
                print('Fue un empate!')
            sys.exit(0)
    else:
        p2 += 1 
        print("player 2 ganaste un punto ahora tienes ",p2)
        
        memorama2()

def imprimir():
    contador = 0
    for i in range(len(matrix)):
        print(contador, '', end = '')
        contador += 1
        for j in range(len(matrix[0])):
            print((matrix[i][j]),'', end = '')

        print('\n')

def main():
    while variable == 5:
        random.shuffle(matrix2)
        for i in matrix2:
            random.shuffle(i)
        print(matrix,"\n",matrix2)
        memorama()
        
#----------------------------------------variables globales----------------------------------|       
x=0        
y=0
x2=0
y2=0
p1 = 0
p2 = 0
matrix = []
matrix2 = []
variable = 5
filas=int(input("filas"))
columnas=int(input("columnas"))

for i in range (filas):
    matrix2.append([])
    for j in range(1,columnas+1):
        matrix2[i].append(j)

for i in range(filas):
    matrix.append([])
    for j in range(columnas):
        matrix[i].append("-")
main()