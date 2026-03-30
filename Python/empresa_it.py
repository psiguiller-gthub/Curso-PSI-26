class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    
    def presentarse(self):
        print(f"Hola, soy el Programador {self.nombre}, programo en {self.lenguaje} y gano {self.salario}.")
        print(f"Hola, soy el Administrador {self.nombre}, tengo {self.servidores_a_cargo} servidores a cargo y gano {self.salario}.")
        return f"Hola, soy el Empleado {self.nombre} y gano {self.salario}."
    
class Programador(Empleado):
    def __init__(self, lenguaje, nombre, salario):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje

class Administrador(Empleado):
    def __init__(self, servidores_a_cargo, nombre, salario):
        super().__init__(nombre, salario)
        self.servidores_a_cargo = servidores_a_cargo

    

programador_01 = Programador("Python", "Juan", 50000)

programador_01.presentarse()

administrador_01 = Administrador(5, "Maria", 60000)

administrador_01.presentarse()

# Funcion presentarse() en Empleado, se llama desde Programador y Administrador, 
# mostrando la información específica de cada clase.
# hacerla por separado en cada clase, pero se repite el código de presentación, lo que no es eficiente.