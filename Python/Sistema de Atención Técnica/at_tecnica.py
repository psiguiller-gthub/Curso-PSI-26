class Usuario:
    def __init__(self, id_usuario, descripcion_incidencia, prioridad):
        self.id_usuario = id_usuario
        self.descripcion_incidencia = descripcion_incidencia
        self.prioridad = prioridad

    def crear_incidencia(self, id_usuario, descripcion_incidencia, prioridad):
        return id_usuario, descripcion_incidencia, prioridad

class Tecnico:
    def __init__(self, id_tecnico, disponibilidad, descripcion_incidencia):
        self.id_tecnico = id_tecnico
        self.disponibilidad = disponibilidad
        self.descripcion_incidencia = descripcion_incidencia

class AtencionTecnica:
    def __init__(self):
        self.tickets = []

    def crear_ticket(self, descripcion):
        ticket = {"id": len(self.tickets) + 1, "descripcion": descripcion, "estado": "abierto"}
        self.tickets.append(ticket)
        return ticket
    
    def estado_ticket(self, ticket_id):
        for ticket in self.tickets:
            if ticket["id"] == ticket_id:
                return ticket["estado"]
        return None

    def cerrar_ticket(self, ticket_id):
        for ticket in self.tickets:
            if ticket["id"] == ticket_id:
                ticket["estado"] = "cerrado"
                return ticket
        return None

    def listar_tickets(self):
        return self.tickets

# CASOS DE USO

incidencia1 = "No puedo acceder a mi correo electrónico."
usuario1 = Usuario(1, incidencia1, "alta")
atencion = AtencionTecnica()
ticket1 = atencion.crear_ticket(usuario1.descripcion_incidencia)
print(f"Ticket creado: {ticket1}")