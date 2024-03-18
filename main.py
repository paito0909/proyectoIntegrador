#Pedir el nombre del jugador por teclado.

nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre} te damos la bienvenida al laberinto")

#Escribir un programa que corra un bucle infinito leyendo e imprimiento las teclas y sólo terminará cuando se presione la tecla ↑ indicada como UP
import readchar
import readchar.key

print("Presiona las teclas de dirección (flecha arriba, abajo, izquierda, derecha). Presiona la flecha hacia arriba para salir.")
while True:
    key = readchar.readkey()
    
    if key == readchar.key.UP:
        print("Saliendo del programa.")
        break
    elif key == readchar.key.RIGHT:
        print("→")
    elif key == readchar.key.LEFT:
        print("←")
    elif key == readchar.key.DOWN:
        print("↓")
    else:
        print("Movimiento inválido")
        
        
#Para esta sección del proyecto integrador necesitaremos aprender a manipular la terminal:

#Iniciar con un número en 0, leer la tecla `n` del teclado en un bucle, por cada presionada, borrar la terminal y e imprimir el nuevo número hasta el número 50.

#La operación de borrar la terminal e imprimir el nuevo número debe estar en su propia función.

#Para borrar la terminal antes de imprimir nuevo contenido usar la instrucción: os.system('cls' if os.name=='nt' else 'clear'), para esto se debe importar la librería os

import os

def clear_terminal():
    """Función para limpiar la terminal"""
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    """Función principal"""
    input("Presiona 'n' y Enter para comenzar...")
    numero = 0
    while numero <= 50:
        input("Presiona 'n' y Enter para continuar...")
        clear_terminal()
        print(numero)
        numero += 1

if __name__ == "__main__":
    main()
    
    