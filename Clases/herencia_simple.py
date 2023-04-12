class Vehiculo:

    def __init__(self, marca, modelo):
        self.set_marca(marca)
        self.set_modelo(modelo)
        self.set_parado()

    def set_marca(self, marca):
        self.marca=marca
    
    def set_modelo(self, modelo):
        self.modelo=modelo

    def set_arrancado(self):
        self.arrancado = True

    def set_parado(self):
        self.arrancado = False

    def get_marca(self):
        return self.marca
    
    def get_modelo(self):
        return self.modelo

    def get_estado(self):
        return self.arrancado
    
    def __repr__(self):
        return f'Vehiculo({self.get_marca()!r}, {self.get_modelo()!r})'

    def __str__(self):
        return f'Marca: {self.get_marca()}, Modelo: {self.get_modelo()} y el vehículo está: {"Arrancado." if self.get_estado() else "Parado."}'
    
class Moto(Vehiculo):

    def __init__(self, marca, modelo, matricula):
        super().__init__(marca, modelo)
        self.__matricula = matricula
        self.set_arrancado()
        self.down_caballito()

    def get_matricula(self):
        return self.__matricula

    def up_caballito(self):
        self.hcaballito = "Voy haciendo el caballito."
    
    def down_caballito(self):
       	self.hcaballito = "Estoy con las dos ruedas en el asfalto."

    def estado(self):
        return self.hcaballito
    
    def __repr__(self):
        return f'Moto({self.get_marca()!r}, {self.get_modelo()!r}, {self.get_matricula()!r})'


moto =  Moto("Honda", "CBR", "1425KJH")
print("\n\n**********************")
print(moto.estado())   # Muestra el estado de la moto, en cuestión si está o no haciendo el caballito.
moto.up_caballito() # La moto se pone a haceer el caballito.
print(moto.estado())   # Muestra el estado de la moto, en cuestión si está o no haciendo el caballito.

print(repr(moto))    # Muestra la representación interna de su prorpia clase.
print(moto) # Muestra la representación legible de la superclase.