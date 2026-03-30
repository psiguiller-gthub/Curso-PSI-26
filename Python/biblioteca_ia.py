from datetime import datetime

class Libro:
    def __init__(self, id_libro, titulo, autor, isbn):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

class Usuario:
    def __init__(self, id_usuario, nombre, email, telefono):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.historial_prestamos = [] # Guardará objetos de la clase Prestamo

    def mostrar_historial(self):
        """Muestra de forma legible los libros que el usuario ha tomado."""
        print(f"\n--- Historial de {self.nombre} ---")
        if not self.historial_prestamos:
            print("No hay préstamos registrados.")
            return
        
        for p in self.historial_prestamos:
            # Accedemos a los atributos del objeto Prestamo 'p'
            estado = f"Devuelto el {p.fecha_devolucion}" if p.fecha_devolucion else "Pendiente"
            print(f"Libro ID: {p.id_libro} | Prestado: {p.fecha_prestamo} | Estado: {estado}")

class Prestamo:
    def __init__(self, id_prestamo, id_usuario, id_libro, id_funcionario, fecha_prestamo):
        self.id_prestamo = id_prestamo
        self.id_usuario = id_usuario
        self.id_libro = id_libro
        self.id_funcionario = id_funcionario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = None # Se inicializa en None hasta que se devuelva

class Funcionario:
    def __init__(self, id_funcionario, nombre):
        self.id_funcionario = id_funcionario
        self.nombre = nombre

    def consultar_disponibilidad(self, libro):
        return libro.disponible
    
    def crear_prestamo(self, id_prestamo, usuario, libro):
        """Encapsula la lógica de verificación y creación."""
        if self.consultar_disponibilidad(libro):
            fecha_hoy = datetime.now().strftime("%d/%m/%Y")
            
            # Instanciamos el préstamo
            nuevo_prestamo = Prestamo(
                id_prestamo, usuario.id_usuario, libro.id_libro, 
                self.id_funcionario, fecha_hoy
            )
            
            # Actualizamos estados
            libro.disponible = False
            usuario.historial_prestamos.append(nuevo_prestamo)
            print(f"✅ Préstamo creado: '{libro.titulo}' entregado a {usuario.nombre}.")
        else:
            print(f"❌ Error: El libro '{libro.titulo}' ya está prestado.")

    def gestionar_devolucion(self, usuario, libro):
        """Busca el préstamo activo en el historial del usuario y lo cierra."""
        for p in usuario.historial_prestamos:
            # Buscamos el préstamo que coincida con el libro y no tenga fecha de devolución
            if p.id_libro == libro.id_libro and p.fecha_devolucion is None:
                p.fecha_devolucion = datetime.now().strftime("%d/%m/%Y")
                libro.disponible = True
                print(f"🔄 Libro '{libro.titulo}' devuelto correctamente por {usuario.nombre}.")
                return
        print(f"⚠️ No se encontró un préstamo activo de '{libro.titulo}' para este usuario.")

# --- PRUEBAS DEL SISTEMA ---

# 1. Inicialización (Usando tus ejemplos de ISBN)
libro1 = Libro(1, "Cien Años de Soledad", "Gabriel García Márquez", "978-3-16-148410-0")
libro2 = Libro(2, "Don Quijote", "Miguel de Cervantes", "978-1-23-456789-5")

user1 = Usuario(123, "Tomas", "tomas@example.com", "555-1234")
staff1 = Funcionario(1, "Mari Pili")

# 2. Flujo de préstamo
print(f"¿Disponible '{libro1.titulo}'?: {staff1.consultar_disponibilidad(libro1)}")
staff1.crear_prestamo(100, user1, libro1)

# 3. Intento de préstamo de libro no disponible
staff1.crear_prestamo(101, user1, libro1)

# 4. Ver historial y Devolución
user1.mostrar_historial()
staff1.gestionar_devolucion(user1, libro1)

# 5. Estado final
print(f"¿Disponible '{libro1.titulo}'?: {staff1.consultar_disponibilidad(libro1)}")
