import   csv
data=open("F:\py/test/学生信息一览表.csv",'r',newline="")
datal=csv.reader(data)
t=0
list_5=[None]*100
list_5_length=0
for i in datal:
    if t==0:
         print(i)
         t=t+1

         for y in i:
             print(y)
             s=str(y)
             list_5[list_5_length]=s
             list_5_length=list_5_length+1

    else:
        break


print(list_5[0:list_5_length])



