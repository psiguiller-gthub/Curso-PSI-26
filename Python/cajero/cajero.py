class Cuenta:
    def __init__(self, cliente, saldo, n_cuenta):
        self.cliente = cliente
        self.saldo = saldo
        self.n_cuenta = n_cuenta

    def consultar_saldo(self):
        print(f"El saldo de la cuenta de {self.cliente} es: {self.saldo} euros.")

    def debitar_monto(self, cantidad):   # falta gestionar el cajero
        if cantidad > self.saldo:
            print("No tiene fondos suficientes.")
        else:
            self.saldo -= cantidad
            print(f"Se han retirado {cantidad} euros de la cuenta de {self.cliente}.")

class Cajero:
    def __init__(self, id_cajero, ubicacion):
        self.id_cajero = id_cajero
        self.ubicacion = ubicacion

    def retirar_dinero(self, cuenta, cantidad):
        print(f"Intentando retirar {cantidad} euros de la cuenta de {cuenta.cliente} en el cajero {self.id_cajero} ubicado en {self.ubicacion}.")
        cuenta.debitar_monto(cantidad)