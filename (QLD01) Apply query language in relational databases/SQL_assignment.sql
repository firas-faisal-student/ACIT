Select Customer_id,max(purch_amt),order_date from orders where order_date='2016-09-10' group by Customer_id ;
