# Definimos una lista de diccionarios con la información detallada de cada fruta
tienda = [
    {"nombre" : "manzana", "precio": 10}, 
    {"nombre" : "pera", "precio": 20}    
]

# Definimos un diccionario para relacionar un número de entrada con el nombre de la fruta
frutas = {
    "1" : "manzana",
    "2" : "pera"
}

intentos = 2  # Límite de errores permitidos
intento = 0   # Contador de errores actual

# Bucle principal: se ejecuta mientras no superes los 2 intentos
while intento < intentos:
    num_prod = input("Ingrese el numero del producto: ") # Pide "1" o "2"
    
    # Verifica si el número ingresado existe en el diccionario 'frutas'
    if num_prod in frutas:
        # Muestra el nombre de la fruta (ej. "manzana")
        print(f"El producto seleccionado es: {frutas[num_prod]}") 
        
        # Pide la cantidad al usuario (Ojo: se guarda como texto/str)
        cantidad = input("Ingrese la cantidad del producto: ")
        
        # ERROR AQUÍ: 'tienda' es una lista, no puedes acceder a [precio] directamente.
        # Además, 'cantidad' es texto y debe ser convertido a entero (int) para multiplicar.
        # precio1 = {tienda[precio]} * cantidad 
        
        # Intenta imprimir el total (esto fallará por la línea anterior)
        print("Total ", num_prod, "=", "precio1")
        
        # Reinicia los contadores para entrar en el segundo bucle
        intento = intentos # Esto rompe el bucle actual
        intentos = 2
        intento = 0
        
        # Segundo bucle para preguntar si quiere otro producto
        while intento < intentos:
            num_prod = input("Quiere otro producto: ")
            
            if num_prod in frutas:
                print(f"El producto seleccionado es: {frutas[num_prod]}") 
                cantidad = input("Ingrese la cantidad del producto: ")
                
                # ERROR AQUÍ: 'precio' no está definido como variable numérica
                # precio *= cantidad
                intento = intentos # Rompe el bucle si acierta
            else:
                print("El numero del producto no es valido.")
                intento += 1 # Suma error si falla
                
        # Este mensaje saldrá siempre porque 'intentos' vale 2
        if intentos == 2: print("Numero de intentos no validos superado")
        
    else:
        # Si el primer código de producto no existe, suma error
        print("El numero del producto no es valido.")
        intento += 1

# Este mensaje también saldrá siempre al final
if intentos == 2: print("Numero de intentos no validos superado")
