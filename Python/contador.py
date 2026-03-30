import time

contador = 10

print("Iniciando secuencia de despegue...")

while contador > 0:
    print (contador)
    contador = contador - 1
    time.sleep(1)

print("¡DESPEGUE!")
