'''
Escribir en Python una función recursiva llamada unicos(secuencia) que reciba una secuencia\
de números enteros en la que todos aparecen dos o más veces, excepto dos de ellos que aparecen exactamente una vez.\
La función deberá devolver un conjunto de tipo set que contenga sólo esos dos elementos únicos.

Importante:

La función debe ser pura.
La llamada a la función debe provocar la ejecución de una función recursiva que genere un proceso iterativo.
No se puede usar ningún bucle while, for, definiciones por comprensión ni expresiones generadoras.

Por ejemplo:

unicos([1, 9, 8, 8, 7, 6, 1, 6]) == {7, 9}
'''


def aux_unicos(secuencia, indice ,salida):
    if len(secuencia) == indice:
        return salida
    if secuencia.count(secuencia[indice]) == 1:
        salida.add(secuencia[indice])
    indice += 1
    return aux_unicos(secuencia, indice, salida)

def unicos(secuencia):
    return aux_unicos(secuencia, 0, set())


def unicos1(secuencia):


    def auxiliar(sec, acc):
        print(sec, "->", acc)
        if len(sec) == 0 :
            return acc
        n = sec[0]
        if secuencia.count(n) == 1:
            acc.add(n)
        return auxiliar(sec[1:], acc)


    return auxiliar(secuencia, set())
