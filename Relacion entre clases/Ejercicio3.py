class Hora:
    def __init__(self, hora, minutos):
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
            self.set_minutos(0)
        else:
            self.set_minutos(self.get_minutos()+1)

    def __str__(self):
        return f'La hora actual es: {self.get_hora():>2}:{self.get_minutos():>02}'
