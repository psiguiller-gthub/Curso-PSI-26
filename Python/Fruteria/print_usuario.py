def print_menu_frutas(frutas):
    print("--- Menú de Frutas ---")
    for numero, datos in frutas.items():
        nombre_fruta = datos['nombre']
        precio_fruta = datos['precio']
        print(f"{numero}. {nombre_fruta} ({precio_fruta} euros/kilo)")

def print_resumen_compra(compras):
    print("Lista de compras:")
    if len(compras) == 0:
        print("No se compró ninguna fruta.")
    else:
        for articulo in compras:
            nombre_articulo = articulo['nombre']
            precio_unitario = articulo['precio']
            cantidad_kilos = articulo['kilos']
            subtotal_articulo = articulo['subtotal']
        
            print(f"- {cantidad_kilos} kg de {nombre_articulo} a {precio_unitario} euros/kg: {subtotal_articulo} euros")

    total_pagar = sum(item['subtotal'] for item in compras)
    print(f"Total a pagar: {total_pagar} euros")

def print_compra_actual(nombre_elegida, kilos, subtotal):
    print(f"El costo de {kilos} kilos de {nombre_elegida} es: {subtotal} euros.")

def print_fallos_actuales(fallos, limite_fallos):
    print(f"La fruta no es válida. Llevas {fallos} fallo(s) de {limite_fallos}.")

def print_final_fallo():
    print("Has alcanzado el límite de fallos permitidos. Finalizando compra.")