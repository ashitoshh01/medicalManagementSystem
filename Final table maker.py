import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='system',database='harsh22')
if conn.is_connected():
    print('successfully connected')

c=conn.cursor()
c.execute('create table Store_details(Phone int(13),Name varchar(25),Address varchar(50))')
c.execute('create table product_details(Product_Name varchar(25),product_Price float(10))')
c.execute('create table worker_details(Worker_name varchar(25),Worker_work varchar(10),Worker_age int(3), Worker_salary float(10),Phone_no int(13))')
print ('done')
