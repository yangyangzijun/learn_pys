import  re
import csv
def creat_table(s):
    patt1='.+?{'
    patt2='.*?,|.+?}'

    str_1=re.search(patt1,s)
    s=s[len(str_1[0]):100]
    list=re.compile(patt2).findall(s)

    file=open("F:\py/test/"+str_1[0][:-1]+".csv",'w',newline='')


    file.writelines(list)
    for li in list:
        print(li[0:-1])
        file.writelines(li[0:-1]+',')


    file.close()
def insert_into(s):
    patt1 = '.+?{'
    patt2 = "'.+?',|.+?'}"

    str_1 = re.search(patt1, s)
    s = s[len(str_1[0]):100]
    list = re.compile(patt2).findall(s)

    file = open("F:\py/test/" + str_1[0][:-1] + ".csv",'a',newline='')
    # file.writelines(list)
    writer=csv.writer(file)

    i=0
    list_1=list
    for li in list:
        list_1[i]=li[1:-2]
        i=i+1
        print(li[1:-2])

    writer.writerow(list_1)
    file.close()

str1=str(input())
part1="creat table.*?"
part2="insert into.+?"
if re.match(part1,str1):
    creat_table(str1[12:100])
if re.match(part2,str1):
    insert_into(str1[12:100])

