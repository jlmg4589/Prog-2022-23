

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

def numeros_perfectos1(numeros):
    return auxiliar_perfector1(numeros, set(), 1, 0)

def auxiliar_perfector1(numeros, conjunto, contador, suma):
    if len(numeros) == 0:
        return conjunto
    if numeros[0] > contador:
        suma += contador if numeros[0]%contador == 0 else 0
        contador += 1
        return auxiliar_perfector1(numeros, conjunto, contador, suma)
    if numeros[0] == suma:
        conjunto.add(numeros[0])
    return auxiliar_perfector1(numeros[1:], conjunto, 1, 0)



def numeros_perfectos(numeros):
    conjunto = set()
    auxiliar_perfector(numeros, conjunto)
    print(conjunto.update())
    return conjunto

def auxiliar_perfector(numeros, conjunto):
    
    for numero in numeros:
        perfecto = 0
        for indice in range(1, numero):
            if numero%indice == 0:
                perfecto += indice
        if perfecto == numero:
            conjunto.add(numero)



""" fdf """
def numeros_perfectos3(numeros):
    """ dfsf """
    conjunto = set()
    return numeros_perfectos_auxiliar(numeros, 0, conjunto)
def numeros_perfectos_auxiliar(numeros, indice, conjunto):
    """ fdf """
    if indice < len(numeros):
        if es_perfecto(numeros[indice], 1, 0) is True:
            conjunto.add(numeros[indice])
        return numeros_perfectos_auxiliar(numeros, indice+1, conjunto)
    return conjunto
def es_perfecto(numero, contador, sumatoria):
    """ f """
    print(sumatoria, numero)
    if numero <= contador:
        return False
    if numero % contador == 0:
        sumatoria += contador
    if sumatoria == numero:
        print(sumatoria, numero)
        return True
    return es_perfecto(numero, contador+1, sumatoria)