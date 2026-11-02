-- Write your query below
Select name from customers as c
where id not in (select customer_id from orders)