# bases de datos de tipo SQL y DBMS - PostgreSQL:

1. ¿Qué significa SQL?
- a) Structured Query Language
- b) Structured Question Language
- c) Structured Queue Language
- d) Structured Quorum Language

2. ¿Qué es un DBMS?
- a) Una base de datos relacional
- b) Un sistema de gestión de bases de datos
- c) Un lenguaje de programación
- d) Un sistema operativo

3. ¿Qué es PostgreSQL?
- a) Un lenguaje de programación
- b) Una base de datos relacional
- c) Un sistema operativo
- d) Un sistema de gestión de bases de datos

4. ¿Cuál es el comando SQL para seleccionar todos los datos de una tabla llamada "clientes"?
- a) SELECT ALL FROM clientes;
- b) SELECT clientes;
- c) SELECT * FROM clientes;
- d) SELECT datos FROM clientes;

5. ¿Cuál es el comando SQL para eliminar una tabla llamada "productos"?
- a) DELETE productos;
- b) DROP TABLE productos;
- c) REMOVE productos;
- d) DESTROY TABLE productos;

6. ¿Cuál es el comando SQL para agregar una nueva fila a una tabla llamada "empleados"?
- a) ADD ROW empleados (column1, column2) VALUES (value1, value2);
- b) INSERT INTO empleados (column1, column2) VALUES (value1, value2);
- c) CREATE ROW empleados (column1, column2) VALUES (value1, value2);
- d) APPEND empleados (column1, column2) VALUES (value1, value2);

7. ¿Qué es una PK (clave primaria) en una tabla? **PK**
- a) Un campo que identifica de manera única cada fila de una tabla
- b) Un campo que se utiliza para ordenar los datos en una tabla
- c) Un campo que se utiliza para filtrar los datos en una tabla
- d) Un campo que se utiliza para unir varias tablas

8. ¿Qué es una consulta SQL?
- a) Una solicitud para agregar o eliminar una fila en una tabla
- b) Una solicitud para modificar una fila en una tabla
- c) Una solicitud para recuperar datos de una o varias tablas
- d) Una solicitud para crear una nueva tabla en una base de datos

9. ¿Qué es una restricción de clave externa en una tabla? **FK**
- a) Un campo que identifica de manera única cada fila de una tabla
- b) Un campo que se utiliza para ordenar los datos en una tabla
- c) Un campo que se utiliza para unir varias tablas
- d) Un campo que asegura que los valores en una columna de la tabla están presentes en otra tabla

10. ¿Cuál es el comando SQL para actualizar los datos en una tabla llamada "productos"?
- a) UPDATE productos SET datos;
- b) MODIFY productos datos;
- c) CHANGE productos datos;
- d) ALTER TABLE productos SET datos;

11. ¿Qué es una transacción en una base de datos?
- a) Un conjunto de operaciones que se realizan en una base de datos como una unidad lógica
- b) Un conjunto de tablas relacionadas en una base de datos
- c) Un conjunto de comandos SQL que se ejecutan juntos en una base de datos
- d) Una operación que se realiza en una base de datos en un momento específico

12. ¿Qué es un índice en una base de datos? - Nosotros no los trabajamos **?**
- a) Un conjunto de tablas relacionadas en una base de datos
- b) Una herramienta para ordenar los datos en una tabla
- c) Un campo que identifica de manera única cada fila de una tabla
- d) Una estructura de datos que mejora el rendimiento de las consultas en una tabla

13. ¿Qué es una vista en una base de datos? - Nosotros no los trabajamos **?**
- a) Una copia de seguridad de una base de datos
- b) Una tabla virtual que se crea a partir de una o varias tablas existentes
- c) Un conjunto de reglas que se aplican a una tabla
- d) Un conjunto de comandos SQL que se ejecutan juntos en una base de datos
```sql
-- Crear una vista que une 'empleados' con 'departamentos'
CREATE VIEW vista_empleados_departamentos AS
SELECT e.nombre AS empleado_nombre, d.nombre AS departamento_nombre
FROM empleados e
JOIN departamentos d ON e.departamento_id = d.id;

SELECT * FROM vista_empleados_departamentos;
```

