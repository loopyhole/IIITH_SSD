use CUSTOMER_DB;

delimiter //
create procedure get_sr()
	begin
		select CUST_NAME, GRADE from customer where OPENING_AMT+RECEIVE_AMT > 10000;
    end
//

call get_sr()
