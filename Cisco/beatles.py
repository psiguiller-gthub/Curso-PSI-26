# paso 1
beatles = []
print("Paso 1:", beatles)

# paso 2
beatles.append("Jhon Lenon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

# paso 3
for i in range(2):
    miembro = input("Introduce el miembro a añadir: ")
    beatles.append(miembro)
    i += 1
        
print("Paso 3:", beatles)

# paso 4
del beatles[-1] # Elimina al último
del beatles[-1]
print("Paso 4:", beatles)

# paso 5
beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fav", len(beatles))
