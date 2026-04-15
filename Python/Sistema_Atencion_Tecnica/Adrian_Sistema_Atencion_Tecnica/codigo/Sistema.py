from Tecnico import Tecnico
from Ticket import Ticket
from Usuario import Usuario


class Sistema:
    """clase principal del codigo, vincula y gestiona que un usuario 
        genere un ticket y asigna un tecnico generado a ese ticket
    """

    def crear_ticket(self, id_ticket: int, usuario: Usuario, descripcion: str, prioridad: int, lista_Tecnicos) -> Ticket:
        """ Crea un ticket con los parametros dados (ver clase ticket)

        Args:
            id_ticket (int): ID del ticket generado
            usuario (Usuario): Usuario que genera el reporte
            descripcion (str): descripcion del reporte
            prioridad (int): priodirad de reparacion (para el tecnico)
            lista_Tecnicos: listado de tecnicos disponibles 
            
        Returns:
            Ticket:
        """
        tecnico = self._buscar_tecnico_disponible(lista_Tecnicos)
        ticket = Ticket(id_ticket, usuario, tecnico, descripcion, prioridad)
        tecnico.ticket_asignado = ticket
        print(f"Asignado ticket ID: {ticket.id}, a Tecnico ID: {ticket.tecnico.id}")
        return ticket

    def actualizar_estado_ticket(self, tecnico: Tecnico, nuevo_estado: int):
        """
            El tecnico actualiza el estado de su ticket adjunto

        Args:
            tecnico (Tecnico):
            nuevo_estado (int): ver clase Ticket
        """
        tecnico.ticket_asignado.estado = nuevo_estado

    def cerrar_ticket(self, ticket: Ticket):
        """
            Pone el estado del ticket a cerrado, desacopla al tecnico del ticket y notifica al usuario
            El ticket guardara el tecnico que lo ha cerrado

        Args:
            ticket (Ticket):
        """

        ticket.estado = 1 #cerrado
        ticket.tecnico.ticket_asignado = None
        print(f"Cerrado ticket ID: {ticket.id}, a Tecnico ID: {ticket.tecnico.id}")
        ticket.usuario.recibir_notificacion_cierre_ticket(f"Ticket ID: {ticket.id} cerrado")

    def _buscar_tecnico_disponible(self, lista_tecnicos) -> Tecnico:
        """
        Busca el primer tecnico que no tenga un ticket asignado de lista_tecnicos

        Args:
            lista_tecnicos (Tecnico[]):

        Returns:
            Tecnico o none
        """
        encontrado = None
        for tecnico in lista_tecnicos:
            if tecnico.ticket_asignado == None:
                encontrado = tecnico
                break
        return encontrado