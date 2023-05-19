class Albaran:

    __numero_registro = 0
    __lista_albaranes = []

    def __init__(self, id_albaran, descripcion_articulo, cantidad):
        Gestion_articulos.agregar_cantidad_articulo(descripcion_articulo, cantidad)
        self.__set_num_registro()
        self.__set_id_albaran(id_albaran)
        self.__set_articulo(descripcion_articulo)
        self.__set_cantidad(cantidad)
        Albaran.__lista_albaranes.append(self)

    def __repr__(self):
        return f'Albaran({self.get_id_albaran()!r}, {self.get_articulo()!r}, {self.get_cantidad()})'

    def __str__(self):
        return f'{self.get_num_registro()} -> Id de Albarán: {self.get_id_albaran()}; Artículo: {self.get_articulo()}, {self.get_cantidad()} [uds]'

    def __set_num_registro(self):
        Albaran.__numero_registro += 1
        self.__numero_registro = Albaran.__numero_registro

    def __set_id_albaran(self, id_albaran):
        self.__id_albaran = id_albaran

    def __set_articulo(self, articulo):
        self.__articulo = articulo

    def __set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def get_num_registro(self):
        return self.__numero_registro

    def get_id_albaran(self):
        return self.__id_albaran

    def get_articulo(self):
        return self.__articulo

    def get_cantidad(self):
        return self.__cantidad

    @staticmethod
    def listar_albaranes():
        print("-"*100)
        for i in Albaran.__lista_albaranes:
            print(i)
        print()
        print(f'Se han realizado {repr(str(len(Albaran.__lista_albaranes)))} entradas')
        print("-"*100)

class Gestion_articulos:
    """
        Da de alta nuevos articulos para usarlos en el almacén.
    """
    __lista_articulos = []
    __nombres_articulos = []

    @staticmethod
    def alta_articulo(nuevo_articulo):
        """
            Agrega un nuevo artículo con una cantidad a 0, en el caso de no existir previamente.
        """
        if not Gestion_articulos.consultar_existencia_articulo(nuevo_articulo):
            Gestion_articulos.__lista_articulos.append(Articulo(nuevo_articulo, 0))
            Gestion_articulos.__nombres_articulos.append(nuevo_articulo)
            return
        raise ValueError("Artículo ya dado de alta.")

    @staticmethod
    def consultar_existencia_articulo(articulo):
        """
            Comprueba si un artículo existe, devuelve True = Existe; False = No existe
        """
        if articulo in Gestion_articulos.__nombres_articulos:
            return True
        return False

    @staticmethod
    def consultar_cantidad_articulo(articulo):
        if Gestion_articulos.consultar_existencia_articulo(articulo):
            indice = Gestion_articulos.__nombres_articulos.index(articulo)
            return Gestion_articulos.__lista_articulos[indice].get_cantidad()
        raise ValueError("Artículo no dado de alta.")

    @staticmethod
    def retirar_cantidad_articulo(articulo, cantidad):
        if Gestion_articulos.consultar_existencia_articulo(articulo):
            cantidad_articulo = Gestion_articulos.consultar_cantidad_articulo(articulo)
            indice = Gestion_articulos.__nombres_articulos.index(articulo)
            if cantidad <= cantidad_articulo:
                cantidad_articulo -= cantidad
                Gestion_articulos.__lista_articulos[indice].set_cantidad(cantidad_articulo)
                return
            raise ValueError(f'No hay stock suficiente del artículo {articulo}')
        raise ValueError(f"Artículo: {articulo} no dado de alta.")

    @staticmethod
    def agregar_cantidad_articulo(articulo, cantidad):
        if Gestion_articulos.consultar_existencia_articulo(articulo):
            indice = Gestion_articulos.__nombres_articulos.index(articulo)
            cantidad_articulo = Gestion_articulos.__lista_articulos[indice].get_cantidad()
            Gestion_articulos.__lista_articulos[indice].set_cantidad(cantidad + cantidad_articulo)
            return
        raise ValueError("Artículo no dado de alta.")

    @staticmethod
    def imprimir_articulos():
        print("-"*100)
        for x in Gestion_articulos.__nombres_articulos:
            indice = Gestion_articulos.__nombres_articulos.index(x)
            print(Gestion_articulos.__lista_articulos[indice])
        print("")
        print("Total de artículos dados de alta: ", len(Gestion_articulos.__lista_articulos), "[uds]")
        print("-"*100)

class Articulo:
    def __init__(self, nombre, cantidad):
        self.set_nombre(nombre)
        self.set_cantidad(cantidad)

    def __repr__(self):
        return f'Articulo({self.get_nombre()!r},{self.get_cantidad()!r})'

    def __str__(self):
        return f'{self.get_nombre()}: {self.get_cantidad()} [uds]'

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad


Gestion_articulos.alta_articulo("Tornillos")
Gestion_articulos.alta_articulo("Tablero")
Gestion_articulos.alta_articulo("Pata")
Gestion_articulos.alta_articulo("Mango")
Gestion_articulos.alta_articulo("Cabeza")
Gestion_articulos.alta_articulo("Cristal")
Gestion_articulos.alta_articulo("Marco")
Albaran("ALB: 7463", "Tablero", 20)
Albaran("ALB: 7463", "Pata", 80)
Albaran("ALB: 7463", "Tornillos", 1600)
Albaran("ALB: 7464", "Mango", 15)
Albaran("ALB: 7464", "Cabeza", 18)
Albaran("ALB: 7465", "Cristal", 25)
Albaran("ALB: 7465", "Marco", 24)
Gestion_articulos.imprimir_articulos()
