CREATE DATABASE IF NOT EXISTS datos_db;

USE datos_db;

CREATE TABLE IF NOT EXISTS Personas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    edad INT,
    peso DECIMAL(5,2),
    altura DECIMAL(5,2),
    fecha_nacimiento DATE,
    direccion VARCHAR(100),
    telefono VARCHAR(15)
);

INSERT INTO Personas (nombre, apellido, edad, peso, altura, fecha_nacimiento, direccion, telefono)
VALUES 
    ('Pedro', 'Martínez', 35, 80.3, 1.78, '1989-07-15', 'Calle 1, Ciudad X', '555-1111'),
    ('Ana', 'López', 28, 65.1, 1.65, '1996-03-20', 'Avenida 2, Ciudad Y', '555-2222'),
    ('Carlos', 'García', 45, 90.5, 1.82, '1979-11-05', 'Calle 3, Ciudad Z', '555-3333'),
    ('Laura', 'Hernández', 30, 70.0, 1.70, '1992-09-10', 'Avenida 4, Ciudad W', '555-4444'),
    ('Roberto', 'Díaz', 42, 85.2, 1.75, '1982-04-25', 'Calle 5, Ciudad V', '555-5555'),
    ('María', 'Sánchez', 29, 62.8, 1.63, '1995-08-12', 'Avenida 6, Ciudad U', '555-6666'),
    ('Jorge', 'Gómez', 38, 88.0, 1.80, '1986-01-30', 'Calle 7, Ciudad T', '555-7777'),
    ('Elena', 'Rodríguez', 27, 68.4, 1.68, '1997-06-18', 'Avenida 8, Ciudad S', '555-8888'),
    ('Miguel', 'Pérez', 33, 75.9, 1.75, '1991-12-03', 'Calle 9, Ciudad R', '555-9999'),
    ('Sofía', 'Torres', 31, 72.3, 1.67, '1993-10-22', 'Avenida 10, Ciudad Q', '555-0000');