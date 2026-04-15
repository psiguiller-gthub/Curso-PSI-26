class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def consultarSaldo(self):
        return self.saldo

    def debitar(self, monto):
        self.saldo -= monto

class CajeroAutomatico:
    def __init__(self, efectivo_disponible):
        self.efectivo_disponible = efectivo_disponible

    def validarEfectivoDisponible(self, monto):
        return self.efectivo_disponible >= monto

    def retirarEfectivo(self, monto):
        self.efectivo_disponible -= monto

class Transaccion:
    def ejecutar(self, cuenta, cajero, monto):

        if monto % 10 == 0:
            
            if cajero.validarEfectivoDisponible(monto):
                
                if cuenta.consultarSaldo() >= monto:
                    
                    cuenta.debitar(monto)
                    cajero.retirarEfectivo(monto)
                    print(f"Retiro exitoso: {monto}€")
                
                else:
                    print("Error: Saldo insuficiente en tu cuenta.")
            else:
                print("Error: El cajero no dispone de efectivo suficiente.")
        else:
            print("Error: El importe debe ser múltiplo de 10€.")

# casos de uso
# valores iniciales
saldo_cuenta = 5000
efectivo_cajero = 300
monto_retiro = 300

# inicializar la cuenta, el cajero y transacción
mi_cuenta = CuentaBancaria("ES21-1234", saldo_cuenta)
mi_cajero = CajeroAutomatico(efectivo_cajero)
mi_proceso = Transaccion()

print("-"*30)
print(f"Saldo inicial cuenta: {saldo_cuenta}€")
print(f"Efectivo inicial en cajero: {efectivo_cajero}€")
print(f"Intentando retirar: {monto_retiro}€")
print("-"*30)
print()
print("*"*30)
mi_proceso.ejecutar(mi_cuenta, mi_cajero, monto_retiro)
print(f"Saldo actual cuenta: {mi_cuenta.consultarSaldo()}€")
print(f"Efectivo disponible en cajero: {mi_cajero.efectivo_disponible}€")
print("*"*30)

 



