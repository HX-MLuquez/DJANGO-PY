drop table clientes CASCADE;
drop table productos CASCADE;
drop table compras CASCADE;

create table clientes(
    cliente_id serial primary key,
    nombre varchar(50) not null,
    apellido varchar(50) not null,
    direccion varchar(250) not null,
    dni varchar(50) not null unique
);

create table productos(
    producto_id serial primary key,
    codigo varchar(250) not null unique
);

create table compras(
    compra_id serial primary key,
    cliente_id int,
    producto_id int,
    foreign key(cliente_id) references clientes(cliente_id),
    foreign key(producto_id) references productos(producto_id) 
);

INSERT INTO clientes (nombre, apellido, direccion, dni)
VALUES ('Mano', 'Lopez', 'Italia 32', '2398472'), ('Juli', 'Gonzales', 'Brasis 232', '65445546');
