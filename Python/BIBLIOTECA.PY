# SISTEMA:Biblioteca

# Tarea: Gestion de préstamos de libros.

"""
clases
- Libro
    - id_libro
    - titulo
    - autor
    - isbn    
    - disponible (booleano)
- Usuario
    - id_usuario    
    - nombre
    - email
    - telefono
    - historial_prestamos []   
----------------------------------------------------    
    + solicita_libro()
    + devuelve_libro()
- Prestamo
    - id_prestamo
    - id_usuario
    - id_libro
    - id_funcionario
    - fecha_prestamo
    - fecha_devolucion
- Funcionario
    - nombre
    - id_funcionario
----------------------------------------------------    
    + consultar_disponibilidad_libro()
    + crear_prestamo()
    + devolver_libro()

catalogo = [libro1, libro2]
"""

# Usuario solicita prestamo de libro --> Funcionario verifica disponibilidad del libro --> Si disponible, se crea un nuevo prestamo y se actualiza el estado del libro a no disponible.
# El prestamo se agrega al historial del usuario. Si no disponible, se informa al usuario que el libro no está disponible.

"""
Usuario solicita prestamo de libro --> Funcionario verifica disponibilidad del libro --> Si disponible, se crea un nuevo prestamo --> y se actualiza el estado del libro a no disponible.
--> El prestamo se agrega al historial del usuario.--> Usuario devuelve el prestamo --> funcionario actualiza prestamo a disponible --> y actualiza el historial del usuario.

        

"""

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
        self.historial_prestamos = []

    def consultar_catalogo(self, catalogo):
        print(f"\nCatálogo consultado por {self.nombre}:")
        for libro in catalogo:
            estado = "Disponible" if libro.disponible else "Prestado"
            print(f"- {libro.titulo} de {libro.autor} ({estado})")

    def historial_prestamos(self, id_prestamo, id_usuario, id_libro, id_funcionario, usuario, libro, fecha_prestamo, fecha_devolucion):
        print(f"\nHistorial de prestamos de {self.nombre}")    
        for prestamo in self.historial_prestamos:
            print(f"\n{Funcionario(funcionario1.nombre)} le prestó a {self.nombre} el libro {Libro(libro1.titulo)} el {Prestamo(fecha_prestamo)} y fué devuelto el {Prestamo(fecha_devolucion)}")

    
class Prestamo:
    def __init__(self, id_prestamo, id_usuario, id_libro, id_funcionario, fecha_prestamo, fecha_devolucion):
        self.id_prestamo = id_prestamo
        self.id_usuario = id_usuario
        self.id_libro = id_libro
        self.id_funcionario = id_funcionario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

class Funcionario:
    def __init__(self, id_funcionario, nombre):
        self.id_funcionario = id_funcionario
        self.nombre = nombre

    def consultar_disponibilidad_libro(self, libro):
        return libro.disponible
    
    def crear_prestamo(self, id_prestamo, usuario, libro, fecha_prestamo, fecha_esperada):
        if self.consultar_disponibilidad_libro(libro):
            # Lógica para crear un nuevo préstamo
            prestamo = Prestamo(id_prestamo, usuario.id_usuario, libro, self.id_funcionario, fecha_prestamo, fecha_esperada)
            usuario.historial_prestamos.append(prestamo)
            libro.disponible = False            
            print(f"{usuario.nombre} se lleva {libro.titulo} el {fecha_prestamo} para devolver {fecha_esperada}.")
        else:
            print(f"El libro '{libro.titulo}' no está disponible.")
      

    def devolver_libro(self, usuario, libro, prestamo, fecha_real_devolucion):
        for prestamo in usuario.historial_prestamos:
            if prestamo.id_libro == libro.id_libro and prestamo.fecha_devolucion is None:
                prestamo.fecha_devolucion = fecha_real_devolucion
                libro.disponible = True
                print(f"El libro '{libro.titulo}' ha sido devuelto por {usuario.nombre}.")
                return



libro1 = Libro(1, "Cien Años de Soledad", "Gabriel García Márquez", "978-3-16-148410-0")
libro2 = Libro(2, "Don Quijote de la Mancha", "Miguel de Cervantes", "978-1-23-456789-0")

catalogo = [libro1, libro2]

usuario1 = Usuario(123, "Tomas", "tomas@example.com", "555-1234")
usuario2 = Usuario(456, "Adrian", "adrian@example.com", "555-5678")

funcionario1 = Funcionario(1, "Mari Pili")

# Casos de USO
print(f"{funcionario1.consultar_disponibilidad_libro(catalogo[0])}")  # True
funcionario1.crear_prestamo(100, usuario1, catalogo[0], "23/03/2026", "28/04/2026")
print(f"{funcionario1.consultar_disponibilidad_libro(catalogo[0])}")  # False

usuario1.historial_prestamos
