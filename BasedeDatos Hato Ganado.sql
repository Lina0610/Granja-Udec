create database ganadodb;
use ganadodb;

create table ganado(
id int auto_increment primary key not null,
especie varchar(50), 
raza varchar(50), 
edad integer,
peso integer,
produccion float
);

select * from ganado;

insert into ganado values (null,"Vaca","Housten",10,200,500.0);

