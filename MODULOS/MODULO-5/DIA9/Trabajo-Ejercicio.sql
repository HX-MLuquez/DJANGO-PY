

Instalamos

En postgres -> botón derecho y crear base de datos 


en la CMD
> sc query postgresql-x64-14

> db -> esquemas -> tablas -> impor data <- archivo .csv 

> peliculas -> ver tabla -> propiedades -> DDL
-- public.peliculas definition

-- Drop table

-- DROP TABLE public.peliculas;

CREATE TABLE public.peliculas (
	id int4 NULL,
	"Pelicula" varchar(64) NULL,
	"Año estreno" int4 NULL,
	"Director" varchar(50) NULL
);


> peliculas -> leer datos en la consola SQL
SELECT id, "Pelicula", "Año estreno", "Director"
FROM public.peliculas;

select max("Año estreno") from peliculas;
select count(id) from peliculas where "Director" = 'Peter Jackson'

SELECT id, "Pelicula", "Año estreno", "Director"
FROM peliculas where "Director" ilike '%tim%';

