# Write your MySQL query statement below
SELECT IFNULL(
   (select num FROM MyNumbers
   GROUP BY num
   having COUNT(num) = 1
   order by num DESC limit 1),null)as num;
