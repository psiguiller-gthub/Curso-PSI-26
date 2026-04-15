class Cuenta_bancaria:
    def __init__(self, saldo, numero_de_cuenta):
        self.saldo = saldo
        self.numero_de_cuenta = numero_de_cuenta
       
    def consultar_saldo (self,monto):
        #saldo que te devuelve el cliente
        return monto <=  self.saldo
    
    def debitar (self,monto):
        #el saldo -lo que sacas
        self.saldo -= monto

class Cajero_automatico:
    def __init__(self,saldo):
        self.saldo = saldo
     
    def validar_efectivo_disponible(self,monto):
        return self.saldo >= monto

    def retirar_efectivo(self,monto):
        self.saldo -= monto


class Transaccion:
   def realizar_transaccion(self,objeto_cuenta,objeto_cajero,monto):
        if monto % 10 == 0: 
            if objeto_cuenta.consultar_saldo (monto):
                if objeto_cajero.validar_efectivo_disponible (monto):
                     objeto_cuenta.debitar(monto)
                     objeto_cajero.retirar_efectivo(monto)
                     print (f"Transacion exitosa: Retire sus {monto}€.Saldo restante: {objeto_cuenta.saldo}€")
                else:            
                    print ("Error:El cajero no dispone de efectivo suficiente")
            else:
                print ("Error:Saldo insufiente en su cuenta")
        else:
            print ("Error:El monto debe de ser multiplo de 10")
            
            
saldo_cuenta=5000
saldo_cajero=30000
monto= 100

mi_cuenta = Cuenta_bancaria(123456, saldo_cuenta)
mi_cajero = Cajero_automatico(saldo_cajero)
mi_gestor = Transaccion()

# --- Casos de uso CORREGIDOS ---

# Caso 1: Éxito (100€)
mi_gestor.realizar_transaccion(mi_cuenta,mi_cajero,100)

# Caso 2: Error de múltiplo (85€)
mi_gestor.realizar_transaccion(mi_cuenta,mi_cajero, 85)

# Caso 3: Error de saldo en cuenta (intentar sacar 10.000€ teniendo 5.000€)
mi_gestor.realizar_transaccion(mi_cuenta, mi_cajero, 10000)