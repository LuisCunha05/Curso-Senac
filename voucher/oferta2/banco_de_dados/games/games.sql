create database game;
use game;

describe venda;
select * from venda;
select count(*) from venda;
select avg(Global_Sales) from venda;
select * from venda where Global_Sales > (select avg(Global_Sales) from venda);
select * from venda where Global_Sales > 2;
select * from venda where Platform='PS2' and Global_Sales > 10;
select * from venda where Platform='Wii' order by JP_Sales desc;
select * from venda where Platform='Wii' order by NA_Sales desc;
select * from venda where Name like 'Just Dance%' order by Global_Sales desc;
select * from venda where Publisher='Ubisoft' order by Global_Sales desc;
select * from venda where Publisher like 'Sony%' order by Global_Sales desc;
select distinct Publisher from venda;