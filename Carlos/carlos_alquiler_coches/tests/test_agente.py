import pytest
from cliente import Cliente
from vehiculo import Vehiculo
from agente import Agente
from alquiler import Alquiler
from datetime import date

@pytest.fixture
def agente_de_prueba():
    return Agente(1, "Prueba")


@pytest.fixture
def cliente_sin_alquileres():
    return Cliente("12345678A", "Josefa", "josefa@example.com", "+34661335473")


@pytest.fixture
def cliente_con_un_alquiler():
    cliente = Cliente("12345678A", "Josefa", "josefa@example.com", "+34661335473")
    cliente.anyadir_alquiler_al_historial(Alquiler(1, "12345678A", 1, "1234", date.today(), date(2026, 4, 27)))
    
    return cliente


@pytest.fixture
def vehiculo_de_prueba():
    return Vehiculo("1234", "rojo", "Fiat", "modelazo")


@pytest.fixture
def vehiculo_no_disponible():
    return Vehiculo("1234", "rojo", "Fiat", "modelazo", True, False)


def test_constructor(agente_de_prueba):
    assert agente_de_prueba.nombre == "Prueba"
    assert agente_de_prueba.id_agente == 1
    

@pytest.mark.parametrize("vehiculo, resultado_esperado", [
    (Vehiculo(1, "t", "s", "n", False, True), True),
    (Vehiculo(1, "t", "s", "n", False, False), False),
    (Vehiculo(1, "t", "s", "n", False, True), True),
])
def test_consultar_disponibilidad(agente_de_prueba, vehiculo, resultado_esperado):
    assert agente_de_prueba.consultar_disponibilidad(vehiculo) == resultado_esperado
    

def test_crear_alquiler(capsys, agente_de_prueba, cliente_sin_alquileres, vehiculo_de_prueba):
    agente_de_prueba.crear_alquiler(1, cliente_sin_alquileres, vehiculo_de_prueba, date.today(), date(2026, 4, 27))
    assert len(cliente_sin_alquileres.historial) == 1
    assert vehiculo_de_prueba.disponible == False
    captured = capsys.readouterr()
    assert "Alquiler realizado" in captured.out
    

def test_crear_alquiler_de_vehiculo_no_disponible(capsys, agente_de_prueba, cliente_sin_alquileres, vehiculo_no_disponible):
    agente_de_prueba.crear_alquiler(1, cliente_sin_alquileres, vehiculo_no_disponible, date.today(), date(2026, 4, 27))
    captured = capsys.readouterr()
    assert "Vehículo no disponible" in captured.out
    

def test_devolver_vehiculo(agente_de_prueba, cliente_con_un_alquiler, vehiculo_no_disponible):
    agente_de_prueba.devolver_vehiculo(vehiculo_no_disponible, cliente_con_un_alquiler, date.today())
    assert cliente_con_un_alquiler.historial[0].fecha_devolucion == date.today()
    assert vehiculo_no_disponible.disponible == True