
--?
SELECT current_database() datname, pg_is_in_recovery() as read_only,current_setting('archive_mode') archive,current_setting('wal_level') wal_level;


CREATE DATABASE copilot;
\c copilot;

CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    email VARCHAR(50)
);

SELECT * FROM clientes;

DROP TABLE clientes;

Volvimos a crear
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    email VARCHAR(50)
);

Anexar columna (cambia la estructura de la tabla)

ALTER TABLE clientes 
ADD COLUMN nombre TEXT;

\d clientes;


--* CHECK

ALTER TABLE clientes 
ADD COLUMN edad INT CHECK (edad > 17);

INSERT INTO clientes (email, nombre, edad) VALUES ('mano@sasa.com', 'Manolo', 18);

CREATE TABLE "Productos" (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50)
);


INSERT INTO clientes (email, nombre, edad) VALUES ('dede@sasa.com', 'Juan', 11);
"""
INSERT INTO clientes (email, nombre, edad) VALUES ('dede@sasa.com', 'Juan', 11);
ERROR:  el nuevo registro para la relación «clientes» viola la restricción «check» «clientes_edad_check»
DETALLE:  La fila que falla contiene (2, dede@sasa.com, Juan, 11).
"""
INSERT INTO clientes (email) VALUES ("");

UPDATE clientes SET nombre = 'Fede', edad = 20 WHERE id = 3;


ALTER TABLE clientes 
ADD COLUMN numero_cuenta INT UNIQUE;
INSERT INTO clientes (email, nombre, edad, numero_cuenta) VALUES ('sasa@sasa.com', 'Jime', 21, 101);

INSERT INTO clientes (email, nombre, edad, numero_cuenta) VALUES ('sisi@sasa.com', 'Vane', 32, 101);
"""
ERROR:  llave duplicada viola restricción de unicidad «clientes_numero_cuenta_key»
DETALLE:  Ya existe la llave (numero_cuenta)=(101).
"""



CREATE TABLE ordenes (
 id INT PRIMARY KEY,
 cantidad INT,
 cliente_id INT,
 FOREIGN KEY (cliente_id) REFERENCES clientes (id)
);




-- EJERCICIO GUIADO

CREATE DATABASE bancaria;
\c bancaria;
a. ID
b. Nombre
c. Apellido
d. Rut
e. Teléfono.
f. Email.

CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    rut VARCHAR(50) NOT NULL UNIQUE,
    telefono VARCHAR(50),
    email VARCHAR(50) NOT NULL UNIQUE
);

a. ID
b. Número de cuenta.
c. Fecha de creación.
d. Balance.
La clave foránea deberás definirla en el campo correspondiente para que se 
genere la relación con clientes.

CREATE TABLE cuentas (
    id SERIAL PRIMARY KEY,
    numero_cuenta INT NOT NULL UNIQUE,
    fecha DATE NOT NULL,
    balance DECIMAL(10,2) NOT NULL,
    cliente_id INT,
    FOREIGN KEY (cliente_id) REFERENCES clientes (id)
);

INSERT INTO clientes (nombre, apellido, rut, telefono, email) 
VALUES ('camila','gonzalez','18.058.880-9','147258','cami@gmail.com'),
('francisca','valenzuela','21.471.745-6','852963','fran@gmail.com'),
('fernando','gonzalez','14.458.125-k','874125','feña@gmail.com');

INSERT INTO cuentas (numero_cuenta, fecha, balance, cliente_id)
VALUES (231, '2015-01-12', 50000.00, 1), (101, '2017-11-01', 35000.00, 2); 


SELECT c.nombre, c.apellido, c.email, cu.numero_cuenta, cu.fecha, cu.balance 
FROM clientes AS c 
JOIN cuentas AS cu 
ON c.id = cu.cliente_id; 
"""
 nombre   |  apellido  |     email      | numero_cuenta |   fecha    | balance
-----------+------------+----------------+---------------+------------+----------
 camila    | gonzalez   | cami@gmail.com |           231 | 2015-01-12 | 50000.00
 francisca | valenzuela | fran@gmail.com |           101 | 2017-11-01 | 35000.00
(2 filas)
"""

SELECT c.id, c.nombre, c.apellido, c.email, cu.numero_cuenta, cu.fecha, cu.balance, cu.cliente_id
FROM clientes AS c 
LEFT JOIN cuentas AS cu 
ON c.id = cu.cliente_id; 
"""
 id |  nombre   |  apellido  |     email      | numero_cuenta |   fecha    | balance  | cliente_id
----+-----------+------------+----------------+---------------+------------+----------+------------
  1 | camila    | gonzalez   | cami@gmail.com |           231 | 2015-01-12 | 50000.00 |          1
  2 | francisca | valenzuela | fran@gmail.com |           101 | 2017-11-01 | 35000.00 |          2
  3 | fernando  | gonzalez   | feña@gmail.com |               |            |          |           
(3 filas)
"""

-- ANTIGUEDAD
SELECT * FROM cuentas ORDER BY fecha;
SELECT * FROM cuentas ORDER BY fecha LIMIT 1;
SELECT fecha FROM cuentas ORDER BY fecha LIMIT 1; --  2015-01-12

SELECT c.id, c.nombre, c.apellido, c.email, cu.numero_cuenta, cu.fecha, cu.balance, cu.cliente_id
FROM clientes AS c 
LEFT JOIN cuentas AS cu 
ON c.id = cu.cliente_id
WHERE cu.fecha = (SELECT fecha FROM cuentas ORDER BY fecha LIMIT 1);

"""
 id | nombre | apellido |     email      | numero_cuenta |   fecha    | balance  | cliente_id
----+--------+----------+----------------+---------------+------------+----------+------------
  1 | camila | gonzalez | cami@gmail.com |           231 | 2015-01-12 | 50000.00 |          1
"""

-- APELLIDO y MAYOR BALANCE

-- LOS que no tienen cuenta

-- SUB-QUERY   AVG para sacar promedio del balance, quiero las cuentas con balance mayor al promedio
