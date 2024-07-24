
CREATE DATABASE registro_viajero;
\c registro_viajero;


-- Crear la tabla viajeros
CREATE TABLE viajeros (
    viajero_id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    genero CHAR(5) NOT NULL,
    email VARCHAR(250),
    telefono CHAR(50) NOT NULL,
    rut CHAR(10) NOT NULL UNIQUE
);

-- Crear la tabla destinos
CREATE TABLE destinos (
    destino_id SERIAL PRIMARY KEY,
    nombre_destino VARCHAR(100) NOT NULL,
    ciudad VARCHAR(50),
    pais VARCHAR(50)
);
-- Crear la tabla tickets
CREATE TABLE tickets (
    ticket_id SERIAL PRIMARY KEY,
    destino_id INT REFERENCES destinos (destino_id),
    viajero_id INT REFERENCES viajeros(viajero_id),
    numero_boleto VARCHAR(50) NOT NULL UNIQUE,
    fecha_emision DATE,
    fecha_salida DATE,
    fecha_retorno DATE
);
--* DATE es un tipo de string con un formato específico -> 'YYYY-MM-DD'

-- Inserts para la tabla viajeros
INSERT INTO viajeros (nombre, genero, email, telefono, rut) VALUES
('Juan Perez', 'M', 'juan@email.com', '123456789', '1111111111'),
('Maria Rodriguez', 'F', 'maria@email.com', '987654321', '2222222222'),
('Carlos Gonzalez', 'M', 'carlos@email.com', '111222333', '3333333333'),
('Luisa Martinez', 'F', 'luisa@email.com', '444555666', '4444444444'),
('Pedro Hernandez', 'M', 'pedro@email.com', '777888999', '5555555555'),
('Ana Lopez', 'F', 'ana@email.com', '333444555', '6666666666'),
('Jorge Ramirez', 'M', 'jorge@email.com', '666777888', '7777777777'),
('Sofia Torres', 'F', 'sofia@email.com', '999000111', '8888888888'),
('Daniel Castro', 'M', 'daniel@email.com', '222333444', '9999999999'),
('Laura Garcia', 'F', 'laura@email.com', '555666777', '0000000000'),
('Manuel Silva', 'M', 'manuel@email.com', '888999000', '1231231231'),
('Elena Vargas', 'F', 'elena@email.com', '111222333', '4564564564'),
('Gabriel Morales', 'M', 'gabriel@email.com', '444555666', '7897897897'),
('Isabel Rios', 'F', 'isabel@email.com', '777888999', '0120120120'),
('Hector Mendoza', 'M', 'hector@email.com', '333444555', '9876543210');

select * from viajeros;
-- Inserts para la tabla destinos
INSERT INTO destinos (nombre_destino, ciudad, pais) VALUES
('Playa del Carmen', 'Playa del Carmen', 'México'),
('Machu Picchu', 'Cuzco', 'Perú'),
('Torres del Paine', 'Puerto Natales', 'Chile'),
('Gran Barrera de Coral', 'Queensland', 'Australia'),
('Monte Everest', 'Khumbu', 'Nepal'),
('Santorini', 'Santorini', 'Grecia'),
('Marrakech', 'Marrakech', 'Marruecos'),
('Kioto', 'Kioto', 'Japón'),
('Marrakech', 'Marrakech', 'Marruecos'),
('Marrakech', 'Marrakech', 'Marruecos'),
('Marrakech', 'Marrakech', 'Marruecos'),
('Marrakech', 'Marrakech', 'Marruecos'),
('Marrakech', 'Marrakech', 'Marruecos'),
('Marrakech', 'Marrakech', 'Marruecos'),
('Marrakech', 'Marrakech', 'Marruecos');

