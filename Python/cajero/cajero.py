class Cuenta:
    def __init__(self, cliente, saldo_cuenta, n_cuenta):
        self.cliente = cliente
        self.saldo_cuenta = saldo_cuenta
        self.n_cuenta = n_cuenta

    def consultar_saldo(self):
        print(f"El saldo de la cuenta de {self.cliente} es: {self.saldo_cuenta} euros.")

    def debitar_saldo(self, monto):   # falta gestionar el cajero
        if monto > self.saldo_cuenta:
            print("No tiene fondos suficientes.")
        else:
            self.saldo_cuenta -= monto
            print(f"Se han retirado {monto} euros de la cuenta de {self.cliente}.")

class Cajero:
    def __init__(self, id_cajero, saldo_cajero):
        self.id_cajero = id_cajero
        self.saldo_cajero = saldo_cajero

    def validar_efectivo_disponible(self, monto):
        if self.saldo_cajero > monto:
            print(f"El cajero {self.id_cajero} tiene suficiente efectivo para retirar {monto} euros.")
            return True
        else:
            print(f"El cajero {self.id_cajero} no tiene suficiente efectivo para retirar {monto} euros.")
            return False

    def retirar_efectivo(self, monto):
        if self.validar_efectivo_disponible( monto):
            self.saldo_cajero = self.saldo_cajero - monto
            print(f"Se han retirado {monto} euros del cajero {self.id_cajero}.")
        else:
            print(f"No se ha podido retirar {monto} euros del cajero {self.id_cajero}.")        

class Transaccion:
    
    def procesar_transaccion(cuenta_bancaria, cajero, monto):
        if monto %10 == 0:
            if monto <= cuenta_bancaria.saldo_cuenta:
                if monto <= cajero.saldo_cajero:
                    cajero.retirar_efectivo(monto)
                    cuenta_bancaria.saldo_cuenta -= monto
                    print(f"Transacción exitosa: {monto} € retirados de la cuenta de {cuenta_bancaria.cliente}.")
                else:
                    print(f"Transacción fallida: El cajero no tiene suficiente efectivo para retirar {monto} €.")    
            else:
                print(f"Transacción fallida: {monto} € es mayor o igual al saldo disponible en cuenta ({cuenta_bancaria.saldo_cuenta} euros).")
        else:
            print(f"Transacción fallida: El monto {monto} € no es múltiplo de 10.")

# CASOS DE USO  

cliente = "Aniceto"
saldo_cuenta = 500
n_cuenta = "ES1234567890"
cuenta_bancaria = Cuenta(cliente, saldo_cuenta, n_cuenta)

monto = 150
id_cajero = "1"
saldo_cajero = 1000
cajero = Cajero(id_cajero, saldo_cajero)

Transaccion.procesar_transaccion(cuenta_bancaria, cajero, monto)