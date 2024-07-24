
const ejercicio02 = '';
SELECT * FROM movies WHERE duration < 90;
-- SELECT id, title, year, ratings, duration, "originalTitle", "releaseDate", actors FROM movies WHERE duration < 90;
SELECT id, title, year, duration, "originalTitle", "releaseDate", actors FROM movies WHERE duration < 90;

const ejercicio03 = '';
SELECT * FROM movies WHERE year BETWEEN 1930 AND 1940;
SELECT id, title, year, duration, "originalTitle", "releaseDate", actors FROM movies WHERE year BETWEEN 1930 AND 1940;

const ejercicio04 = '';
SELECT title FROM movies WHERE title LIKE '%til%';
-- con el LIKE no funcionan las comillas "" solo las ''

const ejercicio05 = '';
SELECT title FROM movies WHERE cardinality (actors) = 1;

const ejercicio06 = '';
SELECT title, AVG(rating) FROM movies, unnest(ratings) rating GROUP BY title;

const ejercicio07 = '';
SELECT actors FROM movies WHERE title LIKE '%Fast and%' AND year = 2016;


-- cardinality: La función cardinality() en SQL se utiliza para obtener el número de elementos 
-- en un conjunto de datos que se almacena como un arreglo.

--! Recordar que en sql no se almacenan objetos y/o arreglos pero por medio de una herramienta como postgres si.
-- Si no se está usando PostgreSQL o una implementación similar que permita almacenar objetos y arreglos, 
-- entonces no se pueden almacenar directamente en una tabla de SQL.
--! unnest() descompone cada elemento del array en una columna separada

--! AVG es una función de agregación en SQL que se utiliza para calcular el promedio de un conjunto de valores numéricos.

