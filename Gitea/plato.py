class Plato:
    def __init__(self, nombre, ingredientes, principales, precio, calorias, bebidas, menu, vegetariano, alergenos, guarnicion):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.principales = principales
        self.precio = precio
        self.calorias = calorias
        self.bebidas = bebidas
        self.menu = menu
        self.vegetariano = vegetariano
        self.alergenos = alergenos
        self.guarnicion = guarnicion

    def imprimir_array(self, txt, elementos): # Función para imprimir un array en plan Generico.
        print(f"{txt}:")
        for elemento in elementos:
            print(f"- {elemento}") # print(f"\n{elemento}")
    
    def listar_plato(self):
        print(f"Plato: {self.nombre}")
        self.imprimir_array("Ingredientes", self.ingredientes)
        print(f"Precio: {self.precio}€")
        print(f"Calorías: {self.calorias} kcal")
        self.imprimir_array("Bebidas", self.bebidas)
        print(f"Menú: {self.menu}")
        print(f"Vegetariano: {'Sí' if self.vegetariano else 'No'}")         
        self.imprimir_array("Alergenos", self.alergenos)
        print(f"Guarnición: {self.guarnicion}")

        """
        print(f"Alergenos: {', '.join(self.alergenos) if self.alergenos else 'Ninguno'}") # Join es para convertir la lista de alergenos en una cadena separada por comas. Unir
        """

ingredientes = ["Pollo", "Verduras", "Pasta", "Queso", "Pescado"]
principales = True
precio = 12.99
calorias = 600
bebidas = ["Agua", "Tinto", "Refresco", "Cerveza"]
menus = ["Desayuno", "Comida", "Cena"]
vegetariano = False
alergenos = ["Gluten", "Lácteos", "nueces", "Marisco", "pepino"]
guarnicion = "Arroz"

seleccion_ingredientes = [ingredientes[0], ingredientes[2]]
seleccion_bebidas = [bebidas[3], bebidas[2]]
seleccion_menu = menus[1]
seleccion_alergenos = [alergenos[1], alergenos[4]]


plato1 = Plato("Pasta con pollo", seleccion_ingredientes, principales, precio, calorias, seleccion_bebidas, seleccion_menu, vegetariano, seleccion_alergenos, guarnicion)

plato1.listar_plato()