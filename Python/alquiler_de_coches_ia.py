class Vehiculo:
    def __init__(self, id_vehiculo, nombre, matricula, anyo, marca, modelo, tipo):
        self.id_vehiculo = id_vehiculo
        self.nombre = nombre
        self.matricula = matricula
        self.disponible = True  # Atributo necesario

class Cliente:
    def __init__(self, id_cliente, nombre, telefono, correo):
        self.nombre = nombre
        self.historial_alquilados = [] # Inicializar lista
    
    def consultar_flota(self, flota):
        for v in flota:
            estado = "Disponible" if v.disponible else "Alquilado"
            print(f"El {v.nombre} está {estado}")

    def listar_historial(self):
        for alq in self.historial_alquilados:
            print(f"- {alq.vehiculo.nombre} | Desde: {alq.fecha_alquiler}")

class Alquiler:
    def __init__(self, id_alquiler, cliente, vehiculo, fecha_alquiler, fecha_entrega):
        self.vehiculo = vehiculo
        self.fecha_alquiler = fecha_alquiler
        self.fecha_entrega = fecha_entrega

class Agente:
    def __init__(self, id_agente, nombre):
        self.nombre = nombre

    def consultar_disponibilidad(self, vehiculo):
        return vehiculo.disponible
    
    def crear_alquiler(self, id_alquiler, cliente, vehiculo, fecha_ini, fecha_fin):
        if self.consultar_disponibilidad(vehiculo):
            vehiculo.disponible = False
            nuevo_alquiler = Alquiler(id_alquiler, cliente, vehiculo, fecha_ini, fecha_fin)
            cliente.historial_alquilados.append(nuevo_alquiler)
            return nuevo_alquiler
        return None

# --- INSTANCIAS ---
v1 = Vehiculo(1, "Seat Leon", "4563DFG", "2006", "Seat", "Leon", "Style")
flota = [v1]
cliente1 = Cliente(1, "Eustaquio", "602", "eu@ex.com")
agente = Agente(1, "Aniceto")

# --- PRUEBA ---
alquiler = agente.crear_alquiler(100, cliente1, v1, "27/03/2026", "13/04/2026")
if alquiler:
    print(f"Alquilado: {alquiler.vehiculo.nombre}")
cliente1.listar_historial()