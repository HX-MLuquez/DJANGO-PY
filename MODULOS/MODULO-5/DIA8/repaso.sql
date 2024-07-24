

CREATE DATABASE rickimint;

\c rickimint;

CREATE TABLE especies (
    id SERIAL PRIMARY KEY, 
    especie TEXT NOT NULL
);

CREATE TABLE personajes (
    id SERIAL PRIMARY KEY, 
    nombre TEXT NOT NULL,
    especie_id INT,
    FOREIGN KEY (especie_id) REFERENCES especies(id)
    -- perfil_id INT,
    -- FOREIGN KEY (perfil_id) REFERENCES perfil(id)
);

CREATE TABLE perfil (
    id SERIAL PRIMARY KEY, 
    descripcion TEXT NOT NULL,
    personaje_id INT,
    FOREIGN KEY (personaje_id) REFERENCES personajes(id)
);

-- la FK en caso de 1:1 esta puede ir en cualquier tabla


-- la FK en caso de 1:N esta DEBE ir en el MUCHOS
-- Una Especie PERTENECE a MUCHOS PERSONAJES
-- La FK si o si DEBE IR       en     |
INSERT INTO especies (especie)
VALUES ('humano'), ('alien'), ('reptil'), ('plutoneano');

INSERT INTO personajes (nombre, especie_id)
VALUES ('Rick Sanches', 1), ('Morty', 1), ('Summer', 1), ('Pomi', 4), ('Mama Reina', 2);


SELECT p.*, e.especie FROM personajes AS p
JOIN especies AS e
ON e.id = p.especie_id;


INSERT INTO personajes (nombre, especie_id)
VALUES ('Auto commit', 3);

--* TRANSACCIONES
BEGIN;
INSERT INTO personajes (nombre, especie_id)
VALUES ('Pajaro', 2);
UPDATE personajes SET especie_id = 4 WHERE nombre = 'Rick Sanches';
SELECT * FROM personajes;
ROLLBACK;
-- Entender el auto COMMIT

BEGIN;
INSERT INTO personajes (nombre, especie_id)
VALUES ('Pajaro', 2);
UPDATE personajes SET especie_id = 4 WHERE nombre = 'Rick Sanches';
SELECT * FROM personajes;
COMMIT;

--* ROLLBACK + TRUNCATE especies CASCADE;
TRUNCATE especies;

BEGIN;
TRUNCATE especies CASCADE;
SELECT * FROM personajes;
ROLLBACK;


--* SAVE-POINT
BEGIN;
DELETE FROM personajes WHERE id = 4;
SELECT * FROM personajes;
SAVEPOINT punto_uno;

TRUNCATE especies CASCADE;
ROLLBACK TO SAVEPOINT punto_uno;

DELETE FROM personajes;
SELECT * FROM personajes;
COMMIT;