class Vehiculo:
    """Clase que gestiona la entrada y salida del stock de vehículos."""
    stock_vehiculos = {}

    def __init__(self, matricula, marca):
        self.set_matricula(matricula)
        self.set_marca(marca)
        self.set_id_entrada()
        self.alta()

    def set_id_entrada(self):
        """Método que establece el id de entrada correcto según los números establecidos \
            previamente en el stock"""
        id_entrada = 1
        for vehiculo in Vehiculo.stock_vehiculos.values():
            if id_entrada != vehiculo.get_id_entrada():
                self.id_entrada = id_entrada
                return
            id_entrada += 1
        self.id_entrada = id_entrada

    def alta(self):
        """Este método da de alta un nuevo vehículo siempre que no exista previamente."""
        if self.get_matricula() in Vehiculo.stock_vehiculos:
            raise ValueError("Vehículo dado de alta.")
        Vehiculo.stock_vehiculos[self.get_matricula()] = self

    def set_matricula(self, matricula):
        """Método que asigna/crea un nuevo atributo matrícula."""
        self.matricula = matricula

    def set_marca(self, marca):
        """Método que asigna/crea un nuevo atributo marca."""
        self.marca = marca

    def get_matricula(self):
        """Método que devuelve el valor del atributo matrícula."""
        return self.matricula

    def get_marca(self):
        """Método que devuelve el valor del atributo marca."""
        return self.marca

    def get_id_entrada(self):
        """Método que devuelve el valor del atributo id_entrada."""
        return self.id_entrada

    def __repr__(self):
        """Método que crea la representación normal."""
        return f'Vehiculo({self.get_matricula()!r},{self.get_marca()!r})'

    def __str__(self):
        """Método que crea una representación legible para el usuario cuando se utilice,
        por ejemplo la función 'print(objeto_Vehiculo)'."""
        return f'- Matrícula: {self.get_matricula()}\n' + \
               f'- Marca: {self.get_marca()}\n' + \
               f'- Id de entrada: {self.get_id_entrada()}'

    def __hash__(self):
        return hash(self.get_matricula())

    @staticmethod
    def baja(matricula):
        """Método estático para dar de baja un vehículo del stock."""
        if matricula not in Vehiculo.stock_vehiculos:
            raise ValueError("El vehículo con la matrícula indicada no está dado de alta.")
        Vehiculo.stock_vehiculos.pop(matricula)
        print(f"Vehículo con mátricula {matricula}, dado de baja correctamente.")

    @staticmethod
    def imprimir_stock():
        """Método estático para imprimir todos los vehículos dados de alta."""
        contador = 0
        print("*"*50)
        print("*" + " "*21 + "STOCK" + " "*22 + "*")
        print("*"*50)
        for vehiculo in Vehiculo.stock_vehiculos.values():
            print(vehiculo)
            contador += 1
            print("*"*50)
        print(f"El número total de vehículos en el stock es: {contador}")

class Coche(Vehiculo):
    def __init__(self, matricula, marca, modelo, potencia):
        if matricula in Vehiculo.stock_vehiculos:
            Vehiculo.stock_vehiculos[matricula].baja()
        super().__init__(matricula, marca)
        self.set_modelo(modelo)
        self.set_potencia(potencia)

    def set_modelo(self,modelo):
        self.modelo = modelo

    def set_potencia(self, potencia):
        self.potencia = potencia

    def get_modelo(self):
        return self.modelo

    def get_potencia(self):
        return self.potencia

    def __str__(self):
        return super().__str__() + \
               f'\n- Modelo: {self.get_modelo()}' + \
               f'\n- Potencia: {self.get_potencia()} CV'

    def __repr__(self):
        return super().__repr__()[:-1].replace("Vehiculo", "Coche") + \
               f',{self.get_modelo()!r},{self.get_potencia()})'
