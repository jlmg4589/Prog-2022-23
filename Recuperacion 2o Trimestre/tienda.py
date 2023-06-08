from typing import Any
from produccion import *

class Venta:

    __lista = {}

    def __init__(self, producto, cantidad, cliente):
        self.set_producto(producto)
        Productos.retirar_producto(producto, cantidad)
        self.set_cantidad(cantidad)
        self.set_cliente(cliente)
        self.set_id()

    def set_cliente(self, cliente):
        self.__cliente = cliente

    def set_producto(self, producto):
        self.__producto = producto

    def set_id(self):
        tamano = len(Venta.__lista)
        self.__id = tamano + 1
        Venta.__lista[self.get_id()] = self

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def get_id(self):
        return self.__id

    def get_producto(self):
        return self.__producto
    
    def get_cantidad(self):
        return self.__cantidad
    
    def get_cliente(self):
        return self.__cliente

    def __str__(self):
        return  f"-> ID de venta: {self.get_id()}; Nombre del producto: {self.get_producto()}; " + \
                f"Cantidad: {self.get_cantidad()} [uds]" + \
                f"\n\nDatos del cliente: {self.get_cliente()}" 

    @staticmethod
    def imprimir_ventas():
        print("-"*100)
        for venta in Venta.__lista.values():
            print(venta)
            print("-"*100)

class Cliente():
    """
        Clase cliente, crea los distintos clientes.
    """
    def __init__(self, nombre, nif, direccion, telefono):
        self.set_nombre(nombre)
        self.set_nif(nif)
        self.set_direccion(direccion)
        self.set_telefono(telefono)

    def __repr__(self):
        return f'Cliente({self.get_nombre()!r},{self.get_nif()!r}, '\
            f'{self.get_direccion()!r}, {self.get_articulos()})'

    def __str__(self):
        return f'\n- Denominación: {self.get_nombre()}\n- NIF: {self.get_nif()}\n'\
            f'- Dirección: {self.get_direccion()}\n- Contacto: {self.get_articulos()}'

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_nif(self, nif):
        self.__nif = nif

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def get_nombre(self):
        return self.__nombre

    def get_nif(self):
        return self.__nif

    def get_direccion(self):
        return self.__direccion

    def get_articulos(self):
        return self.__telefono

