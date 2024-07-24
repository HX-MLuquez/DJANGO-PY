

Actividad guiada: Aplicando rollback en cuentas
bancarias.

Para este ejercicio seguiremos trabajando en la base de datos de cuentas bancarias,
recuerda que la trabajamos en la sesión anterior. La acción de volver atrás las transacciones
que se realicen sobre una tabla la realizaremos a través de save point y rollback.

Resumen de códigos:

CREATE DATABASE banca_test;
\c banca_test;

1. Creación de la tabla:
create table cuentas (
    numero_cuenta int primary key,
    balance float check(balance >= 0.00)
);

"""
 numero_cuenta | balance
---------------+---------
(0 filas)
"""

2. Inserción de registros:
INSERT INTO cuentas (numero_cuenta, balance) values (1, 1000);
INSERT INTO cuentas (numero_cuenta, balance) values (2, 1000);
"""
 numero_cuenta | balance
---------------+---------
             1 |    1000
             2 |    1000
"""
3. Transacción controlada donde pasamos los $1000 de la cuenta 1 a la cuenta 2.
BEGIN;
UPDATE cuentas set balance = balance - 1000 where numero_cuenta = 1;
UPDATE cuentas set balance = balance + 1000 where numero_cuenta = 2;

4. Confirmamos la transacción:
COMMIT;

"""
 numero_cuenta | balance
---------------+---------
             1 |       0
             2 |    2000
(2 filas)
"""

Sin embargo,
podemos verificar que en las transacciones que terminan en error no se altera el
estado de nuestros datos. ¿Y cómo lo hacemos?
Ejecuta el siguiente código en tu terminal.

BEGIN TRANSACTION;
UPDATE cuentas SET balance = balance + 1000 WHERE numero_cuenta = 2;
UPDATE cuentas SET balance = balance - 1000 WHERE numero_cuenta = 1;
"""
select * from cuentas;
ERROR:  transacción abortada, las órdenes serán ignoradas hasta el fin de bloque de transacción
"""
ROLLBACK;
"""
banca_test=!# ROLLBACK;
ROLLBACK
banca_test=# select * from cuentas;
 numero_cuenta | balance
---------------+---------
             1 |       0
             2 |    2000
"""

"""
ERROR:  el nuevo registro para la relación «cuentas» viola la restricción «check» «cuentas_balance_check»
DETALLE:  La fila que falla contiene (1, -1000).
banca_test=!# COMMIT;
ROLLBACK
banca_test=#
"""

Al ejecutarlo veremos el siguiente error debido a la restricción de la columna balance que
realizamos con check al momento de crear la tabla.
DETAIL: Failing row contains (1, -1000).

● Paso 3: Verificamos el estado de la tabla.

select * from cuentas;
"""
banca_test=# select * from cuentas;
 numero_cuenta | balance
---------------+---------
             1 |       0
             2 |    2000
(2 filas)
"""

Como verás no hubo ningún cambio en los datos, a pesar de haber cargado $1000 a la
cuenta 2 primero, esta no se realiza, puesto que la resta al balance de la cuenta 1 devolvió
un error.

Si por alguna razón, en medio de una transacción se decide que ya no se quiere registrar los
cambios (tal vez nos dimos cuenta de que estamos actualizando todos los registros de
nuestra base y no es lo que buscábamos), se puede recurrir a la orden ROLLBACK en lugar
de COMMIT y todas las actualizaciones hasta ese punto quedarán canceladas.

Save point
Recordemos que con Save point podemos tener un mayor control de las transacciones por
medio de puntos de recuperación.

● Paso 4: Intentemos registrar una nueva cuenta de número 3 en nuestra tabla
“cuentas” con un saldo de $5000 y justo luego guardemos ese punto de la
transacción con un SAVEPOINT de nombre “nueva_cuenta”.

BEGIN TRANSACTION;
INSERT INTO cuentas(numero_cuenta, balance) VALUES (3,
5000);

SAVEPOINT nueva_cuenta;

● Paso 5: Hasta este punto tenemos la transacción en curso y hemos fijado que
podríamos volver a este estado en cualquier circunstancia. Ahora, intentemos
transferir a esta nueva cuenta $3000 desde la cuenta 2. Para esto continua la
transacción de la siguiente manera.

UPDATE cuentas SET balance = balance + 3000 WHERE numero_cuenta = 3;
UPDATE cuentas SET balance = balance - 3000 WHERE numero_cuenta = 2;
-- Justo acá deberás recibir un error
ROLLBACK TO nueva_cuenta;
COMMIT;

"""
ERROR:  el nuevo registro para la relación «cuentas» viola la restricción «check» «cuentas_balance_check»
DETALLE:  La fila que falla contiene (2, -1000).
banca_test=!# ROLLBACK TO nueva_cuenta;
ROLLBACK
banca_test=*# commit;
COMMIT
banca_test=# select * from cuentas;
 numero_cuenta | balance
---------------+---------
             1 |       0
             2 |    2000
             3 |    5000
"""

