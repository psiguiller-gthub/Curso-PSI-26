class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre        

    def crear_incidencia(self, descripcion_incidencia, prioridad):
# El usuario solo entrega los datos necesarios para crear el ticket, sin preocuparse por el estado o el técnico asignado
        return {'descripcion': descripcion_incidencia, 'prioridad': prioridad, 'usuario': self.nombre}

class Ticket:
    def __init__(self, id_ticket, datos_incidencia):
        self.id_ticket = id_ticket
        self.descripcion = datos_incidencia['descripcion']
        self.prioridad = datos_incidencia['prioridad']
        self.usuario = datos_incidencia['usuario']
        self.estado = 'pendiente'
        self.tecnico_asignado = None

class Tecnico:
    def __init__(self, id_tecnico, nombre, disponible):
        self.id_tecnico = id_tecnico
        self.nombre = nombre
        self.disponible = disponible
        self.ticket_tecnico = None # Para saber el ticket asignado al técnico
        
    def atender_ticket(self, ticket):
# Verificar el estado del ticket antes de asignarlo al técnico
# Asignar el ticket al técnico, asignar estado "en proceso" y al técnico como NO disponible        
        if self.disponible and ticket.estado == 'pendiente':
            ticket.estado = 'en proceso'
            ticket.tecnico_asignado = self.nombre
            self.ticket_tecnico = ticket # Guardamos el ticket asignado al técnico
            self.disponible = False
            print(f"Técnico {self.nombre} está trabajando en el ticket -> {ticket.id_ticket}")
            return True
        return False
    
    def cerrar_ticket(self):
        if self.ticket_tecnico and self.ticket_tecnico.estado == 'en proceso':
            self.ticket_tecnico.estado = 'cerrado'
            print(f"Técnico {self.nombre} ha cerrado el ticket -> {self.ticket_tecnico.id_ticket}")
            self.ticket_tecnico = None # Liberamos el ticket del técnico
            self.disponible = True # El técnico vuelve a estar disponible
            return True
        return False
    
class AtencionTecnica:
    def __init__(self):
        self.tickets = []
        self.prioridad = {'alta': 1, 'media': 2, 'baja': 3}

    def crear_ticket(self, datos_incidencia):
        id_ticket = len(self.tickets) + 1
        ticket = Ticket(id_ticket, datos_incidencia)
        self.tickets.append(ticket)
    # Ordenar los tickets por prioridad cada vez que se crea uno nuevo
        self.tickets.sort(key=lambda x: self.prioridad.get(x.prioridad, 3))
        return ticket
    """Esta línea es el "motor de búsqueda" que decide qué ticket es más importante. Básicamente, 
le dice a Python: "No ordenes alfabéticamente, ordena usando estos valores numéricos".
Aquí el desglose paso a paso:
.sort(): Es una función de Python que ordena la lista de tickets "in-place" (modifica la lista original directamente).
key=: Aquí defines el criterio de ordenación. Le dices a Python: "Antes de comparar dos tickets, pásalos por esta regla".
lambda x:: Es una función anónima rápida. La x representa a cada ticket (diccionario) que está dentro de la lista.
self.niveles.get(x['prioridad'], 3):
Busca en el diccionario niveles (que definimos como {"alta": 1, "media": 2, "baja": 3}).
Mira la "prioridad" del ticket actual (x).
El truco: Si el ticket es "alta", devuelve un 1. Si es "baja", devuelve un 3.
El , 3 final es un valor por defecto: si alguien escribe mal la prioridad (ej. "urgente"), 
el sistema le asigna un 3 (prioridad baja) para que no rompa el código.
En resumen:
Python ve una lista de diccionarios, pero gracias a esa línea, los ve como una lista de números (1, 2 o 3). 
Como el 1 es menor que el 3, los tickets de prioridad "alta" (valor 1) se mueven automáticamente al principio de la lista.
"""            
    def obtener_siguiente_ticket(self):
    # Busca el siguiente ticket pendiente (el de mayor prioridad) y lo devuelve
        for ticket in self.tickets:
            if ticket.estado == 'pendiente':
                return ticket
        return None
    #   return next((t for t in self.tickets if t.estado == "pendiente"), None)"""REFACTORIZADO: Esta línea hace exactamente lo mismo que el bucle for, pero de una forma más compacta y elegante.
    #   next(): Es una función que devuelve el siguiente elemento de un iterador. En este caso, el iterador es la lista de tickets filtrada por la condición."

    def listar_tickets(self):
        print("Tickets creados:")
        for ticket in self.tickets:
            print(f"{ticket.id_ticket}: {ticket.descripcion} (Prioridad: {ticket.prioridad})")
        return self.tickets
    # Para que liste todos los tickets, el return tiene que estar fuera del bucle for. Si lo ponemos dentro, el buclese detendría después de la primera iteración.

