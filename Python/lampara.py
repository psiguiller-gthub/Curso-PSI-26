class Lampara:
    def __init__(self, color, encendida=False):
        self.color = color
        self.encendida = encendida
    
    def encender(self):
        self.encendida = True
    
    def apagar(self):
        self.encendida = False

    def cambiar_estado(lampara):
        if lampara.encendida:
            lampara.apagar()
            print("La lámpara se ha apagado.")
        else:
            lampara.encender()
            print("La lámpara se ha encendido.")
        
lampara_01 = Lampara("roja", encendida=True)
lampara_02 = Lampara("verde", encendida=False)

print(f"Color de lampara 01: {lampara_01.color}")
print(f"Color de lampara 02: {lampara_02.color}")   
print(f"¿Está encendida lampara 01? {lampara_01.encendida}")
print(f"¿Está encendida lampara 02? {lampara_02.encendida}")

#cambiar el estado de la lampara 01
Lampara.cambiar_estado(lampara_01)
print(f"¿Está encendida lampara 01? {lampara_01.encendida}")

#cambiar el estado de la lampara 02
Lampara.cambiar_estado(lampara_02)
print(f"¿Está encendida lampara 02? {lampara_02.encendida}")



