from bs4 import BeautifulSoup
import requests
import smtplib
from email.message import EmailMessage

def notifications():
    url="https://ssc.nic.in/"
    r=requests.get(url)
    html_content=r.content
    soup=BeautifulSoup(html_content,'html.parser')

    container=soup.findAll("div",{"class":"eachNotification"})
    i=0
    date=[]
    news=[]
    link=[]
    f=open("ssc.txt","w")
    for x in container:
        date=x.span.text
        news=x.a.text.strip()
        link=x.a.get('href')
        f.write(date)
        f.write("\n")
        f.write(news)
        f.write("\n")
        f.write(link)
        f.write("\n")
        print(date)
        print(news)
        print(link)
        print("\n")
        i+=1
        
        if i==3:
            break
    f.close()
    f=open("ssc.txt","r")
    data=f.read()
    f.close()
    return data



def alert():
    email_list=['satishrjk07@gmail.com','singhshanky140@gmail.com','dikshantbisht02@gmail.com']
    body=notifications()
    for i in range(0,len(email_list)):
        
        subject="SSC NOTIFICATIONS"
        msg=EmailMessage()
        msg.set_content(body)
        msg['subject']=subject
        
        msg['to']=email_list[i]
        user="satishrjk07@gmail.com"
        password="pkbymvrwxzaukmuu"
        msg['from']= user
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(user,password)
        server.send_message(msg)
        
        server.quit()
        print("email sent to",email_list[i])

if __name__ == "__main__":
    # alert("hey","hello world","satishrjk07@gmail.com")
    
    alert()



    

