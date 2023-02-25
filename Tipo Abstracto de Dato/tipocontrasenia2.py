""" Módulo que crea y gestiona usuarios. """

def credencial(user, key):
    """Función selectora."""
    def login():
        """Devuelve el login del usuario los credenciales pasados"""
        return user

    def modificar_contrasenia(old_key ,new_key):
        """Función mutadora que en este caso no devuelve ningún dato perteneciente al TAD,
        pero sí modifica un dato del TAD."""
        nonlocal key
        if old_key == key:
            key = new_key
            return print("Contraseña acatualizada")
        return print("Contraseña no actualizada, no coinciden ambas contraseñas")

    def modificar_login(oldkey ,login):
        """Función mutadora que en este caso no devuelve ningún dato perteneciente al TAD,
        pero sí modifica un dato del TAD."""

        nonlocal user
        if oldkey == key:
            user = login
            return print("Nombre de usuario atualizado a:", user)
        return print("La contraseña introducida es incorrecta para el usuario:", user)

    def credencial_menu(accion):
        """Función que despacha."""
        if accion == 'login':
            return login()
        if accion == 'contraseña':
            return print("No es posible mostrar la contrasña por seguridad.")
        if accion == 'modContraseña':
            return modificar_contrasenia
        if accion == 'modLogin':
            return modificar_login
        raise ValueError('Acción incorrecta')

    print("----------------------------------------------------")
    print("Usuario:", user,",creado")
    print("----------------------------------------------------")
    return credencial_menu
