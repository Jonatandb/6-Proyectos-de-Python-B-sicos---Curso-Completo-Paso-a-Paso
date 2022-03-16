import os
import random  # https://docs.python.org/es/3.11/library/random.html?highlight=random#module-random

os.system('cls')


def jugar():
    usuario = input(
        "Escoge una opción: 'pi' para piedra, 'pa' para papel, 'ti' para tijera.\n").lower()
    computadora = random.choice(['pi', 'pa', 'ti'])

    print(f"La computadora eligió {computadora}")

    if usuario == computadora:
        return '!Empate!'

    if ganó_el_jugador(usuario, computadora):
        return '!Ganaste!'

    return '!Perdiste!'


def ganó_el_jugador(jugador, oponente):
    # Retornar True (verdadero) si gana el jugador.
    # Piedra gana a Tijera (pi > ti).
    # Tijera gana a Papel (ti > pa).
    # Papel gana a Piedra (pa > pi).
    if ((jugador == 'pi' and oponente == 'ti')
                or (jugador == 'ti' and oponente == 'pa')
                or (jugador == 'pa' and oponente == 'pi')
            ):
        return True
    else:
        return False


print(jugar())

input("\n\x1B[3mPresione Enter para finalizar.\x1B[0m")
