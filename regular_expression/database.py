import  re
import csv
def update(s):
    patt1='.+? set'
    patt2='set .+?while'
    patt3=' .+?=|,.+?='
    patt4="'.+?'"
    patt5="while .+?[<=>]'.+'"
    patt6=" .+?[<=>]|,.+?[<=>]"
    patt7="'.+?'"
    patt8="[=><]'"
    list_1=re.compile(patt1).findall(s)
    list_2=re.compile(patt2).findall(s)
    list_3=re.compile(patt3).findall(str(list_2))
    list_4=re.compile(patt4).findall(str(list_2))
    list_5=re.compile(patt5).findall(s)
    list_6=re.compile(patt6).findall(str(list_5))
    list_7=re.compile(patt7).findall(str(list_5))
    list_7_1=[]#条件列的值
    for l in list_7:
        list_7_1.append(l[1:-1])
    print(list_6)
    list_6_1=[]#条件的列
    list_8=re.compile(patt8).findall(str(list_5))
    list_while=[]
    for l in list_8:
        list_while.append(l[:-1])
    print(list_while)
    for l in list_6:
        list_6_1.append(l[1:-1])

    print(list_6_1)
    print(list_7_1)
    list_3_1=[]#更新的列
    list_4_1=[]#更新的值
    for l in list_3:
        list_3_1.append(l[1:-1])
    for l in list_4:
        list_4_1.append(l[1:-1])
    print(list_3_1)
    print(list_4_1)
    file_name=list_1[0][0:-4]#文件名
    list_read=[]

    data = open("F:\py/test/" + str(file_name) + ".csv", 'r', newline="")
    datal = csv.reader(data)
    for l in datal:
        print(l)
        list_read.append(l)
    data.close()
    location_while=[]
    location_value=[]
    t = 0
    for l in list_6_1:
        t = 0
        for i in list_read[0]:
            if l==i:
                location_while.append(t)

                break
            else:
                t=t+1
    t = 0
    for l in list_3_1:
        t = 0
        for i in list_read[0]:
            if l == i:
                location_value.append(t)

                break
            else:
                t = t + 1



    print(location_while)
    print(location_value)

    for l in list_read:
        flag=0
        ttt = 0

        for i in range(0,len(location_while)):

            if str(list_while[0])=="="and l[location_while[i]]==list_7_1[i]:
                print()
            elif str(list_while[0])=="<"and l[location_while[i]]<list_7_1[i]:
                print()
            elif str(list_while[0])==">"and l[location_while[i]]>list_7_1[i]:

                print()
            elif str(list_while[0])==">="and l[location_while[i]]>=list_7_1[i]:
                print()
            elif str(list_while[0])=="<="and l[location_while[i]]<=list_7_1[i]:
                print()
            else:
                flag=1
                break
        if flag==0:
            for pp in range(0,len(location_value)):
                l[location_value[pp]]=list_4_1[pp]

    print(list_while[0])
    print(list_read)
    data = open("F:\py/test/" + str(file_name) + ".csv", 'w', newline="")
    datal = csv.writer(data)
    for l in list_read:
        datal.writerow(l)
    data.close()






    print(s)
def delete(s):
    patt1='.+? '
    patt2=" \S+?[=><]'.+?'"
    patt3='[=><]'
    patt4=' .+?'+patt3
    patt5="'.+?'"
    list_1=re.search(patt1,s)
    list_2=re.compile(patt2).findall(s)
    print(list_2)

    list_3=re.compile(patt3).findall(str(list_2))
    list_4=re.search(patt4,str(list_2))
    list_5=re.compile(patt5).findall(str(list_2))
    print(list_3)
    print(list_4[0][1:-1])
    print(list_1[0][0:-1])
    print(list_5[0][1:-1])
    list_read=[]
    data = open("F:\py/test/" + str(list_1[0][0:-1]) + ".csv", 'r', newline="")
    datal=csv.reader(data)
    for l in datal:
        print(l)
        list_read.append(l)
    print(list_read)
    data.close()
    location=0
    for l in list_read[0]:
        if l==str(list_4[0][1:-1]):
            break

        else:
            location=location+1
    print(location)

    str1 = ""
    for l in list_3:
        str1 = str1 + str(l)
    print(str1)
    list_write= []
    list_write.append(list_read[0])
    for l in list_read[1:]:
        if str1=='=':
            if l[location]==list_5[0][1:-1]:
                print('uu')
            else:
                list_write.append(l)
        if str1=='>=':
            if l[location]>=list_5[0][1:-1]:
                print('uu')
            else:
                list_write.append(l)
        if str1=='<=':
            if l[location]<=list_5[0][1:-1]:
                print('uu')
            else:
                list_write.append(l)
        if str1 == '<':
            if l[location] < list_5[0][1:-1]:
                print('uu')
            else:
                list_write.append(l)
        if str1 == '>':
            if l[location] > list_5[0][1:-1]:
                print('uu')
            else:
                list_write.append(l)
    print(list_write)
    data = open("F:\py/test/" + str(list_1[0][0:-1]) + ".csv", 'w', newline="")
    write = csv.writer(data)
    for i in list_write:
        write.writerow(i)
