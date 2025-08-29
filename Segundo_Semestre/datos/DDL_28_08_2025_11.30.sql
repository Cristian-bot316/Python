CREATE TABLE IF NOT EXISTS nacionalidad(
    id_nacionalidad INT AUTO_INCREMENT,
    pais VARCHAR(50) NOT NULL ,
    nacionalidad VARCHAR(50) NOT NULL,

    CONSTRAINT pk_nacionalidad PRIMARY KEY (id_nacionalidad)
);

INSERT INTO nacionalidad(pais,nacionalidad) VALUES('chile','chileno');


CREATE TABLE IF NOT EXISTS autor(
    id_autor INT AUTO_INCREMENT,
    nombre_autor VARCHAR(100) NOT NULL,
    pseudonimo VARCHAR(50) NULL,
    id_nacionalidad INT NULL,
    bio VARCHAR(255) NULL,


    CONSTRAINT pk_autor PRIMARY KEY (id_autor),
    CONSTRAINT fk_autor_nacionalidad FOREIGN KEY (id_nacionalidad) REFERENCES nacionalidad(id_nacionalidad)
);



CREATE TABLE IF NOT EXISTS comuna(
id_comuna INT AUTO_INCREMENT,
codigo_comuna VARCHAR(5) NOT NULL,
nombre_comuna VARCHAR(50) NOT NULL,

CONSTRAINT pk_comuna PRIMARY KEY (id_comuna)
);



CREATE TABLE IF NOT EXISTS direccion(
    id_direccion INT 
    id_comuna INT NOT NULL,
    calle VARCHAR(50) NOT NULL,
    numero VARCHAR(10) NULL,
    departamento VARCHAR(10) NULL,
    AUTO_INCREMENT,
    
    CONSTRAINT pk_direccion PRIMARY KEY (id_direccion),
    CONSTRAINT FK_direccion_comuna FOREIGN KEY (id_comuna) REFERENCES comuna (id_comuna)
);


CREATE TABLE IF NOT EXISTS biblioteca(
    id_biblioteca INT AUTO_INCREMENT,


);




CREATE TABLE IF NOT EXISTS lector(
    id_lector INT AUTO_INCREMENT

);


CREATE TABLE IF NOT EXISTS categoria(
    id_categoria INT AUTO_INCREMENT,


);





CREATE TABLE IF NOT EXISTS libro(
    id_libro INT AUTO_INCREMENT,
    id_biblioteca INT NOT NULL,
    id_autor INT NOT NULL,
    id_categoria INT NULL,


);



CREATE TABLE IF NOT EXISTS prestamo (
    id_prestamo INT AUTO_INCREMENT,
    id_libro INT NOT NULL,
    rut_lector INT NOT NULL,
    fecha_prestamo DATETIME NOT NULL,
    fecha_devolucion DATETIME NOT NULL,
    fecha_entrega DATETIME NOT NULL,

    CONSTRAINT pk_prestamo PRIMARY KEY (id_prestamo),
    CONSTRAINT fk_prestamo_libro FOREIGN KEY (id_libro) REFERENCES libro (id_libro,),
    CONSTRAINT fk_prestamo_lector FOREIGN KEY (rut_lector) REFERENCES lector (rut_lector,)



);

