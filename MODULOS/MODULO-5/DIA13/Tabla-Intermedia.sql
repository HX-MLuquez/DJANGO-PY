Crear tabla usuarios y productos 
         nombre email   nombre precio 

N:M

N:*

*:*

MUCHOS a MUCHOS <-> Tabla intermedia usuarios_productos 

CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    precio INT NOT NULL
);


CREATE TABLE usuarios_productos (
    id SERIAL PRIMARY KEY,
    usuario_id INT REFERENCES usuarios (id),
    producto_id INT REFERENCES productos (id),
    -- PRIMARY KEY(usuario_id, producto_id)
);


INSERT INTO usuarios (nombre, email) 
VALUES ("Manuela", "m@,com"), ("Jimena", "mw@,com"), ("Vanesa", "mc@,com"), ("Toto", "mv@,com");



8. ON DELETE CASCADE 


