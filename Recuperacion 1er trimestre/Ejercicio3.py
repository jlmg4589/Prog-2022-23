"""

En una empresa ha habido un fallo y necesita implementar una función llamada ordenar_palabra(palabra)
que resuelva el siguiente problema.
El problema es que han realizado una encuesta, y al almacenar los datos en su base de datos, los nombres
de cada usuario se han "codificado" sin querer. El programa de codificación realiza un intercambio de letras 
por cada par que haya disponible en una palabra. Por ejemplo:

* Si introducimos: Jose -> oJes
* Si introducimos: Irene -> rInee

Se puede observar que en el caso de que la longitud de la palabra sea impar, el elemento desubicado queda
invariante.

Por tanto, la función debe actuar en sentido inverso a la codificación realizada en el formulario de forma
errónea.

Por ejemplo:
>>>> ordenar_palabra("ePrdo")
Pedro

"""


def ordenar_palabra1(palabra):
    """DocString"""
    return "".join([f"{palabra[indice+1]}{palabra[indice]}" \
            if (indice != (len(palabra)-1)) else f"{palabra[indice]}" \
            for indice in range(0, len(palabra), 2)])

def ordenar_palabra(palabra):
    """DocString"""
    respuesta=""
    for indice in range(0, len(palabra)-1, 2):
        respuesta += f'{palabra[indice+1]}{palabra[indice]}'
    if len(palabra) % 2 == 1:
        respuesta += palabra[-1]
    return respuesta
