menus_las_palmeras = ["Chivito", "Bocadillo de Tortilla", "Carne de caballo con ajos"]
menus_el_pirata = ["Bocadillo de Calamares", "Bocadillo de Melon", "Bocadillo de Jamon"]

class LasPalmeras:
    def __init__(self, menus = [], nombre = "Las Palmeras"):
        self.menus = menus
        self.nombre = nombre

class ElPirata:
    def __init__(self, menus = [], nombre = "El Pirata"):
        self.menus = menus
        self.nombre = nombre

class Bocadillo():
    def __init__(self, menu):
        self.menu = menu

def imprimir_menus_bar(bar):
    i=0
    print(linea_separacion1)
    print(f"Los menús del bar {bar.nombre} son:")
    for menu in bar.menus:
        print(f"\tMenu {i}--{menu}") # \t es un tabulador para alinear el texto, y {i} es el número del menú.
        i += 1
    print(linea_separacion1)

def imprimir_menu(bocadillo):
    print(linea_separacion2)
    print(f"\tEl menú del bocadillo es: · {bocadillo.menu}")
    print(linea_separacion2)

def agregar_menu_bar(bar, menu):
    bar.menus.append(menu) # Agregar un nuevo menú al bar utilizando el método append().

def eliminar_menu_bar(bar, menu):
    if menu in bar.menus: # Verificar si el menú existe en la lista de menús del bar.
        bar.menus.remove(menu) # Eliminar el menú del bar utilizando el método remove().
    else:
        print(f"El menú {menu} no existe en el bar {bar.nombre}.") # Imprimir un mensaje de error si el menú no existe en el bar.


bar_las_palmeras = LasPalmeras(menus_las_palmeras, nombre="Las Palmeras") # Instanciar un Objeto de la clase LasPalmeras con el menú de las palmeras. 
# Variable = Objeto(Parametros)
bar_el_pirata = ElPirata(menus_el_pirata, nombre="El Pirata") # Instanciar un Objeto de la clase ElPirata con el menú de El Pirata.
# Variable = ObjetoTipo(Datos)
bocadillo_silverio = Bocadillo("Bocadillo de Lentejas con Ketchup") # Instanciar un Objeto de la clase Bocadillo con el menú del bocadillo de Silverio.
linea_separacion1 = "="*45 # Crear una variable con una cadena de caracteres que se repite 40 veces para usarla como línea de separación.
linea_separacion2 = "*"*45

# casos de uso: Imprimir el menú del bar Las Palmeras, el menú del bar El Pirata y el menú del bocadillo de Silverio.
imprimir_menus_bar(bar_las_palmeras)
agregar_menu_bar(bar_las_palmeras, "Fuet con Nocilla") # Agregar un nuevo menú al bar Las Palmeras.
imprimir_menus_bar(bar_las_palmeras)

eliminar_menu_bar(bar_las_palmeras, "Carne de caballo con ajos") # Eliminar un menú del bar Las Palmeras.
imprimir_menus_bar(bar_las_palmeras)

#imprimir_menus_bar(bar_el_pirata)
#imprimir_menu(bocadillo_silverio)

