"""
Juego de adivinar el número con el usuario
"""

import random

def main():
    """
    Damos como entrada los límites superior e inferior de un intervalo numérico.
    El usuario deberá adivinar el número aleatorio seleccionado de ese intervalo.
    """
    lim_in = int(input("Ingrese el valor más pequeño del intervalo: "))
    lim_sup = int(input("Ingresa el valor más grande del intervalo: " ))
    num_secreto = random.randint(lim_in, lim_sup)
    intentos = 0
    while True:
        intentos += 1
        num_usuario = int(input("Trata de adivinar el número secreto ingresando un valor numérico "))
        if num_usuario < num_secreto:
            print('Intenta con un número más grande')
        elif num_usuario > num_secreto:
            print('Intenta con un número más pequeño')
        else:
            print(f'¡Ganaste, adivinaste el número secreto en {intentos} intentos')
            break
if __name__ == "__main__":
    main()

:wq

