"""Modulo para la construcción de la clase Usuario"""
class Usuario:
    def __init__(self, usuario, contrasenia, dni):
        self.usuario = usuario
        self.__contrasenia = contrasenia
        self.__dni = dni

    def __eq__(self,otro):
        if type(self) != type(otro):
            raise NotImplementedError("Error")
        return self.__dni == otro.get_dni()

    def __hash__(self):
        return hash(self.__dni)

    def __repr__(self):
        return f'Usuario({repr(self.usuario)}, {self.__contrasenia}, "{self.__dni}")'

    def __str__(self):
        return str("Clase tipo Usuario: 1) Usuario: " + f'{self.usuario}' + " 2) Contraseña: ****")

    def get_dni(self):
        return self.__dni

    def consulta_usuario(self):
        return self.usuario

    def cambio_contrasenia(self, old_pass, new_pass):
        if self.__contrasenia == old_pass:
            self.__contrasenia = new_pass
            return repr("Contraseña actializada correctamente.")
        return repr("No ha sido posible cambiar al contraseña, la contraseña anterior no coincide.")

    def cambio_usuario(self, contrasenia, usuario):
        if self.__contrasenia == contrasenia:
            self.usuario = usuario
            print("usuario cambiado correctamente.")
            return self.usuario 
        raise Exception("Contraseña pasada incorrecta.")
