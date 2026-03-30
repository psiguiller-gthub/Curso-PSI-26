from alquiler import Alquiler
from cliente import Cliente
from vehiculo import Vehiculo
from datetime import date

class Agente:
    def __init__(self, id_agente: int, nombre: str) -> None:
        self._id_agente = id_agente
        self._nombre = nombre
        
        
    @property
    def id_agente(self) -> int:
        return self._id_agente
    
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre


    def consultar_disponibilidad(self, vehiculo) -> bool:
        return vehiculo.disponible
    
    
    def crear_alquiler(self, id_alquiler: int, cliente: Cliente, vehiculo: Vehiculo, fecha_alquiler: date, fecha_devolucion: date) -> str:
        if not self.consultar_disponibilidad(vehiculo):
            print("Vehículo no disponible")
        else:
            alquiler = Alquiler(id_alquiler, cliente.dni, self.id_agente, vehiculo.matricula, fecha_alquiler, fecha_devolucion)
            cliente.historial.append(alquiler)
            vehiculo.disponible = False
            print("Alquiler realizado")


    def devolver_vehiculo(self, vehiculo: Vehiculo, cliente: Cliente, fecha_devolucion: date):
        for alquiler in cliente.historial:
            if alquiler.matricula_vehiculo == vehiculo.matricula:
                alquiler.fecha_devolucion = fecha_devolucion
                vehiculo.disponible = True