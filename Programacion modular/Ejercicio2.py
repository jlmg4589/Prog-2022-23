import sys

pi=1

if(int(sys.argv[1]) == 1):
    import math
    print("Valor de Pi, utilizando el módulo desde otro marco: ",math.pi)
elif(int(sys.argv[1]) == 2):
    from math import pi
    print("Valor de Pi, importando Pi como nueva variable dentro del marco principal: ",pi)
else:
    from math import *
    print("Valor de Pi, importando todo el módulo dentro del módulo Ejercicio2.py: ",pi)

print("El valor de pi en el módulo Ejercicio2 es: ", pi)
