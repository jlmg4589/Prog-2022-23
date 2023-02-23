
__key = list()

def credencial(user, local_key):
    """Crea un TAD para credenciales (Usuario y contraseña)."""
    global __key
    __key.append(local_key)
    index_key=len(__key)-1
    
    def credenciales(index):
        if (index == 0):
            return user
        else:
            return index_key
        
    return credenciales

# Función selectora.
def login(credencial):
    """Devualeve el login del usuario los credenciales pasados"""
    return credencial(0)

# Función selectora.
def contrasenia(credencial):
    return __key[credencial(1)]

# Función mutadora que en este caso no devuelve ningún dato perteneciente al TAD, pero sí modifica un dato del TAD.
def modificarContrasenia(credencial, old_key ,new_key):
    global __key
    if (old_key == __key[credencial(1)]):
        __key[credencial(1)]=new_key
        return print("Contraseña actualizada")
    else:
        return print("Contraseña no actualizada, no coinciden ambas c")


