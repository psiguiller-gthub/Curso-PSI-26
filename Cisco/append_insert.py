# 3.4.8 Agregando elementos a una lista: append() y insert()

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

my_list = []  # Creando una lista vacía.
 
for i in range(5):
    my_list.insert(0, i + 1)
 
    print(my_list)
 
 # No hace una cuenta atras, sino que va insertando del 1 al 5 y desplazandolos a la derecha