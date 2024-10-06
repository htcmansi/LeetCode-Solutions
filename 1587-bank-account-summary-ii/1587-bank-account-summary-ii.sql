# Write your MySQL query statement below
select Users.name , SUM(Transactions.amount) as balance from Users 
JOIN Transactions On 
Users.account = Transactions.account 
GROUP BY Transactions.account
Having balance > 10000;