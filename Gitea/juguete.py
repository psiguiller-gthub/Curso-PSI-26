class Juguete:
    def __init__(self, nombre, color, tamano):
        self.nombre = nombre
        self.color = color
        self.tamano = tamano

def reemplazar_nombre(buscar_nombre, nuevo_nombre, items):
    for item in items:
        if item.nombre == buscar_nombre:
           item.nombre = nuevo_nombre

juguete_01 = Juguete("Pelota", "Roja", "L")
juguete_02 = Juguete("Pelota", "Rosa", "XL")
juguete_03 = Juguete("Cohete", "Verde", "M")
juguete_04 = Juguete("Muñeca", "Azul", "S")

jugueteria = [juguete_01, juguete_02, juguete_03, juguete_04]

print(f"Nombre: {item.nombre}, Color: {item.color}, Tamaño: {item.tamano}" for item in jugueteria)

reemplazar_nombre("Pelota", "Balón", jugueteria)

print(juguete_02.nombre)  # Salida: Balón
print(juguete_01.nombre)
print(juguete_03.nombre)
print(juguete_04.nombre)