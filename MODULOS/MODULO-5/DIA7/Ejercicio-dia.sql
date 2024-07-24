--* Actividad guiada: Mawashi Cars
El programador de la base de datos de la empresa Mawashi Cars Spa ha logrado
avanzar bastante en los requisitos levantados del software, pero luego de mostrarle los
avances al cliente surgieron nuevos requerimientos que deben ser atendidos.
La base de datos de Mawashi Cars SPA debe contener por los momentos dos tablas, una
para autos y otra para ventas.

En la tabla de autos existirán los campos:
● ID
● marca
● modelo
● año
● color
● precio

En la tabla ventas:
● Fecha
● Id_auto
● Cliente
● Referencia
● Cantidad
● Método de pago.

Vamos con los pasos del ejercicio para definir los campos desde SQL.

● Paso 1: Creamos la base de datos con el nombre mawashi_cars.
create database mawashi_cars;

● Paso 2: Nos conectamos a la base de datos.
\c mawashi_cars;

● Paso 3: Creamos la tabla autos.

create table autos(id int primary key, marca varchar(25), modelo
varchar(25), año varchar(25), color varchar(25), precio float);


● Paso 4: Creamos la tabla de ventas.

create table ventas(id serial unique not null, fecha varchar(20),
id_auto int, cliente varchar(25), referencia int, cantidad float,
metodo_pago varchar(10), foreign key (id_auto) references autos(id));


● Paso 5: Insertamos 3 registros en la tabla autos.
insert into autos (id, marca, modelo, año, color, precio) values (1,
'Toyota', 'Corolla Araya', '1991', 'Blanco', 1200000);
insert into autos (id, marca, modelo, año, color, precio) values (2,
'Mazda', 'Mazda 3', '2000', 'Azul',2000000);
insert into autos (id, marca, modelo, año, color, precio) values (3,
'Chevrolet', 'Spark', '1998', 'Verde Oscuro', 1200000);
INSERT INTO autos (id, marca, modelo, año, color, precio) VALUES (4,
'Nissan', 'Versa', 2018, 'Gris Plata', 5000000);
INSERT INTO autos (id, marca, modelo, año, color, precio) VALUES (5,
'Hyundai', 'Accent', 2022, 'Rojo', 10500000);
INSERT INTO autos (id, marca, modelo, año, color, precio) VALUES (6,
'Kia', 'Rio', 2020, 'Negro', 8000000);
INSERT INTO autos (id, marca, modelo, año, color, precio) VALUES (7,
'Volkswagen', 'Gol', 2015, 'Azul Marino', 3500000);
INSERT INTO autos (id, marca, modelo, año, color, precio) VALUES (8,
'Fiat', 'Mobi', 2017, 'Blanco', 2800000);
INSERT INTO autos (id, marca, modelo, año, color, precio) VALUES (9,
'Suzuki', 'Swift', 2019, 'Gris Oxford', 6200000);
INSERT INTO autos (id, marca, modelo, año, color, precio) VALUES (10,
'Peugeot', '208', 2021, 'Rojo', 9800000);

● Paso 6: Insertamos algunas ventas.
insert into ventas (fecha, id_auto, cliente, referencia, cantidad,
metodo_pago) values('2020-10-15', 1, 'Chuck', 43224, 12000000,
'Débito');
insert into ventas (fecha, id_auto, cliente, referencia, cantidad,
metodo_pago) values('2020-11-15', 1, 'Donnie', 43334, 12000000,
'Transfer');
insert into ventas (fecha, id_auto, cliente, referencia, cantidad,
metodo_pago) values('2020-12-15', 3, 'Jet', 43444, 12000000, 'Cheque');
insert into ventas (fecha, id_auto, cliente, referencia, cantidad,
metodo_pago) values('2021-01-05', 1, 'Peter', 43335, 12000000,
'Débito');
insert into ventas (fecha, id_auto, cliente, referencia, cantidad,
metodo_pago) values('2021-01-15', 1, 'Abigail', 43554, 12000000,
'Transfer');
insert into ventas (fecha, id_auto, cliente, referencia, cantidad,
metodo_pago) values('2021-02-01', 3, 'Jhon', 43456, 12000000, 'Cheque');
INSERT INTO ventas (fecha, id_auto, cliente, referencia, cantidad,
metodo_pago)
VALUES ('2021-02-01', 2, 'Walter', 54321, 2000000, 'Efectivo');
INSERT INTO ventas (fecha, id_auto, cliente, referencia, cantidad,
metodo_pago)
VALUES ('2021-03-15', 3, 'Sarah', 54322, 1200000, 'Tarjeta');
INSERT INTO ventas (fecha, id_auto, cliente, referencia, cantidad,
metodo_pago)
VALUES ('2021-04-05', 4, 'Jessica', 54323, 5000000, 'Débito');
INSERT INTO ventas (fecha, id_auto, cliente, referencia, cantidad,
metodo_pago)
VALUES ('2021-05-25', 5, 'Luis', 54324, 10500000, 'Transfer');

