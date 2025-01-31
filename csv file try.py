import csv
f=open("myfile.csv","w")
w=csv.writer(f)
lst=["RNO","NAME","MARKS"]
w.writerow(lst)
n=int(input("how many records"))
for x in range(n):
    r=int(input("roll no"))
    n=input("name")
    m=int(input("marks"))
    lst2=[r,n,m]
    w.writerow(lst2)
f.close()    
          
          
f=open("myfile.csv","r")
rec=csv.reader(f)
for i in rec:
    print(i)
f.close() 