14. ¿Qué es una función en una base de datos? - Nosotros no los trabajamos **?**
- a) Un conjunto de comandos SQL que se ejecutan juntos en una base de datos
- b) Un conjunto de reglas que se aplican a una tabla
- c) Un programa que realiza una tarea específica en una base de datos
- d) Un conjunto de tablas relacionadas en una base de datos

15. ¿Qué es una subconsulta en una base de datos?
- a) Una consulta que se ejecuta después de que se complete otra consulta
- b) Una consulta que se ejecuta dentro de otra consulta
- c) Una consulta que se ejecuta en una tabla secundaria
- d) Una consulta que se ejecuta en una tabla relacionada

16. ¿Qué es una base de datos NoSQL? - Nosotros no los trabajamos **?**
- a) Una base de datos que utiliza SQL para realizar consultas
- b) Una base de datos que utiliza tablas y relaciones
- c) Una base de datos que no utiliza SQL para realizar consultas
- d) Una base de datos que solo se puede acceder en línea





## Ejemplos

### Transacción
Supongamos que tienes una tabla "cuentas" en una base de datos que contiene información sobre cuentas bancarias, incluyendo el número de cuenta, el nombre del titular y el saldo. Quieres transferir $500 de la cuenta 1234 a la cuenta 5678. Para hacer esto, necesitarás realizar dos operaciones en la base de datos: actualizar el saldo de la cuenta 1234 y actualizar el saldo de la cuenta 5678. Para asegurarte de que estas operaciones se realicen correctamente, puedes utilizar una transacción.

En SQL, una transacción se inicia con el comando "BEGIN" y se finaliza con el comando "COMMIT" o "ROLLBACK". Aquí está el ejemplo de cómo se vería una transacción para la transferencia de dinero:

```sql
BEGIN;
UPDATE cuentas SET saldo = saldo - 500 WHERE num_cuenta = 1234;
UPDATE cuentas SET saldo = saldo + 500 WHERE num_cuenta = 5678;
COMMIT;
```

### Restricción
 Una restricción es una regla que se aplica a los datos de una tabla, y se utiliza para garantizar que los datos sean precisos, consistentes y coherentes.

Una restricción puede ser de varios tipos, por ejemplo:

- Restricción de clave primaria (primary key): garantiza que los valores en una columna sean únicos y no nulos.
- Restricción de clave externa (foreign key): garantiza que los valores en una columna correspondan a los valores en otra columna en otra tabla.
- Restricción de verificación (check constraint): garantiza que los valores en una columna cumplan con una condición específica.
- Restricción de unicidad (unique constraint): garantiza que los valores en una columna sean únicos, pero permite que haya valores nulos.




## DATO de color

Empresas importantes que utilizan SQL como sistema de gestión de datos:

- Facebook: Utiliza MySQL como su sistema de gestión de bases de datos relacional para almacenar y administrar una gran cantidad de datos de usuarios.

- Google: Utiliza Google BigQuery, que es una base de datos de análisis de datos en la nube que utiliza SQL como lenguaje de consulta.

- Amazon: Utiliza Amazon Relational Database Service (RDS), que es un servicio de bases de datos relacional que admite múltiples motores de bases de datos, incluido MySQL y PostgreSQL.

- Uber: Utiliza MySQL como su sistema de gestión de bases de datos relacional para almacenar y administrar datos de usuarios, viajes y conductores.

- Netflix: Utiliza PostgreSQL como su sistema de gestión de bases de datos relacional para almacenar y administrar una gran cantidad de datos de películas y series.

### Para ingresar desde otra consola usar el comando:
```bash
psql -U postgres
```
Pero debemos tener la variable de entorno en nuestro PATH de sistema