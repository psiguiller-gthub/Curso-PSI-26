class Cuenta_bancaria:
    def __init__(self, numero, saldo_cuenta):
        self.numero = numero
        self.saldo_cuenta = saldo_cuenta

    def consultar_saldo_cliente(self, monto):
        return monto <= self.saldo_cuenta
    
    def debitar(self, monto):    
        self.saldo_cuenta -= monto
        
class Cajero_automatico:
    def __init__(self, saldo_cajero):
        self.saldo_cajero = saldo_cajero
    
    def validar_efectivo_disponible(self, monto):
        return self.saldo_cajero >= monto
    
    def retirar_efectivo(self, monto):
        self.saldo_cajero -= monto
        
class Transaccion:   
    def realizar_transaccion(self, objeto_cuenta, objeto_cajero, monto): # Nombres más claros
        if monto % 10 == 0: 
            # REGLA 1: Verificar si el cliente tiene saldo
            if objeto_cuenta.consultar_saldo_cliente(monto): 
                # REGLA 2: Verificar si el cajero tiene efectivo
                if objeto_cajero.validar_efectivo_disponible(monto): 
                    objeto_cuenta.debitar(monto)
                    objeto_cajero.retirar_efectivo(monto)
                    print(f"Éxito: Retire sus {monto}€. Saldo restante: {objeto_cuenta.saldo_cuenta}€")
                else:    
                    print("Error: El cajero no dispone de efectivo suficiente.")
            else:
                print("Error: Saldo insuficiente en su cuenta.")
        else:
            print("Error: El monto debe ser múltiplo de 10€.")

# Variables
saldo_cuenta = 5000
saldo_cajero = 25000
monto_retiro = 100

mi_cuenta = Cuenta_bancaria(123456789, saldo_cuenta)
mi_cajero = Cajero_automatico(saldo_cajero)
mi_gestor = Transaccion()
  
# Casos de uso
mi_gestor.realizar_transaccion(mi_cuenta, mi_cajero, 26000) # Falla cajero
mi_gestor.realizar_transaccion(mi_cuenta, mi_cajero, 548)   # Falla múltiplo 10
mi_gestor.realizar_transaccion(mi_cuenta, mi_cajero, 6000)  # Falla saldo cliente
mi_gestor.realizar_transaccion(mi_cuenta, mi_cajero, 100)   # Éxito

           