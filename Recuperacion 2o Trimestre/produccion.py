from almacen import *

"""
    Crear una clase producto.
"""

class Productos():
    __registro_articulos = {}

    def __init__(self, nombre, articulos):
        self.set_nombre(nombre)
        self.set_cantidad(0)
        self.set_articulos(articulos)
        self.alta()

    def alta(self):
        if self.get_nombre() in Productos.__registro_articulos:
            raise ValueError("Este producto ya ha sido dado de alta.")
        Productos.__registro_articulos[f"{self.get_nombre()}"] = self

    @staticmethod
    def montar(articulo, cantidad):
        if articulo not in Productos.__registro_articulos:
            raise ValueError(f"Produccto: {articulo} no dado de alta.")
        art = Productos.__registro_articulos[articulo]
        while cantidad > 0:
            for artic, cant in art.get_articulos().items():
                Gestion_articulos.retirar_cantidad_articulo(artic, cant)
            art.set_cantidad(articulo.get_cantidad() + 1)
            cantidad -= 1

    """@staticmethod
    def baja(articulo):
        if articulo not in list(Productos.__registro_articulos.keys()):
            raise ValueError(f"Produccto: {articulo} no dado de alta.")
        Productos.__registro_articulos.pop(f"{articulo}")
    """
    
    @staticmethod
    def imprimir_productos():
        contador = 1
        for articulo in Productos.__registro_articulos.values():
            print("*"*50)
            print(f"Producto número: {contador}")
            print(articulo)
            contador += 1
        print("*"*50)

    @staticmethod
    def retirar_producto(articulo, cantidad):
        if articulo in Productos.__registro_articulos:
            if Productos.__registro_articulos[articulo].get_cantidad() >= cantidad:
                producto = Productos.__registro_articulos[articulo]
                producto.set_cantidad(producto.get_cantidad() - cantidad)
                return
            raise ValueError("No hay stock suficiente.")
        raise ValueError("Producto no dado de alta.")

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_articulos(self, articulos):
        self.__articulos = articulos

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def __str__(self):
        return f'\n-> Produccto: {self.get_nombre()}\n-> Cantidad en stock: {self.get_cantidad()}\n' + \
                'Cada unidad está constituida por:\n' + \
                "".join([f"  * {articulo} -> {cantidad} [uds]\n" for articulo, cantidad in self.__get_articulos().items()])

    def __repr__(self):
        return f"Productos({self.get_nombre()!r}, {self.__get_articulos()})"

    def get_nombre(self):
        return self.__nombre

    def __get_articulos(self):
        return self.__articulos

    def get_cantidad(self):
        return self.__cantidad
