
# Introducir nota
n = float(input("Introduce Nota: "))
# recogiendo solo el entero de la division
""""
entero = n // 1
print(entero)
# recogiendo solo el decimal de la division
dec = n - entero
print(dec)

#Comparando los decimales si son mayores e iguales a 0.5 o menores a 0.5, para redondear arriba o abajo
if dec >= 0.5:
    entero += 1
else:
    entero -= 1

print("NOTA = ", entero)
"""
x=n
def redondear (n):
    if n - int(n) < 0.5:
        return int(n)
        x = n
    else:
        return int(n) + 1
        x = n + 1
print("NOTA = ", x)

print("NO VA, EL MIO DEL COMENTARIO SI, CORREGIR EL OTRO")
