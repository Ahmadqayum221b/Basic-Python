create table Games (
game_id serial Primary Key,
title varchar(50),
genre varchar(50),
publisher varchar(50),
release_year int
);

create table Sales(
sale_id serial primary key,
game_id int references Games(game_id),
region varchar(50),
copies_sold int,
revenue int
);

create table Reviews(
review_id serial primary key,
game_id int references Games(game_id),
score int
);

--3 Tables have been created, Games,Reviews,Sales.
select * from Games;
select * from Sales;
select * from Reviews;

--Which genre generates the most revenue?
select g.genre as Genre,SUM(s.revenue) as Revenue 
from Games g Inner Join 
Sales s on g.game_id = s.game_id group by 
g.genre order by Revenue DESC;
--Which publisher sells the most copies?
select SUM(s.copies_sold) as Copies_Sold,g.publisher as Publisher
from Games g Inner Join Sales s on s.game_id = g.game_id group by
Publisher order by Copies_Sold DESC;
--Which region buys the most games?
select s.region as Region,SUM(s.copies_sold) as GamesBought
from Sales s group by Region order by GamesBought DESC;
--Does review score affect sales?
select s.copies_sold as Copies_Sold,
r.score as ReviewScore from Sales s Join Reviews r
on s.game_id = r.game_id;
--Top 10 Games by Revenue
select g.title as Games,s.revenue as Revenue 
from Games g Join Sales s on g.game_id = s.game_id order by
Revenue DESC limit 10;