# Array

frutas = {
    "1" : {"nombre" : "manzana", "precio": 10}, 
    "2" : {"nombre" : "pera", "precio": 20}    
}

intentos = 2
intento = 0
while intento < intentos:
    num_prod = input("Ingrese el numero del producto: ")
    if num_prod in frutas:
        print(f"El producto seleccionado es: {frutas[num_prod]}") 
        cantidad = input("Ingrese la cantidad del producto: ")
        precio1 = {frutas[precio]} * cantidad
        print("Total ", num_prod, "=", precio1)
        intento = intentos
        intentos = 2
        intento = 0
        while intento < intentos:
            num_prod = input("Quiere otro producto: ")
            if num_prod in frutas:
                print(f"El producto seleccionado es: {frutas[num_prod]}") 
                cantidad = input("Ingrese la cantidad del producto: ")
                precio *= cantidad
                intento = intentos
            else:
                print("El numero del producto no es valido.")
                intento += 1
        if intentos == 2: print("Numero de intentos no validos superado")
    else:
        print("El numero del producto no es valido.")
        intento += 1
if intentos == 2: print("Numero de intentos no validos superado")


"""
- pedir numero producto
- pedir cantidad
- pedir si quiere otro
    encaso S pedir numero producto
    encaso N FINALIZAR
- COSTE COMPRA
"""
