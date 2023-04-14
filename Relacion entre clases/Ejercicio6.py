"""

6. Crear la clase abstracta Instrumento que almacena en una lista las notas musicales de
una melodía (dentro de una misma octava). El método concreto add añade nuevas notas
musicales. La clase también dispone del método abstracto interpretar con la siguiente
signatura:
interpretar() -> None
que, en cada subclase que herede de Instrumento, mostrará por la salida las notas
musicales según las interprete. Las notas serán constantes estáticas definidas dentro de
la clase Nota, de la siguiente forma:
class Nota:
DO = 'do'
RE = 're'
MI = 'mi'
FA = 'fa'
SOL = 'sol'
LA = 'la'
SI = 'si'

7. Crear la clase Piano como subclase de la clase Instrumento del ejercicio anterior.

"""
from abc import ABC, abstractmethod

class Nota: #Notas musicales disponibles.
    DO = 'do'
    RE = 're'
    MI = 'mi'
    FA = 'fa'
    SOL = 'sol'
    LA = 'la'
    SI = 'si'

class Instrumento(ABC):

    melodia=[]

    def add(self, nota):
        if nota == Nota.DO:
            Instrumento.melodia.append(Nota.DO)
        elif nota == Nota.RE:
            Instrumento.melodia.append(Nota.RE)
        elif nota == Nota.MI:
            Instrumento.melodia.append(Nota.MI)
        elif nota == Nota.FA:
            Instrumento.melodia.append(Nota.FA)
        elif nota == Nota.SOL:
            Instrumento.melodia.append(Nota.SOL)
        elif nota == Nota.LA:
            Instrumento.melodia.append(Nota.LA)
        elif  nota == Nota.SI:
            Instrumento.melodia.append(Nota.SI)
        else:
            raise f'Nota no definida.'

    @abstractmethod
    def interpretar(self):
        ...

class Piano(Instrumento):  

    def interpretar(self):
        if not bool(self.melodia):
            print("No ha añadido ninfuna melodía aún.")
            return
        print(self.melodia[0::2]) #Definimos qué va a interpretar en el caso del Piano de toda la melodía disponible.