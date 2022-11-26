/* Antes de verificar as consultas, é necessário rodar "musicas-ScriptDeCriaçãoDeTabelas.sql";
obs: no caso de dúvidas, consulte a modelagem do banco de dados
*/
-- QUERIES (consultas):

-- 1) Selecionar o nome (Customer.FirstName) e a soma dos valores das contas dos usuários (Invoice.Total)
--    filtrando pelos usuários que tiveram a soma das contas maiores que 40 e ordenados de modo que os maiores valores apareçam primeiro;

select Customer.Customerid, Customer.FirstName, sum(Invoice.Total) from customer
inner join invoice on customer.customerid =  invoice.customerid
group by Customer.Customerid, Customer.FirstName having sum(Invoice.Total) > 40
order by sum(Invoice.Total) desc;

-- 2) Exiba a soma de tempo das musicas em milissegundos agrupados pelos nomes dos países de origem dos usuários;

select customer.country, sum(track.milliseconds) as musicas_milissegundos from customer
inner join invoice on customer.customerid = invoice.customerid
inner join invoiceline on invoice.invoiceid = invoiceline.invoiceid
inner join track on invoiceline.trackid = track.trackid
group by customer.country;

-- 3) Selecione o país de origem dos usuários que mais escutam músicas do tipo Rock;


select customer.country, count(rock_songs.genreid) from customer
inner join invoice on customer.customerid = invoice.customerid
inner join invoiceline on invoice.invoiceid = invoiceline.invoiceid
inner join (select * from track where genreid = 1) as rock_songs on invoiceline.trackid = rock_songs.trackid
group by customer.country 
order by count(rock_songs.genreid) desc;

-- 4) Selecione o nome do artista mais tocado no Brasil;

select customer.country, mode() within group (order by artist.name) artista_mais_tocado from customer 
inner join invoice on customer.customerid = invoice.customerid
inner join invoiceline on invoice.invoiceid = invoiceline.invoiceid
inner join track on invoiceline.trackid = track.trackid
inner join album on track.albumid = album.albumid
inner join artist on album.artistid = artist.artistid
group by customer.country having country = 'Brazil'

-- 5) Selecione os nomes dos artistas mais tocados agrupados por países de origem dos usuários;

select customer.country, mode() within group (order by artist.name) artista_mais_tocado from customer 
inner join invoice on customer.customerid = invoice.customerid
inner join invoiceline on invoice.invoiceid = invoiceline.invoiceid
inner join track on invoiceline.trackid = track.trackid
inner join album on track.albumid = album.albumid
inner join artist on album.artistid = artist.artistid
group by customer.country

-- 6) Selecione o nome dos artistas associados com o título dos seus álbuns;

select artist.artistid, artist.name, album.title, album.artistid from artist 
inner join album on artist.artistid = album.artistid
order by artist.artistid

-- 7) Selecione o nome dos artistas associados com o nome das músicas (Track.name) de forma paginada com 10 resultados por página;

select artist.artistid, artist.name, track.name, track.trackid from artist 
inner join album on artist.artistid = album.artistid
inner join track on album.albumid = track.albumid
order by artist.artistid limit 10 offset (1-1)*10;

-- 8) Selecione o nome das playlists e o total de músicas (Track.name) agrupadas pelas playlists que pertencem e ordenadas pelas playlists que possuem mais músicas;



-- 9) Exiba o nome do gênero e a média de tempo das músicas em milisegundos agrupadas por gênero;



-- 10) Exiba o nome do álbum que possui a maior média de tempo em milisegundos cujo o gênero musical é Rock;



-- 11) Selecione o nome dos consumidores que tiveram as contas (invoice.total) maiores que a média;


-- 12) Selecione os álbuns do artiste que possui a maior quantidade de álbuns lançados;



-- 13) Selecione o nome da playlist que possui a maior quantidade de músicas (Track.name);



-- 14) Selecione o nome do gênero musical que possui a menor quantidade de músicas (Track.name);



-- 15) Selecione o nome de todos os funcionários associados com o nome de todos os consumidores que eles tiveram suporte (Customer.SupportRepld);



-- 16) Selecione o nome do gênero musical do artista que possui a menor quantidade de músicas (Track.name);



-- 17) Selecione o nome do artista que possui mais músicas com diferentes gêneros musicais;



-- 18) Selecione a quantidade de músicas compradas por país de origem dos usuários;



-- 19) Selecione o país de origem dos consumidores que mais compraram músicas do gênero musical Jazz;

