from bs4 import BeautifulSoup
import requests
from tkinter import *
url="https://ssc.nic.in/"
r=requests.get(url)
html_content=r.content
soup=BeautifulSoup(html_content,'html.parser')

container=soup.findAll("div",{"class":"eachNotification"})
i=0
for x in container:
    date=x.span.text
    news=x.a.text.strip()
    link=x.a.get('href')
    print(date)
    print(news)
    print(link)
    print("\n")
    i+=1
    if i==10:
        break

