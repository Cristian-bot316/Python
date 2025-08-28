CREATE TABLE nacionalidad(
    id_nacionalidad INT AUTO_INCREMENT,
    pais VARCHAR(50) NOT NULL ,
    nacionalidad VARCHAR(50) NOT NULL,

    CONSTRAINT pk_nacionalidad PRIMARY KEY (id_nacionalidad)
);

INSERT INTO nacionalidad(pais,nacionalidad) VALUES('chile','chileno');