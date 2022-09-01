use CUSTOMER_DB;

Delimiter //
CREATE PROCEDURE get_val()
BEGIN
   DECLARE done INT DEFAULT 0;
   DECLARE cname VARCHAR(255) DEFAULT "";
   DECLARE ccity VARCHAR(255) DEFAULT "";
   DECLARE ccountry VARCHAR(255) DEFAULT "";
   DECLARE grade decimal(10,0) DEFAULT 0.0;
   DECLARE agent CURSOR FOR
   SELECT CUST_NAME,CUST_CITY,CUST_COUNTRY,GRADE FROM customer where AGENT_CODE like 'A00%';
   DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
   OPEN agent;
   label:LOOP
	FETCH agent INTO cname, ccity, ccountry, grade;
	IF done = 1 THEN LEAVE label;
	END IF;
	SELECT cname, ccity, ccountry,grade;
	END LOOP label;
	CLOSE agent;
END//

call get_val();