def select(s):
    patt1='.+?,|.+? '
    patt2='from .+'
    list_1=re.compile(patt1).findall(s)
    list_3=re.compile(patt2).findall(s)
    list_2=list_1[0:-1]
    list_2_length=0
    for lii in list_1[0:-1]:
        list_2[list_2_length]=lii[0:-1]
        list_2_length=list_2_length+1
    list_4=list_3[0][5:100]
    print(list_2)
    print(list_4)
    if list_2[0]=="*":
        data = open("F:\py/test/" + str(list_4) + ".csv", 'r', newline="")
        datal = csv.reader(data)
        for l in datal:
            print(l)
    else:
        list_5 = [None] * 100
        list_5_length = 0
        data = open("F:\py/test/" + str(list_4) + ".csv", 'r', newline="")
        datal = csv.reader(data)
        datal_1 = datal
        t = 0
        for i in datal:
            if t == 0:
                t = t + 1;
                for y in i:
                    list_5[list_5_length] = str(y)
                    list_5_length = list_5_length + 1
            else:
                break
        data.close()
        list_5 = list_5[0:list_5_length]
        print(list_5)
        location = [0] * len(list_2)
        location_length = 0
        for ll in list_2:
            location_1 = 0
            for tt in list_5:
                if ll == tt:
                    location[location_length] = location_1
                    location_length = location_length + 1
                    break
                location_1 = location_1 + 1
        print(location)
        data = open("F:\py/test/" + str(list_4) + ".csv", 'r', newline="")
        datal = csv.reader(data)
        for o in datal:
            for lll in location:
                mat = "{:^10}"
                print(mat.format(o[lll]), end="")
            print()

def creat_table(s):
        patt1 = '.+?{'
        patt2 = '.*?,|.+?}'

        str_1 = re.search(patt1, s)
        s = s[len(str_1[0]):100]
        list = re.compile(patt2).findall(s)
        file = open("F:\py/test/" + str_1[0][:-1] + ".csv", 'w', newline='')
        list_1 = list
        i = 0
        for li in list:
            print(li[0:-1])
            list_1[i] = li[0:-1]
            i = i + 1
        writer = csv.writer(file)
        writer.writerow(list_1)
        file.close()
        return list_1


def insert_into(s):
    patt1 = '.+?{'
    patt2 = "'.+?',|.+?'}"
    str_1 = re.search(patt1, s)
    s = s[len(str_1[0]):100]
    list = re.compile(patt2).findall(s)
    file_1 = open("F:\py/test/" + str_1[0][:-1] + ".csv", 'r', newline='')
    datal = csv.reader(file_1)
    test=list*2
    length=0
    for t in datal:
        print(t[0])
        test[length]=t[0]
        length=length+1
    test=test[0:length]
    file_1.close()
    file = open("F:\py/test/" + str_1[0][:-1] + ".csv",'a',newline='')
    writer=csv.writer(file)
    i=0
    list_2=list
    for li in list:
        list_2[i]=li[1:-2]
        i=i+1
    flag=0
    for tt in test:
        if tt==list_2[0]:
            flag=1
    if flag==0:
        if str(list_2[2])=="男" or str(list_2[2])=="女":
            if int(list_2[3])>15 and int(list_2[3])<45:
                writer.writerow(list_2)
            else:
                print("the age is not right")
        else:
            print("the sex is not right")
    else:
        print("the number is exit")
    file.close()
for i in  range(0,100):
    str1=str(input())
    part1="creat table.*?"
    part2="insert into.+?"
    part3='select .+?'
    part4='delete from .+?'
    part5='update .+?'
    if re.match(part1,str1):
        creat_table(str1[12:100])
    if re.match(part2,str1):
        insert_into(str1[12:100])
    if re.match(part3,str1):
        select(str1[7:1000])
    if re.match(part4,str1):
        delete(str1[12:100])
    if re.match(part5,str1):
        update(str1[7:])


    if str1=='quit':
        break
    else:
        print("syntax error")





