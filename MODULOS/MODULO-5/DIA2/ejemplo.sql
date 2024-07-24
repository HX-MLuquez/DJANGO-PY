CREATE TABLE IF NOT EXISTS tabla1 (
  id int NOT NULL,
  letra varchar(40) NOT NULL
);

INSERT INTO tabla1 (id, letra) VALUES
(1, 'Uno'),
(2, 'Dos'),
(3, 'Tres'),
(4, 'Cuatro');



CREATE TABLE IF NOT EXISTS tabla2 (
  id int NOT NULL,
  valores varchar(50) NOT NULL
);

INSERT INTO tabla2 (id, valores) VALUES
(3, 'Tres'),
(4, 'Cuatro'),
(5, 'Cinco'),
(6, 'Seis');


select * from tabla1 a INNER JOIN tabla2 b on a.id = b.id;

#ESTE EJEMPLO REEMPLAZA EL INNER JOIN
select tabla1.*,tabla2.*  from tabla1,tabla2 where tabla1.id = tabla2.id;


select * from tabla1 a LEFT OUTER JOIN tabla2 b on a.id = b.id;
select * from tabla1 a RIGHT OUTER JOIN tabla2 b on a.id = b.id;

select * from tabla1 a FULL OUTER JOIN tabla2 b on a.id = b.id;

