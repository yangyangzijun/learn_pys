import  re
import csv
def creat_table(s):
    patt1='.+?{'
    patt2='.*?,|.+?}'

    str_1=re.search(patt1,s)
    s=s[len(str_1[0]):100]
    list=re.compile(patt2).findall(s)

    file=open("F:\py/test/"+str_1[0][:-1]+".csv",'w',newline='')


    list_1=list
    i=0
    for li in list:
        print(li[0:-1])
        list_1[i]=li[0:-1]
        i=i+1
    writer=csv.writer(file)
    writer.writerow(list_1)

    file.close()
    return list_1
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
    list_2=list
    for li in list:
        list_2[i]=li[1:-2]
        i=i+1

    if str(list_2[2])=="男" or str(list_2[2])=="女":


        if int(list_2[3])>15 and int(list_2[3])<45:
            writer.writerow(list_2)
        else:
            print("the age is not right")
    else:
        print("the sex is not right")

    file.close()

str1=str(input())
part1="creat table.*?"
part2="insert into.+?"
if re.match(part1,str1):
    creat_table(str1[12:100])
if re.match(part2,str1):
    insert_into(str1[12:100])