-- Inserts para la tabla tickets
INSERT INTO tickets (viajero_id, destino_id, numero_boleto, fecha_emision, fecha_salida, fecha_retorno) VALUES
(1, 1, 'T111111', '2024-01-04', '2024-01-10', '2024-01-20'),
(2, 2, 'T222222', '2024-01-05', '2024-02-01', '2024-02-15'),
(2, 3, 'T333333', '2024-01-06', '2024-03-05', '2024-03-20'),
(4, 4, 'T444444', '2024-01-07', '2024-04-12', '2024-05-01'),
(5, 5, 'T555555', '2024-01-08', '2024-06-02', '2024-06-20'),
(6, 1, 'T666666', '2024-01-09', '2024-07-15', '2024-08-01'),
(4, 2, 'T777777', '2024-01-10', '2024-09-03', '2024-09-20'),
(8, 3, 'T888888', '2024-01-11', '2024-10-18', '2024-11-01'),
(9, 4, 'T999999', '2024-01-12', '2024-12-05', '2024-12-20'),
(10, 5, 'T101010', '2024-01-13', '2025-01-02', '2025-01-20'),
(15, 1, 'T1111111', '2024-01-14', '2025-02-10', '2025-02-25'),
(12, 2, 'T121212', '2024-01-15', '2025-03-15', '2025-04-01'),
(13, 3, 'T131313', '2024-01-16', '2025-05-02', '2025-05-20'),
(14, 4, 'T141414', '2024-01-17', '2025-06-12', '2025-06-30'),
(15, 5, 'T151515', '2024-01-18', '2025-07-20', '2025-08-05');


-- ---------------------------------------------------------------
Guía de Ejercicio

-- Consulta 1:
SELECT viajeros.nombre, tickets.numero_boleto, destinos.nombre_destino
FROM viajeros
LEFT JOIN tickets ON viajeros.viajero_id = tickets.viajero_id
LEFT JOIN destinos ON tickets.destino_id = destinos.destino_id;


SELECT viajeros.*, tickets.*, destinos.*
FROM viajeros
LEFT JOIN tickets ON viajeros.viajero_id = tickets.viajero_id
LEFT JOIN destinos ON tickets.destino_id = destinos.destino_id;
-- Consulta 2: Mostrar la información del boleto T123456 junto con los detalles del viajero y destino
SELECT viajeros.*, tickets.*, destinos.*
FROM viajeros
LEFT JOIN tickets ON viajeros.viajero_id = tickets.viajero_id
LEFT JOIN destinos ON tickets.destino_id = destinos.destino_id
WHERE tickets.numero_boleto = 'T123456';
"""
(0 filas)
"""

tickets.numero_boleto

-- Consulta 3: Listar todos los viajeros que tienen fecha de salida o de retorno el '2024-01-10'
SELECT DISTINCT viajeros.*
FROM viajeros
JOIN tickets ON viajeros.viajero_id = tickets.viajero_id
WHERE tickets.fecha_salida = '2024-01-10' OR tickets.fecha_retorno = '2024-01-10';

tickets.fecha_salida y retorno
-- Consulta 4: Obtener el número total de boletos por cada género
SELECT viajeros.genero, COUNT(tickets.viajero_id) AS cantidad 
FROM viajeros 
JOIN tickets ON viajeros.viajero_id = tickets.viajero_id
GROUP BY viajeros.genero;


viajeros.genero
-- Consulta 5: Obtener un listado de todos los viajeros que han viajado a Playa del Carmen
SELECT viajeros.*
FROM viajeros
JOIN tickets ON viajeros.viajero_id = tickets.viajero_id
JOIN destinos ON tickets.destino_id = destinos.destino_id
WHERE destinos.nombre_destino = 'Playa del Carmen';


destinos.nombre_destino

--! Al ELIMINAR data - ¿? ERROR de que no nos deja por su vínculo con una FK
Ejemplo:
DELETE FROM viajeros WHERE viajero_id = 1; --! ERROR FK
-- DEBEMOS eliminar en cascada
DELETE FROM tickets WHERE viajero_id = 1;
DELETE FROM viajeros WHERE viajero_id = 1;

--! Tabla nueva - Eliminar columnas de otra tabla e incorporar su FK

--* 1. Crean la tabla NUEVA
--* 2. Tabla destinos anexan la FK pais_id
--* 3. Reemplazo correcto de las columnas a eliminar de una fila y reemplazan por su FK
--* 4. Ya habiendo migrado todos esos datos vamos a eliminar esas columnas
ALTER TABLE destinos
DROP COLUMN pais,
DROP COLUMN ciudad;



-- --------------------------------------
ALTER TABLE destinos 
ADD COLUMN paisid INTEGER, 
FOREIGN KEY (paisid) REFERENCES pais(pais_id); --! FOREIGN KEY ¿?


