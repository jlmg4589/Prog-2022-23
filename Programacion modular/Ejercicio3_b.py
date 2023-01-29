import random

# Ejercicio que pide al usuario 5 cadenas y que luego las imprima en un orden aleatorio.

x = list()

for i in range(5):
    x.append(input("Introduce el elemento de la lista: "))

random.shuffle(x)

print(x)