import time
from plyer import notification
import mysql.connector
from datetime import datetime,date
import smtplib
from email.message import EmailMessage

def data_base():
    
    conn=mysql.connector.connect(host="localhost",
    username="root",
    password="satish",
    db="finance")
    if conn:
        print(" Database connected")
    cursor=conn.cursor()
    query1="create table Costumers(Sr_no int NOT NULL,Name varchar(20) NOT NULL,Costumer_Id varchar(5),Amount_Taken float,Installment_Date date,PRIMARY KEY(Costumer_Id);"
    name=[]
    c_id=[]
    amount=[]
    Dt=list()
    cursor.execute("select Name from Costumers")
    count=len(cursor.fetchall())
    
    print(count,"Rows in table") 
    for i in range(1,count+1):
        query_info="select Installment_Date from Costumers where Sr_no='{Sr_no}'".format(Sr_no=i)
        cursor.execute(query_info)
        result=cursor.fetchall()
        t=result[0]
        Dt.append(t[0])
        # print(Dt)
    print(Dt)
    today=datetime.now()
    # print(today.strftime('%d'))
    # print(Dt[1].strftime('%d'))

    for j in range(0,len(Dt)):
        if Dt[j].strftime('%d')==today.strftime('%d'):
            
            query_name="select Name from Costumers where date(Installment_Date)=curdate()"
            cursor.execute(query_name)
            result=cursor.fetchall()
            name=result[0]
            name=str(name[0])
            print(name)     #NAME
            query_email="select email from Costumers where date(Installment_Date)=curdate()"
            cursor.execute(query_email)
            result=cursor.fetchall()
            email=result[0]    
            email=str(email[0])
            
            print(email)        #EMAIL
            print(Dt[j])        #DATE
            #Desktop Notification
            notification.notify(
            title='INSTALLMENT REMINDER',
            message="""Hey {Name} your Install Is pending""".format(Name=name),
            app_icon='icon/piggy.ico',
            timeout=5
            )
            time.sleep(22)
            #email send
            # msg=EmailMessage()
            # body="Hello Mr.{Name} today is your installment date".format(Name=name)
            # msg.set_content(body)
            # msg['subject']="Installment Alert"
            # msg['to']=email
            # user="satishrjk07@gmail.com"
            # password="bgpbighpylwrbqit"
            # msg['from']=user
            # server=smtplib.SMTP("smtp.gmail.com",587)
            # server.starttls()
            # server.login(user,password)
            # server.send_message(msg)
            # print("Email sent")
            # server.quit()

            # Alert()
        
     
#     print("Database")
#     print("PRESS 1 FOR INSERT VALUES\n")
#     print("------->\t")
#     print("PRESS 2 FOR SHOW DATA \n")
#     print("------->\t")
#     print("PRESS 3 FOR UPDATE \n")
#     print("------->\t")
#     print("PRESS 4 FOR DELETE \n")
#     print("------->\t")
#     print("PRESS 5 FOR DROP COLUMN ")
#     print("------->\t")
#     operation=int(input())
#     if operation==1:

#         Sr_no=int(input("Enter Sr.no \t"))
#         Name=str(input("Enter Name \t"))
#         Costumer_Id=str(input("Enter Costumer Id \t"))
#         Amount=float(input("Enter Amount Taken \t"))
#         Date_input=tuple(input("Type date dd/mm/year: "))
#         Date=datetime.now()
#         Email=input("enter emil")

#         query2="Insert into Costumers(Sr_no,Name,Costumer_Id,Amount_Taken,Installment_Date,Email) values(%s,%s,%s,%s,%s,%s)"
#         val=(Sr_no,Name,Costumer_Id,Amount,Date,Email)
#         cursor.execute(query2,val)
#         conn.commit()
#         print(cursor.rowcount,"row(s) inserted")

#     if operation==2:
#         query4="select * from Costumers order by Sr_no"
#         cursor.execute(query4)
#         result=cursor.fetchall()
#         for x in result:
#             print(x)

#     if operation==3:
#         column=input("Enter column which one you want to change \t")
#         val=input("Enter new val of column \t")
#         identity=input("Enter Name whose data want to change \t")
#         query3="""update Costumers set {column}='{val}' where Name='{identity}'""".format(column=column,val=val,identity=identity)
#         cursor.execute(query3)
#         conn.commit()
#         print(cursor.rowcount,"row(s) updated")

#     if operation==4:
#         dele=input("Enter Name whose record want to delete")
#         queryd="delete from Costumers where Name='{dele}'".format(dele=dele)
#         cursor.execute(queryd)
#         conn.commit()
#         print(cursor.rowcount,"row(s) deleted")
        
    

 


# def Alert():
#      notification.notify(
#         title='INSTALLMENT REMINDER',
#         message='Hey Satish your Install Is pending',
#         app_icon='icon/piggy.ico',
#         timeout=5
#     )
#      time.sleep(22)





if __name__=='__main__':
    print(date.today())
    data_base()
    
   
