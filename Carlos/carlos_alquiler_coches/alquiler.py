from datetime import date

class Alquiler:
    def __init__(self, id_alquiler: int, dni_cliente: str, id_agente: int, matricula_vehiculo: str, fecha_alquiler: date, fecha_devolucion: date) -> None:
        self._id_alquiler = id_alquiler
        self._dni_cliente = dni_cliente
        self._id_agente = id_agente
        self._matricula_vehiculo = matricula_vehiculo
        self._fecha_alquiler = fecha_alquiler
        self._fecha_devolucion = fecha_devolucion


    @property
    def id_alquiler(self) -> int:
        return self._id_alquiler
    
    @id_alquiler.setter
    def id_alquiler(self, id_alquiler: int) -> None:
        self._id_alquiler = id_alquiler


    @property
    def dni_cliente(self) -> int:
        return self._dni_cliente
    
    
    @dni_cliente.setter
    def dni_cliente(self, dni_cliente: int) -> None:
        self._dni_cliente = dni_cliente
        
    
    @property
    def id_agente(self) -> int:
        return self._id_agente
    

    @id_agente.setter
    def id_agente(self, id_agente: int):
        self._id_agente = id_agente

   
    @property
    def matricula_vehiculo(self) -> int:
        return self._matricula_vehiculo
    
    
    @matricula_vehiculo.setter
    def matricula_vehiculo(self, matricula_vehiculo: int) -> None:
        self._matricula_vehiculo = matricula_vehiculo


    @property
    def fecha_alquiler(self) -> date:
        return self._fecha_alquiler
    
    
    @fecha_alquiler.setter
    def fecha_alquiler(self, fecha_alquiler: date) -> None:
        self._fecha_alquiler = fecha_alquiler


    @property
    def fecha_devolucion(self) -> date:
        return self._fecha_devolucion
    
    
    @fecha_devolucion.setter
    def fecha_devolucion(self, fecha_devolucion: date) -> None:
        self._fecha_devolucion = fecha_devolucion


    def __str__(self) -> str:
        return f"Alquiler(ID: {self.id_alquiler}, Cliente: {self.dni_cliente}, Agente: {self.id_agente}, Vehículo: {self.matricula_vehiculo}, Fecha alquiler: {self.fecha_alquiler}, Fecha devolución: {self.fecha_devolucion})"
        
    