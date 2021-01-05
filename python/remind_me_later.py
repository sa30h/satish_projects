import imaplib
import email
user="satishrjk07@gmail.com"
password="swivdgvmzqkogsvt"
mail=imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(user,password)
mail.select("inbox")
mail.create("item2")
mail.list()
result,data=mail.uid('search',None,"ALL")
inbox_item_list=data[0].split()
most_recent=inbox_item_list[-1]
oldest=inbox_item_list[0]
result2,email_data=mail.uid('fetch',most_recent,'(RFC822)')
raw_email=email_data[0][1].decode("utf-8")
email_message=email.message_from_string(raw_email)
tos=email_message['to']
froms=email_message['from']
sub=email_message['subject']
date_=email_message['date']
print("Date:",date_)
print("From:",froms)
print("Subject:",sub)
print("To:",tos)
sub_list=sub.split(",")
date_alert=sub_list[1]
print(type(date_alert))




