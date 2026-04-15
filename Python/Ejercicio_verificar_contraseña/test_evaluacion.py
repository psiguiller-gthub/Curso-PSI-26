import pytest
import csv
from implementacion import validar_password

# Función para leer los datos del CSV y devolver una lista de tuplas
def cargar_datos_csv():
    datos = []
    with open('datos_prueba.csv', mode='r', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            # Convertimos el string 'True'/'False' a booleano real
            esperado = fila['resultado_esperado'] == 'True'
            datos.append((fila['password'], esperado))
    return datos

# ==========================================
# PRUEBAS PARAMETRIZADAS
# ==========================================

# Usar parametrize para ejecutar la prueba por cada fila del CSV
@pytest.mark.parametrize("password, resultado_esperado", cargar_datos_csv())
def test_validar_password_csv(password, resultado_esperado):
    # La prueba pasa si el resultado de la función coincide con el esperado
    assert validar_password(password) == resultado_esperado