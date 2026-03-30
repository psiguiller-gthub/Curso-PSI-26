from alquiler import Alquiler
from vehiculo import Vehiculo

class Cliente:
    def __init__(self, dni: str, nombre: str, email: str, telefono: str):
        self._dni = dni
        self._nombre = nombre
        self._email = email
        self._telefono = telefono
        self._historial = []

    
    @property
    def dni(self) -> str:
        return self._dni

   
    @property
    def nombre(self) -> str:
        return self._nombre
    
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre

    
    @property
    def email(self) -> str:
        return self._email
    
    
    @email.setter
    def email(self, email: str) -> None:
        self._email = email

    
    @property
    def telefono(self) -> str:
        return self._telefono
    
    
    @telefono.setter
    def telefono(self, telefono: str) -> None:
        self._telefono = telefono


    @property
    def historial(self) -> list:
        return self._historial
    
    
    def anyadir_alquiler_al_historial(self, alquiler: Alquiler) -> None:
        self._historial.append(alquiler)
        
    
    def listar_historial(self):
        for alquiler in self.historial:
            print(alquiler)
    
    
    def consultar_catalogo(self, lista_vehiculos: list[Vehiculo]) -> str:
        for vehiculo in lista_vehiculos:
            print(vehiculo)