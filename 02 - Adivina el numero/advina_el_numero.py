import os
import random  # https://docs.python.org/es/3.11/library/random.html?highlight=random#module-random

os.system('cls')

print("\nAdivina el número\n")


def adivina_el_número(x):
    print("==========================")
    print(" !Bienvenido(a) al Juego! ")
    print("==========================")
    print("\nTu meta es adivinar el número generado por la computadora.")

    número_aleatorio = random.randint(1, x)  # Número aleatorio entre 1 y x.

    predicción = 0

    while predicción != número_aleatorio:
        # El usuario ingresa un número
        predicción = int(input(f"\nAdivina un número entre 1 y {x}: "))

        if predicción < número_aleatorio:
            print("\nIntenta otra vez. Este número es muy pequeño.")
        elif predicción > número_aleatorio:
            print("\nIntenta otra vez. Este número es muy grande.")

    print(
        f"!Felicitaciones! Adivinaste el número {número_aleatorio} correctamente.")


adivina_el_número(10)

input("\n\x1B[3mPresione Enter para finalizar.\x1B[0m")
