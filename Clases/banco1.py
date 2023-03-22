class Cliente:

    def __init__(self, dni, nombre, apellidos):
        self.set_dni(dni)
        self.set_nombre(nombre)
        self.set_apellidos(apellidos)

    def __repr__(self):
        return f'Cliente({(self.get_dni())!r}, {(self.get_nombre())!r}, {(self.get_apellidos())!r})'

    def __eq__(self, otro_cliente):
        if not isinstance(otro_cliente, Cliente):
            raise NotImplementedError(
                "No coinciden los tipos de datos pasados.")
        return self.get_dni() == otro_cliente.get_dni()

    def __hash__(self):
        return hash(self.get_dni())

    def __str__(self):
        return f'Cliente: {self.get_nombre()} {self.get_apellidos()} con DNI: {self.get_dni()}'

    def set_dni(self, dni):
        self.__dni = dni

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos

    def get_dni(self):
        return self.__dni

    def get_nombre(self):
        return self.__nombre

    def get_apellidos(self):
        return self.__apellidos


class Cuenta:
    __numero = 0

    def __init__(self, cliente, movimientos=None):
        Cuenta.__numero += 1
        self.__set_numero(Cuenta.__numero)
        self.set_titular(cliente)
        self.__saldo = 0
        if movimientos is None:
            self.__movimiento = []
            return
        self.__movimiento = movimientos

    def __eq__(self, otra_cuenta):
        if not isinstance(otra_cuenta, Cuenta):
            raise NotImplementedError("No coinciden los tipos de datos pasados")
        return self.get_numero() == otra_cuenta.get_numero()

    def __hash__(self):
        return hash(self.get_numero)

    def __repr__(self):
        return f'Cuenta({self.get_titular()!r}, {self.get_movimiento()})'

    def __str__(self):
        cadena = f'Cuenta numero: {self.get_numero()}, con Titular: '
        cadena += f'{self.get_titular().get_nombre()} {self.get_titular().get_apellidos()}'
        return cadena

    def __set_numero(self, numero):
        self.__numero = numero

    def get_numero(self):
        return self.__numero

    def set_titular(self, cliente):
        self.__titular = cliente

    def get_titular(self):
        return self.__titular

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def set_movimiento(self, concepto, cantidad):
        self.__movimiento.append(Movimientos(concepto, cantidad, self))

    def get_movimiento(self):
        return self.__movimiento[:]

    def imprimir_movimientos(self):
        if len(self.get_movimiento()) == 0:
            raise ValueError("No hay movimientos en esta cuenta.")
        print("-"*(len(f'Movimiento  100: {self.get_movimiento()[0]}')+10))
        for i in range(len(self.get_movimiento())):
            print(f'Movimiento  {i+1}: {self.get_movimiento()[i]}')
        print(f'Saldo disponible: {self.get_saldo()}')
        print("-"*(len(f'Movimiento  100: {self.get_movimiento()[0]}')+10))


class Movimientos:

    def __init__(self, concepto, cantidad, cuenta):
        self.set_operacion(concepto, cantidad, cuenta)
        self.set_concepto(concepto)
        self.set_cantidad(cantidad)

    def __repr__(self):
        return f'Movimientos({repr(self.get_concepto())}, {self.get_cantidad()})'

    def __str__(self):
        return f'Concepto: {self.get_concepto()} - Cantidad: {self.get_cantidad()}'

    def set_concepto(self, concepto):
        self.__concepto = concepto

    def get_concepto(self):
        return self.__concepto

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def get_cantidad(self):
        return self.__cantidad

    def set_operacion(self, concepto, cantidad, cuenta):
        if concepto not in ('Retirar', 'Ingresar') or cantidad < 0:
            raise ValueError(
                "El concepto debe ser, Ingresar o Retirar. La cantidad debe ser siempre positiva.")
        if concepto == 'Retirar' and cantidad <= cuenta.get_saldo():
            cuenta.set_saldo(cuenta.get_saldo()-cantidad)
            return
        if concepto == "Ingresar":
            cuenta.set_saldo(cuenta.get_saldo()+cantidad)
            return
        raise ValueError("No hay fondos suficientes para la cantidad a retirar.")
