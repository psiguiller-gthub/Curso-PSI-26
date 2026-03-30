class Lampara:
    def __init__(self, color, encendida=False):
        self.color = color
        self.encendida = encendida
        
    def encender(self):
        self.encendida = True

    def apagar(self):
        self.encendida = False

    def interruptor_lampara(lampara):
        if lampara.encendida:
            lampara.apagar()
            print("La lámpara se ha apagado.")
        else:
            lampara.encender()
            print("La lámpara se ha encendido.")

lampara_01 = Lampara("rojo", encendida=True)
lampara_02 = Lampara("verde", encendida=False)

print(f"Color de la lámpara_01: {lampara_01.color}")
print(f"Lámpara_01 ¿encendida?: {lampara_01.encendida}")

# lampara_01.encender()
# print(f"Lámpara encendida: {lampara_01.encendida}")

Lampara.interruptor_lampara(lampara_01)
print(f"Lámpara interruptor: {lampara_01.encendida}")

# lampara_01.apagar()
# print(f"Lámpara encendida: {lampara_01.encendida}")
print(f"Color de la lámpara_02: {lampara_02.color}")
print(f"Lámpara_02 ¿encendida?: {lampara_02.encendida}")

Lampara.interruptor_lampara(lampara_02)
print(f"Lámpara interruptor: {lampara_02.encendida}")
