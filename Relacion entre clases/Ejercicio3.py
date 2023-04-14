"""3. Diseñar la clase Hora, que representa un instante de tiempo compuesto por la hora (de
0 a 23) y los minutos. Dispone de los métodos:
• __init__(hora,minutos): construye un objeto con los datos pasados como argumentos.
• inc(): incrementa el instante en un minuto y no devuelve nada.
• set_minutos(valor): asigna un valor (si es válido) a los minutos. Devuelve True
o False según se haya podido modificar los minutos o no.
• set_hora(valor): asigna un valor (si está comprendido entre 0 y 23) a la hora.
Devuelve True o False según se haya podido cambiar la hora o no.
• __str__(): devuelve una cadena con la representación de la hora."""


class Hora:
    def __init__(self, hora=int, minutos=int):
        if not self.set_hora(hora):
            raise ValueError("Rango de horas inválido (00-23)")
        if not self.set_minutos(minutos):
            raise ValueError("Rango de minutos inválido (00-59)")

    def set_hora(self, hora):
        if hora in range(0,24):
            self.hora = hora
            return True
        return False

    def set_minutos(self, minutos):
        if minutos in range(0,60):
            self.minutos = minutos
            return True
        return False

    def get_hora(self):
        return self.hora

    def get_minutos(self):
        return self.minutos

    def inc(self):
        if self.get_minutos() == 59:
            if self.get_hora() == 23:
                self.set_hora(0)
            else:
                self.set_hora(self.get_hora() +1)
            self.set_minutos(0)
        else:
            self.set_minutos(self.get_minutos()+1)

    def __str__(self):
        return f'La hora actual es: {self.get_hora():>02}:{self.get_minutos():>02}'
