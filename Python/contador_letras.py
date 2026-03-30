frase = input(f"Escribir frase: ")
letra_buscada = input(f"Letra a buscar: ")

contador = 0
for letra in frase: # letra es un item
    if letra.lower() == letra_buscada:
        contador = contador + 1

print(f"La letra '{letra_buscada}' aparece {contador} veces en la frase.")

contador_metodo = frase.lower().count(letra_buscada)
print(f"La letra '{letra_buscada}' aparece {contador_metodo} veces en la frase.")

