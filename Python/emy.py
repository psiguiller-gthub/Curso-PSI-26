import random

# Variables de configuración de los límites del tablero
LIMITE_TABLERO = 5
NUMERO_DE_BARCOS = 3
# 1. Creamos la lista vacía para almacenar las coordenadas de los barcos
flota = []
# numero de intentos
intent=0
intent_final=5
# TRADUCCION
BIENVENIDO = "Bienvenido a Batalla Naval"
MENSAJE_BIENVENIDA =f"Encuentra los {len(flota)} barcos escondidos en el tablero. ¡Buena suerte!"
ESCRIBE_FILA = f"Escribe Fila (1-{LIMITE_TABLERO}): _"
ESCRIBE_COLUMNA = f"Escribe Columna (1-{LIMITE_TABLERO}): _"
ERROR_COORDENADAS_FUERA_RANGO = "¡ERROR! Esas coordenadas están fuera del mapa."
BARCO_HUNDIDO = "Muy Bien! Has hundido un barco."
OBJETIVO_AGUA = "¡AGUA! Intenta de nuevo."
VICTORIA = "Felicidades, Has ganado!"
FIN_DEL_JUEGO = "Final del juego"
BARCOS_PRESENTES = f"Barcos presentes: {len(flota)}"


def generar_coordenada(limite):
    x = random.randint(1, limite)
    y = random.randint(1, limite)
    return (x, y)

#con esto genero 3 posiciones aleatorias para los barcos
def flota_aleatoria():
    while len(flota) < NUMERO_DE_BARCOS:
        posicion = generar_coordenada(LIMITE_TABLERO)
        if posicion not in flota:
            flota.append(posicion)
    return flota

#pedir coordenadas al usuario
def pedir_coordenadas():
    intento_fila = (input(ESCRIBE_FILA))
    intento_col = (input(ESCRIBE_COLUMNA))
    return intento_fila, intento_col



print(BIENVENIDO)
print(MENSAJE_BIENVENIDA)
print(f"Tienes {intent_final} intentos para encontrar los barcos.")
print(f"El limite del tablero es de {LIMITE_TABLERO}x{LIMITE_TABLERO}.")
# Ahora 'flota' contiene: [(x1, y1), (x2, y2), (x3, y3)...]
print(f"La flota está lista: {len(flota)} barcos generados.")
print("¡Buena suerte!")

flota_aleatoria()

intento_fila, intento_col = pedir_coordenadas()
print(len(flota))

# iteración del bucle
while intent < intent_final and len(flota) > 0:
    intent = intent+1
    print(f"Intento {intent} de {intent_final}.")


# comprueba que las coordenadas estén dentro del rango permitido del 1 al límite del tablero
    while intento_fila not in range(1, LIMITE_TABLERO+1) or intento_col not in range(1, LIMITE_TABLERO+1):
        print(ERROR_COORDENADAS_FUERA_RANGO)
        intento_fila, intento_col = pedir_coordenadas()


        # Creamos una lista con el intento del jugador
        intento = [intento_fila, intento_col]

        # 3. results
        if intento in flota:
            print(BARCO_HUNDIDO)
            flota.remove(intento)
            
        else:
            print(OBJETIVO_AGUA)

        print(BARCOS_PRESENTES)

print(VICTORIA)


