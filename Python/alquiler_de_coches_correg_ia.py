class Vehiculo:
    def __init__(self, id_vehiculo, vehiculo, matricula, anyo, marca, modelo, tipo):
        #self.vehiculo = marca+modelo+tipo
        self.vehiculo = vehiculo
        self.matricula = matricula
        self.anyo = anyo    
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo            

class Cliente:
    def __init__(self, id_cliente, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo        

    def consultar_flota(self, flota):
        print(f"\nEnseñar Flota a {self.nombre}:")
        for vehiculo in flota:
            estado = "Disponible" if vehiculo.disponible else "Alquilado"
            print(f"\nEl {self.vehiculo} está {estado}")

    def listar_historial(self):
        print(f"\nHistorial de Alquileres de {self.nombre}")
        for alquilado in self.historial_alquilados:
            print(f"- {alquilado.vehiculo} - {alquilado.fecha_alquilado} - {alquilado.fecha_entrega}")
            
class Alquiler:
    def __init__(self, id_alquiler, id_cliente, vehiculo, id_agente, fecha_alquiler, fecha_entrega):
        self.vehiculo = vehiculo
        self.fecha_alquiler = fecha_alquiler
        self.fecha_entrega = fecha_entrega

class Agente:
    def __init__(self, id_agente, nombre):
        self.nombre = nombre

    def consultar_disponibilidad(self, vehiculo, disponible):
        self.disponible = True
        return vehiculo.disponible
    
    def crear_alquiler(self, id_alquiler, vehiculo, cliente, agente, fecha_alquiler, fecha_entrega):
        if self.consultar_disponibilidad(vehiculo):
            vehiculo.disponible = False
            alquilado = Alquiler(id_alquiler, cliente, vehiculo, fecha_alquiler, fecha_entrega)
            cliente.historial_alquilados.append(alquilado)
            print(f"El {vehiculo} se ha alquilado exitósamente.")
        else:
            print(f"El {vehiculo} NO está disponible.")            

    def devolver_vehiculo(self, vehiculo, cliente, fecha_real_entrega):
        for alquilado in cliente.historial.alquilados:
            if alquilado.vehiculo.id_vehiculo == vehiculo.id_vehiculo:
                alquilado.fecha_entrega = fecha_real_entrega
                vehiculo.disponible = True

            
    # Declaracion de Variables
            
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
disponible_antes = agente.consultar_disponibilidad_vehiculo(flota[0])
print(f"¿'{flota[0].vehiculo}' está disponible?: {'Sí' if disponible_antes else 'No'}\n")

print("\n--- PASO 3: El Agente crea el Alquiler ---")
agente.crear_alquiler(100, cliente1, flota[0], "27/03/2026", "13/04/2026")
agente.crear_alquiler(100, cliente1, flota[0], "15/04/2026", "30/04/2026")
print(f"{cliente1.nombre} a alquilado el {Vehiculo1.vehiculo} el {alquilado.fecha_alquiler}")
print() 

print("\n--- PASO 4: Comprobar disponibilidad después del Alquiler ---")
disponible_despues = agente.consultar_disponibilidad_vehiculo(flota[0])
print(f"¿'{flota[0].vehiculo}' está disponible?: {disponible_despues}\n")

print("\n--- PASO 5: Estado actualizado de la Flota ---")
cliente1.consultar_flota(flota)

print("\n--- PASO 6: Revisar el historial del Cliente ---")
cliente1.listar_historial()

print("\n==========================================\n")

"""
Tu código tiene varios errores de lógica y de referencia que impedirán que se ejecute. Aquí están los principales puntos a corregir:
1. Atributos no inicializados
En Vehiculo: No guardas el id_vehiculo, por lo que al intentar compararlo en devolver_vehiculo dará error. Además, los vehículos no nacen con el atributo self.disponible.
En Cliente: No inicializas self.historial_alquilados = [] en el __init__. Sin esto, no puedes hacer .append().
2. Errores de Referencia (Scope)
En consultar_flota: Usas self.vehiculo dentro de un bucle donde el objeto se llama vehiculo. Debería ser vehiculo.vehiculo (o mejor, cambia el nombre del atributo para no confundirte).
En el PASO 3: Intentas imprimir alquilado.fecha_alquiler, pero la variable alquilado solo existe dentro del método del agente, no fuera de él.
3. Inconsistencia en Métodos
consultar_disponibilidad: El método se llama así en la clase, pero en el cuerpo del programa lo llamas consultar_disponibilidad_vehiculo. Además, el método está mal definido: recibe un parámetro disponible que no usa y asigna self.disponible = True al agente (lo cual no tiene sentido).
crear_alquiler: La definición pide 6 argumentos, pero al llamarlo le pasas 5.
Solución sugerida (Código corregido):
python

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

Usa el código con precaución
"""