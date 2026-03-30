import pytest
from vehiculo import Vehiculo

@pytest.fixture
def vehiculo_de_prueba():
    return Vehiculo("123", "rojo", "Fiat", "modelazo")


@pytest.fixture
def vehiculo_automatico_no_disponible():
    return Vehiculo("123", "rojo", "Fiat", "modelazo", True, False)


def test_constructor(vehiculo_de_prueba):
    assert vehiculo_de_prueba.matricula == "123"
    assert vehiculo_de_prueba.color == "rojo"
    assert vehiculo_de_prueba.marca == "Fiat"
    assert vehiculo_de_prueba.modelo == "modelazo"
    assert vehiculo_de_prueba.automatico == False
    assert vehiculo_de_prueba.disponible == True
    

def test_automatico_y_disponible_como_parametros(vehiculo_automatico_no_disponible):
    assert vehiculo_automatico_no_disponible.automatico == True
    assert vehiculo_automatico_no_disponible.disponible == False
    

def test_str(capsys, vehiculo_de_prueba):
    print(vehiculo_de_prueba)
    captured = capsys.readouterr()
    assert str(vehiculo_de_prueba) in captured.out