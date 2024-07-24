


CREATE DATABASE transacciones;

\c transacciones;

CREATE TABLE cuentas (
    numero_cuenta INT PRIMARY KEY,
    balance FLOAT CHECK(balance >= 0.00)
);

SELECT * FROM cuentas;

INSERT INTO cuentas (numero_cuenta, balance) 
VALUES (1, 1000), (2, 1000), (3, 5000);

\echo :AUTOCOMMIT;

-- BEGIN;
UPDATE cuentas SET balance = balance - 1000 WHERE numero_cuenta = 3;
-- COMMIT;


-- TRANSACCION
BEGIN;
UPDATE cuentas SET balance = balance - 100 WHERE numero_cuenta = 3;
SELECT * FROM cuentas;
COMMIT;


-- ROLLBACK - Vuelve al último COMMIT seguro anterior
BEGIN;
UPDATE cuentas SET balance = balance - 300 WHERE numero_cuenta = 3;
SELECT * FROM cuentas;
ROLLBACK;



-- AUTO-COMMIT
UPDATE cuentas SET balance = balance + 5000 WHERE numero_cuenta = 3;
SELECT * FROM cuentas;


-- ROLLBACK - Vuelve al último COMMIT seguro anterior
BEGIN;
UPDATE cuentas SET balance = balance - 8000 WHERE numero_cuenta = 3;
SELECT * FROM cuentas;
ROLLBACK;

"""
transacciones=# SELECT * FROM cuentas;
 numero_cuenta | balance
---------------+---------
             1 |       0
             2 |    2000
             3 |    7900
(3 filas)
"""

-- SAVEPOINT - Crear commit intermedios dentro de una transacción

BEGIN;
UPDATE cuentas SET balance = balance - 1000 WHERE numero_cuenta = 2;
UPDATE cuentas SET balance = balance + 1000 WHERE numero_cuenta = 1;
SELECT * FROM cuentas;

SAVEPOINT punto_a;

UPDATE cuentas SET balance = balance - 5000 WHERE numero_cuenta = 3;
UPDATE cuentas SET balance = balance + 5000 WHERE numero_cuenta = 1;
SELECT * FROM cuentas;

ROLLBACK TO punto_a;
SELECT * FROM cuentas;
COMMIT;

