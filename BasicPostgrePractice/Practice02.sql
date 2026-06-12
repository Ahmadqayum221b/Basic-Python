Create table SteamGames
(
	ID Serial Primary Key,
	Game Varchar(50),
	Genre Varchar(50),
	Ratings float,
	CopiesSold int
);

insert into SteamGames (Game,Genre,Ratings,CopiesSold) Values
(
	'Red Dead Redemption 2','Action',9.8,20000
);
insert into SteamGames (Game,Genre,Ratings,CopiesSold) Values
(
	'Fifa 22','Sports',9.1,10000
),
(
	'Call of Duty','Action',9.5,24000
),
(
	'Farcry 5','Action',9.4,22000
);

select * from SteamGames;

--now we have to find Total Revenue. 2 is the price of each game.
select Game,Avg(CopiesSold * 2) as TotalRevenue from SteamGames Group by Game;
--now we check those genres that have more than 9.4 rating using as for grouping both the columns.
select (Game,Genre) as PerfectGames from SteamGames where Ratings > 9.2 group by Game,Genre;
--now we check those genres that have more than 9.4 ratings using normal group by, and where.
--the reason we have used where before group by is because first of all we cannot use 
-- where when we are using group by, for that we use having but having takes either Max,min,avg of those multiple lines and sums up into one.
--so for that first we filter out the thing than we group them together.
select Game,Genre from SteamGames where Ratings > 9.2 group by Game,Genre;