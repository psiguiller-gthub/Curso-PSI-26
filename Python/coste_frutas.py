frutas = {
    "1": {"nombre": "manzana", "precio": 10},
    "2": {"nombre": "banana", "precio": 15},
    "3": {"nombre": "naranja", "precio": 20},
    "4": {"nombre": "pera", "precio": 25}
}

compras = []
total_opciones = len(frutas)

print("--- Menú de Frutas ---")
for numero, datos in frutas.items():
    nombre_fruta = datos['nombre']
    precio_fruta = datos['precio']
    print(f"{numero}. {nombre_fruta} ({precio_fruta} euros/kilo)")


comprando = True
fallos = 0
limite_fallos = 3

while comprando:
    seleccion = input(f"Ingrese el número de la fruta que desea comprar del 1 al {total_opciones}: ")
    
    if seleccion in frutas:
        fruta_elegida = frutas[seleccion]
        nombre_elegida = fruta_elegida['nombre']
        precio_elegida = fruta_elegida['precio']
        
        kilos = float(input(f"Ingrese la cantidad de {nombre_elegida} en kilos: "))
        subtotal = precio_elegida * kilos
        
        item_comprado = {
            "nombre": nombre_elegida,
            "precio": precio_elegida,
            "kilos": kilos,
            "subtotal": subtotal
        }
        compras.append(item_comprado)
        
        print(f"El costo de {kilos} kilos de {nombre_elegida} es: {subtotal} euros.")
        
        seguir_comprando = input("¿Desea comprar más frutas? (s/n): ")
        if seguir_comprando.lower() != 's':
            comprando = False
    else:
        fallos += 1
        print(f"La fruta no es válida. Llevas {fallos} fallo(s) de {limite_fallos}.")
        
        if fallos >= limite_fallos:
            print("Has alcanzado el límite de fallos permitidos. Finalizando compra.")
            comprando = False


total_pagar = sum(item['subtotal'] for item in compras)


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
    
print(f"Total a pagar: {total_pagar} euros")