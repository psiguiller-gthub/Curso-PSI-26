import Tecnico
from Usuario import Usuario


class Ticket:
    """
        representa una incidencia del usuario que a avierto un ticket

    """
    def __init__(self, id: int, usuario: Usuario, tecnico: Tecnico, descripcion: str, prioridad: int, estado: int = 3):
        """

        Args:
            id (int): Id del ticket
            usuario (Usuario): usuario que reporta la incidencia
            tecnico (Tecnico): tecnico asignado
            descripcion (str): descripcion que el usuario a aportado
            prioridad (int): prioridad de resolucion para el tecnico
            estado (int, optional): estado del ticket: 3=Pendiente, 2=En progreso, 1=Cerrado. Defaults to 3.
        """
        self.id = id
        self.usuario = usuario
        self.tecnico = tecnico
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.estado = estado # 3=Pendiente, 2=En progreso, 1=Cerrado