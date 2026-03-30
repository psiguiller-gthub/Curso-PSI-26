class Libro:
    def __init__(self, id_libro, autor, titulo, isbn):
        self.id_libro = id_libro
        self.autor = autor
        self.titulo = titulo
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

    def listar_historial(self):
        print(f"\nHistorial de préstamos de {self.nombre}:")
        for prestamo in self.historial_prestamos:
            print(f"- {prestamo.libro.titulo} ({prestamo.fecha_prestamo} - {prestamo.fecha_devolucion})")

class Prestamo:
    def __init__(self, id_prestamo, id_usuario, libro, id_funcionario, fecha_prestamo, fecha_devolucion):
        self.id_prestamo = id_prestamo
        self.id_usuario = id_usuario
        self.libro = libro 
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
        if not self.consultar_disponibilidad_libro(libro):
            print("El libro no está disponible para préstamo.")
        else:
            prestamo = Prestamo(id_prestamo, usuario.id_usuario, libro, self.id_funcionario, fecha_prestamo, fecha_esperada)
            usuario.historial_prestamos.append(prestamo)
            libro.disponible = False
            print("Préstamo creado exitosamente.")

    def devolver_libro(self, libro, usuario, fecha_real_devolucion):
        for prestamo in usuario.historial_prestamos:
            if prestamo.libro.id_libro == libro.id_libro:
                prestamo.fecha_devolucion = fecha_real_devolucion
                libro.disponible = True

libro1 = Libro(1, "Kitti", "Miau Miau conversaciones con mi gato", "ES123456789")
libro2 = Libro(2, "Isabel", "Tarta de chocolate", "ES987654321")

catalogo = [libro1, libro2]

usuario1 = Usuario(123, "Tomas", "tomas@example.com", "666666666")
usuario2 = Usuario(456, "Adrian", "adrian@example.com", "777777777")

funcionario1 = Funcionario(1, "Mari Pili")

print("\n--- PASO 1: Estado inicial del catálogo ---")
usuario1.consultar_catalogo(catalogo)

print("\n--- PASO 2: Comprobar disponibilidad antes del préstamo ---")
disponible_antes = funcionario1.consultar_disponibilidad_libro(catalogo[0])
print(f"¿'{catalogo[0].titulo}' está disponible?: {'Sí' if disponible_antes else 'No'}\n")

print("\n--- PASO 3: El funcionario crea el préstamo ---")
funcionario1.crear_prestamo(100, usuario1, catalogo[0], "23/03/2026", "23/04/2026")
funcionario1.crear_prestamo(100, usuario1, catalogo[0], "23/03/2026", "23/04/2026")
funcionario1.crear_prestamo(100, usuario1, catalogo[1], "23/03/2026", "23/04/2026")
print() 

print("\n--- PASO 4: Comprobar disponibilidad después del préstamo ---")
disponible_despues = funcionario1.consultar_disponibilidad_libro(catalogo[0])
print(f"¿'{catalogo[0].titulo}' está disponible?: {disponible_despues}\n")

print("\n--- PASO 5: Estado actualizado del catálogo ---")
usuario1.consultar_catalogo(catalogo)

print("\n--- PASO 6: Revisar el historial del usuario ---")
usuario1.listar_historial()

print("\n==========================================\n")