# CASOS DE USO

atencion = AtencionTecnica()

# Crear un usuarios y reportar incidencias
usuario1 = Usuario(1, "Clotilde")
usuario2 = Usuario(2, "Aniceto")

# Crear un ticket para las incidencias de los usuarios
atencion.crear_ticket(usuario1.crear_incidencia("No encuentro el ratón.", "baja"))
atencion.crear_ticket(usuario2.crear_incidencia("No puedo iniciar sesión.", "alta"))

# Listar los tickets antes de obtener alguno (ordenados por prioridad)
atencion.listar_tickets()

# Crear técnicos y asignar disponibilidad
tecnico1 = Tecnico(1, "Bonifacio", False)
tecnico2 = Tecnico(2, "Escolastico", True) # El técnico está disponible para atender el ticket
tecnicos = [tecnico1, tecnico2]

# Obtener el siguiente ticket a atender (el de mayor prioridad)
# Saldrá el de Aniceto con prioridad "alta" aunque entró después del de Bonifacia.
siguiente_ticket = atencion.obtener_siguiente_ticket()
print(f"\n Siguiente ticket a atender: {siguiente_ticket.id_ticket}: {siguiente_ticket.descripcion} (Prioridad: {siguiente_ticket.prioridad})")

# En la función atender_ticket:
# Verificar el estado del ticket antes de asignarlo al técnico
# Asignar el ticket al técnico, asignar estado "en proceso" y al técnico como NO disponible

#tecnico2.atender_ticket(siguiente_ticket)
print(f"\nEl técnico {tecnico2.nombre} ha sido asignado al ticket {siguiente_ticket.id_ticket} que está {siguiente_ticket.estado}")

# Buscar técnico disponible para atender el siguiente ticket (si hay alguno pendiente)
if siguiente_ticket:
    print(f"Siguiente ticket pendiente: #{siguiente_ticket.id_ticket} ({siguiente_ticket.prioridad})")
    asignado = False
    for tecnico in tecnicos:
        if tecnico.disponible:
            tecnico.atender_ticket(siguiente_ticket)
            asignado = True
            break # Importante: dejamos de buscar técnicos
    else:
        if not asignado:
            print("\nNo hay técnicos disponibles para atender el siguiente ticket.")
else:
    print("\nNo hay tickets pendientes para asignar.")


# Verificamos el resultado
print(f"\nEstado final del ticket: {siguiente_ticket.estado}")
if siguiente_ticket.tecnico_asignado:
    print(f"Atendido por: {siguiente_ticket.tecnico_asignado}")    

# Cerrar el ticket después de resolver la incidencia
print("\n--- Resolviendo incidencia... ---")
tecnicos[1].cerrar_ticket()

# 5. VERIFICACIÓN FINAL
print(f"Estado final del ticket: {siguiente_ticket.estado}")
print(f"¿Está {tecnicos[1].nombre} disponible para un nuevo ticket?: {tecnicos[1].disponible}") # Saldrá True