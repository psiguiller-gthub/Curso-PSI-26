class Vehiculo:    
    def __init__(self, chasis, motor, ruedas, color):
        self.chasis = chasis
        self.motor = motor
        self.ruedas = ruedas
        self.color = color

class Coche(Vehiculo):
    def __init__(self, chasis, motor, ruedas, color, aire_acondicionado, puertas, direccion_asistida, carroceria):
        super().__init__(chasis, motor, ruedas, color)
        self.aire_acondicionado = aire_acondicionado
        self.puertas = puertas
        self.direccion_asistida = direccion_asistida
        self.carroceria = carroceria

    def mostrar_informacion(self):
        print(f"Coche: {self.color}, {self.puertas} puertas, Motor: {self.motor}, Carrocería: {self.carroceria}")

class Moto(Vehiculo):
    def __init__(self, chasis, motor, ruedas, color, pata_cabra, pedales, manubrio):
        super().__init__(chasis, motor, ruedas, color)
        self.pata_cabra = pata_cabra
        self.pedales = pedales
        self.manubrio = manubrio

    def mostrar_informacion(self):
        print(f"Moto: {self.color}, Motor: {self.motor}, Manubrio: {self.manubrio}, Pata cabra: {self.pata_cabra}, Pedales: {self.pedales}")

#casos de uso
coche_01 = Coche("chasis_01", "motor_01", 4, "rojo", True, 4, True, "sedan")
moto_01 = Moto("chasis_02", "motor_02", 2, "azul", True, True, True)

coche_01.mostrar_informacion()
moto_01.mostrar_informacion()
