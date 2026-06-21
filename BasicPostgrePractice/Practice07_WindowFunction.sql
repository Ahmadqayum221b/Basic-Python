--Window's Function.
select * from steamgames;
--Find the Ranking of the games based on Rating.
select game,ratings,rank() over (
	order by ratings DESC
) as Rank from steamgames;
--Find the RowNumber of the games as it is.
select id,game,genre,row_number() over (
	order by id ASC
) as RowNumber from steamgames;
--Finding the previous ratings of the games.
select id,game,genre,ratings,lag(ratings) over(
	order by ratings
) as Previous_Rating from steamgames;
--Finding the ahead ratings of the games.
select id,game,genre,ratings,lead(ratings) over(
	order by ratings 
) as Previous_Rating from steamgames;