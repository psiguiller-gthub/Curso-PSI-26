import pytest
from alquiler import Alquiler
from datetime import date

@pytest.fixture
def alquiler_de_prueba():
    return Alquiler(1, "2", 3, "4", date.today(), date(2026, 4, 27))


def test_constructor(alquiler_de_prueba):
    assert alquiler_de_prueba.id_alquiler == 1
    assert alquiler_de_prueba.dni_cliente == "2"
    assert alquiler_de_prueba.id_agente == 3
    assert alquiler_de_prueba.matricula_vehiculo == "4"
    assert alquiler_de_prueba.fecha_alquiler == date.today()
    assert alquiler_de_prueba.fecha_devolucion == date(2026, 4, 27)
    

def test_str(capsys, alquiler_de_prueba):
    print(alquiler_de_prueba)
    captured = capsys.readouterr()
    assert str(alquiler_de_prueba) in captured.out