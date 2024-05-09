create database cultivosdb;
use cultivosdb;

create table cultivos(
id int auto_increment primary key not null,
nombre varchar(50), 
tipo varchar(50), 
area integer, 
redimiento integer
);

insert into cultivos values (null,"Papa","Grande",200,100);

select * from cultivos;

DELETE from cultivos WHERE cultivos.id=1;


