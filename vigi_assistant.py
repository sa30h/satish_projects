import pyttsx3
import platform
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import mysql.connector
import pandas as pd


engine=pyttsx3.init('sapi5')
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)
rate=engine.getProperty('rate')
engine.setProperty('rate',135)

def command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......//////////....////")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing.....////////..////")
        query=r.recognize_google(audio,'en-in')
        print("User Said:{query} \n")
    except Exception as e:
        print("I did't understand!!! Please Repeat!!")
        return "none"
    return query


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def system_info():
    machine=platform.machine()
    version=platform.version()
    users=platform.uname()
    platform_info=platform.system()
    processor=platform.processor()
    speak(processor)

def greet():
    current_time=datetime.datetime.now()
    year=current_time.year
    return year

def data_base():                        #line 51 to 90 database operations
    conn=mysql.connector.connect(host="localhost",user="root",password="satish",database="assistant")
    my_cursor=conn.cursor()
    tablename="student"
    operation=input("Choose CRUD operation")
    operation=operation.lower()
    if "create table" in operation:
        try:
            query_create='create table  student(Name varchar(20),Surname varchar(10),Age int)'
            my_cursor.execute(query_create)
            print("Table Created")
        except Exception as a:
            print("oops..something went wrong!!")

    elif "show" in operation:
        try:
            query_show='show tables'
            my_cursor.execute(query_show)
            for x in my_cursor:
                print("DATABASE HAS",x)
        except Exception as b:
            print("Something went worng")
            

    elif "insert" in operation:
        try:
            query_insert="insert into student(Name,Surname,Age) values('Akshunya','Yadav',21)"
            my_cursor.execute(query_insert)
            conn.commit()
            print(my_cursor.rowcount,"record inserted.")
        except Exception as c:
            print("Something went wrong")
    elif "select" in operation:
        try:
            query_show="select *from student"
            result=my_cursor.execute(query_show)
            for x in result:
                print(x)
        except Exception as e:
            print("cant show records")   

def csv_operations():                   #read csv function
    speak("please tell me file name")
    file=command()

    data_file=pd.read_csv(file)
    
    print(data_file)
    
 
        
    



    


if __name__=='__main__':
    # speak("hello mr parmod")
    csv_operations()
    # data_base()
    # while True:
    #     query=command().lower()

    #     if "wikipedia" in query:
    #         print("searching wikipeadia")
    #         query=query.replace("wikipedia", "")
    #         results=wikipedia.summary(query,sentences=2)
    #         print(results)
    #         speak("according to wikipedia")
    #         speak(results)

    #     elif "open youtube" in query:
    #         webbrowser.open("youtube.com")

    #     elif "sleep" in query:
    #         speak("Ok sir, i am signing out and this is edited in github")
    #         exit()
            



