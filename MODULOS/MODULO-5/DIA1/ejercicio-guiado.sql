
\c postgres;

1. Crear base de datos de nombre "ebuy"
2. Conectarnos a la DB ebuy 
3. Crear la tabla clientes con los atributos id, nombre, apellido, email, nivel ("normal" o "premium")
4. Insertar 5 clientes 
5. Ver lista de tabla/s creadas
6. Ver todos los clientes 
7. Ver todos los clientes donde el nivel sea premium 
8. Ver todos los clientes ordenada descendentemente por nombre 


-- Ayuda de los comandos
CREATE DATABASE ...; 
\c ...;
CREATE TABLE ... (... ..., ... ...);
INSERT INTO ... (..., ...) VALUES (..., ...);
\dt;
SELECT * FROM ...;
SELECT * FROM ... WHERE ... = ...;
SELECT * FROM ... ORDER BY ... ...;

