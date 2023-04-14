"""4. A partir de la clase Hora diseñada en el ejercicio anterior, implementar la clase
HoraExacta, que incluye en la hora los segundos. Además de los métodos heredados
desde la clase Hora, dispondrá de:

    • __init__(hora,minutos,segundos): construye un objeto con los datos pasados
    como argumentos.
    • set_segundos(valor): asigna un valor (si está comprendido entre 0 y
    59) a los segundos. Devuelve True o False según se haya podido cambiar los
    segundos o no.
    • inc(): incrementa la hora en un segundos."""

"""5. Añadir a la clase HoraExacta un método que compare si dos horas (la invocante y otra
pasada como argumento al método) son iguales o distintas. ¿Cómo debería llamarse ese
método?"""

from Ejercicio3 import *

class HoraExacta(Hora):

    def __init__(self, hora, minutos, segundos):
        super().__init__(hora, minutos)
        if not self.set_segundos(segundos):
            raise ValueError("Rango de segundos inválido (00-59)")


    def set_segundos(self, segundos):
        if segundos in range(0,60):
            self.segundos = segundos
            return True
        return False

    def get_segundos(self):
        return self.segundos

    def inc(self):
        if self.get_segundos() == 59:
            super().inc()
            self.set_segundos(0)
        else:
            self.set_segundos(self.get_segundos() + 1)

    def __eq__(self, otra_hora):

        if not isinstance(otra_hora, type(self)):
            return NotImplemented

        num_self = self.get_hora()*100**2 + self.get_minutos()*100 + self.get_segundos()
        num_otra_hora =  otra_hora.get_hora()*100**2 + otra_hora.get_minutos()*100 + otra_hora.get_segundos()

        return num_self == num_otra_hora
    
    def __str__(self):
        return super().__str__() + f':{self.get_segundos():>02}'
