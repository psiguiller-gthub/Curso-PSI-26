def pedir_num_fruta(total_opciones):
    seleccion = input(f"Ingrese el número de la fruta que desea comprar del 1 al {total_opciones}: ")
    return seleccion

def pedir_cantidad(nombre_elegida):
    kilos = float(input(f"Ingrese la cantidad de {nombre_elegida} en kilos: "))
    return kilos

def pedir_seguir_comprando():
    seguir_comprando = input("¿Desea comprar más frutas? (s/n): ")
    return seguir_comprando.lower() == 's'
