f1 = open("myfile1.txt","w")
L = ["Paracetamol=50 \n","Dolo=40 \n","Protein=120 \n","Amoxylin=24 \n","Amcoral=56 \n","HBSTER=46 \n","Amfolin=36 \n","Nutrister Chocolate=10 \n","Nutrister Vanilla=15 \n","Finelet=44 \n"]
f1.write("***Here's The Stock Available*** \n")
f1.writelines(L)
f1.close()

f=open('myfile1.txt','r')
data=f.read()
print(data)
f.close()
