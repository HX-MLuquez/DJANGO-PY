

CREATE database paloma;

\c paloma;

CREATE TABLE clientes (
    id INT UNIQUE NOT NULL,
    name TEXT NOT NULL, 
    email  VARCHAR(50) 
);

\d clientes;

SELECT * FROM clientes; 

INSERT INTO clientes (id, name) 
VALUES (1, 'Pepe'), (2, 'Juan'), (3, 'Jose');

ALTER TABLE clientes ALTER COLUMN email SET NOT NULL;
--! ERROR:  la columna «email» de la relación «clientes» contiene valores null

UPDATE clientes SET email = 'email a solicitar' WHERE email IS NULL;
UPDATE clientes SET fecha = COALESCE(fecha, '2024-01-01');


--Todo_ Anexar una CONSTRAINS - RESTRINCCION a la columna email
ALTER TABLE clientes ALTER COLUMN email SET NOT NULL;

\d clientes;
"""
 Columna |         Tipo          | Ordenamiento | Nulable  | Por omisi¾n
---------+-----------------------+--------------+----------+-------------
 id      | integer               |              | not null |
 name    | text                  |              | not null |
 email   | character varying(50) |              | not null |
═ndices:
    "clientes_id_key" UNIQUE CONSTRAINT, btree (id)
"""

INSERT INTO clientes (id, name, email) 
VALUES (4, 'Manolo', 'man@gmail.com');

--Todo_ Agregar una nueva columna

ALTER TABLE clientes ADD COLUMN fecha DATE; 'YYYY-MM-DD'

INSERT INTO clientes (id, name, email, fecha) 
VALUES (5, 'Josue', 'man@gmail.com', '2024-07-17');

----------------------------------------


CREATE TABLE productos (
    id INT PRIMARY KEY, -- UNIQUE NOT NULL
    nombre VARCHAR(50), 
    code VARCHAR(250) 
);

\d productos;

SELECT * FROM productos; 

INSERT INTO productos (id, nombre) 
VALUES (1, 'galleta'), (2, 'harina');

INSERT INTO productos (id, nombre, code) 
VALUES (3, 'dulce', 'DS-23000');

-- 1. Ejercicio: El code debe ser NOT NULL
ALTER TABLE productos ALTER COLUMN code SET NOT NULL;
--! ERROR:  la columna «code» de la relación «productos» contiene valores null

UPDATE productos SET code = 'AA-00000' WHERE code IS NULL;
ALTER TABLE productos ALTER COLUMN code SET NOT NULL; -- OK 

INSERT INTO productos (id, nombre, code) 
VALUES (4, 'jugo', 'DS-99000');

ALTER TABLE productos ALTER COLUMN code DROP NOT NULL;


--Todo_ RELACIONES - REFERENCIAS - ASOCIACIONES - SQL MODELO RELACIONAL
--* PK -> FK


CREATE TABLE autores (
    id INT PRIMARY KEY, 
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE libros (
    id INT PRIMARY KEY, 
    titulo VARCHAR(50) NOT NULL,
    autor_id INT NOT NULL,
    FOREIGN KEY (autor_id) REFERENCES autores(id)
);

\libros

"""
 Columna  |         Tipo          | Ordenamiento | Nulable  | Por omisi¾n
----------+-----------------------+--------------+----------+-------------
 id       | integer               |              | not null |
 titulo   | character varying(50) |              | not null |
 autor_id | integer               |              | not null |
═ndices:
    "libros_pkey" PRIMARY KEY, btree (id)
Restricciones de llave forßnea:
    "libros_autor_id_fkey" FOREIGN KEY (autor_id) REFERENCES autores(id)
"""

INSERT INTO autores (id, nombre) 
VALUES (4, 'Miguel Cervantes'), (56, 'Borges');

INSERT INTO libros (id, titulo, autor_id) 
VALUES (1, 'El Quijote de la Mancha', 4),  (2, 'La biblioteca de Babel', 56),  (3, 'Ficciones', 56);


DELETE FROM autores;
--! ERROR:  update o delete en «autores» viola la llave foránea «libros_autor_id_fkey» en la tabla «libros»
-- DETALLE:  La llave (id)=(4) todavía es referida desde la tabla «libros».

-- SOLUCION - Ir eliminando desde las Tablas hijas hacia las tablas padre
DELETE FROM libros;
DELETE FROM autores; -- OK

-- OTRA SOLUCION de eliminar en CASCADA
TRUNCATE autores;
"""
ERROR:  no se puede truncar una tabla referida en una llave foránea
DETALLE:  La tabla «libros» hace referencia a «autores».
SUGERENCIA:  Trunque la tabla «libros» al mismo tiempo, o utilice TRUNCATE ... CASCADE.
"""
TRUNCATE autores CASCADE;

-- ELIMINA VARIAS TABLAS EN CASCADA
"""
NOTICE:  truncando además la tabla «libros»
TRUNCATE TABLE
"""
