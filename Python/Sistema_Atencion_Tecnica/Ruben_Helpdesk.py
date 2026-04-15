""" Se requiere diseñar el núcleo lógico de un sistema de atención técnica para los empleados
de una empresa. El sistema debe permitir que un usuario reporte una incidencia tecnológica 
con su equipo y que un técnico pueda gestionar, diagnosticar y resolver dicho problema.

Reglas de Negocio:

1. Registro de Incidencias: Para registrar un fallo, el usuario debe describir el problema,
indicar la prioridad y vincular su código de empleado.

2. Generación de Tickets: Cada vez que se reporta un problema, el sistema debe crear un
ticket de soporte único y asignarlo automáticamente a un técnico disponible.

 3. Gestión y Actualización: El técnico encargado debe revisar la incidencia y actualizar el
estado del ticket (por ejemplo, de "Pendiente" a "En progreso" o "Cerrado").

4. Cierre y Aviso: Una vez que el técnico logra solucionar la avería, debe cerrar el ticket, y el
sistema tiene que notificar al usuario sobre la resolución."""

import uuid

class Ticket:
    """Representa una incidencia técnica en el sistema."""
    def __init__(self, descripcion, prioridad, codigo_empleado):
        self.id = str(uuid.uuid4())[:8]  # Generación de ID único corto
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.codigo_empleado = codigo_empleado
        self.estado = "Pendiente"
        self.tecnico_asignado = None

    def __str__(self):
        tecnico = self.tecnico_asignado.nombre if self.tecnico_asignado else "Sin asignar"
        return f"[Ticket {self.id}] Estado: {self.estado} | Prioridad: {self.prioridad} | Técnico: {tecnico}"

class Tecnico:
    """Representa a un técnico de soporte."""
    def __init__(self, id_tecnico, nombre):
        self.id_tecnico = id_tecnico
        self.nombre = nombre
        self.esta_disponible = True

class HelpdeskSystem:
    """Gestor principal de incidencias y técnicos."""
    def __init__(self):
        self.tickets = {}
        self.tecnicos = []

    def agregar_tecnico(self, tecnico):
        """Registra un técnico en el sistema."""
        self.tecnicos.append(tecnico)

    def registrar_incidencia(self, descripcion, prioridad, codigo_empleado):
        """Regla 1 y 2: Registra el problema y asigna un técnico automáticamente."""
        nuevo_ticket = Ticket(descripcion, prioridad, codigo_empleado)
        
        # Buscar primer técnico disponible
        tecnico_libre = next((t for t in self.tecnicos if t.esta_disponible), None)
        
        if tecnico_libre:
            nuevo_ticket.tecnico_asignado = tecnico_libre
            nuevo_ticket.estado = "En progreso"
            tecnico_libre.esta_disponible = False
            print(f"Sistema: Ticket {nuevo_ticket.id} asignado a {tecnico_libre.nombre}.")
        else:
            print(f"Sistema: Ticket {nuevo_ticket.id} creado, pero no hay técnicos disponibles.")

        self.tickets[nuevo_ticket.id] = nuevo_ticket
        return nuevo_ticket.id

    def actualizar_estado(self, ticket_id, nuevo_estado):
        """Regla 3 y 4: Gestión de estados y cierre con aviso."""
        if ticket_id not in self.tickets:
            print("Error: El ticket no existe.")
            return

        ticket = self.tickets[ticket_id]
        ticket.estado = nuevo_estado
        print(f"Sistema: El ticket {ticket_id} ha cambiado a '{nuevo_estado}'.")

        if nuevo_estado.lower() == "cerrado":
            self._finalizar_ticket(ticket)

    def _finalizar_ticket(self, ticket):
        """Maneja la liberación del técnico y la notificación al usuario."""
        if ticket.tecnico_asignado:
            ticket.tecnico_asignado.esta_disponible = True
        
        # Regla 4: Notificar al usuario
        self._notificar_usuario(ticket)

    def _notificar_usuario(self, ticket):
        print(f"NOTIFICACIÓN PARA EMPLEADO {ticket.codigo_empleado}: "
              f"Su incidencia '{ticket.descripcion}' ha sido RESUELTA.")

# Ejemplo de uso:
if __name__ == "__main__":
    # Inicializar sistema
    soporte = HelpdeskSystem()
    
    # Agregar técnicos
    soporte.agregar_tecnico(Tecnico("T1", "Ramón García"))
    soporte.agregar_tecnico(Tecnico("T2", "Ana López"))

    # 1 y 2. Registrar incidencias
    id_t1 = soporte.registrar_incidencia("La pantalla no enciende", "Alta", "EMP123")
    id_t2 = soporte.registrar_incidencia("Teclado pegajoso", "Baja", "EMP456")

    # 3. Actualizar estado
    soporte.actualizar_estado(id_t1, "En progreso")
    
    # 4. Cerrar y avisar
    soporte.actualizar_estado(id_t1, "Cerrado")
    
    # Ver estado actual del segundo ticket
    print(soporte.tickets[id_t2])
