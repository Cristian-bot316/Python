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
    id_direccion INT AUTO_INCREMENT,
    id_comuna INT NOT NULL,
    calle VARCHAR(50) NOT NULL,
    numero VARCHAR(10) NULL,
    departamento VARCHAR(10) NULL,
    
    
    CONSTRAINT pk_direccion PRIMARY KEY (id_direccion),
    CONSTRAINT FK_direccion_comuna FOREIGN KEY (id_comuna) REFERENCES comuna (id_comuna)
);













