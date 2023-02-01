import sys

def fib(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)  # Itera tantas veces haga falta hasta devolver un valor por return y va almacenando los datos necesarios en memoria.

def fib_iter(numero):
    return _fib_aux(numero)


def _fib_aux(numero):
    
    fn = fn_1 = buffer = 0

    while (numero > 0):
        if (fn == 0):
            fn = 1
        else:
            buffer = fn         # Almaceno el valor actual de f(n)
            fn = fn_1 + fn      # Actualizo el valor de f(n)
            fn_1 = buffer       # Actualizo el valor de f(n-1) utilizando el buffer.
        
        numero -= 1
    
    return fn

if (__name__ == "__main__"):

    if(len(sys.argv) == 1):
        print("fib(8) vale: ", fib(8), "(correcto)")
        print("fib_iter(8) vale: ", fib_iter(9), "(incorrecto)")
    else:
        print("El resultado para f(",sys.argv[1],") es: ", fib(int(sys.argv[1])))