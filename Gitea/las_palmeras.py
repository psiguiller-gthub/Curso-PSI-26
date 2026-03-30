class LasPalmeras:
    def __init__(self, menus = []):
        self.menus = menus

class Bocadillos(LasPalmeras):
    def __init__(self, menu = []):
        super().__init__(menu)
    #   self.menu.extend(["Bocadillo de Jamón", "Bocadillo de Pollo", "Bocadillo Vegetal"])

menus = ["Chivito", "Brascada", "Calamares", "Almusafes", "Vegetal", "Atun con olivas", "Carne de caballo con ajos", "Rojo y Negro"]
las_palmeras = LasPalmeras(menus)

i = 0
for menu in las_palmeras.menus:
    print(f"Menu: {i} · {menu}")
    i += 1

bocadillo_guille = Bocadillos(las_palmeras.menus[1])
print(f"\nEl bocadillo de Guille es: {bocadillo_guille.menus}")

bocadillo_prisca = Bocadillos(las_palmeras.menus[6])
print(f"El bocadillo de Prisca es: {bocadillo_prisca.menus}\n")