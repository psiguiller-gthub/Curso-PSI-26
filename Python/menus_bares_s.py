menus_las_palmeras = ["Chivito", "Bocadillo de tortilla", "Carne de caballo con ajos"]
menus_el_pirata = ["Bocadillo de calamares", "Bocadillo de melón", "Bocadillo de jamón"]

class Las_palmeras:
    def __init__(self, menus=[]):
        self.menus = menus

class El_pirata:
    def __init__(self, menus=[]):
        self.menus = menus

class Bocadillo():
    def __init__(self, menu):
        self.menu = menu

def imprime_menu(bocadillo):
    longitud_del_separador = 70
    print("*"*longitud_del_separador)
    print(f"El menú del bocadillo es: {bocadillo.menu}")
    print("*"*longitud_del_separador)

def imprime_menus_bar(bar):
    i=0
    longitud_del_separador = 50
    print("="*longitud_del_separador)
    print(f"Los menús del bar son:")
    for menu in bar.menus:
        print(f"Menu {i}: {menu}")
        i+=1
    print("="*longitud_del_separador)

def agregar_menu_bar(bar, menu):
    bar.menus.append(menu)

bar_las_palmeras = Las_palmeras(menus_las_palmeras)
bar_el_pirata = El_pirata(menus_el_pirata)
bocadillo_silverio = Bocadillo("Bocadillo de garbanzos con mayonesa")

# casos de uso añadir menu al bar
# antes de agregar el menú
imprime_menus_bar(bar_las_palmeras)
# agregar el menú
agregar_menu_bar(bar_las_palmeras, "Bocadillo de tortilla de uñas")
# después de agregar el menú
imprime_menus_bar(bar_las_palmeras)

# quitar un menú del bar