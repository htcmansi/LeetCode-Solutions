# Write your MySQL query statement below
select IFNULL(
(select distinct salary from Employee
order by salary DESC limit 1 offset 1),Null)as SecondHighestSalary;