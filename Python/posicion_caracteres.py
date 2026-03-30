#str = ["o", "l", "h", "a"]
#print(f"{str[2]}{str[0]}{str[1]}{str[3]}")

hola = "HOLA"      
posicion = hola.find("L") # Si no lo encuenctra devuelve un -1
print(posicion)

posicion = hola.index("L") # Si no lo encuenctra devuelve un ValueError
print(posicion)            # Con numeros tiene que ser index si o si