● Paso 7: Obtenemos un reporte con el nombre de los clientes registrados en la tabla
venta, junto con la marca y el modelo del auto asociado a la venta realizada.

SELECT cliente, marca, modelo FROM ventas INNER JOIN autos ON
ventas.id_auto=autos.id;

-- Ejercicio propuesto 1
La empresa Mawashi Cars ha notado que aproximadamente un 30% de sus autos no se han
vendido y está considerando la posibilidad de negociar un convenio con una compañía
aliada con estos vehículos, pero necesitará una tabla que muestre los autos que no han sido
vendidos.
Realizar la consulta necesaria para obtener todos los autos cuyos id no se encuentran en la
tabla Ventas.
SELECT  

-- Ejercicio propuesto 2
El dueño de la empresa Mawashi Cars se dio cuenta que para facilitar el proceso de
auditoría, sería beneficioso saber los registros que no tienen relación entre ambas tablas
para hacer el cruce con la información cedida anteriormente y terminar la auditoría.
Realizar la sentencia SQL necesaria para satisfacer este requerimiento
SELECT 

--* EXTRAS
-- Ejercicio propuesto 3: Contar el número total de ventas realizadas por cada método de pago.
SELECT metodo_pago, COUNT(*) AS ventas
FROM ventas
GROUP BY metodo_pago;

"""
 metodo_pago | ventas
-------------+--------
 Transfer    |      3
 Cheque      |      2
 Efectivo    |      1
 Tarjeta     |      1
 Débito      |      3
"""

-- Ejercicio propuesto 4: Obtener la suma total de ingresos por cada cliente.
SELECT cliente, SUM(cantidad) AS total_ingresos
FROM ventas
GROUP BY cliente;

"""
 cliente | total_ingresos
---------+----------------
 Jet     |       12000000
 Chuck   |       12000000
 Peter   |       12000000
 Donnie  |       12000000
 Jessica |        5000000
 Walter  |        2000000
 Sarah   |        1200000
 Abigail |       12000000
 Luis    |       10500000
 Jhon    |       12000000
"""

-- Ejercicio propuesto 5: Listar todas las ventas realizadas después del 1 de enero de 2021.
SELECT *
FROM ventas
WHERE fecha > '2021-01-01';

SELECT ventas.*, autos.*
FROM ventas 
JOIN autos 
ON ventas.id_auto = autos.id 
WHERE fecha > '2021-01-01';

"""
 id |   fecha    | id_auto | cliente | referencia | cantidad | metodo_pago
----+------------+---------+---------+------------+----------+-------------
  4 | 2021-01-05 |       1 | Peter   |      43335 | 12000000 | Débito
  5 | 2021-01-15 |       1 | Abigail |      43554 | 12000000 | Transfer
  6 | 2021-02-01 |       3 | Jhon    |      43456 | 12000000 | Cheque
  7 | 2021-02-01 |       2 | Walter  |      54321 |  2000000 | Efectivo
  8 | 2021-03-15 |       3 | Sarah   |      54322 |  1200000 | Tarjeta
  9 | 2021-04-05 |       4 | Jessica |      54323 |  5000000 | Débito
 10 | 2021-05-25 |       5 | Luis    |      54324 | 10500000 | Transfer
"""

-- Ejercicio propuesto 6: Obtener la suma total de ingresos por cada marca de auto.
SELECT autos.marca, SUM(ventas.cantidad) AS ventas 
FROM ventas 
JOIN autos 
ON ventas.id_auto = autos.id 
GROUP BY autos.marca;

"""
   marca   |  ventas
-----------+----------
 Chevrolet | 25200000
 Toyota    | 48000000
 Nissan    |  5000000
 Hyundai   | 10500000
 Mazda     |  2000000
"""


--> Encuesta de cierre de día https://forms.gle/m4UkmSVECYhTMQqGA


SELECT c.nombre, c.apellido 
FROM clientes AS c
LEFT JOIN cuentas AS cu
ON c.id = cu.cliente_id
WHERE cu.numero_cuenta NOT IN (SELECT numero_cuenta FROM cuentas); --! ERROR

SELECT * FROM clientes WHERE id NOT IN (SELECT cliente_id from cuentas);

