Create Table CarSales (
	car_id serial primary key,
	brand varchar(50),
	model varchar(50),
	year int,
	mileage int,
	price int,
	city varchar(50)
);

select * from CarSales;

--here i have selected only those cars that are in between 2020 and 2024, belongs to peshawar and mileage less than 100000
select * from CarSales where city = 'Peshawar' and mileage < 100000 and year between 2020 and 2024;