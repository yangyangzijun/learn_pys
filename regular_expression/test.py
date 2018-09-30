import   csv
data_read=open("F:\py/test/学生信息一览表.csv",'r',newline="")

datal=csv.reader(data_read)

t=0
list=[]
for l in datal:
    print(l)
    list.append(l)
data_read.close()
print(list)

data_write=open("F:\py/test/学生信息一览表.csv",'w',newline="")
write=csv.writer(data_write)
for i in list[1:10]:
    write.writerow(i)



