import pytest
from cliente import Cliente
from alquiler import Alquiler
from vehiculo import Vehiculo
from datetime import date

@pytest.fixture
def catalogo_de_prueba_con_dos_coches():
    return [
        Vehiculo("coche1", "d", "l", "d"),
        Vehiculo("coche2", "d", "l", "d"),
    ]


@pytest.fixture
def cliente_sin_alquileres():
    return Cliente("12345678A", "Josefa", "josefa@example.com", "+34661335473")


@pytest.fixture
def cliente_con_dos_alquileres():
    cliente = Cliente("12345678A", "Josefa", "josefa@example.com", "+34661335473")
    cliente.anyadir_alquiler_al_historial(Alquiler(1, "12345678A", 1, "1", date.today(), date(2026, 4, 27)))
    cliente.anyadir_alquiler_al_historial(Alquiler(2, "12345678A", 1, "1", date.today(), date(2026, 4, 27)))
    
    return cliente

@pytest.fixture
def alquileres_de_prueba():
       return [
           Alquiler(1, "12345678A", 1, "1", date.today(), date(2026, 4, 27)),
           Alquiler(2, "12345678A", 1, "1", date.today(), date(2026, 4, 27))
        ] 


def test_constructor(cliente_sin_alquileres):
    assert cliente_sin_alquileres.dni == "12345678A"
    assert cliente_sin_alquileres.nombre == "Josefa"
    assert cliente_sin_alquileres.email == "josefa@example.com"
    assert cliente_sin_alquileres.telefono == "+34661335473"
    assert len(cliente_sin_alquileres.historial) == 0


def test_anyadir_alquiler_al_historial(cliente_sin_alquileres, alquileres_de_prueba):
    cliente_sin_alquileres.anyadir_alquiler_al_historial(alquileres_de_prueba[0])
    assert len(cliente_sin_alquileres.historial) == 1
    cliente_sin_alquileres.anyadir_alquiler_al_historial(alquileres_de_prueba[1])
    assert len(cliente_sin_alquileres.historial) == 2
    

def test_listar_historial(capsys, cliente_con_dos_alquileres):
    cliente_con_dos_alquileres.listar_historial()
    captured = capsys.readouterr()
    assert str(cliente_con_dos_alquileres.historial[0]) in captured.out
    assert str(cliente_con_dos_alquileres.historial[1]) in captured.out
    

def test_consultar_catalogo(capsys, cliente_sin_alquileres, catalogo_de_prueba_con_dos_coches):
    cliente_sin_alquileres.consultar_catalogo(catalogo_de_prueba_con_dos_coches)
    captured = capsys.readouterr()
    assert str(catalogo_de_prueba_con_dos_coches[0]) in captured.out
    assert str(catalogo_de_prueba_con_dos_coches[1]) in captured.out