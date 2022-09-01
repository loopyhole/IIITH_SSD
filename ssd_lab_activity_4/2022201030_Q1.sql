use CUSTOMER_DB
delimiter //
create procedure getsum( in a int, in b int, out res int)
   begin
   set res=a+b;
   end
//

call getsum(4, 4, @c);
select @c