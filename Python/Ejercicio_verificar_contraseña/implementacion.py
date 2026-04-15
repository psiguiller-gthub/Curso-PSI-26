# ==========================================
# FUNCIONES DE APOYO
# ==========================================

# TODO: Función para verificar si el texto contiene al menos un numero
def tiene_numero(texto):
    encontrado = False
    indice = 0
    while indice < len(texto) and encontrado == False:
        if texto[indice].isdigit():
            encontrado = True
        indice += 1
    return encontrado

# TODO: Función para verificar si el texto contiene caracteres especiales (@, #, !, $)
def tiene_especial(texto):
    encontrado = False
    especiales = "@#!$"
    indice = 0
    while indice < len(texto) and encontrado == False:
        if texto[indice] in especiales:
            encontrado = True
        indice += 1
    return encontrado

# TODO: Función para verificar si la longitud es correcta (minimo 8)
def tiene_longitud_valida(texto):
    return len(texto) >= 8

# ==========================================
# FUNCION PRINCIPAL DE LOGICA
# ==========================================

# TODO: Función para validar y reportar errores especificos
def validar_password(password):
    es_valida = True

    if not tiene_longitud_valida(password):
        print("Fallo: La contraseña debe tener al menos 8 caracteres")
        es_valida = False

    if not tiene_numero(password):
        print("Fallo: La contraseña debe incluir al menos un numero")
        es_valida = False

    if not tiene_especial(password):
        print("Fallo: La contraseña debe incluir un caracter especial (@, #, !, $)")
        es_valida = False

    if es_valida:
        print("Contraseña aceptada")
        return True
    else:
        print("Contraseña rechazada")
        return False