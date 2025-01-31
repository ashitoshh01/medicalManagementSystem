import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='system',database='harsh11')
if conn.is_connected():
    print('Successfully Connected')
c=conn.cursor()
c.execute('create table Store_details(Phone_Number int(30),Name varchar(25),Shop_no varchar(40))')
c.execute('create table product_details(Product_Name varchar(25),Product_Price float(10))')
c.execute('create table worker_details(Worker_name varchar(25),Worker_work varchar(50),Worker_age int(3), Worker_salary float(10),Phone_no int(50))')
 

print('Tables Successfully Created')
print('\n')


print('********************AMSTER HEALTHCARE********************')
print('\n')
print('*******************Welcome********************')
print('1.Login')
print('2.Exit')
choice=int(input('enter your choice:'))
if choice==1:
    user_name=input('Enter User name=')
    password=input('Enter Password=')
    while user_name=='harsh' and password=='akaharsh':
        print('>>>>>>>>>>Mr Harsh Account Access<<<<<<<<<<')
        print('\n')
        print(' *****************>Menu<*****************')
        print('1.Medical Store Details')
        print('2.Product details')
        print('3.Worker details')
        print('4.See all Medical Store Details')
        print('5.See all Product details')
        print('6.See all Worker details')
        print('7.See one Medical Store Details')
        print('8.See one Product details')
        print('9.See one Worker details')
        print('10.Stocks Available')
        print('11.Add Purchase Order')
        print('12.To Exit')
        choice=int(input('enter the choice'))
        if choice==1:
            a1=input('Name of Medical=')
            a2=int(input('Contact No='))
            a3=int(input('Enter Shop No='))
            sql_insert="insert into Store_details values("+str(a2)+",'"+(a1)+"',"+str(a3)+")"
            c.execute(sql_insert)
            conn.commit()
            print('Data Added')


        elif choice==2:
            b1=input('Enter  Product Name=')
            b2=float(input('Enter the Price='))
            sql_insert="insert into Product_details values(""'"+(b1)+"',"+str(b2)+")"
            c.execute(sql_insert)
            conn.commit()
            print('Data Added')


        elif choice==3:
            c1=input('Enter your name=')
            c2=input('Enter Assigned work=')
            c3=int(input('Enter your age='))
            c4=float(input('Enter your salary='))
            c5=int(input('Enter your  phone number='))
            sql_insert="insert into Worker_details values(" "'"+(c1)+"'," "'"+(c2)+"',"+str(c3)+","+str(c4)+","+str(c5)+ ")"
            c.execute(sql_insert)
            conn.commit()
            print('Data Added')


        elif choice==4:
            t=conn.cursor()
            t.execute('select*from Store_details')
            record=t.fetchall()
            for i in record:
                print('******************************************')
                print(i)
                print('******************************************')
                
        elif choice==5:
            t=conn.cursor()
            t.execute('select*from Product_details')
            record=t.fetchall()
            for i in record:
                print('******************************************')
                print(i)
                print('******************************************')

        elif choice==6:
            t=conn.cursor()
            t.execute('select*from Worker_details')
            record=t.fetchall()
            for i in record:
                print('******************************************')
                print(i)
                print('******************************************')
                
                
        elif choice==7:
            a=input('Enter Store Name to Display:-')
            t='select*from Store_details where Name=("{}")'.format(a)
            c.execute(t)
            v=c.fetchall()
            for i in v:
                print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                print(v)
                print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
      
                 
        elif choice==8:
            a=input('Enter Product Name To Dispaly:-')
            t='select*from Product_details where Product_Name=("{}")'.format(a)
            c.execute(t)
            v=c.fetchall()
            for i in v:
                print('############################################')
                print(v)
                print('############################################')
               
        elif choice==9:
            a=input('Enter Worker name To Display:-')
            t='select*from Worker_details where Worker_name=("{}")'.format(a)
            c.execute(t)
            v=c.fetchall()
            for i in v:
                print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
                print(v)
                print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
      

        elif choice==10:
            print('******************************************')
            f1 = open("myfile1.txt","w")
            L = ["Paracetamol=50 \n","Dolo=40 \n","Protein=120 \n","Amoxylin=24 \n","Amcoral=56 \n","HBSTER=46 \n","Amfolin=36 \n","Nutrister Chocolate=10 \n","Nutrister Vanilla=15 \n","Finelet=44 \n"]
            f1.write("***Here's The Stock Available*** \n")
            f1.writelines(L)
            f1.close()

            f=open('myfile1.txt','r')
            data=f.read()
            print(data)
            f.close()
            print('******************************************')

        elif choice==11:
            print('******************************************')
            print('Welcome to Purchase Order Mention Items to Purchase')
            import csv
            f=open("order.csv","w")
            w=csv.writer(f)
            lst=["SNO","ITEM NAME","QUANTITY"]
            w.writerow(lst)
            n=int(input("How many Items To Order?"))
            for x in range(n):
                r=int(input("Sr No:-"))
                n=input("Item Name:-")
                m=int(input("Quantity:-"))
                lst2=[r,n,m]
                w.writerow(lst2)
            f.close()

            f=open("order.csv","r")
            rec=csv.reader(f)
            print('***********Here is The Order Summery**********')
            for i in rec:
                print(i)
            f.close()
            
            
        elif choice==12:
             exit()
            
                            

    else:
        print('Wrong password, Try again ')
        
            
if choice==2:
    exit()
