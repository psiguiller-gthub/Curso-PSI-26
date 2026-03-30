class Vehiculo:
    def __init__(self, matricula: str, color: str, marca: str, modelo: str, automatico: bool = False, disponible: bool = True) -> None:
        self._matricula = matricula
        self._color = color
        self._marca = marca
        self._modelo = modelo
        self._automatico = automatico
        self._disponible = disponible
    

    @property
    def matricula(self) -> str:
        return self._matricula
    
    
    @matricula.setter
    def matricula(self, matricula: str) -> None:
        self._matricula = matricula

    
    @property
    def color(self) -> str:
        return self._color
    
    
    @color.setter
    def color(self, color: str) -> None:
        self._color = color

    
    @property
    def marca(self) -> str:
        return self._marca
    
    
    @marca.setter
    def marca(self, marca: str) -> None:
        self._marca = marca

    
    @property
    def modelo(self) -> str:
        return self._modelo
    
    
    @modelo.setter
    def modelo(self, modelo: str) -> None:
        self._modelo = modelo

    
    @property
    def automatico(self) -> bool:
        return self._automatico
    
    
    @automatico.setter
    def automatico(self, automatico: bool) -> None:
        self._automatico = automatico
        
    
    @property
    def disponible(self) -> bool:
        return self._disponible
    
    
    @disponible.setter
    def disponible(self, disponible: bool) -> None:
        self._disponible = disponible
        
    
    def __str__(self) -> str:
        tipo_cambio = "Automático" if self._automatico else "Manual"
        estado = "Disponible" if self._disponible else "No disponible"

        return ("- Marca: {self.marca} | Modelo: {self.modelo} | Color: {self.color} | Matrícula: {self.matriucula} | Tipo: {tipo_cambio} | Estado: {estado}")