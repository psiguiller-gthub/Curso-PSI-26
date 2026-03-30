# Array

alumnos_clase = [
    {"nombre" : "Ruben", "edad": 44}, 
    {"nombre" : "Carlos", "edad": 33}, 
    {"nombre" : "Guille", "edad": 31},
]

for alumno in alumnos_clase :  # Alumno es un item de alumnos_clase
    # 1ª OPCION
    print(alumno["nombre"], "tiene", alumno["edad"], "años")

    # 2ª OPCION
    print(f"El {alumno["nombre"]} tiene {alumno["edad"]} años")