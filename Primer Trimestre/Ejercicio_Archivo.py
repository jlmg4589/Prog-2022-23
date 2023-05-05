"""

Escribir en Python una función factura() sin parámetros que lea un archivo de texto llamado «factura.txt» con un texto como el siguiente (no tiene por qué ser exactamente igual, pero sí de la misma forma):

Id Denominación   Precio
-- ---------------------
 2 Tuercas          3.70
 6 Tornillos        2.20

 
En la configuración del archivo se puede observar que en cada líea aparece un artículo, donde se detalla el "Id" de cada uno de ellos y el precio del mismo.
El campo de "Id" puede alcanzar un valor máximo de 99 y el precio unitario 99.99. Además, la denominación tiene un máximo de 15 caracteres.

La función deberá crear un archivo «resultado.txt» que contenga el mismo contenido que el archivo original pero añadiendo el importe de cada artículo sin IVA.

Id Denominación    Precio  SIN-IVA
-- --------------- ------ -------
 2 Tuercas           3.70    3.06
 6 Tornillos         2.20    1.82

La función no debe devolver nada.

Indicación: se pueden usar campos de sustitución en una f-string con los siguientes formatos:

    {cadena:anchof} para alinear una cadena a la izquierda.
    {numero:ancho.decimalesf} para alinear un número a la derecha.

Por ejemplo:

>>> f'{"Hola":15}'
'Hola           '
>>> f'{6 * 2.20:9.2f}'
'    13.20'

"""

def factura():
    """Ejercicio de archivos"""
    fact = [x.rstrip() for x in open('factura.txt').readlines()]
    res = open('resultado.txt',"w")
    res.write("Ud Denominación    Precio SIN-IVA\n")
    res.write("-- --------------- ------ -------\n")
    for x in range(2,len(fact)):
        resultado = round(float(fact[x][-5:]) / 1.21,2)
        res.write(f'{fact[x][:2]} {fact[x][3:18]} {fact[x][-5:]:>6s} {resultado:>7.2f}\n')
    res.close()