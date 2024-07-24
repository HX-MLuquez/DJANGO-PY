

"""
Paso 1: Creamos una base de datos de comidas típicas chilenas.
"""
CREATE DATABASE comidas_tipicas;
"""
● Paso 2: Creamos una tabla llamada cocina chilena con los campos id y 
nombre. 
"""
CREATE TABLE cocina_chilena(
    id INTEGER,            -- NUMBER siempre INTEGER
    nombre VARCHAR(50) -- STRING siempre
);


"""
Paso 3: Insertamos 2 registros a la tabla con sus respectivos campos.
"""
INSERT INTO cocina_chilena (id, nombre) VALUES (1,'Pastel de choclo');
INSERT INTO cocina_chilena (id, nombre) VALUES (2, 'Umitas');

"""
Paso 4: Para actualizar un registro utilizamos update.
"""
--! Es muy IMPORTANTE que el DELETE como el UPDATE ver siempre de si tiene que ir acompañado de un WHERE
UPDATE cocina_chilena SET nombre='Humitas' WHERE id = 2;
"""
Con el código SQL anterior estamos:
1. Utilizamos la sentencia update.
2. Pasamos el nombre de la tabla en la cual se ejecutará el update
3. Utilizamos set, seleccionamos el nombre de la columna y el nuevo valor para el 
registro.
4. Evaluamos condicionalmente con where la selección del registro cuyo ID sea 2.
"""

"""
Ingresa 3 registros más a la tabla e intenciona el update en al menos 2 de ellos
"""
INSERT INTO cocina_chilena (id, nombre) VALUES (3, 'Paltas'), (44, 'Langostino'), (5, 'Azado');

UPDATE cocina_chilena SET nombre='Asado' WHERE id = 5;
UPDATE cocina_chilena SET id=4 WHERE id = 44;


"""
Paso 5: Eliminar un registro lo podremos hacer con la sentencia Delete. Así 
como hicimos con la actualización, utilizaremos el id para capturar un registro 
puntual.
"""
DELETE FROM cocina_chilena WHERE id = 4;

"""
Paso 6: Eliminar múltiples registros en la tabla. Para ello añadiremos platos de 
cocina chilena.
"""
INSERT INTO cocina_chilena (id, nombre) VALUES (6,'Cazuela');
INSERT INTO cocina_chilena (id, nombre) VALUES (7,'Empanada chilena');
INSERT INTO cocina_chilena (id, nombre) VALUES (8,'Charquicán');

--* IN
DELETE FROM cocina_chilena WHERE id IN (3, 4, 5);




-- -----------------------------------------------------------------
-- -----------------------------------------------------------------
-- -----------------------------------------------------------------
"""
Crea una nueva base de datos, en ella deberás almacenar información de perros o 
gatos, los campos deberán ser:
1. ID
2. Nombre
3. Raza
4. Edad
Ingresa al menos unos 5 registros e intenciona las acciones de:
"""
● Update.
● Delete.

CREATE TABLE perros (
    id INTEGER PRIMARY KEY,
    nombre VARCHAR(50),
    raza VARCHAR(50),
    edad INTEGER 
);

INSERT INTO perros (id, nombre, raza, edad) 
VALUES (1, 'Boby', 'Picho', 21), (2, 'Fido', 'Doberman', 1), (3, 'Can', 'Salchicha', 7), (4, 'Dingo', 'San Bernardo', 4), (5, 'Willy', 'Caniche', 12);

UPDATE perros SET edad = 101;

SELECT * FROM perros;
"""
[ {}, {}, {}, {}, {}]
"""

SELECT * FROM perros WHERE id = 3;
"""
    {
        'id': 3,
        'nombre': 'Can',
        'raza': 'Salchicha',
        'edad': 7
    }
"""

--! CUIDADO con el PERRO
DELETE FROM perros;



INSERT INTO cocina_chilena (id, nombre, descripcion) VALUES (88,'Chuju', 'Es muy picante');

"""
    {
        'id': ...,
        'nombre': '...',
        'descripcion': '', None 
    }

    [ {}, {}, {}, {}, {}]
    comidas[0]['descripcion']
"""



"""
 id |      nombre      |  descripcion
----+------------------+----------------
  1 | Pastel de choclo |
  2 | Humitas          |
  6 | Cazuela          |
  7 | Empanada chilena |
  8 | Charquicán       |
 88 | Chuju            | Es muy picante
(6 filas)
"""

--* IN - Nos brinda comparar no por un solo dato sino por varios
SELECT * FROM cocina_chilena WHERE nombre IN ('Humitas', 'Cazuela', 'Chuju');


CREATE TABLE usuarios (
    id INTEGER NOT NULL,
    nombre VARCHAR(50),
    rut VARCHAR(50) UNIQUE
);

INSERT INTO usuarios (id, nombre, rut) VALUES (88,'Ema', '7777');
INSERT INTO usuarios (id, nombre, rut) VALUES (1,'Toto', '7777');



