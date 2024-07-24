-- POSTGRES SQL un motor (sistema de manejo SQL) open source
--todo_ SQL -> Lenguaje estructurado en consultas
-- TABLAS - ENTIDADES (OBJETO)
--   - Filas
--   - Columnas (un atributo específico - atómico )
-- RELACIONAL (PK - FK) - ASOCIACIONES -
-- Base de Datos
-- QUERIES (consultas) ->  Lenguaje (su propia sintáxis)


-- -------------------------------------------------------------------------
-- -------------------------------------------------------------------------
-- -------------------------------------------------------------------------

--!IMPORTANTE - Cada Tabla en sí la podemos pensar como una LISTA
-- personas [{}{}{}]

-- peliculas <- la tabla peliculas es una LISTA -> [{}{}{}{}{}]
```
 PK (único)
 id |                        title                        |   year    |  type
----+-----------------------------------------------------+-----------+--------
  1 | Batman v Superman: Dawn of Justice                  | 2016      | movie
  2 | Superman Returns                                    | 2006      | movie
  3 | Superman                                            | 1978      | movie
  4 | Superman II                                         | 1980      | movie
  5 | Superman III                                        | 1983      | movie
  6 | Batman v Superman: Dawn of Justice Ultimate Edition | 2016      | movie
  7 | Superman IV: The Quest for Peace                    | 1987      | movie
  8 | Superman & Lois                                     | 2021      | series
  9 | Superman/Batman: Apocalypse                         | 2010      | movie
 10 | Lois & Clark: The New Adventures of Superman        | 1993-1997 | series
 11 | The Matrix                                          | 1999      | movie

```

SELECT * FROM peliculas;
--* -> [{}{}{}{}{} etc] <- nos trae una LISTA en definitiva

SELECT * FROM peliculas WHERE id = 4;
--* -> {id:4, "title": "Superman II", "year": "1980", "type": "movie"}
SELECT * FROM peliculas WHERE year = "1980";




-- -------------------------------------------------------------------------
-- -------------------------------------------------------------------------
-- -------------------------------------------------------------------------

--*   SQL  -  NO SQL (MONGO DB) 
-- En NO SQL se usan Colecciones
--  4 | Superman II                                         | 1980      | movie
-- {"id":4, 
-- "title": "Superman II", 
-- "year": "1980", 
-- "type": 
-- "movie"} -  JSON  BSON



-- -------------------------------------------------------------------------
-- -------------------------------------------------------------------------
-- -------------------------------------------------------------------------

-- Ejercicio

CREATE DATABASE ejercicio_ahora;
\c ejercicio_ahora;

CREATE TABLE especies (
    id SERIAL PRIMARY KEY,
    especie TEXT NOT NULL
);

CREATE TABLE personajes (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    especie_id INTEGER,
    FOREIGN KEY (especie_id) REFERENCES especies(id)
);

INSERT INTO especies (especie) VALUES ('Alien'), ('Humano'), ('Kriptoniano');
"""
 id |   especie
----+-------------
  1 | Alien
  2 | Humano
  3 | Kriptoniano
(3 filas)
"""


INSERT INTO personajes (nombre, especie_id) VALUES ('Pepe', 3), ('Manolo', 1), ('Juan', 1), ('Jimena', 2), ('Romina', 1);
"""
 id | nombre | especie_id
----+--------+------------
  1 | Pepe   |          3
  2 | Manolo |          1
  3 | Juan   |          1
  4 | Jimena |          2
  5 | Romina |          1
(5 filas)
"""
-- 1. Buscar a Pepe
SELECT * FROM personajes WHERE nombre = 'Pepe';
"""
 id | nombre | especie_id
----+--------+------------
  1 | Pepe   |          3
(1 fila)

pepe {
    'id': 1,
    'nombre': 'Pepe',
    'especie_id': 3
}
SELECT * FROM especies WHERE id = pepe['especie_id'];
"""
-- 2. Saber especie de Pepe
SELECT * FROM especies WHERE id = 3;


SELECT * FROM especies WHERE id = (SELECT especie_id FROM personajes WHERE nombre = 'Pepe');

"""
MOLDE
personaje {
    id: 1,
    nombre: "...",
    epecie_id = NUMBER  <-   ASOCIADO - RELACIONADO -> tabla especies del atributo  id SERIAL PRIMARY KEY,
}
"""

-- {
--     1
--     2
--     3
--     4 pass  X
--     5
--     6
--     7
--     8
--     9 tel  X
--     10
--     11
--     12
--     13
--     14  X
--     15
-- }