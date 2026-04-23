# Array

frutas_clase = [
    {"nombre" : "manzana", "precio": 44}, 
    {"nombre" : "pera", "precio": 33}, 
    {"nombre" : "melon", "precio": 31},
]

num_frutas = len(frutas_clase)   # num_frutas = 3 frutas
precios = 0

for fruta in frutas_clase :       # Fruta es un item de frutas_clase
    precios = precios + fruta ["precio"]

print(f"El promedio es: {precios/num_frutas}")
