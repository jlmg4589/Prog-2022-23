"""

Escribir en Python una fucnión llamada "vuelta(precio,entrega)" que determine la cantidad a devolver, indicando en cada elemento de la lista una cadena que indique 
el número de monedas y su cantidad para cada una de las monedas a devolver. Este cálculo se ha de realizar teniendo en cuenta que la cantidad de dinero (número de
billetes y monedas) debe ser mçinimo.
Observación: Considerar las siguientes cantidades de dinero 500, 200, 50, 20, 10, 5, 2. 1 €

Por ejemplo:
>>>> cuelta(12, 60)
['2->20', '1->5', '1->2', '1->1']

"""


""" sf """
def vuelta(precio, cash) -> list:
    """ dsdf """
    monedas = [500, 200, 50, 20, 10, 5, 2, 1]
    cambio = []
    suma = 0
    for moneda in monedas:
        if moneda <= (cash - suma - precio):
            cantidad = (cash - suma - precio)//moneda
            cambio.append(f'{cantidad}->{moneda}')
            suma += cantidad * moneda
        if suma == cash - precio:
            print(cambio)
            break
