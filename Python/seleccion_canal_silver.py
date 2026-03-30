canales = {
"1" : "TV1",
"2" : "TV2",
"3" : "Antena 3",
"4" : "Cuatro",
"5" : "T5",
"6" : "La Sexta"
}
intentos = 3
intento = 0
while intento < intentos:
    seleccion_canal = input("Ingrese el canal que desea ver: ")
    if seleccion_canal in canales:
        print(f"El canal seleccionado es: {canales[seleccion_canal]}")
        intento = intentos
    else:
        print("El canal no es valido.")
        intento += 1
if intentos == 3: print("Numero de intentos no validos superado")
