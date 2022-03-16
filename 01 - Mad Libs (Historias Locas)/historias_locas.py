# organización = "freeCodeCamp"

# print("Aprende a programar con " + organización)
# print("Aprende a programar con {}".format(organización))
# print(f"Aprende a programar con {organización}")  # f-string


# Mad Libs (Historias Locas)
import os

os.system('cls')

print("\nMad Libs (Historias Locas)\n")

adj = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
sustantivo_plural = input("Sustantivo (plural): ")

madlib = f"\n!Programar es tan {adj}! Siempre me emociona porque me encanta {verbo1} problemas. !Aprende a {verbo2} con freeCodeCamp y alcanza tus {sustantivo_plural}!"

print(madlib)

input("\n\x1B[3mPresione Enter para finalizar.\x1B[0m")


# Crear .exe:
# Ejecutar:   $ pip install pyinstaller
# Luego:      $ pyinstaller --clean --onefile historias_locas.py
