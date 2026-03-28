# fiz a tebela com uma view para ultilizar os dados futuramente, utilizei uma query simples com MYSQL
# para trazer os clientes de forma mais dinamica e rapida queria coloca uma INTO  no comeco para popular a tabela, mas como é uma view nao tem como, entao deixei a query simples para ser ultilizada futuramente.
CREATE VIEW  data_cliente as  
SELECT DISTINCT  p.id_processo,c.id_cliente,c.nome,c.estado from clientes c
INNER JOIN processos p on c.id_cliente = p.id_cliente 
WHERE c.estado ='SP' AND YEAR(p.data_abertura) = 2023;
