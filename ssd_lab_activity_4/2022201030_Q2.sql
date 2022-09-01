use CUSTOMER_DB;

delimiter //
create procedure get_wa(in wa varchar(50))
	begin
		select CUST_NAME from customer where WORKING_AREA = wa;
    end
//

call get_wa("Bangalore")
