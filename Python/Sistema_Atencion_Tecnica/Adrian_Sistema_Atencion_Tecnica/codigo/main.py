from Tecnico import Tecnico
from Ticket import Ticket
from Usuario import Usuario
from Sistema import Sistema


#funcion para imprimir los datos del ticket, mover a clase
#Ticket si conviene
def imprimir_datos_ticket(ticket: Ticket):
    print(f"Ticket ID: \t{ticket.id}")
    print(f"\t Usuario: \t{ticket.usuario.id}")
    print(f"\t Tecnico: \t{ticket.tecnico.id}")
    print(f"\t Descripcion: \t{ticket.descripcion}")
    print(f"\t Prioridad: \t{ticket.prioridad}")
    print(f"\t Estado: \t{ticket.estado}")

def imrpimir_datos_tecnico(tecnico: Tecnico):
    print(f"Datos del tecnico: {tecnico.id}")
    if tecnico.ticket_asignado != None:
        print(f"Tiene un ticket asignado:")
        imprimir_datos_ticket(tecnico.ticket_asignado)
    else:
        print(f"\tNo Hay Ticket asignado:")


usuario1 = Usuario(1)
usuario2 = Usuario(2)

tecnico1 = Tecnico(1)
tecnico2 = Tecnico(2)
listado_tecnicos = [tecnico1, tecnico2]


helpDesk = Sistema()


#caso normal

#usuario reporta incidencia
ticket = helpDesk.crear_ticket(1, usuario1, "primer reporte", "1", listado_tecnicos)
tecnico_encargado_ticket1 = ticket.tecnico

#comprobar los datos del ticket
print("-"*20)
print(f"El ticket generado:")
imprimir_datos_ticket(ticket)
print("-"*20)

# el tecnico recoje el ticket y lo pasa a estado 2 (en progreso)
helpDesk.actualizar_estado_ticket(tecnico_encargado_ticket1, 2)
print("-"*20)
imprimir_datos_ticket(ticket)
print("-"*20)

# el tecnico ha solucionado y se cierra el ticket
helpDesk.cerrar_ticket(ticket)

print("-"*20)
imprimir_datos_ticket(ticket)
print()
imrpimir_datos_tecnico(tecnico_encargado_ticket1)
print("-"*20)
