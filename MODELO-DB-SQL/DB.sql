--* Script PostgreSQL
-- Datos Semillas - Migrar data
-- Llevar data a migrar a un path simple (corto)
-- Ejecutar
-- \i C:/Temp/script_clientes_productos.sql;
--! La barra \ en windows en las rutas se recomienda cambiar a /
-- 1 Copiar path -> C:\Users\mauuu\OneDrive\Escritorio\DJANGO-PY 2024\MODELO-DB-SQL\DB.sql
-- 2 en Windows cambiar la barra \ a barra /
-- 3 ver de que los nombres de las carpetas no contengan acentos ni caracteres raros como ñ
-- 4 aplicar el import sobre la db creada (ya conectados en nuestra db)
-- 5 de tener algun nombre de carpeta con espacio le ponemos comillas simples
-- \i 'C:/Users/mauuu/OneDrive/Escritorio/DJANGO-PY 2024/MODELO-DB-SQL/DB.sql'
-- \i C:/script/DB.sql 

-- De no funcionar podemos simplemente copiar todo esto y pegar en nuestra sql shell (previo estar conectados a nuestra db)

-- Desde la CMD 
-- C:\Windows\System32>psql -U postgres -d citas_medicas -f C:/Users/mauuu/OneDrive/Escritorio/"DJANGO-PY 2024"/MODELO-DB-S
-- QL/DB.sql
-- Contraseña para usuario postgres:

-- Eliminar tablas si existen (con CASCADE si hay dependencias)
DROP DATABASE IF EXISTS citas_medicas;

SET CLIENT_ENCODING TO 'UTF8';
-- Crear base de datos

-- export PGCLIENTENCODING=UTF8 -- este comando en \i no corre

-- Implementar LC_COLLATE LC_CTYPE para manejo correcto de los acentos
-- CREATE DATABASE citas_medicas;
-- LC_COLLATE='en_US.UTF-8' --! para manejo de error del IMPORT - pero no lo soluciona
-- LC_CTYPE='en_US.UTF-8'
-- ENCODING='UTF8'
-- TEMPLATE=template0;

\encoding UTF8

-- Crear la base de datos
DROP DATABASE IF EXISTS citas_medicas;
CREATE DATABASE citas_medicas
    WITH ENCODING 'UTF8'
    LC_COLLATE='en_US.UTF-8'
    LC_CTYPE='en_US.UTF-8'
    TEMPLATE template0;

-- Conectarse a la base de datos recién creada
\c citas_medicas;

-- Crear las tablas

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

-- Insertar en Especialistas
INSERT INTO Especialistas (nombre, especialidad) VALUES
('Dr. Luis Martínez', 'Cardiología'),
('Dra. María López', 'Dermatología');

-- Insertar en CentroMedico
INSERT INTO CentroMedico (nombre, direccion) VALUES
('Hospital Central', 'Calle Falsa 123'),
('Clínica de Especialidades', 'Avenida Siempre Viva 456');

-- Insertar en Contactos
INSERT INTO Contactos (nombre, email, mensaje) VALUES
('Juan Pérez', 'juan.perez@example.com', 'Consulta sobre disponibilidad de citas.'),
('Ana Gómez', 'ana.gomez@example.com', 'Preguntas sobre los especialistas.');

-- Insertar en Usuarios
INSERT INTO Usuarios (email, password, tipo_usuario) VALUES
('usuario1@example.com', 'password123', 'paciente'),
('usuario2@example.com', 'password456', 'paciente'),
('admin@example.com', 'adminpass', 'admin');

-- Insertar en Agendas
INSERT INTO Agendas (fecha_disponible, hora_disponible, especialista_id, centro_medico_id) VALUES
('2024-08-01', '09:00:00', 1, 1),
('2024-08-02', '10:00:00', 2, 2);

-- Insertar en Citas
INSERT INTO Citas (agenda_id, usuario_id, mensaje) VALUES
(1, 1, 'Primera consulta de cardiología.'),
(2, 2, 'Revisión dermatológica.');

-- Verificar el contenido de las tablas
SELECT * FROM Especialistas;
SELECT * FROM Usuarios;
SELECT * FROM Citas;
SELECT * FROM agendas;

\dt
