"""
Módulo para gestionar los menús de diferentes bares y bocadillos individuales.
"""

class Bar:
    """
    Representa un bar con un nombre y una lista de menús disponibles.
    """
    
    def __init__(self, nombre, menus=None):
        """
        Inicializa un nuevo Bar.

        Args:
            nombre (str): El nombre del bar.
            menus (list, opcional): Lista inicial de menús. Por defecto es una lista vacía.
        """
        self.nombre = nombre
        self.menus = menus if menus is not None else []

    def imprimir_menus(self):
        """
        Imprime por consola todos los menús disponibles en el bar con un separador visual.
        """
        print("=" * 50)
        print(f"Los menús del bar {self.nombre} son:")
        for i, menu in enumerate(self.menus):
            print(f"Menu {i}: {menu}")
        print("=" * 50)

    def agregar_menu(self, menu):
        """
        Añade un nuevo menú a la lista del bar.

        Args:
            menu (str): El nombre o descripción del menú a añadir.
        """
        self.menus.append(menu)

    def quitar_menu(self, menu):
        """
        Elimina un menú de la lista del bar, si este existe.

        Args:
            menu (str): El nombre del menú a eliminar.
        """
        if menu in self.menus:
            self.menus.remove(menu)
        else:
            print(f"El menú '{menu}' no se encuentra en el bar.")


class Bocadillo:
    """
    Representa un bocadillo individual (fuera de la carta de un bar).
    """
    
    def __init__(self, menu):
        """
        Inicializa un nuevo Bocadillo.

        Args:
            menu (str): El nombre o descripción del bocadillo.
        """
        self.menu = menu

    def imprimir(self):
        """
        Imprime por consola la información del bocadillo con un separador visual.
        """
        print("*" * 70)
        print(f"El menú del bocadillo es: {self.menu}")
        print("*" * 70)


# --- Datos iniciales ---
menus_las_palmeras = ["Chivito", "Bocadillo de tortilla", "Carne de caballo con ajos"]
menus_el_pirata = ["Bocadillo de calamares", "Bocadillo de melón", "Bocadillo de jamón"]

# --- Instanciación de objetos ---
bar_las_palmeras = Bar("Las Palmeras", menus_las_palmeras)
bar_el_pirata = Bar("El Pirata", menus_el_pirata)
bocadillo_silverio = Bocadillo("Bocadillo de garbanzos con mayonesa")

# --- Casos de uso ---
# Imprimir los menús iniciales
bar_las_palmeras.imprimir_menus()

# Agregar un menú al bar
bar_las_palmeras.agregar_menu("Bocadillo de tortilla de uñas")
bar_las_palmeras.imprimir_menus()

# Quitar un menú del bar
bar_las_palmeras.quitar_menu("Bocadillo de tortilla")
bar_las_palmeras.imprimir_menus()

# Imprimir el menú del bocadillo suelto
bocadillo_silverio.imprimir()