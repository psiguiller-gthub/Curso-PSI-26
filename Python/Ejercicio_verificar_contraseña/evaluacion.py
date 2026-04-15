from implementacion import validar_password


# ==========================================
# BLOQUE DE PRUEBAS Y EJECUCION
# ==========================================

def ejecutar_pruebas():
    # TODO: Prueba - Error múltiple (corta y sin numero)
    print("Prueba 1:")
    validar_password("abc@")

    # TODO: Prueba - Error de caracteres especiales
    print("\nPrueba 2:")
    validar_password("PasswordSegura123")

    # TODO: Prueba - Todo correcto
    print("\nPrueba 3:")
    validar_password("ClaveMaestra2026#")

# ==========================================
# PUNTO DE ENTRADA PRINCIPAL
# ==========================================

if __name__ == "__main__":
    ejecutar_pruebas()