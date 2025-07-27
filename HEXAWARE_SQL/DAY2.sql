create procedure usp_allemployees
as
begin
select * from employees
end

execute usp_allemployees

create procedure usp_getemployeeinfo
as
begin
select name, department from Employees
end

usp_getemployeeinfo


------------create stored procedure using input parameters------------

create proc usp_employeebydepart
(@dept varchar(20))
as
begin
select * from Employees where Department=@dept
end

exec usp_employeebydepart 'IT'



create proc usp_employeebydepartandname
(@dept varchar(20),@name varchar(200))
as
begin
select * from Employees where Department=@dept and name=@name
end

exec usp_employeebydepartandname'IT','taylor'




------------------------------------------------------------
CREATE PROC spGetSum
(
@num1 int,
@num2 int,
@sum int OUTPUT)
AS
BEGIN
SET @sum=@num1+@num2
END

DECLARE @sumResult int
EXEC spGetSum 10,20,@sumResult OUT
print @sumResult

create PROC Usp_GetEmplyeeCountByID
(@ID int,
@empCount int OUT)
AS
BEGIN
SELECT @empCount=count(ID) FROM Employees WHERE Id=@ID
END

DECLARE @empCount int
EXEC Usp_GetEmplyeeCountByID 3,@empCount OUT
print @empCount

create PROC spGetEmplyeeCountBydepartment
(@deptCount int OUT)
as
BEGIN
SELECT @deptCount=COUNT(ID) FROM Employees WHERE Department='IT'
END


DECLARE @deptCount int
EXEC spGetEmplyeeCountBydepartment @deptCount OUT
Print 'Department : '+CAST(@deptCount as varchar(10)) 

drop proc usp_GetEmplyeeCountBydepartmenthr

create PROC Usp_GetEmplyeeCountBydepartmenthr
(@deptCount int OUT)
as
BEGIN
SELECT @deptCount=COUNT(ID) FROM Employees WHERE Department='HR'
END
 

DECLARE @deptCount int
EXEC Usp_GetEmplyeeCountBydepartmenthr @deptCount OUT
Print 'Department : '+CAST(@deptCount as varchar(10)) 



--------------------------------------------------
-------------USER_DEFINED_FUNCTIONS---------------

create function f1(@num int)
returns int
as
begin
return @num*@num*@num
end

select dbo.f1(34)

create function F_getemplbyid
(@deptId int)
Returns table
as
Return(select ID,name,Department,salary from Employees where id=@deptID)

select * from dbo.F_getemplbyid(2)




-----------------------------------------------------
-----------------ASSIGNEMENT-------------------------

drop function fn_getproductprice

CREATE FUNCTION fn_GetProductPrice 
(@product_id INT)
RETURNS DECIMAL(10, 2)
AS
BEGIN
    DECLARE @price DECIMAL(10, 2);
    SELECT @price = list_price FROM production.products WHERE product_id = @product_id;
    RETURN @price;
END;


SELECT dbo.fn_GetProductPrice(101) AS ProductPrice;




CREATE FUNCTION fn_GetProductsByCategory 
(@category_id INT)
RETURNS TABLE
AS
RETURN (
    SELECT product_id, product_name, list_price
    FROM production.products
    WHERE category_id = @category_id
);

SELECT * FROM fn_GetProductsByCategory(2);


CREATE FUNCTION fn_GetTotalSalesByStore 
(@store_id INT)
RETURNS DECIMAL(18, 2)
AS
BEGIN
    DECLARE @total DECIMAL(18, 2);
    SELECT @total = SUM(oi.list_price * oi.quantity)
    FROM sales.orders o
    JOIN sales.order_items oi ON o.order_id = oi.order_id
    WHERE o.store_id = @store_id;
    RETURN @total;
END;


SELECT dbo.fn_GetTotalSalesByStore(1) as totalsales;


CREATE FUNCTION fn_GetOrdersByDateRange 
(@start_date DATE, @end_date DATE)
RETURNS TABLE
AS
RETURN (
    SELECT order_id, customer_id, order_date, store_id
    FROM sales.orders
    WHERE order_date BETWEEN @start_date AND @end_date
);


SELECT * FROM fn_GetOrdersByDateRange('2018-01-01', '2018-12-31');




drop Function fn_GetProductbybrand

CREATE FUNCTION fn_GetProductsByBrand (@brand_id INT)
RETURNS TABLE
AS
RETURN (
    SELECT p.product_id, p.product_name, p.list_price, b.brand_name
    FROM production.products p
    JOIN production.brands b ON p.brand_id = b.brand_id
    WHERE p.brand_id = @brand_id
);

SELECT * FROM fn_GetProductsByBrand(7);

