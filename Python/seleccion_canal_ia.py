# Definimos un diccionario donde la clave es el número (string) y el valor es el nombre del canal
canales = {
    "1" : "TV1",
    "2" : "TV2",
    "3" : "Antena 3",
    "4" : "Cuatro",
    "5" : "T5",
    "6" : "La Sexta"
}

intentos = 3  # Límite máximo de fallos permitidos
intento = 0   # Contador que inicia en cero

# El ciclo se repetirá mientras el contador 'intento' sea menor a 3
while intento < intentos:
    # Solicitamos la entrada al usuario (input siempre devuelve texto)
    seleccion_canal = input("Ingrese el canal que desea ver: ")

    # Verificamos si lo que escribió el usuario existe como clave en nuestro diccionario
    if seleccion_canal in canales:
        # Si existe, imprimimos el nombre del canal accediendo al diccionario
        print(f"El canal seleccionado es: {canales[seleccion_canal]}")
        # Igualamos 'intento' a 'intentos' para romper el ciclo (ya que el usuario acertó)
        intento = intentos
    else:
        # Si no existe, avisamos al usuario y sumamos 1 al contador de fallos
        print("El canal no es valido.")
        intento += 1

# CORRECCIÓN: Usamos una condición para saber si salió del ciclo por agotar los intentos
# Si el contador llegó a 3 sin haber acertado, mostramos el error final
if intento == 3 and seleccion_canal not in canales:
    print("Numero de intentos no validos. Acceso bloqueado.")