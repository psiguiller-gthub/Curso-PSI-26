# Definición de la clase para los empleados que piden ayuda
class Usuario:
    def __init__(self, id_empleado, nombre):
        self.id_empleado = id_empleado  # Guarda el código único del empleado
        self.nombre = nombre            # Guarda el nombre del empleado

# Definición de la clase para el personal de soporte
class Tecnico:
    def __init__(self, nombre):
        self.nombre = nombre            # Guarda el nombre del técnico
        self.disponible = True          # Estado inicial: libre para trabajar

 # Método para cambiar el estado de disponibilidad (True/False)
    def cambiar_disponibilidad(self, estado):
        self.disponible = estado

# Clase que representa el documento del problema técnico
class Ticket:
    def __init__(self, id_ticket, usuario, descripcion, prioridad):
        self.id_ticket = id_ticket      # ID único generado por el sistema
        self.usuario = usuario          # Objeto Usuario que reporta
        self.descripcion = descripcion  # Texto con el problema
        self.prioridad = prioridad      # Nivel: Alta, Media o Baja
        self.estado = "Pendiente"       # Estado inicial por defecto
        self.tecnico = None             # Al inicio no tiene técnico asignado

 # Método simple para cambiar el estado del ticket
    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

# Clase principal que actúa como "Cerebro" o Núcleo del sistema
class Sistema:
    def __init__(self):
        self.tickets = []               # Lista para almacenar todos los tickets creados
        self.tecnicos = []              # Lista de técnicos registrados en el sistema
        self.contador_ids = 1           # Contador para asegurar que cada ID sea único

    # Método para recibir un reporte y crear el objeto Ticket
    def registrar_ticket(self, usuario, descripcion, prioridad):
        # Crea una nueva instancia de Ticket usando el contador actual
        nuevo_ticket = Ticket(self.contador_ids, usuario, descripcion, prioridad)
        self.tickets.append(nuevo_ticket) # Guarda el ticket en la lista global
        self.contador_ids += 1           # Incrementa el contador para el próximo ticket
        self.gestionar_asignacion(nuevo_ticket) # Llama al proceso de asignación

    # Función especializada en buscar un técnico libre (Responsabilidad Única)
    def buscar_tecnico_libre(self):
        tecnico_libre = None            # Variable auxiliar para el resultado
        for tecnico in self.tecnicos:   # Recorre la lista de técnicos
            # Si está libre y aún no hemos encontrado uno, lo seleccionamos
            if tecnico.disponible and tecnico_libre is None:
                tecnico_libre = tecnico
        return tecnico_libre            # Devuelve el objeto técnico o None

    # Método para vincular el ticket con un técnico disponible
    def gestionar_asignacion(self, ticket):
        tecnico = self.buscar_tecnico_libre() # Pide un técnico a la función de búsqueda
        if tecnico:                     # Si encontró a alguien (no es None)
            ticket.tecnico = tecnico    # Vincula el técnico al ticket
            tecnico.cambiar_disponibilidad(False) # Marca al técnico como ocupado
            print(f"Ticket {ticket.id_ticket} asignado a {tecnico.nombre}")
        else:                           # Si no había nadie libre
            print("Aviso: No hay técnicos disponibles.")

    # Método para finalizar el proceso de un ticket
    def resolver_ticket(self, ticket):
        ticket.actualizar_estado("Cerrado") # Cambia el estado a resolución
        if ticket.tecnico:                  # Si el ticket tenía un técnico
            ticket.tecnico.cambiar_disponibilidad(True) # Libera al técnico
        self.enviar_notificacion(ticket)    # Dispara el aviso al usuario

    # Método para comunicar la resolución (Regla de negocio 4)
    def enviar_notificacion(self, ticket):
        print(f"NOTIFICACIÓN a {ticket.usuario.nombre}: Su caso '{ticket.descripcion}' está {ticket.estado}.")
        
        
# --- 1. PREPARACIÓN DE DATOS (ARRAYS/LISTAS) ---

# Creamos la instancia del cerebro del sistema
soporte_it = Sistema()

# Lista de Usuarios (Clientes/Empleados)
usuarios_db = [
    Usuario(101, "Ana García"),
    Usuario(102, "Roberto Soler"),
    Usuario(103, "Lucía Méndez"),
    Usuario(104, "Marcos Peña")
]

# Lista de Técnicos (Personal de soporte)
# Estos los añadimos directamente al sistema
tecnicos_iniciales = [
    Tecnico("Elena"),
    Tecnico("Carlos")
]
soporte_it.tecnicos.extend(tecnicos_iniciales)

# --- 2. PRUEBA DE FUNCIONAMIENTO ---

print("--- FASE 1: Registro de Tickets ---")
# Registramos 3 tickets (Elena y Carlos se ocuparán, el 3º quedará en aviso)
soporte_it.registrar_ticket(usuarios_db[0], "Error en Outlook", "Media")
soporte_it.registrar_ticket(usuarios_db[1], "Pantalla azul", "Alta")
soporte_it.registrar_ticket(usuarios_db[2], "Teclado no funciona", "Baja")

print("\n--- FASE 2: Resolución y Liberación ---")
# Vamos a resolver el ticket 1 para que Elena quede libre
ticket_a_resolver = soporte_it.tickets[0]
soporte_it.resolver_ticket(ticket_a_resolver)

print("\n--- FASE 3: Re-asignación ---")
# Ahora que Elena está libre, intentamos asignar el ticket que quedó pendiente
# (En este código simple, lo hacemos registrando uno nuevo o re-procesando)
soporte_it.registrar_ticket(usuarios_db[3], "Configurar VPN", "Alta")
