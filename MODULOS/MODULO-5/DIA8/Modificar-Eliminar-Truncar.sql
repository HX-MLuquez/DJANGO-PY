


CREATE DATABASE columna;

\c columna


CREATE TABLE phones (
    id INT PRIMARY KEY,
    modelo VARCHAR(50),
    mac_address INT UNIQUE,
    fecha VARCHAR(50)
);

INSERT INTO phones (id, modelo, mac_address, fecha)
VALUES (1, 'Moto 14', '1B:231D', '2024-07-17');
--! ERROR

ALTER TABLE phones ALTER COLUMN mac_address TYPE VARCHAR(50);

INSERT INTO phones (id, modelo, mac_address, fecha)
VALUES (1, 'Moto 14', '1B:231D', '2024-07-17');

SELECT * FROM phones;

ALTER TABLE phones ALTER COLUMN mac_address SET NOT NULL;

-- Probar el funcionamiento de la constrain aplicada mac_address
INSERT INTO phones (id, modelo, fecha)
VALUES (2, 'Moto 280321', '2024-07-17');
--! ERROR

INSERT INTO phones (id, modelo, mac_address, fecha)
VALUES (2, 'Moto 280321', 'AS8979', '2024-07-17');

--* DROP <- Arranca <- Quita la tabla dropeada de la DB
DROP TABLE phones;
--! CUIDADO


DELETE FROM phones; -- <- acompañado WHERE
-- OR
TRUNCATE phones; -- <- Tiene la posibilidad de ELIMINAR en CASCADA

Incorporando los siguientes 
campos a la tabla phones:
● Memoria interna.  memoria_interna
● Memoria ram.  memoria_ram
● Peso.   peso 
● Dimensiones.   dimensiones 
Para estos campos considera que son datos que mezclan datos numéricos y de 
texto. Recuerda asignar el tipo de dato a cada campo la restricción de nulidad.

ALTER TABLE phones ADD COLUMN memoria_interna TEXT NOT NULL;
ALTER TABLE phones ADD COLUMN memoria_ram VARCHAR(50) NOT NULL;
ALTER TABLE phones ADD COLUMN peso VARCHAR(50) NOT NULL;
ALTER TABLE phones ADD COLUMN dimensiones VARCHAR(50) NOT NULL;

INSERT INTO phones (id, modelo, mac_address, fecha, memoria_interna, memoria_ram, peso, dimensiones)
VALUES (2, 'Moto 280321', 'AS8979', '2024-07-17', 'b', 'b', 'b', 'b');

 "phones_pkey" PRIMARY KEY, btree (id)

ALTER TABLE phones ADD PRIMARY KEY (modelo);
-- Error ya que ya tiene PK 

-- Sacamos la PK de la tabla
ALTER TABLE phones DROP CONSTRAINT phones_pkey;

-- Agregamos la PK a la tabla anexada a la columna id
ALTER TABLE phones ADD PRIMARY KEY (id);

--* APLICAR CONSTRAIN SERIAL al ID

--* CREAR
-- Crear la SECUENCIA - SERIAL
CREATE SEQUENCE phones_id_seq;
--* DEFINIR
-- Configuracion
ALTER TABLE phones ALTER COLUMN id SET DEFAULT nextval('phones_id_seq');




----------------------------------------------


CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

INSERT INTO productos (nombre)
VALUES ('raqueta'), ('pelota'), ('bate');

SELECT * FROM productos;

DELETE FROM productos;


TRUNCATE productos;


