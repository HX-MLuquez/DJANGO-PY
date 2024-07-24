

select *, LENGTH(nombre_producto) as cuenta from productos ORDER BY LENGTH(nombre_producto);
select *, LENGTH(producto) as cuenta from ventas ORDER BY LENGTH(producto);
select *, LEFT(categoria,3) as cat from productos;
select SUM(precio) FROM productos;
select MAX(precio) FROM productos;
select MIN(precio) FROM productos;
select COUNT(*) FROM productos where precio > 3000;
select * from productos where precio = (SELECT MAX(precio) from productos);
select AVG(precio) from productos;
select * from productos where precio > (select AVG(precio) from productos);
select COUNT(*) FROM productos where en_stock = true; 
select COUNT(*) FROM productos where en_stock = 't'-- idem al anterior
select * from productos where precio > 7000;
select AVG(precio) from productos where en_stock = True;
--agrupar 
select * from productos;
select MAX(precio) FROM productos GROUP BY categoria;
select categoria,MAX(precio) FROM productos GROUP BY categoria;
select categoria,sum(precio) FROM productos GROUP BY categoria; agrupa por categoría 
select en_stock,sum(precio) FROM productos GROUP BY en_stock; agrupa por false y true
select en_stock,count(categoria) FROM productos GROUP BY en_stock; agrupa por false y true  y los cuenta ojo en espejo 
select avg(cantidad * precio_unitario) as prom_ventas from ventas; 
select sum (cantidad * precio_unitario) as prom_ventas from ventas; 
select producto, avg(cantidad * precio_unitario) as prom_ventas from ventas GROUP BY producto; 
select producto, avg(cantidad * precio_unitario) as prom_ventas from ventas where fecha > '2024-01-05' GROUP BY producto;

select SUM(cantidad * precio_unitario) AS prom_total FROM ventas;

select producto, AVG(cantidad * precio_unitario) AS prom_ventas FROM ventas GROUP BY producto;

select producto, AVG(cantidad * precio_unitario) AS prom_ventas
FROM ventas WHERE fecha > '2024-01-05' GROUP BY producto;


select producto, sum(cantidad * precio_unitario) AS max_por_producto
from ventas group by producto order by max_por_producto desc limit 1;

select fecha, sum(cantidad) as cant_ventas_fecha from ventas group by fecha order by fecha;