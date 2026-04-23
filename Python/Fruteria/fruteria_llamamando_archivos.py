from almacen_frutas import frutas
from parametros_frutas import limite_fallos, fallos, comprando
from pedir_usuario import pedir_num_fruta, pedir_cantidad, pedir_seguir_comprando
from print_usuario import print_final_fallo, print_menu_frutas, print_resumen_compra, print_compra_actual, print_fallos_actuales

compras = []
total_opciones = len(frutas)

while comprando:
    print_menu_frutas(frutas)
    seleccion = pedir_num_fruta(total_opciones)
    
    if seleccion in frutas:
        fruta_elegida = frutas[seleccion]
        nombre_elegida = fruta_elegida['nombre']
        precio_elegida = fruta_elegida['precio']
        
        kilos = pedir_cantidad(nombre_elegida)

        subtotal = precio_elegida * kilos
        
        item_comprado = {
            "nombre": nombre_elegida,
            "precio": precio_elegida,
            "kilos": kilos,
            "subtotal": subtotal
        }
        compras.append(item_comprado)
        
        print_compra_actual(nombre_elegida, kilos, subtotal)

        seguir_comprando = pedir_seguir_comprando()        
    else:
        fallos += 1
        print_fallos_actuales(fallos, limite_fallos)

        if fallos >= limite_fallos:
            print_final_fallo()
            comprando = False

print_resumen_compra(compras)