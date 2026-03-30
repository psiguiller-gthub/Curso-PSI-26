blocks = int(input("Ingresa el número de bloques: "))

#
# Escribe tu código aquí.
#	

capa = 0
bloque_capa = 1

while blocks >= bloque_capa:
    capa += 1
    blocks = blocks - bloque_capa
    bloque_capa += 1

print("La altura de la pirámide:", capa)


# Entrada de muestra: 6 Salida esperada: 3
# Entrada de muestra: 20 Salida esperada: 5
# Entrada de muestra: 1000 Salida esperada: 44
# Entrada de muestra: 2 Salida esperada: 1
