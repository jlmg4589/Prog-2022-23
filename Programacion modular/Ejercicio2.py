import sys

pi=1

if(int(sys.argv[1]) == 1):
    import math
elif(int(sys.argv[1]) == 2):
    from math import pi
elif(int(sys.argv[1]) == 3):
    from math import *

if __name__ == "__main__":
    print("El valor de pi en el módulo Ejercicio2 es: ", pi)
