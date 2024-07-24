

--* Cuándo usar HAVING - Cuando reemplaza WHERE
-- Cuando necesitas filtrar resultados basados en una función de agregado como 
-- COUNT() (cant de filas o (GROUP -> )repeticiones), SUM(), AVG(), MAX(), MIN(), etc.

create database bbdd_gimnasios;

"""
Paso 3: Creamos la tabla clientes con los siguientes campos:
○ Nombre
○ Apellido
○ Rut
○ Email
"""

CREATE TABLE clientes(
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    rut INTEGER,
    email VARCHAR(50)
);

"""
Paso 4: Modificamos la tabla clientes y definimos que el rut será la clave primaria
(Primary Key)
"""
ALTER TABLE clientes ADD PRIMARY KEY(rut);

"""
Paso 5: Creamos la tabla matrículas con los siguientes campos:
○ Monto
○ Estado
○ Asignamos la clave foránea para la integración de ambas tablas con el Rut.
"""
CREATE TABLE matriculas(
    monto VARCHAR(50),
    estado BOOLEAN,
    cliente_rut INTEGER REFERENCES clientes(rut)
);
    -- cliente_rut INTEGER,
    -- FOREIGN KEY (cliente_rut) REFERENCES clientes(rut)
-- );

"""
Paso 6: Insertamos 5 registros en la tabla clientes.
"""
INSERT INTO clientes VALUES ('Cliente 1', 'Apellido cliente 1', 999999999, 'cliente1@email.com');
INSERT INTO clientes VALUES ('Cliente 2', 'Apellido cliente 2', 888888888, 'cliente2@email.com');
INSERT INTO clientes VALUES ('Cliente 3', 'Apellido cliente 3', 777777777, 'cliente3@email.com');
INSERT INTO clientes VALUES ('Cliente 4', 'Apellido cliente 4', 666666666, 'cliente4@email.com');
INSERT INTO clientes VALUES ('Cliente 5', 'Apellido cliente 5', 555555555, 'cliente5@email.com');


"""
Paso 7: Insertamos 5 registros en la tabla matriculas y los asociamos mediante su
rut a cada cliente.
"""
INSERT INTO matriculas (monto, estado, cliente_rut) VALUES ('40000', TRUE, 999999999);
INSERT INTO matriculas (monto, estado, cliente_rut) VALUES ('40000', FALSE, 888888888);
INSERT INTO matriculas (monto, estado, cliente_rut) VALUES ('55000', TRUE, 555555555);
INSERT INTO matriculas (monto, estado, cliente_rut) VALUES ('35000', TRUE, 777777777);
INSERT INTO matriculas (monto, estado, cliente_rut) VALUES ('60000', FALSE, 666666666);


"""
Paso 8: Utilizar el inner join para que se muestren todos los registros que estén
relacionados. Recordemos que esto se ejecuta siempre que exista una columna que
relacione nuestras dos tablas
"""
SELECT c.email, c.rut, m.monto, m.estado
FROM clientes AS c
INNER JOIN matriculas AS m ON c.rut = m.cliente_rut;

"""
              clientes          |    matriculas
       email        |    rut    | monto | estado
--------------------+-----------+-------+--------
 cliente1@email.com | 999999999 | 40000 | t
 cliente2@email.com | 888888888 | 40000 | f
 cliente5@email.com | 555555555 | 55000 | t
 cliente3@email.com | 777777777 | 35000 | t
 cliente4@email.com | 666666666 | 60000 | f
(5 filas)

"""


"""
Paso 9: Podemos incluso agregar funciones anidadas a la consulta, en este caso
supongamos que queremos ordenar según el monto de cada cliente. El orden será
de manera ascendente, es decir del monto menor al mayor, para ello utilizaremos
order by
"""
select email, rut, monto, estado 
from clientes 
inner join matriculas on clientes.rut = cliente_rut 
order by matriculas.monto;


"""
 email        |    rut    | monto | estado
--------------------+-----------+-------+--------
 cliente3@email.com | 777777777 | 35000 | t
 cliente1@email.com | 999999999 | 40000 | t
 cliente2@email.com | 888888888 | 40000 | f
 cliente5@email.com | 555555555 | 55000 | t
 cliente4@email.com | 666666666 | 60000 | f
(5 filas)
"""


"""
Paso 10: Agrupar consultas, para ello añadiremos una matrícula nueva a un RUT ya
existente. Esta agrupación consistirá en obtener aquellos clientes que tienen más de
una matrícula generada.
"""
select monto, count(monto) 
from matriculas 
group by monto 
having count(monto) >= 2;

"""
 monto | count
-------+-------
 40000 |     2
(1 fila)
"""


"""
Paso 11: Hasta el paso 10 recibimos los datos del registro que tiene dos matrículas
asignadas, pero estos datos están incompletos, no sabemos el nombre de la
persona, su rut ni el email. Para solucionarlo debemos primero agrupar a partir de
aquellos campos que tienen una función de agregado implementada, veamos el
código.
"""
select m.monto, count(m.*) from clientes AS c
inner join matriculas AS m on c.rut = m.cliente_rut 
group by m.monto;


"""
  rut    | monto | count
-----------+-------+-------
 777777777 | 35000 |     1
 999999999 | 40000 |     1
 888888888 | 40000 |     1
 666666666 | 60000 |     1
 555555555 | 55000 |     1
(5 filas)
"""


"""
Paso 12: Ya que tenemos la agrupación de los datos ahora podemos usar
nuevamente having para obtener únicamente aquellos registros con los datos
completos que tengan dos o más matrículas, recuerda la cláusula del having.
"""
select email, rut, monto, estado, count(matriculas.*) from clientes
inner join matriculas on clientes.rut = cliente_rut group by email,
monto, rut, estado having count(matriculas.*) >= 2;

"""
 email | rut | monto | estado | count
-------+-----+-------+--------+-------
(0 filas)
"""

"""
1. Elimina los registros de ambas tablas con delete from nombre_tabla
"""
DELETE FROM matriculas;
"""
2. Agregar el atributo necesario
"""
ALTER TABLE matriculas
ADD COLUMN id SERIAL PRIMARY KEY;

"""
Volver a crear data en matriculas
"""
INSERT INTO matriculas (monto, estado, cliente_rut) VALUES ('40000', TRUE, 999999999);
INSERT INTO matriculas (monto, estado, cliente_rut) VALUES ('40000', FALSE, 888888888);
INSERT INTO matriculas (monto, estado, cliente_rut) VALUES ('35000', FALSE, 888888888);



-- -----------------------------------------------------
-- -----------------------------------------------------
-- -----------------------------------------------------

SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'matriculas'
AND column_name = 'cliente_rut';




--! Damos inicio al desafío, en 50 min pausamos para ver como vienen y a seguir. 
-- Y al cierre vemos preguntas y encuesta

--todo_ Si tienen alguna consulta aquí estoy!!!




--! ---------------------------------------------------------------
-- ---------------------------------------------------------------
--TODO ---> ENCUESTA <--- https://forms.gle/m4UkmSVECYhTMQqGA ---> ENCUESTA <---
-- ---------------------------------------------------------------
--! ------------------------------------ 2 MINUTOS ---------------------------


--! y CIERRE de Q&A ¿?? sobre Desafío del día