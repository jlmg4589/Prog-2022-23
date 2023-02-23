
def credencial(user, key):

    # Función selectora.
    def login():
        """Devuelve el login del usuario los credenciales pasados"""
        return user
    
    # Función mutadora que en este caso no devuelve ningún dato perteneciente al TAD, pero sí modifica un dato del TAD.
    def modificarContrasenia(old_key ,new_key):
        nonlocal key
        if (old_key == key):
            key = new_key
            return print("Contraseña acatualizada")
        else:
            return print("Contraseña no actualizada, no coinciden ambas contraseñas")
        
    # Función mutadora que en este caso no devuelve ningún dato perteneciente al TAD, pero sí modifica un dato del TAD.
    def modificarLogin(oldkey ,login):
        nonlocal user
        if (oldkey == key):
            user = login
            return print("Nombre de usuario atualizado a:", user)
        else:
            return print("La contraseña introducida es incorrecta, y es necesaria para cambiar el login del usuario:", user)

    # Función despacha.
    def credencial_menu(accion):
        if accion == 'login':
            return login()
        elif accion == 'contraseña':
            return print("No es posible mostrar la contrasña por seguridad.")
        elif accion == 'modContraseña':
            return modificarContrasenia
        elif accion == 'modLogin':
            return modificarLogin
        else:
            raise ValueError('Acción incorrecta')
    
    print("----------------------------------------------------")
    print("Usuario:", user,",creado")
    print("----------------------------------------------------")
    return credencial_menu