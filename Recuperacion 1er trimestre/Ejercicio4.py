

"""

Escribir en Python una función recursiva llamada numeros_perfectos(numeros) que devuelva un conjunto
con todos los números perfectos ordenados.

Un número perfecto es aquel que es igual a la suma de sus divisores, sin tener en cuenta el
1.

    6 es perfecto, pues 6 = 1 + 2 + 3

* Recordar que un número es divisor, para aquellos que al utilizarlos para dividir a otro, 
su resultado es exacto, o dicho de otro modo, el resto es 0.

Por ejemplo: Resto de 6/3 = 0, Resto de 6/2 = 0, Resto de 6/1 = 0, sin embargo, el resto de
6/4 =  2.
Por tanto, sólo son divisores de 6 en este ejemplo, el 3, 2 y el 1.

Ejemplo de uso:
numeros_perfectos([1,3,5,6,10,28]) -> {6,28}


Importante:

La función debe ser pura.
La llamada a la función debe provocar la ejecución de una función recursiva que genere un proceso iterativo.
No se puede usar ningún bucle while, for, definiciones por comprensión ni expresiones generadoras.

"""

def numeros_perfectos(numeros):
    """Docstring"""
    return aux_perfectos(numeros, set(), 1, 0)

def aux_perfectos(numeros, conjunto, contador, suma):
    """Docstring"""
    if len(numeros) == 0:
        return conjunto
    elif numeros[0] > contador:
        suma += contador if numeros[0] % contador == 0 else 0
        contador += 1
        return aux_perfectos(numeros, conjunto, contador, suma)
    elif numeros[0] == suma:
        conjunto.add(numeros[0])
    return aux_perfectos(numeros[1:], conjunto, 1, 0)