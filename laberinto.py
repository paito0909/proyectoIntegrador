#Implementar una función que reciba el mapa de un laberinto en forma de cadena, y lo convierta a matriz de caracteres.
#Utiliza el siguiente mapa:
#laberinto = """..###################
               #....#...............#
                #.#.#####.#########.#
                #.#...........#.#.#.#
                #.#####.#.###.#.#.#.#
                #...#.#.#.#.....#...#
                #.#.#.#######.#.#####
                #.#...#.....#.#...#.#
                #####.#####.#.#.###.#
                #.#.#.#.......#...#.#
                #.#.#.#######.#####.#
                #...#...#...#.#.#...#
                ###.#.#####.#.#.###.#
                #.#...#.......#.....#
                #.#.#.###.#.#.###.#.#
                #...#.#...#.#.....#.#
                ###.#######.###.###.#
                #.#.#.#.#.#...#.#...#
                #.#.#.#.#.#.#.#.#.#.#
                #.....#.....#.#.#.#.#
                ###################.."""
#Los puntos inicial y final deben ser dados al crear el juego, usar las coordenadas (0,0) para el inicio y (len(mapa)-1, len(mapa[0])-1) para el final.
#Recuerdo: Para separar por filas usar split("\n") y para convertir una cadena a una lista de caracteres usar list(cadena).
#Escribir una función que limpie la pantalla y muestre la matriz (recibe el mapa en forma de matriz)
#Implementar el main loop en una función (recibe el mapa en forma de matriz)
#recibir: mapa List[List[str]], posicion inicial Tuple[int, int], posicion final Tuple[int, int].
#definir dos variavles px y py que contienen las coordenadas del jugador, iniciar como los valores de la posición incial procesar mientras (px, py) no coincida con la coordenada final.Asignar el caracter P en el mapa a las coordenadas (px, py) en todo momento. leer del teclado las teclas de flechas, antes de actualizar la posición, verificar si esta posición tentativa:
#No se sale del mapa
#No es una pared
#Si la nueva posición es válida, actualizar (px, py), poner el caracter P en esta nueva coordenada y restaurar la anterior a mostrar

import os
import tkinter as tk

# Define el laberinto
laberinto = '''..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################..'''

def convertir_mapa_a_matriz(laberinto):
    """Función para convertir el mapa de laberinto en una matriz de caracteres"""
    return [list(fila) for fila in laberinto.split("\n")]

def mostrar_mapa():
    """Función para mostrar el mapa en la ventana"""
    canvas.delete("all")
    for y, fila in enumerate(mapa):
        for x, celda in enumerate(fila):
            if celda == '#':
                canvas.create_rectangle(x*20, y*20, (x+1)*20, (y+1)*20, fill="black")
            elif celda == 'P':
                canvas.create_rectangle(x*20, y*20, (x+1)*20, (y+1)*20, fill="red")
    ventana.update()

def mover_arriba(event):
    """Función para mover hacia arriba"""
    global py
    if py > 0 and mapa[py - 1][px] != '#':
        mapa[py][px] = '.'  # Restaurar espacio vacío
        py -= 1
        mapa[py][px] = 'P'  # Actualizar posición del jugador
        mostrar_mapa()

def mover_abajo(event):
    """Función para mover hacia abajo"""
    global py
    if py < len(mapa) - 1 and mapa[py + 1][px] != '#':
        mapa[py][px] = '.'  # Restaurar espacio vacío
        py += 1
        mapa[py][px] = 'P'  # Actualizar posición del jugador
        mostrar_mapa()

def mover_izquierda(event):
    """Función para mover hacia la izquierda"""
    global px
    if px > 0 and mapa[py][px - 1] != '#':
        mapa[py][px] = '.'  # Restaurar espacio vacío
        px -= 1
        mapa[py][px] = 'P'  # Actualizar posición del jugador
        mostrar_mapa()

def mover_derecha(event):
    """Función para mover hacia la derecha"""
    global px
    if px < len(mapa[0]) - 1 and mapa[py][px + 1] != '#':
        mapa[py][px] = '.'  # Restaurar espacio vacío
        px += 1
        mapa[py][px] = 'P'  # Actualizar posición del jugador
        mostrar_mapa()

# Configurar la ventana
ventana = tk.Tk()
ventana.title("Laberinto")

# Configurar el lienzo
canvas = tk.Canvas(ventana, width=20*len(laberinto.split('\n')[0]), height=20*len(laberinto.split('\n')))
canvas.pack()

# Convertir el laberinto a matriz
mapa = convertir_mapa_a_matriz(laberinto)

# Encontrar la posición inicial del jugador
py, px = 0, 0
for y, fila in enumerate(mapa):
    for x, celda in enumerate(fila):
        if celda == 'P':
            py, px = y, x
            break

# Mostrar el laberinto inicialmente
mostrar_mapa()

# Configurar los eventos de teclado
ventana.bind("<Up>", mover_arriba)
ventana.bind("<Down>", mover_abajo)
ventana.bind("<Left>", mover_izquierda)
ventana.bind("<Right>", mover_derecha)

# Iniciar el bucle de la ventana
ventana.mainloop()