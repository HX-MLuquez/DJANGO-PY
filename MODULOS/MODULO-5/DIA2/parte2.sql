


insert into clientes (cliente_id, nombre) values
(1, 'Juan'),
(2, 'Maria'),
(3, 'Carlos'),
(4, 'Ana'),
(5, 'Luis')
;


insert into pedidos (id, monto, cliente_id) values
(10, 3000, 1),
(20, 800, 1),
(30, 1500, 2),
(40, 2800, 3),
(50, 3200, 5)
;


SELECT AVG(total_venta) as promedio_ventas 
FROM (SELECT cliente_id, SUM(monto) as total_venta 
FROM pedidos GROUP BY cliente_id) AS subquery;

--! JOIN

SELECT * FROM pedidos
JOIN clientes 
ON clientes.cliente_id = pedidos.cliente_id;

SELECT * FROM pedidos
LEFT JOIN clientes 
ON clientes.cliente_id = pedidos.cliente_id;

SELECT * FROM pedidos
RIGHT JOIN clientes 
ON clientes.cliente_id = pedidos.cliente_id;

SELECT * FROM pedidos
INNER JOIN clientes 
ON clientes.cliente_id = pedidos.cliente_id;

SELECT pedidos.cliente_id, clientes.cliente_id FROM pedidos
INNER JOIN clientes 
ON clientes.cliente_id = pedidos.cliente_id;


SELECT pedidos.id, pedidos.monto, pedidos.cliente_id, clientes.cliente_id, clientes.nombre 
FROM pedidos
FULL OUTER JOIN clientes  
ON clientes.cliente_id = pedidos.cliente_id;

--! RENOMBRANDO - AS -
SELECT p.id, p.monto, p.cliente_id, c.cliente_id, c.nombre 
FROM pedidos p
FULL OUTER JOIN clientes c
ON c.cliente_id = p.cliente_id;


SELECT id, monto FROM pedidos; 