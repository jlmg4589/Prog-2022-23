
"""
DocString
"""

from Ejercicio_1 import *

class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.set_titular(titular)
        self.set_cantidad(cantidad)

    def set_titular(self, titular):
        self.__titular = titular

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def get_titular(self):
        return self.__titular

    def get_cantidad(self):
        return self.__cantidad

    def ingresar(self, cantidad):
        if self.__valida_cantidad(cantidad):
            self.set_cantidad(self.get_cantidad() + cantidad)

    def retirar(self,cantidad):
        if self.__valida_cantidad(cantidad):
            self.set_cantidad(self.get_cantidad() - cantidad)

    def __valida_cantidad(self, cantidad) -> bool:
        if cantidad <= 0:
            print("La cantidad introducida no es válida. Debe ser un número mayor de 0.")
            return False
        return True
    
    def mostrar(self):
        print(self)

    def __repr__(self):
        return f"Cuenta({self.get_titular()!r},{self.get_cantidad()!r})"
    
    def __str__(self):
        return f"Titular: {self.get_titular()}\n" + \
                f"Fondos: {self.get_cantidad()}"

class CuentaJoven(Cuenta):
    
    def __init__(self, titular, nacimiento, cantidad=0):
        super().__init__(titular, cantidad)
        self.set_nacimiento(nacimiento)
        if not self.esTitularValido():
            raise ValueError("No se ha dado de alta al usuario. No cumple los requisitos (18>=edad<=25).")

    def set_nacimiento(self, nacimiento):
        self.nacimiento = nacimiento

    def get_nacimiento(self):
        return self.nacimiento

    def esTitularValido(self):
        return (self.get_nacimiento().edad() > 17 and self.get_nacimiento().edad() < 26)

    def __repr__(self):
        lista = super().__repr__().replace("Cuenta", "CuentaJoven").split(",")
        return lista[0] + f",{self.get_nacimiento()!r}," + lista[1]

    def __str__(self):
        return super().__str__() + f"\nEdad: {self.get_nacimiento().edad()}"
