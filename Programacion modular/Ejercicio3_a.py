import random

numero = int(input("Introduce un número entre el 1 y el 100:"))

if (numero == random.randint(1,100)):
    print("Has acertado el número, Enhorabuena!!!")
else:
    print("Lo siento, no ha tenido suerte...")
