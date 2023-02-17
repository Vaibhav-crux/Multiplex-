import mysql.connector
from datetime import *
conn=mysql.connector.connect(user='root',host='localhost',password='vaibn')
cursor=conn.cursor()
data_saver=''
z=True
while z:
    s=(str)(input("DO YOU WANT TO DELETE PREVIOUS DATA OF RAJ MULTIPLEX(YES OR NO):"))
    s=s.upper()
    if((s=="YES")or(s=="NO")):
        z=False
if(s=="YES"):
    cursor.execute('SHOW DATABASES')
    db=cursor.fetchall()
    c=0
    t1=('raj_multiplex',)
    for i in range(len(db)-1):
        if(db[i]==t1):
            cursor.execute("DROP DATABASE RAJ_MULTIPLEX")
            c=1
    if(c==1):
        cursor.execute("CREATE DATABASE RAJ_MULTIPLEX")
    else:
        cursor.execute("CREATE DATABASE RAJ_MULTIPLEX")
d=0
if(s=="NO"):
    cursor.execute('SHOW DATABASES')
    db=cursor.fetchall()
    c=0
    t1=('raj_multiplex',)
    for i in db:
        if(i==t1):
           d=1
    if(d==1):
        pass
    else:
        cursor.execute("CREATE DATABASE RAJ_MULTIPLEX")

dd1=date.today()#DATE OF TODAY
dd2=(str)(dd1+timedelta(days=1))#DATE OF TOMORROW
dd3=(str)(dd1+timedelta(days=2))#DATE OF DAY AFTER TOMORROW
dd1=(str)(dd1)

