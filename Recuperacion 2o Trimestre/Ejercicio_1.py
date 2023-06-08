from datetime import datetime
now = datetime.now()

class Fecha:

    def __init__(self, anio, mes, dia):
        self.anio = anio
        self.mes = mes
        self.dia = dia

    def set_anio(self, anio):
        self.anio = anio

    def set_mes(self, mes):
        self.mes = mes

    def set_dia(self, dia):
        self.dia = dia

    def get_anio(self):
        return self.anio

    def get_mes(self):
        return self.mes

    def get_dia(self):
        return self.dia

    def to_string(self):
        """DocString"""
        return f"{self.get_dia():02}/{self.get_mes():02}/{self.get_anio():04}"

    def edad(self):
        """DocString"""
        if now.month < self.get_mes() or (now.month == self.get_mes() and now.day < self.get_dia()):
            return now.year - self.get_anio() - 1
        return now.year - self.get_anio()

    def __repr__(self):
        return f"Fecha({self.get_anio()}, {self.get_mes()}, {self.get_dia()})"

    def __str__(self):
        return f"Fecha: {self.to_string()}"

    def __eq__(self, otra_fecha):
        fecha1 = self.get_anio()*10000 + self.get_mes()*100 + self.get_dia()
        fecha2 = otra_fecha.get_anio()*10000 + otra_fecha.get_mes()*100 + otra_fecha.get_dia()
        return fecha1 == fecha2
