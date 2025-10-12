select * from senso where estado = 'Mato Grosso do Sul'; -- 1
select * from senso where populacao < 1000; -- 2
select * from senso where nome_mun = 'Campo Grande' or nome_mun = 'Terenos'; -- 3
select * from senso where estado = 'Mato Grosso do Sul' and populacao > 100000; -- 4
select estado, nome_mun from senso order by nome_mun; -- 5
select nome_mun from senso where pib = (select max(pib) from senso); -- 6
select nome_mun from senso where pib_per_cap = (select max(pib_per_cap) from senso); -- 7
select nome_mun from senso where populacao = (select max(populacao) from senso); -- 8
select nome_mun from senso where populacao = (select min(populacao) from senso); -- 9
select * from senso where nome_mun like '%i'; -- 10
select count(estado) from senso; -- 11
select avg(pib) from senso; -- 12
select * from senso where nome_mun like 'c%'; -- 13

select * from senso where estado = 'Mato Grosso do Sul' and populacao > 1000 and populacao < 10000; -- 14
select avg(populacao) from senso; -- 14
select * from senso where estado = 'Mato Grosso do Sul' and pib > (select avg(pib) from senso); -- 14
select count(nome_mun) from senso where populacao > 10000 and populacao < 100000; -- 14
select * from senso where nome_mun like '%co' and populacao > (select avg(populacao) from senso); -- 14
