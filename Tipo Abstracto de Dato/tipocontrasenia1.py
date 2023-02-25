"""Módulo para el TAD de (Usuario, Contraseña)"""

__KEY = []

def credencial(user, local_key):
    """Crea un TAD para credenciales (Usuario y contraseña)."""
    #global __KEY
    __KEY.append(local_key)
    index_key=len(__KEY)-1

    def credenciales(index):
        if index == 0:
            return user
        return index_key

    return credenciales

def login(in_credencial):
    """Devualeve el login del usuario los credenciales pasados"""
    return in_credencial(0)

def contrasenia(in_credencial):
    """Función selectora."""
    return __KEY[in_credencial(1)]

def modificar_contrasenia(in_credencial, old_key ,new_key):
    """Función mutadora que en este caso no devuelve ningún dato perteneciente al TAD,
    pero sí modifica un dato del TAD."""
    #global __KEY

    if old_key == __KEY[in_credencial(1)]:
        __KEY[in_credencial(1)]=new_key
        return print("Contraseña actualizada")
    return print("Contraseña no actualizada, no coinciden ambas contraseñas")
