-- Crear la tabla Autores
CREATE TABLE Autores (
    AutorID INT PRIMARY KEY,
    NombreAutor VARCHAR(50) NOT NULL
);

-- Crear la tabla Libros
CREATE TABLE Libros (
    LibroID INT PRIMARY KEY,
    Titulo VARCHAR(100) NOT NULL,
    AutorID INT,
    FOREIGN KEY (AutorID) REFERENCES Autores(AutorID)
);

-- Inserts adicionales para la tabla Autores
INSERT INTO Autores (AutorID, NombreAutor) VALUES (2, 'Autor A');
INSERT INTO Autores (AutorID, NombreAutor) VALUES (3, 'Autor B');
INSERT INTO Autores (AutorID, NombreAutor) VALUES (4, 'Autor C');
INSERT INTO Autores (AutorID, NombreAutor) VALUES (5, 'Autor D');
INSERT INTO Autores (AutorID, NombreAutor) VALUES (6, 'Autor E');
INSERT INTO Autores (AutorID, NombreAutor) VALUES (7, 'Autor F');
INSERT INTO Autores (AutorID, NombreAutor) VALUES (8, 'Autor G');
INSERT INTO Autores (AutorID, NombreAutor) VALUES (9, 'Autor H');
INSERT INTO Autores (AutorID, NombreAutor) VALUES (10, 'Autor I');

-- Inserts adicionales para la tabla Libros
INSERT INTO Libros (LibroID, Titulo, AutorID) VALUES (102, 'Libro 1', 2);
INSERT INTO Libros (LibroID, Titulo, AutorID) VALUES (103, 'Libro 2', 3);
INSERT INTO Libros (LibroID, Titulo, AutorID) VALUES (104, 'Libro 3', 4);
INSERT INTO Libros (LibroID, Titulo, AutorID) VALUES (105, 'Libro 4', 5);
INSERT INTO Libros (LibroID, Titulo, AutorID) VALUES (106, 'Libro 5', 6);
INSERT INTO Libros (LibroID, Titulo, AutorID) VALUES (107, 'Libro 6', 7);
INSERT INTO Libros (LibroID, Titulo, AutorID) VALUES (108, 'Libro 7', 8);
INSERT INTO Libros (LibroID, Titulo, AutorID) VALUES (109, 'Libro 8', 9);
INSERT INTO Libros (LibroID, Titulo, AutorID) VALUES (110, 'Libro 9', 10);
INSERT INTO Libros (LibroID, Titulo, AutorID) VALUES (111, 'Libro 10', 1);