CREATE TABLE nunusuarios (
    id INTEGER,
    nombre VARCHAR(50),
    rut VARCHAR(50) 
);
INSERT INTO nunusuarios (id, nombre, rut) VALUES (88,'Ema', '7777');
INSERT INTO nunusuarios (id, nombre, rut) VALUES (1,'Toto', '7777');



Primary Key: Es un tipo de restricción que impedirá que un dato pueda repetirse.
Primary Key => Not Null + Unique

● Foreign Key: Estas claves son otro tipo de restricción que impedirán que se agregue 
un registro asociado a uno no existente, o que se borre un registro relacionado.

 id INTEGER PRIMARY KEY, -- == id INTEGER NOT NULL UNIQUE,



-- --------------------------------------------------------------------------
-- --------------------------------------------------------------------------
CREATE DATABASE viajes;
\c viajes;


CREATE TABLE boletos (
    id INTEGER PRIMARY KEY,
    numero_asiento VARCHAR(50) NOT NULL UNIQUE,
    clase VARCHAR(50) NOT NULL
); 

CREATE TABLE pasajeros (
    id INTEGER PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    rut VARCHAR(50) UNIQUE,
    boleto_id INTEGER,
    FOREIGN KEY (boleto_id) REFERENCES boletos(id)
);


INSERT INTO boletos (id, numero_asiento, clase) 
VALUES (1,'RS-12', 'alta'), (5,'MS-12', 'media'), (6,'MS-11', 'media');

INSERT INTO pasajeros (id, nombre, rut, boleto_id) 
VALUES (1,'Lucas', '7777', 6), (2,'Penelope', '5555', 5);



--! ERROR 'RS-12' ya existe
INSERT INTO boletos (id, numero_asiento, clase) 
VALUES (11,'RS-12', 'baja');

--! ERROR falta nombre que tiene NOT NULL
INSERT INTO pasajeros (id, rut, boleto_id) 
VALUES (1, '7777', 6);

--! ERROR  la KEY 15 NO existe en la tabla boletos
INSERT INTO pasajeros (id, nombre, rut, boleto_id) 
VALUES (101,'Pepe', '3333', 15);


"""
ASI debe SER
UN pasajero tiene UN boleto
Un boleto pertenece a UN pasajero

RELACIÓN de 1:1



!ASí lo hemos realizado AHORA
UN pasajero tiene UN boleto
UN boleto pertenece a MUCHOS pasajeros

RELACIÓN de 1:N     1:*
"""
INSERT INTO pasajeros (id, nombre, rut, boleto_id) 
VALUES (101,'Pepe', '3333', 5);

UPDATE pasajeros SET boleto_id = 1 WHERE id = 101;

DELETE FROM pasajeros WHERE id =1;
"""
RELACIÓN de N:M    *:*  MUCHOS a MUCHOS 

boletos
 id | numero_asiento | clase
----+----------------+-------
  1 | RS-12          | alta
  5 | MS-12          | media
  6 | MS-11          | media

pasajeros
 id  |  nombre  | rut  | 
-----+----------+------+-
   1 | Lucas    | 7777 |        
   2 | Penelope | 5555 |         
 101 | Pepe     | 3333 |        


SE CREA NUEVA TABLA INTERMEDIA (compuesta) y tiene puras FK
pasajeros_boletos

 id  |  boleto_id  | pasajero_id  | 
-----+-------------+--------------+-
   1 |     1       |     1        |         
   2 |     5       |     1        |         
   3 |     6       |     101      |         
   4 |     1       |     101      |   


"""

SERIAL PRIMARY KEY <- Se agrega solo <- se va auto incrementando y nunca se repite

CREATE TABLE vuelos (
    id SERIAL PRIMARY KEY,
    numero_vuelo VARCHAR(50) NOT NULL UNIQUE,
    boleto_id INTEGER,
    pasajero_id INTEGER,
    FOREIGN KEY (boleto_id) REFERENCES boletos(id),
    FOREIGN KEY (pasajero_id) REFERENCES pasajeros(id)
); 

INSERT INTO vuelos (numero_vuelo, boleto_id, pasajero_id) 
VALUES ('777', 5, 2);



TIPO de DATOS
CHAR VARCHAR(50) TEXT STRING son lo mismo 

NUMEROS  INTEGER FLOAT 

BOOLEAN    True False

DATE TIMESTAMP    fecha

--! CUIDADO - ERRORES - RELACIONES - EFECTO CASCADA de RELACIONES de DATOS
DELETE FROM boletos;

ALTER TABLE boletos ADD COLUMN precio INTEGER NOT NULL;
ALTER TABLE boletos ADD COLUMN fecha VARCHAR(50) NOT NULL;


INSERT INTO boletos (id, numero_asiento, clase, precio, fecha) 
VALUES (1,'RS-12', 'alta', 123, '2024-07-09'), (5,'MS-12', 'media', 23, '2024-07-09'), (6,'MS-11', 'media', 55, '2024-07-09');