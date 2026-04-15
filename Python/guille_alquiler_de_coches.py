class Vehiculo:
    def __init__(self, id_vehiculo, descripcion, matricula, anyo, marca, modelo, tipo):        
        self.descripcion = descripcion
        self.matricula = matricula
        self.anyo = anyo    
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo            
        self.disponible = True  # Atributo necesario

class Cliente:
    def __init__(self, id_cliente, nombre, telefono, correo):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo     
        self.historial_alquilados = []   

    def consultar_flota(self, flota):
        print(f"Enseñar Flota a {self.nombre}:")
        for vehiculo in flota:
            estado = "Disponible" if vehiculo.disponible else "Alquilado"
            print(f"El {vehiculo.descripcion} está {estado}")

    def listar_historial(self):
        print(f"Historial de Alquileres de {self.nombre}")
        for alquilado in self.historial_alquilados:
            print(f"- {alquilado.vehiculo.descripcion} - {alquilado.fecha_alquiler} - {alquilado.fecha_entrega}")
            
class Alquiler:
    def __init__(self, id_alquiler, id_cliente, vehiculo, id_agente, fecha_alquiler, fecha_entrega):
        self.id_alquiler = id_alquiler
        self.id_cliente = id_cliente
        self.id_agente = id_agente
        self.vehiculo = vehiculo
        self.fecha_alquiler = fecha_alquiler
        self.fecha_entrega = fecha_entrega

class Agente:
    def __init__(self, id_agente, nombre):
        self.id_agente = id_agente
        self.nombre = nombre

    def consultar_disponibilidad(self, vehiculo):
        return vehiculo.disponible
    
    def crear_alquiler(self, id_alquiler, vehiculo, cliente, agente, fecha_alquiler, fecha_entrega):
        if self.consultar_disponibilidad(vehiculo):
            vehiculo.disponible = False
            alquilado = Alquiler(id_alquiler, cliente.id_cliente, vehiculo, self.id_agente, fecha_alquiler, fecha_entrega)
            cliente.historial_alquilados.append(alquilado)
            print(f"{cliente.nombre} ha alquilado el {vehiculo.descripcion} el {fecha_alquiler}.")
        else:            
            print(f"El {vehiculo.descripcion} NO está disponible.")            

    def devolver_vehiculo(self, vehiculo, cliente, fecha_real_entrega):
        for alquilado in cliente.historial.alquilados:
            if alquilado.vehiculo.id_vehiculo == vehiculo.id_vehiculo:
                alquilado.fecha_entrega = fecha_real_entrega
                vehiculo.disponible = True

            
    # Declaracion de Variables INSTANCIAR (dar vida)
            
Vehiculo1 = Vehiculo(1, "Seat Leon Style", "4563DFG", "2006", "Seat", "Leon", "Style")
Vehiculo2 = Vehiculo(2, "Volkswagen Golf GTI", "7594FGH", "2008", "Volkswagen", "Golf", "GTI")

flota = [Vehiculo1, Vehiculo2]

cliente1 = Cliente(1, "Eustaquio", "602030401", "euquio@example.pio")
cliente2 = Cliente(2, "Escolástica", "604090709", "escotica@example.ica")

agente = Agente(1, "Aniceto")


    # CASOS DE USO

print("\n--- PASO 1: Estado inicial de la Flota ---")
cliente1.consultar_flota(flota)

print("\n--- PASO 2: Comprobar disponibilidad antes del Alquiler ---")
disponible_antes = agente.consultar_disponibilidad(flota[0])
print(f"¿'{flota[0].descripcion}' está disponible?: {'Sí' if disponible_antes else 'No'}\n")

print("\n--- PASO 3: El Agente crea el Alquiler ---")
agente.crear_alquiler(100, flota[0], cliente1, agente, "27/03/2026", "13/04/2026")
agente.crear_alquiler(100, flota[0], cliente1, agente,  "15/04/2026", "30/04/2026")
# MAL No se puede acceder a alquilado, está fuera de la funcion
# print(f"{cliente1.nombre} a alquilado el {Vehiculo1.vehiculo} el {alquilado.fecha_alquiler}")
print(f"{cliente1.nombre} a alquilado el {Vehiculo1.descripcion}")
print() 

print("\n--- PASO 4: Comprobar disponibilidad después del Alquiler ---")
disponible_despues = agente.consultar_disponibilidad(flota[0])
print(f"¿'{flota[0].descripcion}' está disponible?: {disponible_despues}")

print("\n--- PASO 5: Estado actualizado de la Flota ---")
cliente1.consultar_flota(flota)

print("\n--- PASO 6: Revisar el historial del Cliente ---")
cliente1.listar_historial()

print("\n==========================================\n")