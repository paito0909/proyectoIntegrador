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