--* Script PostgreSQL

-- Llevar data a migrar a un path simple (corto)
-- Ejecutar
-- \i C:/Temp/script_clientes_productos.sql;
--! La barra \ en windows en las rutas se recomienda cambiar a /

-- Eliminar tablas si existen (con CASCADE si hay dependencias)
DROP TABLE IF EXISTS Citas CASCADE;
DROP TABLE IF EXISTS Agendas CASCADE;
DROP TABLE IF EXISTS CentroMedico CASCADE;
DROP TABLE IF EXISTS Especialistas CASCADE;
DROP TABLE IF EXISTS Usuarios CASCADE;
DROP TABLE IF EXISTS Contactos CASCADE;

-- Crear base de datos
CREATE DATABASE citas_medicas;

-- Conectarse a la base de datos
\c citas_medicas;

-- Crear tabla Contactos
CREATE TABLE Contactos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    mensaje TEXT NOT NULL
);

-- Crear tabla Usuarios
CREATE TABLE Usuarios (
    id SERIAL PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    tipo_usuario VARCHAR(50) NOT NULL
);

-- Crear tabla Especialistas
CREATE TABLE Especialistas (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    especialidad VARCHAR(100) NOT NULL
);

-- Crear tabla CentroMedico
CREATE TABLE CentroMedico (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion TEXT NOT NULL
);

-- Crear tabla Agendas
CREATE TABLE Agendas (
    id SERIAL PRIMARY KEY,
    fecha_disponible DATE NOT NULL,
    hora_disponible TIME NOT NULL,
    especialista_id INTEGER NOT NULL REFERENCES Especialistas(id),
    centro_medico_id INTEGER NOT NULL REFERENCES CentroMedico(id)
);

-- Crear tabla Citas
CREATE TABLE Citas (
    id SERIAL PRIMARY KEY,
    agenda_id INTEGER NOT NULL REFERENCES Agendas(id),
    usuario_id INTEGER NOT NULL REFERENCES Usuarios(id),
    mensaje TEXT
);


-- Insertar datos semilla

-- Insertar en Contactos
INSERT INTO Contactos (nombre, email, mensaje) VALUES
('Juan Pérez', 'juan.perez@example.com', 'Consulta sobre disponibilidad de citas.'),
('Ana Gómez', 'ana.gomez@example.com', 'Preguntas sobre los especialistas.');

-- Insertar en Usuarios
INSERT INTO Usuarios (email, password, tipo_usuario) VALUES
('usuario1@example.com', 'password123', 'paciente'),
('usuario2@example.com', 'password456', 'paciente'),
('admin@example.com', 'adminpass', 'admin');

-- Insertar en Especialistas
INSERT INTO Especialistas (nombre, especialidad) VALUES
('Dr. Luis Martínez', 'Cardiología'),
('Dra. María López', 'Dermatología');

-- Insertar en CentroMedico
INSERT INTO CentroMedico (nombre, direccion) VALUES
('Hospital Central', 'Calle Falsa 123'),
('Clínica de Especialidades', 'Avenida Siempre Viva 456');

-- Insertar en Agendas
INSERT INTO Agendas (fecha_disponible, hora_disponible, especialista_id, centro_medico_id) VALUES
('2024-08-01', '09:00:00', 1, 1),
('2024-08-02', '10:00:00', 2, 2);

-- Insertar en Citas
INSERT INTO Citas (agenda_id, usuario_id, mensaje) VALUES
(1, 1, 'Primera consulta de cardiología.'),
(2, 2, 'Revisión dermatológica.');
