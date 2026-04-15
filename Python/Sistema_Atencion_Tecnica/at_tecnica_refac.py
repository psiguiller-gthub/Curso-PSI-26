from enum import Enum
from typing import List, Optional

class Prioridad(Enum):
    ALTA = 1
    MEDIA = 2
    BAJA = 3

class Ticket:
    def __init__(self, id_ticket: int, descripcion: str, prioridad: Prioridad, usuario: str):
        self.id = id_ticket
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.usuario = usuario
        self.estado = "pendiente"
        self.tecnico_asignado: Optional[str] = None

    def __repr__(self):
        return f"[{self.prioridad.name}] Ticket {self.id}: {self.descripcion} ({self.estado})"

class Usuario:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def reportar_incidencia(self, descripcion: str, prioridad: Prioridad):
        # El usuario solo entrega los datos necesarios
        return {"descripcion": descripcion, "prioridad": prioridad, "usuario": self.nombre}

class Tecnico:
    def __init__(self, nombre: str, disponible: bool = True):
        self.nombre = nombre
        self.disponible = disponible
        self.ticket_actual: Optional[Ticket] = None

    def atender_ticket(self, ticket: Ticket) -> bool:
        if self.disponible and ticket.estado == "pendiente":
            ticket.estado = "en proceso"
            ticket.tecnico_asignado = self.nombre
            self.ticket_actual = ticket
            self.disponible = False
            print(f"-> Técnico {self.nombre} trabajando en ticket {ticket.id}")
            return True
        return False

    def cerrar_ticket(self) -> bool:
        if self.ticket_actual:
            print(f"-> Técnico {self.nombre} cerró el ticket {self.ticket_actual.id}")
            self.ticket_actual.estado = "cerrado"
            self.ticket_actual = None
            self.disponible = True
            return True
        return False

class SistemaSoporte:
    def __init__(self):
        self.tickets: List[Ticket] = []

    def crear_ticket(self, datos: dict):
        nuevo_ticket = Ticket(
            id_ticket=len(self.tickets) + 1,
            descripcion=datos["descripcion"],
            prioridad=datos["prioridad"],
            usuario=datos["usuario"]
        )
        self.tickets.append(nuevo_ticket)
        # Ordenamos por el valor numérico del Enum
        self.tickets.sort(key=lambda t: t.prioridad.value)
        return nuevo_ticket

    def obtener_siguiente_pendiente(self) -> Optional[Ticket]:
        return next((t for t in self.tickets if t.estado == "pendiente"), None)

# --- CASO DE USO ---

soporte = SistemaSoporte()

# Usuarios reportan
u1 = Usuario("Clotilde")
u2 = Usuario("Aniceto")

soporte.crear_ticket(u1.reportar_incidencia("No encuentro el ratón", Prioridad.BAJA))
soporte.crear_ticket(u2.reportar_incidencia("No puedo iniciar sesión", Prioridad.ALTA))

print("Tickets en sistema:", soporte.tickets)

# Gestión de técnicos
tecnicos = [Tecnico("Bonifacio", disponible=False), Tecnico("Escolastico")]

siguiente = soporte.obtener_siguiente_pendiente()

if siguiente:
    for tec in tecnicos:
        if tec.atender_ticket(siguiente):
            break
    else:
        print("No hay técnicos disponibles.")

# Finalización
tecnicos[1].cerrar_ticket()