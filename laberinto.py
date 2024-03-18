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
import random

class Juego:
    def __init__(self, mapa, posicion_inicial, posicion_final):
        self.mapa = mapa
        self.posicion_inicial = posicion_inicial
        self.posicion_final = posicion_final
        self.px, self.py = posicion_inicial

    def clear_terminal(self):
        #Función para limpiar la terminal
        os.system('cls' if os.name=='nt' else 'clear')

    def mostrar_mapa(self):
        #Función para mostrar el mapa en la terminal
        for fila in self.mapa:
            print("".join(fila))

    def mover_arriba(self):
        #Función para mover hacia arriba
        if self.py > 0 and self.mapa[self.py - 1][self.px] != '#':
            self.mapa[self.py][self.px] = '.'  # Restaurar espacio vacío
            self.py -= 1
            self.mapa[self.py][self.px] = 'P'  # Actualizar posición del jugador
            self.mostrar_mapa()

    def mover_abajo(self):
        #Función para mover hacia abajo
        if self.py < len(self.mapa) - 1 and self.mapa[self.py + 1][self.px] != '#':
            self.mapa[self.py][self.px] = '.'  # Restaurar espacio vacío
            self.py += 1
            self.mapa[self.py][self.px] = 'P'  # Actualizar posición del jugador
            self.mostrar_mapa()

    def mover_izquierda(self):
        #Función para mover hacia la izquierda
        if self.px > 0 and self.mapa[self.py][self.px - 1] != '#':
            self.mapa[self.py][self.px] = '.'  # Restaurar espacio vacío
            self.px -= 1
            self.mapa[self.py][self.px] = 'P'  # Actualizar posición del jugador
            self.mostrar_mapa()

    def mover_derecha(self):
        #Función para mover hacia la derecha
        if self.px < len(self.mapa[0]) - 1 and self.mapa[self.py][self.px + 1] != '#':
            self.mapa[self.py][self.px] = '.'  # Restaurar espacio vacío
            self.px += 1
            self.mapa[self.py][self.px] = 'P'  # Actualizar posición del jugador
            self.mostrar_mapa()

    def main_loop(self):
        #Función para el bucle principal del juego
        while (self.px, self.py) != self.posicion_final:
            self.mapa[self.py][self.px] = 'P'  # Marcamos la posición del jugador en el mapa
            self.mostrar_mapa()

            # Leer entrada del usuario y mover al jugador 
        print("¡Felicidades! Has llegado al final del laberinto.")

class JuegoArchivo(Juego):
    def __init__(self, directorio_mapas):
        mapa, posicion_inicial, posicion_final = self.leer_mapa_aleatorio(directorio_mapas)
        super().__init__(mapa, posicion_inicial, posicion_final)

    def leer_mapa_aleatorio(self, directorio_mapas):
        archivos_mapas = os.listdir(directorio_mapas)
        nombre_archivo = random.choice(archivos_mapas)
        path_completo = os.path.join(directorio_mapas, nombre_archivo)
        with open(path_completo, 'r') as archivo_mapa:
            lineas = archivo_mapa.readlines()
            dimensiones = lineas[0].strip().split(',')
            filas = int(dimensiones[0])
            columnas = int(dimensiones[1])
            mapa = [linea.strip() for linea in lineas[1:filas+1]]
            inicio = tuple(map(int, lineas[filas+1].strip().split(',')))
            fin = tuple(map(int, lineas[filas+2].strip().split(',')))
        return mapa, inicio, fin

if __name__ == "__main__":
    juego = JuegoArchivo("directorio_con_mapas")
    juego.main_loop()
    
    
#Encapsulando el juego en una clase
#Ahora que disponemos de muchas más herramientas, podemos notar que reutilizamos la variable que contiene el mapa muchas veces y es molesto llamar funciones desconectadas enviando el mismo parámetro.

L#a programación orientada a objetos viene a nuestro rescate!

#Implementa la clase Juego, ahora el mapa y las posiciones inicial y final son atributos de esta clase, reescribe todas tus funciones anteriores de forma que sean métodos de la clase y todo esté encapsulado.

#Instanciar el juego y ejecutarlo desde el main

#Almacenando mapas en archivos
#En lugar de almacenar el mapa en el mismo código, podemos guardarlo en archivos con sus posiciones de inicio y fin y las dimensiones del mapa en la primera línea del archivo, de esta manera los componentes de la aplicación estarán separados y podremos mejorar la experiencia del juego.

#Crear una nueva clase JuegoArchivo la cual hereda de Juego,
#Reescribir el constructor para leer un archivo al azar de una carpeta que contenga los mapas cada vez que se instancia el juego.Para listar los archivos de un directorio usar os.listdir(path) , esto devolverá una lista con el nombre los archivos en ese directorio
#Para elegir un elemento aleatorio de una lista usar random.choice(lista).
#Note que para poder leer el archivo tenemos que componer el path, una forma de hacerlo es path_completo = f"{path_a_mapas}/{nombre_archivo}"
#Crear un método que lea los datos de estos archivos de mapa y devuelva una cadena que tenga concatenada todas las filas leídas del mapa y las coordenadas de inicio y fin. Al final de la lectura antes de retornar usar cadena.strip() para eliminar caracteres en blanco residuales.

import os
import random

class Juego:
    def __init__(self, mapa, posicion_inicial, posicion_final):
        self.mapa = mapa
        self.posicion_inicial = posicion_inicial
        self.posicion_final = posicion_final
        self.px, self.py = posicion_inicial

    def mostrar_mapa(self):
        #Función para mostrar el mapa en la terminal
        os.system('cls' if os.name=='nt' else 'clear')
        for fila in self.mapa:
            print("".join(fila))

    def mover_arriba(self):
        #Función para mover hacia arriba
        if self.py > 0 and self.mapa[self.py - 1][self.px] != '#':
            self.mapa[self.py][self.px] = '.'  # Restaurar espacio vacío
            self.py -= 1
            self.mapa[self.py][self.px] = 'P'  # Actualizar posición del jugador
            self.mostrar_mapa()

    # Métodos para mover abajo, izquierda y derecha similares a mover_arriba

    def main_loop(self):
        #Función para el bucle principal del juego
        while (self.px, self.py) != self.posicion_final:
            self.mapa[self.py][self.px] = 'P'  # Marcamos la posición del jugador en el mapa
            self.mostrar_mapa()

    # Leer entrada del usuario y mover al jugador en consecuencia

        print("¡Felicidades! Has llegado al final del laberinto.")

class JuegoArchivo(Juego):
    def __init__(self, directorio_mapas):
        mapa, posicion_inicial, posicion_final = self.leer_mapa_aleatorio(directorio_mapas)
        super().__init__(mapa, posicion_inicial, posicion_final)

    def leer_mapa_aleatorio(self, directorio_mapas):
        archivos_mapas = os.listdir(directorio_mapas)
        nombre_archivo = random.choice(archivos_mapas)
        path_completo = os.path.join(directorio_mapas, nombre_archivo)
        with open(path_completo, 'r') as archivo_mapa:
            lineas = archivo_mapa.readlines()
            dimensiones = lineas[0].strip().split(',')
            filas = int(dimensiones[0])
            columnas = int(dimensiones[1])
            mapa = [linea.strip() for linea in lineas[1:filas+1]]
            inicio = tuple(map(int, lineas[filas+1].strip().split(',')))
            fin = tuple(map(int, lineas[filas+2].strip().split(',')))
        return mapa, inicio, fin

if __name__ == "__main__":
    juego = JuegoArchivo("directorio_con_mapas")
    juego.main_loop()




    
    