Error generado:
ERROR: new row for relation "cuentas" violates check constraint
"cuentas_balance_check"
DETAIL: Failing row contains (2, -1000).

Como puedes notar se registró con éxito la cuenta 3, no obstante su balance sigue siendo
$5000 y el balance de la cuenta 2 no se redujo. Esto es porque volvimos al punto guardado,
luego de haber hecho la inserción de nuestra nueva cuenta, a pesar de no haberse
procesado lo que le procedía a esa instrucción.

A continuación, deberás insertar al menos 10 registros
INSERT INTO cuentas (numero_cuenta, balance) 
VALUES (4, 300), (5, 120), (6, 10000), (7, 31000), (8, 15000), (9, 7000), (10, 3000);


Una vez ingresados, genera un reporte con los siguientes datos:
● Reporta aquellas cuentas cuyo balance sea mayor a 2000.
SELECT * FROM cuentas WHERE balance > 2000;
"""
SELECT * FROM cuentas WHERE balance > 2000;
 numero_cuenta | balance
---------------+---------
             3 |    5000
             6 |   10000
             7 |   31000
             8 |   15000
             9 |    7000
            10 |    3000
"""


● Reporta cuántas tienen un balance inferior a 1000.
SELECT * FROM cuentas WHERE balance < 1000;
"""
 numero_cuenta | balance
---------------+---------
             1 |       0
             4 |     300
             5 |     120
"""
● Reporta el promedio total de las cuentas registradas según su balance.
SELECT AVG(balance) AS promedio_cuentas FROM cuentas;
"""
 promedio_cuentas
------------------
             7342
"""
● Reporta el promedio de cuentas cuyo balance sea mayor o igual a 10000.
SELECT AVG(balance) AS promedio_cuentas FROM cuentas WHERE balance > 10000;
"""
 promedio_cuentas
------------------
            23000
"""
Para generar este tipo de reportes puedes utilizar herramientas como:
● Google docs.
● Presentaciones de google.
● Word
● Power Point
Para las dos primeras, solo debes acceder a Drive de tu cuenta gmail y agregar los
pantallazos de los resultados a partir de los códigos que hayas implementado en SQL.

ALTER TABLE cuentas ADD COLUMN fecha DATE;

'YYYY-MM-DD'

INSERT INTO cuentas (numero_cuenta, balance, fecha) 
VALUES (44, 34000, '2024-02-11'), (55, 1200, '2024-02-11');

Monto mas alto si alguna fecha se repite 

SELECT * FROM cuentas WHERE fecha = '2024-02-11' ORDER BY balance DESC LIMIT 1;

SELECT MAX(balance) FROM cuentas WHERE fecha = '2024-02-11';


SELECT * FROM cuentas
WHERE balance = (
    SELECT MAX(balance)
    FROM cuentas
    WHERE fecha = '2024-02-11'
);


-- ------------------------------------------------------------------------------------------------
-- ------------------------------------------------------------------------------------------------

--! SUB-QUERIES

Ejemplo 1: Seleccionar las cuentas cuyo balance es mayor que el balance promedio de todas las cuentas

SELECT * FROM cuentas
WHERE balance > (
    SELECT AVG(balance)
    FROM cuentas
);

Solución:
Esto selecciona todas las cuentas cuyo balance es mayor que el balance promedio de todas las cuentas.

Ejemplo 2: Encontrar las cuentas que tienen el balance más bajo en una fecha específica

SELECT * FROM cuentas
WHERE balance = (
    SELECT MIN(balance)
    FROM cuentas
    WHERE fecha = '2024-02-11'
);

Solución:
Esto selecciona la cuenta con el balance más bajo en la fecha '2024-02-11'.

Ejemplo 3: Seleccionar las cuentas cuyo balance es superior al balance de la cuenta número 5

SELECT * FROM cuentas
WHERE balance > (
    SELECT balance
    FROM cuentas
    WHERE numero_cuenta = 5
);

Solución:
Esto selecciona todas las cuentas cuyo balance es mayor que el balance de la cuenta con numero_cuenta igual a 5.

Ejemplo 4: Seleccionar las cuentas creadas en una fecha específica y cuyo balance es mayor que el balance promedio en esa misma fecha

SELECT * FROM cuentas
WHERE fecha = '2024-02-11'
AND balance > (
    SELECT AVG(balance)
    FROM cuentas
    WHERE fecha = '2024-02-11'
);

Solución:
Esto selecciona todas las cuentas creadas en la fecha '2024-02-11' cuyo balance es mayor que el balance promedio de las cuentas en esa misma fecha.

Ejemplo 5: Encontrar las cuentas cuyo balance es mayor que el balance máximo de las cuentas creadas en una fecha específica anterior

SELECT * FROM cuentas
WHERE balance > (
    SELECT MAX(balance)
    FROM cuentas
    WHERE fecha = '2024-02-10'
);

