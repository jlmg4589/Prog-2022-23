class Articulo:

    def __init__(self, nombre, cantidad):
        self.set_nombre(nombre)
        self.set_cantidad(cantidad)

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def __repr__(self):
        return f'Articulo({self.get_nombre()!r}, {self.get_cantidad()})'

    def __str__(self):
        return f'{self.get_nombre()}: {self.get_cantidad()} [uds]'
    
class Gestion_articulo:

    __lista_articulos = []

    @staticmethod
    def alta_articulo(nombre):
        for articulo in Gestion_articulo.__lista_articulos:
            if articulo.get_nombre() == nombre:
                raise ValueError("Artículo ya dado de alta.")
        Gestion_articulo.__lista_articulos.append(Articulo(nombre, 0))

    @staticmethod
    def agregar_cantidad_articulo(nombre, cantidad):
        for articulo in Gestion_articulo.__lista_articulos:
            if articulo.get_nombre() == nombre:
                cant = articulo.get_cantidad()
                articulo.set_cantidad(cant + cantidad)
                return
        raise ValueError("Artículo no dado de alta.")

    @staticmethod
    def retirar_cantidad_articulo(nombre, cantidad):
        for articulo in Gestion_articulo.__lista_articulos:
            if articulo.get_nombre() == nombre:
                if articulo.get_cantidad() >= cantidad:
                    cant = articulo.get_cantidad()
                    articulo.set_cantidad(cant - cantidad)
                    return
                raise ValueError("No hay suficiente stock de este artículo.")
        raise ValueError("Artículo no dado de alta.")

    @staticmethod
    def imprimir_articulos():
        contador = 0
        print("-"*50)
        for articulo in Gestion_articulo.__lista_articulos:
            print(articulo)
            contador += 1
        print()
        print("Cantidad total de artículo es:", contador)
        print("-"*50)

class Albaran:

    __albaranes = []
    __num_entrada = 0

    def __init__(self, id_albaran, articulo, cantidad):
        Gestion_articulo.agregar_cantidad_articulo(articulo, cantidad)
        self.set_num_entrada()
        self.set_id_albaran(id_albaran)
        self.set_articulo(articulo)
        self.set_cantidad(cantidad)
        Albaran.__albaranes.append(self)

    def set_num_entrada(self):
        Albaran.__num_entrada += 1
        self.__num_entrada = Albaran.__num_entrada

    def set_id_albaran(self, id_albaran):
        self.__id_albaran = id_albaran

    def set_articulo(self, articulo):
        self.__articulo = articulo

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def get_num_entrada(self):
        return self.__num_entrada

    def get_id_albaran(self):
        return self.__id_albaran

    def get_articulo(self):
        return self.__articulo

    def get_cantidad(self):
        return self.__cantidad

    def __str__(self):
        return f'{self.get_num_entrada()} -> Id de Albarán: {self.get_id_albaran()}, {self.get_cantidad()} [uds]'

    def __repr__(self):
        return f'Albaran({self.get_id_albaran()!r},{self.get_articulo()!r},{self.get_cantidad()})'

    @staticmethod
    def listar_albaranes():
        print("-"*50)
        for albaran in Albaran.__albaranes:
            print(albaran)
        print()
        print("-"*50)