cursor.execute("USE RAJ_MULTIPLEX")
if(c==1):
    #From Here Movie 1
    cursor.execute("""CREATE TABLE MOVIE_1_DAY_1_TIME_1
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_1_DATE VARCHAR(50),
                   MOVIE_1_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_1_DAY_1_TIME_2
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_1_DATE VARCHAR(50),
                   MOVIE_1_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_1_DAY_1_TIME_3
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_1_DATE VARCHAR(50),
                   MOVIE_1_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_1_DAY_1_TIME_4
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_1_DATE VARCHAR(50),
                   MOVIE_1_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_1_DAY_1_TIME_5
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_1_DATE VARCHAR(50),
                   MOVIE_1_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_1_DAY_2_TIME_1
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_1_DATE VARCHAR(50),
                   MOVIE_1_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_1_DAY_2_TIME_2
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_1_DATE VARCHAR(50),
                   MOVIE_1_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_1_DAY_2_TIME_3
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_1_DATE VARCHAR(50),
                   MOVIE_1_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_1_DAY_2_TIME_4
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_1_DATE VARCHAR(50),
                   MOVIE_1_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_1_DAY_2_TIME_5
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_1_DATE VARCHAR(50),
                   MOVIE_1_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_1_DAY_3_TIME_1
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_1_DATE VARCHAR(50),
                   MOVIE_1_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_1_DAY_3_TIME_2
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_1_DATE VARCHAR(50),
                   MOVIE_1_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_1_DAY_3_TIME_3
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_1_DATE VARCHAR(50),
                   MOVIE_1_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_1_DAY_3_TIME_4
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_1_DATE VARCHAR(50),
                   MOVIE_1_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_1_DAY_3_TIME_5
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_1_DATE VARCHAR(50),
                   MOVIE_1_TIME VARCHAR(50)
                   )""")
    #From Here Movie 2
    cursor.execute("""CREATE TABLE MOVIE_2_DAY_1_TIME_1
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_2_DATE VARCHAR(50),
                   MOVIE_2_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_2_DAY_1_TIME_2
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_2_DATE VARCHAR(50),
                   MOVIE_2_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_2_DAY_1_TIME_3
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_2_DATE VARCHAR(50),
                   MOVIE_2_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_2_DAY_1_TIME_4
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_2_DATE VARCHAR(50),
                   MOVIE_2_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_2_DAY_1_TIME_5
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_2_DATE VARCHAR(50),
                   MOVIE_2_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_2_DAY_2_TIME_1
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_2_DATE VARCHAR(50),
                   MOVIE_2_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_2_DAY_2_TIME_2
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_2_DATE VARCHAR(50),
                   MOVIE_2_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_2_DAY_2_TIME_3
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_2_DATE VARCHAR(50),
                   MOVIE_2_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_2_DAY_2_TIME_4
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_2_DATE VARCHAR(50),
                   MOVIE_2_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_2_DAY_2_TIME_5
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_2_DATE VARCHAR(50),
                   MOVIE_2_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_2_DAY_3_TIME_1
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_2_DATE VARCHAR(50),
                   MOVIE_2_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_2_DAY_3_TIME_2
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_2_DATE VARCHAR(50),
                   MOVIE_2_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_2_DAY_3_TIME_3
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_2_DATE VARCHAR(50),
                   MOVIE_2_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_2_DAY_3_TIME_4
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_2_DATE VARCHAR(50),
                   MOVIE_2_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_2_DAY_3_TIME_5
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_2_DATE VARCHAR(50),
                   MOVIE_2_TIME VARCHAR(50)
                   )""")
    #From Here Movie 3 
    cursor.execute("""CREATE TABLE MOVIE_3_DAY_1_TIME_1
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_3_DATE VARCHAR(50),
                   MOVIE_3_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_3_DAY_1_TIME_2
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_3_DATE VARCHAR(50),
                   MOVIE_3_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_3_DAY_1_TIME_3
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_3_DATE VARCHAR(50),
                   MOVIE_3_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_3_DAY_1_TIME_4
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_3_DATE VARCHAR(50),
                   MOVIE_3_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_3_DAY_1_TIME_5
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_3_DATE VARCHAR(50),
                   MOVIE_3_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_3_DAY_2_TIME_1
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_3_DATE VARCHAR(50),
                   MOVIE_3_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_3_DAY_2_TIME_2
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_3_DATE VARCHAR(50),
                   MOVIE_3_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_3_DAY_2_TIME_3
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_3_DATE VARCHAR(50),
                   MOVIE_3_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_3_DAY_2_TIME_4
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_3_DATE VARCHAR(50),
                   MOVIE_3_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_3_DAY_2_TIME_5
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_3_DATE VARCHAR(50),
                   MOVIE_3_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_3_DAY_3_TIME_1
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_3_DATE VARCHAR(50),
                   MOVIE_3_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_3_DAY_3_TIME_2
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_3_DATE VARCHAR(50),
                   MOVIE_3_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_3_DAY_3_TIME_3
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_3_DATE VARCHAR(50),
                   MOVIE_3_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_3_DAY_3_TIME_4
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_3_DATE VARCHAR(50),
                   MOVIE_3_TIME VARCHAR(50)
                   )""")
    cursor.execute("""CREATE TABLE MOVIE_3_DAY_3_TIME_5
                  (
                   SEAT_ID VARCHAR(50) NOT NULL,
                   SEAT_CLASS VARCHAR(50) NOT NULL,
                   STATUS VARCHAR(50),
                   MOVIE_3_DATE VARCHAR(50),
                   MOVIE_3_TIME VARCHAR(50)
                   )""")
    l1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
    l2=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
    l3=[]
    for i in l1:
        for j in l2:
            l3.append(i+j)
    for i in range(0,len(l3)):
        t=l3[i]
        if((t[0]=='A')or(t[0]=='B')or(t[0]=='C')or(t[0]=='D')):
            cursor.execute("INSERT INTO MOVIE_1_DAY_1_TIME_1 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd1+"','9:00am')")
            cursor.execute("INSERT INTO MOVIE_1_DAY_1_TIME_2 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd1+"','12:00pm')")
            cursor.execute("INSERT INTO MOVIE_1_DAY_1_TIME_3 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd1+"','3:00pm')")
            cursor.execute("INSERT INTO MOVIE_1_DAY_1_TIME_4 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd1+"','6:00pm')")
            cursor.execute("INSERT INTO MOVIE_1_DAY_1_TIME_5 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd1+"','9:00pm')")
            cursor.execute("INSERT INTO MOVIE_1_DAY_2_TIME_1 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd2+"','9:00am')")
            cursor.execute("INSERT INTO MOVIE_1_DAY_2_TIME_2 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd2+"','12:00pm')")
            cursor.execute("INSERT INTO MOVIE_1_DAY_2_TIME_3 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd2+"','3:00pm')")
            cursor.execute("INSERT INTO MOVIE_1_DAY_2_TIME_4 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd2+"','6:00pm')")
            cursor.execute("INSERT INTO MOVIE_1_DAY_2_TIME_5 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd2+"','9:00pm')")
            cursor.execute("INSERT INTO MOVIE_1_DAY_3_TIME_1 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd3+"','9:00am')")
            cursor.execute("INSERT INTO MOVIE_1_DAY_3_TIME_2 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd3+"','12:00pm')")
            cursor.execute("INSERT INTO MOVIE_1_DAY_3_TIME_3 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd3+"','3:00pm')")
            cursor.execute("INSERT INTO MOVIE_1_DAY_3_TIME_4 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd3+"','6:00pm')")
            cursor.execute("INSERT INTO MOVIE_1_DAY_3_TIME_5 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd3+"','9:00pm')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_1_TIME_1 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd1+"','9:00am')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_1_TIME_2 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd1+"','12:00pm')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_1_TIME_3 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd1+"','3:00pm')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_1_TIME_4 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd1+"','6:00pm')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_1_TIME_5 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd1+"','9:00pm')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_2_TIME_1 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd2+"','9:00am')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_2_TIME_2 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd2+"','12:00pm')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_2_TIME_3 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd2+"','3:00pm')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_2_TIME_4 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd2+"','6:00pm')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_2_TIME_5 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd2+"','9:00pm')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_3_TIME_1 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd3+"','9:00am')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_3_TIME_2 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd3+"','12:00pm')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_3_TIME_3 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd3+"','3:00pm')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_3_TIME_4 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd3+"','6:00pm')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_3_TIME_5 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd3+"','9:00pm')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_1_TIME_1 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd1+"','9:00am')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_1_TIME_2 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd1+"','12:00pm')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_1_TIME_3 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd1+"','3:00pm')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_1_TIME_4 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd1+"','6:00pm')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_1_TIME_5 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd1+"','9:00pm')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_2_TIME_1 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd2+"','9:00am')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_2_TIME_2 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd2+"','12:00pm')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_2_TIME_3 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd2+"','3:00pm')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_2_TIME_4 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd2+"','6:00pm')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_2_TIME_5 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd2+"','9:00pm')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_3_TIME_1 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd3+"','9:00am')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_3_TIME_2 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd3+"','12:00pm')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_3_TIME_3 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd3+"','3:00pm')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_3_TIME_4 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd3+"','6:00pm')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_3_TIME_5 VALUES('"+l3[i]+"','"+"PLATINUM','"+"NOT BOOKED','"+dd3+"','9:00pm')")
        else:
            cursor.execute("INSERT INTO MOVIE_1_DAY_1_TIME_1 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd1+"','9:00am')")
            cursor.execute("INSERT INTO MOVIE_1_DAY_1_TIME_2 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd1+"','12:00pm')")
            cursor.execute("INSERT INTO MOVIE_1_DAY_1_TIME_3 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd1+"','3:00pm')")
            cursor.execute("INSERT INTO MOVIE_1_DAY_1_TIME_4 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd1+"','6:00pm')")
            cursor.execute("INSERT INTO MOVIE_1_DAY_1_TIME_5 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd1+"','9:00pm')")
            cursor.execute("INSERT INTO MOVIE_1_DAY_2_TIME_1 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd2+"','9:00am')")
            cursor.execute("INSERT INTO MOVIE_1_DAY_2_TIME_2 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd2+"','12:00pm')")
            cursor.execute("INSERT INTO MOVIE_1_DAY_2_TIME_3 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd2+"','3:00pm')")
            cursor.execute("INSERT INTO MOVIE_1_DAY_2_TIME_4 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd2+"','6:00pm')")
            cursor.execute("INSERT INTO MOVIE_1_DAY_2_TIME_5 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd2+"','9:00pm')")
            cursor.execute("INSERT INTO MOVIE_1_DAY_3_TIME_1 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd3+"','9:00am')")
            cursor.execute("INSERT INTO MOVIE_1_DAY_3_TIME_2 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd3+"','12:00pm')")
            cursor.execute("INSERT INTO MOVIE_1_DAY_3_TIME_3 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd3+"','3:00pm')")
            cursor.execute("INSERT INTO MOVIE_1_DAY_3_TIME_4 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd3+"','6:00pm')")
            cursor.execute("INSERT INTO MOVIE_1_DAY_3_TIME_5 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd3+"','9:00pm')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_1_TIME_1 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd1+"','9:00am')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_1_TIME_2 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd1+"','12:00pm')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_1_TIME_3 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd1+"','3:00pm')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_1_TIME_4 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd1+"','6:00pm')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_1_TIME_5 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd1+"','9:00pm')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_2_TIME_1 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd2+"','9:00am')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_2_TIME_2 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd2+"','12:00pm')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_2_TIME_3 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd2+"','3:00pm')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_2_TIME_4 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd2+"','6:00pm')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_2_TIME_5 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd2+"','9:00pm')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_3_TIME_1 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd3+"','9:00am')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_3_TIME_2 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd3+"','12:00pm')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_3_TIME_3 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd3+"','3:00pm')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_3_TIME_4 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd3+"','6:00pm')")
            cursor.execute("INSERT INTO MOVIE_2_DAY_3_TIME_5 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd3+"','9:00pm')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_1_TIME_1 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd1+"','9:00am')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_1_TIME_2 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd1+"','12:00pm')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_1_TIME_3 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd1+"','3:00pm')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_1_TIME_4 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd1+"','6:00pm')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_1_TIME_5 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd1+"','9:00pm')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_2_TIME_1 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd2+"','9:00am')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_2_TIME_2 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd2+"','12:00pm')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_2_TIME_3 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd2+"','3:00pm')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_2_TIME_4 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd2+"','6:00pm')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_2_TIME_5 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd2+"','9:00pm')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_3_TIME_1 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd3+"','9:00am')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_3_TIME_2 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd3+"','12:00pm')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_3_TIME_3 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd3+"','3:00pm')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_3_TIME_4 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd3+"','6:00pm')")
            cursor.execute("INSERT INTO MOVIE_3_DAY_3_TIME_5 VALUES('"+l3[i]+"','"+"GOLD','"+"NOT BOOKED','"+dd3+"','9:00pm')")
            
def main_menu():
      print("~"*134*2)
      print("CONNECTED TO RAJ MULTIPLEX.")
      print((" "*60),'WELCOME TO PVR')
      print((" "*60),"``````````````")
      print("SHOW TIMINGS:")
      print("````````````")
      global movie_name
      global timings
      movie_name=['KGF CHAPTER 1','3 IDIOTS','CHHICHHORE']
      timings=['9:00am','12:00pm','3:00pm','6:00pm']
      for i in movie_name:
            print(i,end=' : ')
            for j in timings:
                  print(j,end=' , ')
            print('9:00pm')
      timings.append('9:00pm')
      print()
      z=True
      while z:
          print()
          print("PLEASE SELECT A MOVIE:")
          for i in range(0,len(movie_name)):
                  print(i+1,".",movie_name[i])
          global mn
          mn=(int)(input("ENTER YOUR CHOICE:"))#CHOICE OF MOVIE
          if((mn>=1)and(mn<=3)):
              z=False
          else:
              print("INVALID CHOICE!!!!!!!!")
              z=True
      print()
      z=True
      while z:
          print()
          print("PLEASE SELECT A SHOW TIMING:")
          for i in range(0,len(timings)):
                  print(i+1,".",timings[i])
          global cht
          cht=(int)(input("ENTER YOUR CHOICE:"))#CHOICE OF TIMING
          if((cht>=1)and(cht<=5)):
              z=False
          else:
              print("INVALID CHOICE!!!!!!!!")
              z=True
      print()
      z=True
      while z:
          print()
          print("WHICH DAY:")
          print("1.TODAY")
          print("2.TOMORROW")
          print("3.DAY AFTER TOMORROW")
          global md
          md=(int)(input("ENTER YOUR CHOICE:"))#CHOICE OF DAY
          if(md==1)and(mn==1):
                movie_1()
                z=False
          if(md==1)and(mn==2):
                movie_2()
                z=False
          if(md==1)and(mn==3):
                movie_3()
                z=False
          if(md==2)and(mn==1):
                movie_1()
                z=False
          if(md==2)and(mn==2):
                movie_2()
                z=False
          if(md==2)and(mn==3):
                movie_3()
                z=False
          if(md==3)and(mn==1):
                movie_1()
                z=False
          if(md==3)and(mn==2):
                movie_2()
                z=False
          if(md==3)and(mn==3):
                movie_3()
                z=False
          else:
              print("INVALID CHOICE!!!!!!!!")
              z=True
def movie_1():
  if(md==1):
    if(cht==1):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_1_TIME_1 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_1_TIME_1 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_1_DAY_1_TIME_1 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_1_DAY_1_TIME_1 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

    if(cht==2):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_1_TIME_2 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_1_TIME_2 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_1_DAY_1_TIME_2 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_1_DAY_1_TIME_2 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        
    if(cht==3):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_1_TIME_3 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_1_TIME_3 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_1_DAY_1_TIME_3 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_1_DAY_1_TIME_3 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

    if(cht==4):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_1_TIME_4 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_1_TIME_4 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_1_DAY_1_TIME_4 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_1_DAY_1_TIME_4 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

    if(cht==5):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_1_TIME_5 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_1_TIME_5 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_1_DAY_1_TIME_5 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_1_DAY_1_TIME_5 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
  if(md==2):
    if(cht==1):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_2_TIME_1 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_2_TIME_1 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_1_DAY_2_TIME_1 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_1_DAY_2_TIME_1 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

    if(cht==2):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_2_TIME_2 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_2_TIME_2 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_1_DAY_2_TIME_2 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_1_DAY_2_TIME_2 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        
    if(cht==3):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_2_TIME_3 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_2_TIME_3 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_1_DAY_2_TIME_3 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_1_DAY_2_TIME_3 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

    if(cht==4):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_2_TIME_4 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_2_TIME_4 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_1_DAY_2_TIME_4 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_1_DAY_2_TIME_4 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

    if(cht==5):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_2_TIME_5 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_2_TIME_5 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_1_DAY_2_TIME_5 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_1_DAY_2_TIME_5 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

  if(md==3):
    if(cht==1):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_3_TIME_1 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_3_TIME_1 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_1_DAY_3_TIME_1 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_1_DAY_3_TIME_1 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

    if(cht==2):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_3_TIME_2 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_3_TIME_2 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_1_DAY_3_TIME_2 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_1_DAY_3_TIME_2 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        
    if(cht==3):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_3_TIME_ WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_3_TIME_3 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_1_DAY_3_TIME_3 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_1_DAY_3_TIME_3 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

    if(cht==4):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_3_TIME_4 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_3_TIME_4 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_1_DAY_3_TIME_4 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_1_DAY_3_TIME_4 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

    if(cht==5):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_3_TIME_5 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_1_DAY_3_TIME_5 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_1_DAY_3_TIME_5 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_1_DAY_3_TIME_5 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

def movie_2():
  if(md==1):
    if(cht==1):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_1_TIME_1 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_1_TIME_1 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_2_DAY_1_TIME_1 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_2_DAY_1_TIME_1 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

    if(cht==2):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_1_TIME_2 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_1_TIME_2 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_2_DAY_1_TIME_2 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_2_DAY_1_TIME_2 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        
    if(cht==3):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_1_TIME_3 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_1_TIME_3 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_2_DAY_1_TIME_3 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_2_DAY_1_TIME_3 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

    if(cht==4):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_1_TIME_4 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_1_TIME_4 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_2_DAY_1_TIME_4 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_2_DAY_1_TIME_4 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

    if(cht==5):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_1_TIME_5 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_1_TIME_5 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_2_DAY_1_TIME_5 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_2_DAY_1_TIME_5 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
  if(md==2):
    if(cht==1):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_2_TIME_1 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_2_TIME_1 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_2_DAY_2_TIME_1 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_2_DAY_2_TIME_1 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

    if(cht==2):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_2_TIME_2 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_2_TIME_2 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_2_DAY_2_TIME_2 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_2_DAY_2_TIME_2 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        
    if(cht==3):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_2_TIME_3 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_2_TIME_3 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_2_DAY_2_TIME_3 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_2_DAY_2_TIME_3 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

    if(cht==4):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_2_TIME_4 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_2_TIME_4 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_2_DAY_2_TIME_4 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_2_DAY_2_TIME_4 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

    if(cht==5):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_2_TIME_5 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_2_TIME_5 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_2_DAY_2_TIME_5 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_2_DAY_2_TIME_5 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

  if(md==3):
    if(cht==1):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_3_TIME_1 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_3_TIME_1 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_2_DAY_3_TIME_1 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_2_DAY_3_TIME_1 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

    if(cht==2):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_3_TIME_2 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_3_TIME_2 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_2_DAY_3_TIME_2 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_2_DAY_3_TIME_2 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        
    if(cht==3):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_3_TIME_ WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_3_TIME_3 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_2_DAY_3_TIME_3 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_2_DAY_3_TIME_3 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

    if(cht==4):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_3_TIME_4 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_3_TIME_4 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_2_DAY_3_TIME_4 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_2_DAY_3_TIME_4 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

    if(cht==5):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_3_TIME_5 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_2_DAY_3_TIME_5 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_2_DAY_3_TIME_5 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_2_DAY_3_TIME_5 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

def movie_3():
  if(md==1):
    if(cht==1):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_1_TIME_1 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_1_TIME_1 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_3_DAY_1_TIME_1 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_3_DAY_1_TIME_1 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

    if(cht==2):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_1_TIME_2 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_1_TIME_2 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_3_DAY_1_TIME_2 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_3_DAY_1_TIME_2 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        
    if(cht==3):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_1_TIME_3 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_1_TIME_3 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_3_DAY_1_TIME_3 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_3_DAY_1_TIME_3 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

    if(cht==4):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_1_TIME_4 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_1_TIME_4 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_3_DAY_1_TIME_4 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_3_DAY_1_TIME_4 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

    if(cht==5):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_1_TIME_5 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_1_TIME_5 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_3_DAY_1_TIME_5 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_3_DAY_1_TIME_5 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
  if(md==2):
    if(cht==1):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_2_TIME_1 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_2_TIME_1 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_3_DAY_2_TIME_1 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_3_DAY_2_TIME_1 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

    if(cht==2):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_2_TIME_2 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_2_TIME_2 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_3_DAY_2_TIME_2 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_3_DAY_2_TIME_2 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        
    if(cht==3):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_2_TIME_3 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_2_TIME_3 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_3_DAY_2_TIME_3 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_3_DAY_2_TIME_3 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

    if(cht==4):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_2_TIME_4 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_2_TIME_4 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_3_DAY_2_TIME_4 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_3_DAY_2_TIME_4 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

    if(cht==5):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_2_TIME_5 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_2_TIME_5 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_3_DAY_2_TIME_5 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_3_DAY_2_TIME_5 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

  if(md==3):
    if(cht==1):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_3_TIME_1 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_3_TIME_1 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_3_DAY_3_TIME_1 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_3_DAY_3_TIME_1 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

    if(cht==2):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_3_TIME_2 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_3_TIME_2 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_3_DAY_3_TIME_2 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_3_DAY_3_TIME_2 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        
    if(cht==3):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_3_TIME_ WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_3_TIME_3 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_3_DAY_3_TIME_3 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_3_DAY_3_TIME_3 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

    if(cht==4):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_3_TIME_4 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_3_TIME_4 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_3_DAY_3_TIME_4 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_3_DAY_3_TIME_4 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()

    if(cht==5):
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_3_TIME_5 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='PLATINUM'""")
        se_av_pl=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_pl:
            l.append(i[0])
        se_av_pl=l
        cursor.execute("""SELECT SEAT_ID FROM MOVIE_3_DAY_3_TIME_5 WHERE STATUS='NOT BOOKED' AND SEAT_CLASS='GOLD'""")
        se_av_go=cursor.fetchall()
        l=[]#TO CONVERT se_av_pl AND se_av_go INTO A SIMPLE PLAIN LIST FROM TUPLES INSIDE LIST
        for i in se_av_go:
            l.append(i[0])
        se_av_go=l
        print()
        print("SEATS AVIALABLE IN PLATINUM:",len(se_av_pl))
        print("SEATS AVAILABLE IN GOLD:",len(se_av_go))
        amt=0.0
        z=True
        while z:
                print()
                print("CHOOSE YOUR CLASS:")
                print("1.GOLD(Rs 125 per person)")
                print("2.PLATINUM(Rs 180 per person)")
                ch=(str)(input("ENTER YOUR CHOICE:"))
                if((ch=='1')or(ch=='2')):
                    z=False
                else:
                    print("ENTER A VALID CHOICE.")
                    z=True
        no=(int)(input("ENTER NUMBER OF SEATS:"))
        if(ch=='1'):
            if(no<=(len(se_av_go))):
                for i in range(no):
                    datasaver="UPDATE MOVIE_3_DAY_3_TIME_5 SET STATUS='BOOKED' WHERE SEAT_CLASS='GOLD' AND SEAT_ID='"+se_av_go[i]+"';"
                    cursor.execute(datasaver)
                    conn.commit()
                amt=(125*no)+(0.18*125*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()
        if(ch=='2'):
            if(no<=(len(se_av_pl))):
                for i in range(no):
                   datasaver="UPDATE MOVIE_3_DAY_3_TIME_5 SET STATUS='BOOKED' WHERE SEAT_CLASS='PLATINUM' AND SEAT_ID='"+se_av_pl[i]+"';"
                   cursor.execute(datasaver)
                   conn.commit()
                amt=(180*no)+(0.18*180*no)
                print("AMOUNT:",amt,"(INCLUSIVE OF ALL TAXES.)")
                ticket(no,amt,ch,se_av_pl,se_av_go)
            else:
                print("NOT ENOUGH SEATS!!!!! \nVERY SORRY!!!!!")
                main_menu()


def ticket(no,amt,ch,se_av_pl,se_av_go):
    print("~"*134*2)
    for i in range(no):
        print((" "*60),'RAJ MULTIPLEX')
        print((" "*60),"```````````")
        print((" "*50),"TICKET BOOKED!!!!!!!!")
        if(mn==1):
              print((" "*50),"MOVIE NAME:",movie_name[0])
        if(mn==2):
              print((" "*50),"MOVIE NAME:",movie_name[1])
        if(mn==3):
              print((" "*50),"MOVIE NAME:",movie_name[2])
        if(md==1):
            print((" "*50),"MOVIE DATE:",dd1)
        if(md==2):
            print((" "*50),"MOVIE DATE:",dd2)
        if(md==3):
            print((" "*50),"MOVIE DATE:",dd3)
        if(cht==1):
              print((" "*50),"MOVIE TIME:",timings[0])
        if(cht==2):
              print((" "*50),"MOVIE TIME:",timings[1])
        if(cht==3):
              print((" "*50),"MOVIE TIME:",timings[2])
        if(cht==4):
              print((" "*50),"MOVIE TIME:",timings[3])
        if(cht==5):
              print((" "*50),"MOVIE TIME:",timings[4])
        if(ch=='1'):
            print((" "*50),"SEAT ID:",se_av_go[i])
            print((" "*50),"PRICE OF 1 TICKET:Rs 125")
        if(ch=='2'):
            print((" "*50),"SEAT ID:",se_av_pl[i])
            print((" "*50),"PRICE OF 1 TICKET:Rs 180")
        print((" "*50),"AMOUNT:","Rs:",amt)
        print((" "*50),"THANK YOU FOR VISITING!!!")
        print((" "*50),"HOPE TO SERVE YOU AGAIN.")
        print()
    print("~"*134*2)
    main_menu()
    
conn.commit()
main_menu()
