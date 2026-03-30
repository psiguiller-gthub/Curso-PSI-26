class Vehiculo:
    def __init__(self, chasis, motor, ruedas, color):
        self.chasis = chasis
        self.motor = motor
        self.ruedas = ruedas
        self.color = color

class Coche(Vehiculo):
    def __init__(self, aire_acc, puertas, d_asistida, carroceria, chasis, motor, ruedas, color):
        super().__init__(chasis, motor, ruedas, color)
        self.aire_acc = aire_acc
        self.puertas = puertas
        self.d_asistida = d_asistida
        self.carroceria = carroceria

class Moto(Vehiculo):
    def __init__(self, pata_cabra, pedales, manubrios, chasis, motor, ruedas,color):
        super().__init__(chasis, motor, ruedas, color)
        self.pata_cabra = pata_cabra
        self.pedales = pedales
        self.manubrios = manubrios
        
# casos de uso

coche_01 = Coche("chasis_01", "motor_01", 4, "rojo", True, 4, True, "sedan")
moto_01 = Moto("chasis_02", "motor_02", 2, "azul", True, True, True)