"""
destino_id:3
viajero_id:4
numero_boleto:T171717
fecha_salida:2024-03-28
fecha_retorno:2024-04-01


1. Ticket 1
destino_id:3
viajero_id:4
numero_boleto:T171717
fecha_salida:2024-03-28
fecha_retorno:2024-04-01
2. Ticket 2
destino_id:5
viajero_id:10
numero_boleto:T888888
fecha_salida:2024-03-28
fecha_retorno:2024-04-01
3. Ticket 3
destino_id:4
numero_boleto:T202020
fecha_salida:2024-03-28
fecha_retorno:2024-04-01

"""

INSERT INTO tickets (destino_id, viajero_id, numero_boleto, fecha_salida, fecha_retorno) 
VALUES (3, 4, 'T171717', '2024-03-28', '2024-04-01');
"""
INSERT 0 1
"""

INSERT INTO tickets (destino_id, viajero_id, numero_boleto, fecha_salida, fecha_retorno) 
VALUES (5, 10, 'T888888', '2024-03-28', '2024-04-01');
"""
ERROR:  llave duplicada viola restricción de unicidad «tickets_numero_boleto_key»
DETALLE:  Ya existe la llave (numero_boleto)=(T888888).
"""

INSERT INTO tickets (destino_id, numero_boleto, fecha_salida, fecha_retorno) 
VALUES (4, 'T202020', '2024-03-28', '2024-04-01');
"""
INSERT 0 1
"""


"""
CREATE TABLE tickets (
    ticket_id SERIAL PRIMARY KEY,
    destino_id INT REFERENCES destinos (destino_id),
    viajero_id INT REFERENCES viajeros(viajero_id),
    numero_boleto VARCHAR(50) NOT NULL UNIQUE,
    fecha_emision DATE,
    fecha_salida DATE,
    fecha_retorno DATE
);
"""



SELECT viajeros.*, tickets.*, destinos.*
FROM viajeros
LEFT JOIN tickets ON viajeros.viajero_id = tickets.viajero_id
LEFT JOIN destinos ON tickets.destino_id = destinos.destino_id;


SELECT viajeros.*, tickets.*, destinos.*
FROM viajeros
JOIN tickets ON viajeros.viajero_id = tickets.viajero_id
JOIN destinos ON tickets.destino_id = destinos.destino_id
WHERE destinos.nombre_destino = "Papapapapa";



A continuación borra los siguientes registros:
● Ticket con ID 4
● Viajero con ID 2
● Destino con ID 5
¿Por qué pudiste borrar algunos registros y otros no?
¿Qué solución podrías entregar para borrar todos los registros solicitados?

-- Eliminar
SELECT * FROM tickets;
DELETE FROM tickets WHERE ticket_id = 4;
-- DELETE 1
● Ticket con ID 4
DELETE FROM viajeros WHERE viajero_id = 2;
DELETE FROM tickets WHERE viajero_id = 2;
-- DETALLE:  La llave (viajero_id)=(2) todavía es referida desde la tabla «tickets»
registro_viajero=# DELETE FROM tickets WHERE viajero_id = 2;
DELETE 2
registro_viajero=# DELETE FROM viajeros WHERE viajero_id = 2;
DELETE 1
registro_viajero=#


● Viajero con ID 2
DELETE FROM destinos WHERE destino_id = 5;
-- DETALLE:  La llave (destino_id)=(5) todavía es referida desde la tabla «tickets».
● Destino con ID 5



país_id, nombre_país, ciudad y código_postal

CREATE TABLE paises (
    pais_id SERIAL PRIMARY KEY,
    nombre_pais VARCHAR(50) NOT NULL,
    ciudad VARCHAR(50) NOT NULL,
    codigo_postal VARCHAR(50) NOT NULL
);


INSERT INTO paises (nombre_pais, ciudad, codigo_postal)
VALUES ('México','Playa del Carmen', '493'),
( 'Perú','Cuzco','589'),
('Chile', 'Puerto Natales','211' ),
('Australia','Queensland','069' ),
( 'Nepal','Khumbu','517' ),
( 'Grecia','Santorini','301' ),
('Marruecos','Marrakech','474' ),
( 'Japón','Kioto','399' );

ALTER TABLE destinos ADD COLUMN pais_id INT REFERENCES paises(pais_id);

UPDATE destinos 
SET pais_id = (
    SELECT pais_id 
    FROM paises 
    WHERE paises.nombre_pais = destinos.pais
    LIMIT 1
);



ALTER TABLE destinos
DROP COLUMN pais,
DROP COLUMN ciudad;
