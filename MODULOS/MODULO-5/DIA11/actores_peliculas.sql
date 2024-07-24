-- Creación de la tabla de actores
CREATE TABLE actores (
    id_actor INT PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL
);

-- Creación de la tabla de películas
CREATE TABLE peliculas (
    id_pelicula INT PRIMARY KEY,
    pelicula VARCHAR(30),
    genero VARCHAR(30) NOT NULL
);

-- Creación de la tabla intermedia para la relación N:N entre actores y películas
CREATE TABLE actores_peliculas (
    id SERIAL PRIMARY KEY,
    id_pelicula INT,
    id_actor INT,
    FOREIGN KEY (id_actor) REFERENCES Actores(id_actor),
    FOREIGN KEY (id_pelicula) REFERENCES Peliculas(id_pelicula)
);


1:1   1-1    UNO a UNO

1:N  1:*  Uno a MUCHOS

N:N   N:M   N:*   MUCHOS a MUCHOS


Lista - Diccionario de Datos

-- actores                             descripción
id_actor INT PRIMARY KEY, 
nombre VARCHAR(30) NOT NULL

-- películas
id_pelicula INT PRIMARY KEY ,
pelicula VARCHAR(30) ,
genero VARCHAR(30) NOT NULL


-- actores y películas
id SERIAL PRIMARY KEY,
id_pelicula INT FOREIGN KEY,
id_actor INT FOREIGN KEY,
