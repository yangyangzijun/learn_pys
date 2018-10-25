import pymysql

mydb=pymysql.connect(
    host='127.0.0.1',
    user = "root",
    passwd ="root",
)
tt=mydb.cursor()

tt.execute("show databases")

tt.execute("create database python_database")

tt.execute("use python_database")
tt.execute("create  table  students(sno char(8) primary key , sanme char(10) ,ssex char(2),sage int,major char(20))")

tt.execute("insert  into students values ('20100001','史玉明','女',20,'计算机'),('20100100','李明虎','男',21,'机械'), ('20100234','张翔','男',21,'化工')")

tt.execute("create table award (sno char(8)  ,details varchar (200),primary key(sno),foreign key (sno) references students(sno))")
tt.execute("insert  into  award values ('20100001','2011校奖学金，2012国家奖学金'), ('20100100','2012校奖学金') ")

mydb.commit()


tt.close()

