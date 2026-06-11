--creating table.
Create Table Emps (
	ID Serial Primary key,
	Name Varchar(50),
	Department Varchar(50),
	Salary Int
);

Create Table Emps2 (
	ID Serial Primary key,
	Name Varchar(50),
	Department Varchar(50),
	Salary Int
);
--using selection means viewing the data in the emp table.
select * from Emps;
--inserting data into the emp table.
insert into Emps (Name,Department,Salary) values 
('Ahmad','CS',10000),
('Ali','CS',50000),
('Adnan','CS',20000),
('Hamza','CS',40000),
('Hussain','CS',30000);

insert into Emps2 (Name,Department,Salary) values 
('Ahmad','CS',10000),
('Ali','CS',50000),
('Adnan','CS',20000),
('Hamza','CS',40000),
('Hussain','CS',30000);

insert into Emps2 (Name,Department,Salary) values 
('Faizan','SE',50000);

select * from Emps;

--printing out in ascending order.
select * from Emps order by Salary ASC;
--printing out in descending order.
select * from Emps order by Salary DESC;
--for this we use order by. cause we want this in order.

--for group by. we convert it into clusters.
--in this what we are doing is that we selecting both the dep,and taking the average salary of all those that have same dep and grouping them in one dep.
select Department,AVG(Salary) from Emps2 Group by Department;
--for using a condition where it should fall under the circumstances you can use it something like this.
select * from Emps2 where Salary > 10000 And Salary <= 30000 And Department = 'SE';

--what if you combine both group by and condition, for that you then use having
select Department,AVG(Salary) from Emps2 group by Department having AVG(Salary) >=24000 And Department = 'SE';