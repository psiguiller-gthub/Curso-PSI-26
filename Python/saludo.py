def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

saludo = "Hola, bienvenido a la calculadora básica."
opcion_suma = "1. Suma"
opcion_resta = "2. Resta"
opcion_multiplicacion = "3. Multiplicación"
opcion_division = "4. División"
eleccion_opcion = "Por favor, elige una opción (1/2/3/4): "
recoger_numero1 = "Ingresa el primer número: "
recoger_numero2 = "Ingresa el segundo número: "

print(saludo)
print(opcion_suma)
print(opcion_resta)
print(opcion_multiplicacion)
print(opcion_division)

opcion = input(eleccion_opcion)
# verificar que la opcion es válida
while opcion not in ['1', '2', '3', '4']:
    print("Opción inválida. Por favor, elige una opción válida (1/2/3/4).")
    opcion = input(eleccion_opcion)

num1 = float(input(recoger_numero1))
num2 = float(input(recoger_numero2))

if opcion == '1':
    print("Resultado: ", suma(num1, num2))
elif opcion == '2': 
    print("Resultado: ", resta(num1, num2))
elif opcion == '3':
    print("Resultado: ", multiplicacion(num1, num2))
else :
    print("Resultado: ", division(num1, num2))




