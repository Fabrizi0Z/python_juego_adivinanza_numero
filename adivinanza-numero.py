"""La idea del proyecto es generar un numero del 1 al 100
y que mediante un input, el usuario intente adivinar el numero"""

import random


def juego_adivinanza():
    numero_secreto = random.randint(1, 100)  # La idea es que sean solo numeros enteros
    intentos = 0
    adivinado = False


    print("¡Bienvenido al juego!")
    print("El objetivo es adivinar el número secreto entre 1 y 100")
    print("Buena suerte!")

    while not adivinado:
        # Aca solicito un numero
        numero_usuario = input("Introduza un numero del 1 al 100: ")
        # Verificamos que la entrada sea un numero
        if numero_usuario.isdigit():
            numero_usuario = int(numero_usuario)  # Aca convertimos de str a int
            intentos += 1  # Aca acumulamos el numero de intentos
            if numero_usuario < numero_secreto:
                print(f"El numero secreto es mayor a {numero_usuario}")
            elif numero_usuario > numero_secreto:
                print(f"El numero secreto es menor a {numero_usuario}")
            else:
                print(
                    f"Has ganado! Felicitaciones! El numero {numero_usuario} es el numero secreto y lo has  adivinado en {intentos} intentos."
                )
        else:
            print("Por favor, ingrese un numero válido.")

juego_adivinanza()
