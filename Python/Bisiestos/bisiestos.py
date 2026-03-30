year = int(input("Introduce un año: "))

if year < 1582:
    print("No esta dentro del período del calendario Gregoriano")
else:
    if year % 4 != 0:
        print("No es bisiesto")
    elif year % 100 != 0:
        print("Es bisiesto")
    elif year % 400 != 0:
        print("No es bisiesto")
    else:
        print("Es bisiesto")

"""
Un año es bisiesto si es divisible por 4, pero no por 100,
a menos que también sea divisible por 400. Por ejemplo, 
el año 2000 fue bisiesto porque es divisible por 400, 
mientras que el año 1900 no fue bisiesto porque es divisible 
por 100 pero no por 400. El año 2024 será bisiesto porque es 
divisible por 4 y no por 100.

Desde la introducción del calendario Gregoriano (en 1582), 
se utiliza la siguiente regla para determinar el tipo de año:

si el número del año no es divisible entre cuatro, es un año común.
de lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
de lo contrario, si el número del año no es divisible entre 400, es un año común.
de lo contrario, es un año bisiesto.
Observa el código en el editor - solo lee un número de año y 
debe completarse con las instrucciones que implementan la prueba 
que acabamos de describir.

El código debe mostrar uno de los dos mensajes posibles, 
que son Año Bisiesto o Año Común, según el valor ingresado.

Verificar si el año cae en la era Gregoriana. Consejo: utiliza los operadores != y %.

Prueba tu código con los datos que hemos proporcionado.

Datos de Prueba:
Entrada de muestra: 2000
Salida esperada: Año bisiesto

Entrada de muestra: 2015
Salida esperada: Año comun

Entrada de muestra: 1900
Salida esperada: Año comun

Entrada de muestra: 1999
Salida esperada: Año comun

Entrada de muestra:

1996
Salida esperada:

Output
Año bisiesto
Salida esperada:

Output
No dentro del período del calendario gregoriano
Entrada de muestra:

1580
"""