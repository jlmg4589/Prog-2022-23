"""

1) Los médicos forenses utilizan la longitud de ciertos huesos para determinar la altura de
una persona, cuando la persona estaba viva.
* Para varones:
    - Altura (en cm)= 69.089 + 2.238 * longitud_de_la_tibia
* Para mujeres:
    - Altura (en cm)= 61.412 + 2.317 * longitud_de_la_tibia

Escribir en Python una función llamada "altura_genero()" que, teniendo en cuenta lo
comentado anteriormente, calcule adquiriendo los datos de un archivo (llamado: registro.txt), para ello,
el formato del archivo ha de ser como sigue:

Genero L_Tibia[cm]
------ -----------
  H             30
  M             26
  M             31
  H             50

Al invocar a la función altura_genero()", se debe obtener como resultado otro archivo de salida llamado
"alturas.txt". Además, las alturas se han de truncar para que no tengan parte decimal. Debiéndose obtener:


Genero L_Tibia[cm] Altura[cm]
------ ----------- ----------
  H             30        136
  M             27        123
  M             31        133
  H             50        180

Indicación: se pueden usar campos de sustitución en una f-string con el formato {numero:anchof} para alinear un número
entero a la derecha.

Por ejemplo:
>>> f'{25:9}'
'       25'

"""

""" df """
def altura_genero1():
    """ dsf """
    lineas = [x.rstrip() for x in open('registro.txt', 'r').readlines()]
    resultado = open('alturas.txt', 'w')
    resultado.write(f'{lineas[0]} Altura[cm]\n')
    resultado.write(f'{lineas[1]} ----------\n')
    indice = 2
    for indice in list(range(2,len(lineas))):
        tibia = int(lineas[indice][-2:])
        if lineas[indice][2:3] == 'H':
            altura = int(69.089 + (2.238 * tibia))
        else:
            altura = int(61.412 + (2.317 * tibia))
        resultado.write(f'{lineas[indice]} {altura:10}\n')
