class Cuenta:
    def __init__(self, saldo_cuenta, n_cuenta):
        self.saldo_cuenta = saldo_cuenta
        self.n_cuenta = n_cuenta

    def consultar_saldo(self):
        return self.saldo_cuenta

    def debitar_saldo(self, monto): 
       self.saldo_cuenta -= monto
       
class Cajero:
    def __init__(self, saldo_cajero):
        self.saldo_cajero = saldo_cajero

    def validar_efectivo_disponible(self, monto):
        return self.saldo_cajero >= monto

    def retirar_efectivo(self, monto):
        self.saldo_cajero -= monto

class Transaccion:

    def procesar_transaccion(self, cuenta_bancaria, cajero, monto):
        if monto % 10 == 0:
            if monto <= cuenta_bancaria.consultar_saldo():
                if monto <= cajero.saldo_cajero:
                    cajero.retirar_efectivo(monto)
                    cuenta_bancaria.debitar_saldo(monto)
                    print(f"Transacción exitosa: {monto} € retirados de la cuenta.")
                else:
                    print(f"Transacción fallida: El cajero no tiene suficiente efectivo para retirar {monto} €.")    
            else:
                print(f"Transacción fallida: {monto} € es mayor o igual al saldo disponible en cuenta ({cuenta_bancaria.saldo_cuenta} euros).")
        else:
            print(f"Transacción fallida: El monto {monto} € no es múltiplo de 10.")

# CASOS DE USO  

# EXITO
saldo_cuenta = 1000
n_cuenta = "ES1234567890"
monto = 150
saldo_cajero = 500
cuenta_bancaria = Cuenta(saldo_cuenta, n_cuenta)
cajero = Cajero(saldo_cajero)
ejecutar = Transaccion()
print(f"\nSaldo cuenta: {cuenta_bancaria.saldo_cuenta} € - Saldo cajero: {cajero.saldo_cajero} € - Monto a retirar: {monto} €")
ejecutar.procesar_transaccion(cuenta_bancaria, cajero, monto)

# ERROR: Monto no múltiplo de 10
saldo_cuenta = 1000
n_cuenta = "ES1234567890"
monto = 155
saldo_cajero = 500
cuenta_bancaria = Cuenta(saldo_cuenta, n_cuenta)
cajero = Cajero(saldo_cajero)
ejecutar = Transaccion()
print(f"\nSaldo cuenta: {cuenta_bancaria.saldo_cuenta} € - Saldo cajero: {cajero.saldo_cajero} € - Monto a retirar: {monto} €")
ejecutar.procesar_transaccion(cuenta_bancaria, cajero, monto)

# ERROR: Saldo insuficiente en cuenta
saldo_cuenta = 1000
n_cuenta = "ES1234567890"
monto = 1500
saldo_cajero = 500
cuenta_bancaria = Cuenta(saldo_cuenta, n_cuenta)
cajero = Cajero(saldo_cajero)
ejecutar = Transaccion()
print(f"\nSaldo cuenta: {cuenta_bancaria.saldo_cuenta} € - Saldo cajero: {cajero.saldo_cajero} € - Monto a retirar: {monto} €")
ejecutar.procesar_transaccion(cuenta_bancaria, cajero, monto)

# ERROR: Saldo insuficiente en cajero
saldo_cuenta = 2000
n_cuenta = "ES1234567890"
monto = 1500
saldo_cajero = 500
cuenta_bancaria = Cuenta(saldo_cuenta, n_cuenta)
cajero = Cajero(saldo_cajero)
ejecutar = Transaccion()
print(f"\nSaldo cuenta: {cuenta_bancaria.saldo_cuenta} € - Saldo cajero: {cajero.saldo_cajero} € - Monto a retirar: {monto} €")
ejecutar.procesar_transaccion(cuenta_bancaria, cajero, monto)