import Ticket

class Tecnico:
    """
        Representa un tecnico con un id y
        ticket asignado por defecto en none
    """

    def __init__(self, id: int):
        """
        Args:
            id (int): ID del tecnico
        """
        self.id = id
        self.ticket_asignado = None

        
    def asginar_ticket(self, ticket: Ticket):
        """
            Asigna el ticket al tecnico

        Args:
            ticket (ticket): ticket a asigar
        """
        self.ticket_asignado = ticket