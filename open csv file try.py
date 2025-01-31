import csv
f=open("myfile.csv","r")
rec=csv.reader(f)
for i in rec:
    print(i)
f.close()    
