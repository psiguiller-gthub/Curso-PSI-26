create database musica;
use musica;

create table artistas (
    id_artista int auto_increment primary key,
    nombre varchar(50) not null,
    nick varchar(50),
    pais varchar(100)
);

create table estilos (
    id_estilo int auto_increment primary key,
    nombre varchar(50) not null
);

create table albumes (
    id_album int auto_increment primary key,
    titulo varchar(50) not null,
    fecha_lanzamiento date,
    id_artista int not null,
    id_estilo int not null,
    FOREIGN KEY (id_artista) REFERENCES artistas(id_artista),
    FOREIGN KEY (id_estilo) REFERENCES estilos(id_estilo)
);

INSERT INTO artistas (nombre, nick, pais) VALUES ('Extremoduro', 'Robe', 'España');
INSERT INTO estilos (nombre) VALUES ('Rock');
INSERT INTO albumes (titulo, fecha_lanzamiento, id_artista, id_estilo) VALUES ('Rock Transgresivo', '1991-09-26', 1, 1);
INSERT INTO artistas (nombre, nick, pais) VALUES ('Dr. Evil', 'Masia', 'Segorbe');
INSERT INTO estilos (nombre) VALUES ('Hardcore');
INSERT INTO albumes (titulo, fecha_lanzamiento, id_artista, id_estilo) VALUES ('Newstyle Legacy', '2026-06-26', 2, 2);
INSERT INTO artistas (nombre, nick, pais) VALUES ('Polla Records', 'Evaristo', 'Avila');
INSERT INTO estilos (nombre) VALUES ('Punk');
INSERT INTO albumes (titulo, fecha_lanzamiento, id_artista, id_estilo) VALUES ('Ellos dicen mierda, nosotros amén', '1990-09-26', 3, 3);
INSERT INTO artistas (nombre, nick, pais) VALUES ('Oreja de Van Gogh', 'Amaia', 'España');
INSERT INTO estilos (nombre) VALUES ('Rock');
INSERT INTO albumes (titulo, fecha_lanzamiento, id_artista, id_estilo) VALUES ('Todos estamos bailando la misma canción', '2026-05-09', 4, 1);

mostrar todos los albumes que son del mismo estilo
-----------------------------------------------------
select *
from albumes
where id_estilo = (select id_estilo from estilos where nombre = 'Rock');

select a.nombre as nombre_album, e.nombre as nombre_estilo
from albumes a join estilos e on a.id_estilo = e.id_estilo
where e.nombre = 'Rock';

borrar tuplas
---------------
delete from albumes where id_album = 2;




show tables;
