\l;
CREATE DATABASE osito;
\c osito;
\dt;

CREATE TABLE perros (
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    raza TEXT
);
\dt

SELECT * FROM perros; 
SELECT nombre FROM perros; 

CREATE TABLE personas (
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    apellido TEXT,
    perro INTEGER,
    FOREIGN KEY(perro) REFERENCES perros(id)
);

\dt

SELECT * FROM perros; 
SELECT nombre FROM perros; 

INSERT INTO perros (nombre, raza) VALUES ('boby', 'picho');
INSERT INTO perros (nombre, raza) VALUES ('yiyi', 'doberman'), ('sisi', 'salchicha'),('fufu', 'pekiné');


CREATE TABLE Gatos (
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    raza TEXT
);

create table clientes(
nombre varchar(30),
apellido varchar(30)
);


--! CRUD - CRUD  - SQL 
CREATE  -> INSERT INTO
READ    -> SELECT 
UPDATE  -> UPDATE
DELETE  -> DELETE 

```

```