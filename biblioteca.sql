CREATE DATABASE IF NOT EXISTS biblioteca;
USE biblioteca;

CREATE TABLE Lector (
    id_lector INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(20)
);

CREATE TABLE Estudiante (
    id_lector INT PRIMARY KEY,
    codigo_estudiante VARCHAR(20) UNIQUE NOT NULL,
    FOREIGN KEY (id_lector) REFERENCES Lector(id_lector) ON DELETE CASCADE
);

CREATE TABLE Docente (
    id_lector INT PRIMARY KEY,
    codigo_docente VARCHAR(20) UNIQUE NOT NULL,
    FOREIGN KEY (id_lector) REFERENCES Lector(id_lector) ON DELETE CASCADE
);

CREATE TABLE Bibliotecario (
    id_personal INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE Libro (
    id_libro INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    tipo_libro VARCHAR(50),
    autor VARCHAR(100),
    editorial VARCHAR(100)
);

CREATE TABLE Revista (
    id_revista INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    tipo_revista VARCHAR(50),
    autor VARCHAR(100),
    edicion VARCHAR(50)
);

CREATE TABLE Pedido (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_lector INT NOT NULL,
    id_personal INT NOT NULL,
    id_libro INT DEFAULT NULL,
    id_revista INT DEFAULT NULL,
    fecha_pedido DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (id_lector) REFERENCES Lector(id_lector),
    FOREIGN KEY (id_personal) REFERENCES Bibliotecario(id_personal),
    FOREIGN KEY (id_libro) REFERENCES Libro(id_libro),
    FOREIGN KEY (id_revista) REFERENCES Revista(id_revista)
);

INSERT INTO Lector (nombre, direccion, telefono) VALUES ('Juan Pérez', 'Calle 123', '555-01');
INSERT INTO Estudiante (id_lector, codigo_estudiante) VALUES (1, 'EST-001');
INSERT INTO Bibliotecario (nombre) VALUES ('Admin Carlos');
INSERT INTO Libro (titulo, autor) VALUES ('Cien Años de Soledad', 'Gabo');