/* Antes de verificar as consultas, é necessário rodar "musicas-ScriptDeCriaçãoDeTabelas.sql";
obs: no caso de dúvidas, consulte a modelagem do banco de dados
*/
-- QUERIES (consultas):

-- 1) Selecionar o nome e a soma dos valores das contas dos usuários
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


select customer.country, count(rock_songs.genreid) rock_count from customer
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
group by customer.country having country = 'Brazil';

-- 5) Selecione os nomes dos artistas mais tocados agrupados por países de origem dos usuários;

select customer.country, mode() within group (order by artist.name) artista_mais_tocado from customer 
inner join invoice on customer.customerid = invoice.customerid
inner join invoiceline on invoice.invoiceid = invoiceline.invoiceid
inner join track on invoiceline.trackid = track.trackid
inner join album on track.albumid = album.albumid
inner join artist on album.artistid = artist.artistid
group by customer.country;

-- 6) Selecione o nome dos artistas associados com o título dos seus álbuns;

select artist.artistid, artist.name, album.title from artist 
inner join album on artist.artistid = album.artistid
order by artist.artistid;

-- 7) Selecione o nome dos artistas associados com o nome das músicas de forma paginada com 10 resultados por página;

select artist.artistid, artist.name, track.name musicas, track.trackid from artist 
inner join album on artist.artistid = album.artistid
inner join track on album.albumid = track.albumid
order by artist.artistid limit 10 offset (1-1)*10;

-- 8) Selecione o nome das playlists e o total de músicas agrupadas pelas playlists que pertencem e ordenadas pelas playlists que possuem mais músicas;

select playlist.name, count(playlisttrack.trackid) musicas_total from playlist
inner join playlisttrack on playlist.playlistid = playlisttrack.playlistid
group by playlist.name order by count(playlisttrack.trackid) desc;

-- 9) Exiba o nome do gênero e a média de tempo das músicas em milisegundos agrupadas por gênero;

select genre.name, avg(track.milliseconds) from genre
inner join track on genre.genreid = track.genreid
group by genre.name order by avg(track.milliseconds);

-- 10) Exiba o nome do álbum que possui a maior média de tempo em milisegundos cujo o gênero musical é Rock;

select album.title, avg(rock_songs.milliseconds) from (select * from track where genreid = 1) rock_songs
inner join album on album.albumid = rock_songs.albumid
group by album.title order by avg(rock_songs.milliseconds) desc limit 1;

-- 11) Selecione o nome dos consumidores que tiveram as contas maiores que a média;

select customer.firstname,customer.lastname, invoice.total from customer 
inner join invoice on customer.customerid =invoice.customerid
where invoice.total > (select avg(invoice.total) from invoice)
order by invoice.total;

-- 12) Selecione os álbuns do artista que possui a maior quantidade de álbuns lançados;

select artistid, count(title) from album
group by artistid 
order by count(title) desc limit 1;

select artist.artistid, artist.name,album.albumid, album.title from album
inner join artist on album.artistid = artist.artistid
where album.artistid = (select artistid from album
                        group by artistid 
                        order by count(title) desc limit 1);
                        
-- 13) Selecione o nome da playlist que possui a maior quantidade de músicas;

select Playlist.name, count(trackid) num_musicas from Playlist
inner join playlisttrack on Playlist.Playlistid = playlisttrack.Playlistid
group by Playlist.name order by count(trackid) desc limit 1;

-- 14) Selecione o nome do gênero musical que possui a menor quantidade de músicas;

select genre.name, count(track.trackid) from genre
inner join track on genre.genreid = track.genreid
group by genre.name order by count(track.trackid) asc limit 1;  

-- 15) Selecione o nome de todos os funcionários associados com o nome de todos os consumidores que eles deram suporte;

select Employee.Employeeid, Employee.firstname funcionario, Employee.title cargo, customer.firstname consumidor from Employee
left join customer on Employee.Employeeid = customer.SupportRepid
order by Employee.Employeeid

-- 16) Selecione o nome do gênero musical do artista que possui a menor quantidade de músicas (Track.name);



-- 17) Selecione o nome do artista que possui mais músicas com diferentes gêneros musicais;



-- 18) Selecione a quantidade de músicas compradas por país de origem dos usuários;



-- 19) Selecione o país de origem dos consumidores que mais compraram músicas do gênero musical Jazz;

