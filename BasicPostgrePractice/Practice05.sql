--Learning JOINS.
create Table Users(
	user_id serial primary key,
	name varchar(40)
);

create Table Orders(
	order_id serial primary key,
	user_id integer references Users(user_id),
	name varchar(40)
);

update Users set surname = 'Cheema' where user_id = 2;

select * from Users;
select * from Orders;

--Inner JOIN

select Users.name as UserName,users.surname as Surname, 
Orders.name as Product
from Users inner join Orders on 
Users.user_id = Orders.order_id And users.surname != 'Cheema';

--Left JOIN.
select users.name as Username,users.surname as Surname, 
orders.name as Product from Users 
left join orders on 
users.user_id = orders.order_id and users.surname != 'Qayum';

--Right JOIN.
select users.name as Username,users.surname as Surname, 
orders.name as Product from Users 
right join orders on 
users.user_id = orders.order_id and users.surname != 'Qayum';

--Full JOIN.
select users.name as Username,users.surname as Surname, 
orders.name as Product from Users 
full join orders on 
users.user_id = orders.order_id and Surname != 'Qayum';

--Cross JOIN.
select users.name as Username,orders.name 
as Product from Users Cross Join Orders;

--Self JOIN.
select u.name as Username, s.surname as Surname 
from users u left join users s on u.user_id = s.user_id;

