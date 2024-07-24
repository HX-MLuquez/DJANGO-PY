

-- GUIA de QUERIES

-- PASO 1
CREATE DATABASE nanana;
-- PASO 2 me conecto a mi db nanana
\c nanana;


"""
!PREVIO a GRABAR

\c postgres;


postgres> DROP DATABASE nanana;
postgres> 
"""

--! IMPORTANTE - Me pueden pasar en un archivo de texto LINK de DRIVE . YOUTUBE . VIMEO 
-- Dentro de carpeta comprimida
-- O directamente el video comprimido dentro de una carpeta
-- Graben en la peor pero + + + baja calidad de video pero con AUDIO



Crea una base de datos llamada desafio-tuNombre-tuApellido-3digitos
(2 Puntos)
Ejemplo: desafio-Camila-Fernandez-931
5. Ingresa a la base de datos creada.
(1 Punto)
6. Crea una tabla llamada clientes, con una columna llamada email de tipo
varchar(50), una columna llamada nombre de tipo varchar sin limitación, una
columna llamada teléfono de tipo varchar(16), un campo llamado empresa de
tipo varchar(50) y una columna de tipo smallint, para indicar la prioridad del
cliente. Ahí se debe ingresar un valor entre 1 y 10, donde 10 es más prioritario.
(2 Puntos)
Hint: No hay que limitar el valor de la columna de prioridad, como tipo de dato se
recomienda ocupar smallint.
7. Ingresa 5 clientes distintos con distintas prioridades, el resto de los valores los
puedes inventar.
(1 Punto)
8. Selecciona los tres clientes de mayor prioridad.
(2 Puntos)
9. Selecciona, de la tabla clientes, una prioridad o una empresa, de forma que el
resultado devuelva 2 registros.
(2 Puntos)
10. Sal de postgreSQL.
