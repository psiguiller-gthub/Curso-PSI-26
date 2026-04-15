"""Contexto: Se requiere diseñar el núcleo lógico de un sistema de atención técnica para los 
empleados de una empresa. El sistema debe permitir que un usuario reporte una incidencia 
tecnológica con su equipo y que un técnico pueda gestionar, diagnosticar y resolver dicho problema.
Reglas de Negocio:
1. Registro de Incidencias: Para registrar un fallo, el usuario debe describir el problema, 
indicar la prioridad y vincular su código de empleado.
2. Generación de Tickets: Cada vez que se reporta un problema, el sistema debe crear un 
ticket de soporte único y asignarlo automáticamente a un técnico disponible.
3. Gestión y Actualización: El técnico encargado debe revisar la incidencia y actualizar el 
estado del ticket (por ejemplo, de "Pendiente" a "En progreso" o "Cerrado").
4. Cierre y Aviso: Una vez que el técnico logra solucionar la avería, debe cerrar el ticket, y el 
sistema tiene que notificar al usuario sobre la resolución.
"""



# ---------------- CLASES ----------------

class Usuario:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def reportar_incidencia(self, sistema, descripcion, prioridad):
        return sistema.registrar_incidencia(self, descripcion, prioridad)

    def consultar_estado(self, ticket):
        print("Estado del ticket", ticket.id, ":", ticket.estado)


class Tecnico:
    def __init__(self, nombre):
        self.nombre = nombre
        self.disponible = True

    def asignar_ticket(self, ticket):
        self.disponible = False
        ticket.tecnico = self
        print("Ticket", ticket.id, "asignado a", self.nombre)

    def revisar_incidencia(self, ticket):
        print(self.nombre, "revisando:", ticket.incidencia.descripcion)

    def diagnosticar_problema(self):
        print(self.nombre, "diagnosticando problema...")

    def actualizar_estado(self, ticket, estado):
        ticket.estado = estado
        print("Ticket", ticket.id, "->", estado)

    def resolver_incidencia(self, ticket):
        print(self.nombre, "resolviendo incidencia...")
        self.actualizar_estado(ticket, "CERRADO")
        self.disponible = True


class Incidencia:
    def __init__(self, descripcion, prioridad, usuario):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.usuario = usuario
        self.codigo_empleado = usuario.codigo  # vínculo con empleado


class Ticket:
    contador = 1      # genera numero de ticket

    def __init__(self, incidencia):
        self.id = Ticket.contador
        Ticket.contador += 1
        self.incidencia = incidencia
        self.estado = "PENDIENTE"
        self.tecnico = None


class Notificacion:
    def enviar(self, usuario, mensaje):
        print("Notificación para", usuario.nombre + ":", mensaje)


class SistemaHelpdesk:
    def __init__(self):
        self.tickets = []
        self.tecnicos = []
        self.notificador = Notificacion()

    def agregar_tecnico(self, tecnico):
        self.tecnicos.append(tecnico)

    def registrar_incidencia(self, usuario, descripcion, prioridad):
        incidencia = Incidencia(descripcion, prioridad, usuario)
        ticket = Ticket(incidencia)

        self.tickets.append(ticket)

        print("Ticket", ticket.id, "creado")
        print("Empleado:", incidencia.codigo_empleado)  

        self.asignar_tecnico(ticket)
        return ticket

    def asignar_tecnico(self, ticket):
        for tecnico in self.tecnicos:
            if tecnico.disponible:
                tecnico.asignar_ticket(ticket)
                return
        print("No hay técnicos disponibles")

    def notificar_usuario(self, ticket):
        mensaje = "Tu incidencia ha sido resuelta (Ticket " + str(ticket.id) + ")"
        self.notificador.enviar(ticket.incidencia.usuario, mensaje)


# ---------------- PRUEBAS ----------------

sistema = SistemaHelpdesk()

# Técnicos
t1 = Tecnico("Juan")
t2 = Tecnico("Marta")

sistema.agregar_tecnico(t1)
sistema.agregar_tecnico(t2)

# Usuario
usuario = Usuario("EMP001", "Juan")

# Crear incidencia
ticket = usuario.reportar_incidencia(
    sistema,
    "Error login usuario",
    "ALTA"
)

# Trabajo del técnico
tecnico = ticket.tecnico
tecnico.revisar_incidencia(ticket)
tecnico.diagnosticar_problema()
tecnico.actualizar_estado(ticket, "EN PROGRESO")
tecnico.resolver_incidencia(ticket)

# Notificación
sistema.notificar_usuario(ticket)

# Consultar estado
usuario.consultar_estado(ticket)
