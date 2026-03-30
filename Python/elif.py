# La sentencia if-elif-else, por ejemplo:

x = 10
 
if x == 10: # True
    print("x == 10")
 
if x > 15: # False
    print("x > 15")
 
elif x > 10: # False
    print("x > 10")
 
elif x > 5: # True
    print("x > 5")
 
else:
    print("else no será ejecutado")
 
# Si la condición para if es False, el programa verifica las condiciones de los bloques elif posteriores: el primer elif que sea True es el que se ejecuta.
# Si todas las condiciones son False, se ejecutará el bloque else.

# Sentencias condicionales anidadas, ejemplo:

x = 10
 
if x > 5: # True
    if x == 6: # False
        print("anidado: x == 6")
    elif x == 10: # True
        print("anidado: x == 10")
    else:
        print("anidado: else")
else:
    print("else")
 
