import os
import random  # https://docs.python.org/es/3.11/library/random.html?highlight=random#module-random

os.system('cls')

print("\nLa computadora adivina el número\n")


def adivina_el_número_computadora(x):
    print("==========================")
    print(" !Bienvenido(a) al Juego! ")
    print("==========================")
    print(
        f"\nPiensa un número entre 1 y {x} para que la computadora intente adivinar...")

    límite_inferior = 1
    límite_superior = x

    respuesta = ""
    while respuesta != "c":
        # Generar predicción
        if límite_inferior != límite_superior:  # [1, 10]
            predicción = random.randint(límite_inferior, límite_superior)
        else:
            # también podría ser el límite superior.
            predicción = límite_inferior

        # Obtener respuesta del usuario
        respuesta = input(
            f"\nMi predicción es {predicción}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta, ingresa (C): ").lower()

        if respuesta == "a":
            límite_superior = predicción - 1
        elif respuesta == "b":
            límite_inferior = predicción + 1

    print(
        f"\n!Siii! La computadora adivinó tu número correctamente: {predicción}")


adivina_el_número_computadora(10)

input("\n\x1B[3mPresione Enter para finalizar.\x1B[0m")
