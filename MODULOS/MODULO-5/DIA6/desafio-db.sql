
CREATE DATABASE desafio_mauro;
\c desafio_mauro;


CREATE TABLE IF NOT EXISTS inscritos (
    id SERIAL PRIMARY KEY,
    cantidad INT, 
    fecha DATE, 
    fuente VARCHAR(50)
);

INSERT INTO inscritos(cantidad, fecha, fuente)
VALUES ( 44, '01/01/2021', 'Blog' ), ( 56, '01/01/2021', 'Página' ), ( 39, '01/02/2021', 'Blog' ),
( 81, '01/02/2021', 'Página' ), ( 12, '01/03/2021', 'Blog' ), ( 91, '01/03/2021', 'Página' ),
( 48, '01/04/2021', 'Blog' ), ( 45, '01/04/2021', 'Página' ), ( 55, '01/05/2021', 'Blog' ),
( 33, '01/05/2021', 'Página' ), ( 18, '01/06/2021', 'Blog' ), ( 12, '01/06/2021', 'Página' ),
( 34, '01/07/2021', 'Blog' ), ( 24, '01/07/2021', 'Página' ), ( 83, '01/08/2021', 'Blog' ),
( 99, '01/08/2021', 'Página' );

-- Consulta 1: ¿Cuántos registros hay?
SELECT * FROM inscritos;

SELECT COUNT(*) AS registros FROM inscritos;

"""
 registros
-----------
        16
"""

-- Consulta 2: ¿Cuántos inscritos hay en total?
SELECT SUM(cantidad) AS total_inscritos FROM inscritos;

cantidad
"""
 total_inscritos
-----------------
             774
"""

-- Consulta 3: ¿Cuál o cuáles son los registros de mayor antigüedad? - HINT: ocupar subconsultas
SELECT * FROM inscritos ORDER BY fecha LIMIT 2;

SELECT MIN(fecha) FROM inscritos; -->  2021-01-01

SELECT * FROM inscritos WHERE fecha = (SELECT MIN(fecha) FROM inscritos);

SELECT * FROM inscritos WHERE fecha = (SELECT fecha FROM inscritos ORDER BY fecha LIMIT 1);
SELECT fecha FROM inscritos ORDER BY fecha LIMIT 1;


SELECT fecha FROM inscritos ORDER BY fecha LIMIT 3;
SELECT * FROM inscritos WHERE fecha IN (SELECT fecha FROM inscritos ORDER BY fecha LIMIT 3);
"""
 id | cantidad |   fecha    | fuente
----+----------+------------+--------
  2 |       56 | 2021-01-01 | Página
  1 |       44 | 2021-01-01 | Blog
"""

-- Consulta 4: ¿Cuántos inscritos hay por día? (entendiendo un día como una fecha distinta de ahora en adelante)
SELECT SUM(cantidad) AS total_inscritos FROM inscritos;

SELECT fecha,  SUM(cantidad) AS total_inscritos_dia
FROM inscritos
GROUP BY fecha ORDER BY fecha;
"""
   fecha    | total_inscritos_dia
------------+---------------------
 2021-01-01 |                 100
 2021-02-01 |                 120
 2021-03-01 |                 103
 2021-04-01 |                  93
 2021-05-01 |                  88
 2021-06-01 |                  30
 2021-07-01 |                  58
 2021-08-01 |                 182
"""

-- Consulta 5: ¿Qué día se inscribió la mayor cantidad de personas y cuántas personas se inscribieron ese día?
SELECT fecha,  SUM(cantidad) AS total_inscritos_dia
FROM inscritos
GROUP BY fecha 
ORDER BY total_inscritos_dia DESC
LIMIT 1;
"""
  fecha     | total_inscritos_dia
------------+---------------------
 2021-08-01 |                 182
"""
