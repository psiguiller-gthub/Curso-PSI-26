def secuencia_collatz(n):
    # Validación inicial: debe ser entero positivo
    if n <= 0:
        return "Por favor, introduce un número entero mayor a cero."
    
    pasos = [n]
    
    while n != 1:
        if n % 2 == 0:
            n = n // 2  # Si es par, dividir por 2
        else:
            n = 3 * n + 1  # Si es impar, 3n + 1
        pasos.append(n)
        
    return pasos

# Ejemplo de uso con un número c0
c0 = int(input("Introduce el valor de c0: "))
resultado = secuencia_collatz(c0)

print(f"Secuencia: {resultado}")
print(f"Número de pasos para llegar a 1: {len(resultado) - 1}")


""" Explicación del funcionamiento
Entrada inicial: El programa recibe un número entero positivo.
Bucle while: La condición n != 1 asegura que el código se ejecute repetidamente hasta que se cumpla la hipótesis de Lothar Collatz.
Operador Módulo %: Se utiliza n % 2 == 0 para determinar si el número es par (el resto de la división entre 2 es cero).
División entera //: Se usa el doble slash para asegurar que el resultado sea un número entero y no un flotante (por ejemplo, 4 // 2 = 2 en lugar de 2.0).
Lista de pasos: El programa almacena cada nuevo valor en una lista para que puedas ver el camino completo que tomó el número hasta llegar al 1.
"""