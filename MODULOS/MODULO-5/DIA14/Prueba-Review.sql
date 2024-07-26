

CREATE TABLE respuestas (
    -- usuario_id INT REFERENCES usuario(id) ON DELETE CASCADE,
    usuario_id INT REFERENCES usuario(id),
);

\d respuestas


DELETE FROM usuarios WHERE id = 1;

\d respuestas
'dxdfdsx_sdfsdf_fkey'
ALTER TABLE ... DROP CONSTRAINT 
ALTER TABLE   .... ADD FOREIGN KEY... REFERENCES usuario(id) ON DELETE CASCADE,


-- PARTE 1

1. Crea el modelo (revisa bien cuál es el tipo de relación antes de crearlo), respeta las
claves primarias, foráneas y tipos de datos.

CREATE TABLE peliculas (
    id INT PRIMARY KEY,
    nombre VARCHAR(255),
    annno INT
);

CREATE TABLE tags (
    id INT PRIMARY KEY,
    tag VARCHAR(32)
);

CREATE TABLE peliculas_tags (
    id INT PRIMARY KEY,
    pelicula_id INT REFERENCES peliculas(id),
    tag_id INT REFERENCES tags(id)
);

2. Inserta 5 películas y 5 tags, la primera película tiene que tener 3 tags asociados, la
segunda película debe tener dos tags asociados.

INSERT INTO peliculas (id, nombre, annno)
VALUES (1, 'Peli 1', 1999), (2, 'Peli 2', 1990), (3, 'Peli 3', 1980), (4, 'Peli 4', 2002), (5, 'Peli 5', 2001); 


INSERT INTO tags (id, tag)
VALUES (1, 'Comedia'), (2, 'Drama'), (3, 'Ficción'), (4, 'Acción'), (5, 'Romance'); 

INSERT INTO peliculas_tags (id, pelicula_id, tag_id)
VALUES (1, 1, 1), (2, 1, 5), (3, 1, 2), (4, 2, 3), (5, 2, 4); 

3. Cuenta la cantidad de tags que tiene cada película. Si una película no tiene tags debe
mostrar 0.

SELECT peliculas.nombre,  COUNT(peliculas_tags.tag_id)
FROM peliculas 
LEFT JOIN peliculas_tags ON peliculas.id = peliculas_tags.pelicula_id
GROUP BY peliculas.nombre;

-- Parte 2
CREATE TABLE preguntas (
    id INT PRIMARY KEY,
    pregunta VARCHAR(255),
    respuesta_correcta VARCHAR(255)
);

CREATE TABLE usuarios (
    id INT PRIMARY KEY,
    nombre VARCHAR(255),
    edad INT
);

CREATE TABLE respuestas (
    id INT PRIMARY KEY,
    respuesta VARCHAR(255),
    usuario_id INT REFERENCES usuarios(id),
    pregunta_id INT REFERENCES preguntas(id)
);


4. Crea las tablas respetando los nombres, tipos, claves primarias y foráneas y tipos de
datos.

5. Agrega 5 registros a la tabla preguntas, de los cuales: 
    a. 1. La primera pregunta debe ser contestada correctamente por dos usuarios
    distintos
    b. 2. La pregunta 2 debe ser contestada correctamente por un usuario.
    c. 3. Los otros dos registros deben ser respuestas incorrectas.
    Hint: Contestada correctamente significa que la respuesta indicada en la tabla
    respuestas es exactamente igual al texto indicado en la tabla de preguntas.

INSERT INTO preguntas (id, pregunta, respuesta_correcta)
VALUES (1, 'Como es el sol?', 'Redondo'), (2, 'Como son las estrellas', 'Brillantes'), (3, 'Quien es Julio Cesar', 'Un Emperador'), (4, 'Quien es Violeta Parra', 'Canta autora'), (5, 'cuantos son The Beatles', 'Son cuatro');

INSERT INTO usuarios (id, nombre, edad)
VALUES (1, 'Juana', 19), (2, 'Josefa', 21), (3, 'Jimena', 15), (4, 'Manolo', 33), (5, 'Juan', 44);

INSERT INTO respuestas (id, respuesta, usuario_id, pregunta_id)
VALUES (1, 'Redondo', 1, 1), (2, 'Redondo', 2, 1), (3, 'Brillantes', 3, 2), (4, 'Un cantante', 4, 3), (5, 'Es una actriz', 5, 4);

INSERT INTO respuestas (id, respuesta, usuario_id, pregunta_id)
VALUES (6, 'Un Emperador', 1, 3);
-- preguntas.respuesta_correcta = respuestas.respuesta

6. Cuenta la cantidad de respuestas correctas totales por usuario (independiente de la
pregunta).

SELECT usuarios.nombre, SUM((preguntas.respuesta_correcta = respuestas.respuesta)::int) AS correcta 
FROM usuarios 
JOIN respuestas ON respuestas.usuario_id = usuarios.id
JOIN preguntas ON respuestas.pregunta_id = preguntas.id
GROUP BY usuarios.nombre;
"""
 nombre | correcta
--------+----------
 Juana  |        1
 Josefa |        1
 Jimena |        1
 Manolo |        0
 Juan   |        0
(5 filas)
"""

select u.nombre, COUNT(*) as respuesta_correctas 
from usuarios u 
left join respuestas r on u.id = r.usuario_id 
left join preguntas p on p.id=r.pregunta_id 
WHERE r.respuesta = p.respuesta_correcta 
GROUP BY u.nombre;



7. Por cada pregunta, en la tabla preguntas, cuenta cuántos usuarios tuvieron la
respuesta correcta.

SELECT preguntas.pregunta, COUNT(usuarios.id) AS cantidad_usuarios_con_respusta_correcta 
FROM preguntas
LEFT JOIN respuestas ON respuestas.pregunta_id = preguntas.id 
AND  preguntas.respuesta_correcta = respuestas.respuesta
LEFT JOIN usuarios ON  usuarios.id = respuestas.usuario_id
GROUP BY preguntas.pregunta;

"""
        pregunta         | cantidad
-------------------------+----------
 Como son las estrellas  |        1
 Quien es Julio Cesar    |        0
 Como es el sol?         |        2
 cuantos son The Beatles |        0
 Quien es Violeta Parra  |        0
(5 filas)
"""

8. Implementa borrado en cascada de las respuestas al borrar un usuario y borrar el
primer usuario para probar la implementación.

CREATE TABLE respuestas (
    -- usuario_id INT REFERENCES usuario(id) ON DELETE CASCADE,
    usuario_id INT REFERENCES usuario(id),
);

\d respuestas


DELETE FROM usuarios WHERE id = 1;

\d respuestas
'respuestas_usuario_id_fkey' 

ALTER TABLE respuestas DROP CONSTRAINT respuestas_usuario_id_fkey;
ALTER TABLE respuestas ADD FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE;

DELETE FROM usuarios WHERE id = 1;

9. Crea una restricción que impida insertar usuarios menores de 18 años en la base de
datos.
ALTER TABLE usuarios ADD CONSTRAINT edad CHECK (edad > 18);

10. Altera la tabla existente de usuarios agregando el campo email con la restricción de
único.
ALTER TABLE usuarios ADD COLUMN email VARCHAR(50) UNIQUE;



