--student table created.
create Table Students(
	id serial primary key,
	Name varchar(50),
	Gender varchar(50),
	Age int,
	Department varchar(50),
	city varchar(50)
);
--data inserted.
INSERT INTO Students (Name, Gender, Age, Department, City) VALUES
('Liam Smith', 'Male', 20, 'Computer Science', 'New York'),
('Olivia Johnson', 'Female', 21, 'Electrical Engineering', 'Los Angeles'),
('Noah Williams', 'Male', 19, 'Data Science', 'Chicago'),
('Emma Brown', 'Female', 22, 'Mechanical Engineering', 'Houston'),
('Oliver Jones', 'Male', 20, 'Computer Science', 'Phoenix'),
('Ava Garcia', 'Female', 20, 'Information Technology', 'Miami'),
('Elijah Miller', 'Male', 21, 'Mathematics', 'Seattle'),
('Sophia Davis', 'Female', 19, 'Data Science', 'Austin'),
('James Rodriguez', 'Male', 22, 'Civil Engineering', 'Boston'),
('Isabella Martinez', 'Female', 21, 'Computer Science', 'San Francisco');

--Updating the id = 5 city.
update Students set city = 'Paris' where id = 5;


--Deleting Method. in this we have deleted the row of a person from Paris.
delete from Students where city = 'Paris';
select * from Students;

--Altering a table. in here we will add a new column of sports liking.
alter table Students Add Column FavoriteSports varchar(50);
update Students set favoritesports = 'Hockey' where favoritesports is NULL And id = 2;

--Limit using. we can now only see 5 rows of the table.
select id,name from Students order by id ASC limit 5;

--using distinct, this gives us unique values, means different from others.
select distinct age from Students;

--using between.
select name,city from Students where age between 19 AND 21;

--using like. its like give me those name that starts with E.
select name,city from Students where name like 'E%';

--using in. its like finding the data from specific places as give me this person from the specific city.
select * from Students where city in ('Miami','Boston');