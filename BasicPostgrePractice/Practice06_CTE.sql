--CTE's.
with NewModelCars as (
	select * from carsales;
	where year > 2020
),

NewModelCarWithLowPrice as (
	select AVG(price) as averageprice from NewModelCars 
)

select * from NewModelCars n join NewModelCarWithLowPrice nm
on n.price < nm.averageprice;

with Models as (
	select car_id,model from carsales
),
Brands as (
	select car_id,brand from carsales
)
select 
    c.car_id,
    m.model,
    b.brand 
from carsales c
join Models m on c.car_id = m.car_id 
join Brands b on c.car_id = b.car_id And b.brand = 'Honda'
where c.car_id > 15 limit 30;