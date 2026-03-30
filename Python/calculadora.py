saludo = "Bienvenido a la Calculadora"
opcion_suma = "1. Suma "
opcion_Resta = "2. Resta "
opcion_Multiplicacion = "3. Multiplicacion "
opcion_Division = "4. Division "
eleccion_opcion = "Elige una opcion (1,2,3,4)"
recoger_valor_a = "Dame el primer valor "
recoger_valor_b = "Dame el segundo valor "

#funcion suma
def suma(a, b):
    return a + b

#funcion resta
def resta(a, b):
    return a - b

#funcion multiplicacion
def multiplicacion(a, b):
    return a * b

#funcion division
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error Division por 0"

#Impresion en pantalla
print(saludo)
print(opcion_suma)
print(opcion_Resta)
print(opcion_Multiplicacion)
print(opcion_Division)
print(eleccion_opcion)

#Validar opciones de funcion
opcion = str(input())
while opcion not in ['1', '2','3','4']:
    print("Opción inválida, introduzca una opción válida")
    opcion = str(input())
else:
    print(eleccion_opcion)
    

#Recoger valores
print(recoger_valor_a)
a = int(input())
print(recoger_valor_b)
b = int(input())

#Devolver resultado
if opcion == '1':
    print("Resultado: ", suma(a, b))
elif opcion == '2':
    print("Resultado: ", resta(a, b))
elif opcion == '3':
    print("Resultado: ", multiplicacion(a, b))
else: 
    print("Resultado: ", division(a, b))
