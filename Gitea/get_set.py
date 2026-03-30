class Objeto:
    def __init__(self, nombre = "Manolo", num1 = 0, num2 = 0):
        self.nombre = nombre
        self.num1 = num1
        self.num2 = num2

objeto = Objeto()
print(objeto.nombre)

objeto2 = Objeto("Pepe", 5, 3)
print(objeto2.nombre)        

objeto2.nombre = "Pepito" # Set = Establecer (Asignar) el valor de un atributo. Escribir
print(objeto2.nombre)  # Get = Obtener el valor de un atributo. Leer