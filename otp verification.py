import tkinter
from tkinter import*
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import pymysql
from  mainscreen import *
from tkinter import PhotoImage
import tkinter as tk 
from PIL import Image,ImageTk

t=tkinter.Tk()
t.geometry('800x800')
t.config(bg='light blue')
def sendgmail():
    from_address = "thekenstudy@gmail.com"
    to_address = e3.get()


    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = e2.get()
    msg['From'] = from_address
    msg['To'] = to_address
    mes=str(round(random.random()*19000))

    # Create the message (HTML).
    Text = "thanks your otp is <br>"+mes

    # Record the MIME type - text/html.
    part1 = MIMEText(Text, 'html')

    # Attach parts into message container
    msg.attach(part1)

    # Credentials
    username = 'thekenstudy@gmail.com'  
    password = 'tzfvqdwitwjzkfbd'

    # Sending the email
    ## note - this smtp config worked for me, I found it googling around, you may have to tweak the # (587) to get yours to work
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo()
    server.starttls()
    server.login(username,password)  
    server.sendmail(from_address, to_address, msg.as_string())  
    server.quit()
    messagebox.showinfo('hii','mail send')
    f=open('emailotp.txt','w')
    f.write(e3.get()+'\t'+mes)
    f.close()
    messagebox.showinfo('hi','otp saved')

def verify():
    db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
    cur=db.cursor()
    xa=e1.get()
    xb=e2.get()
    xc=e3.get()
    sql="select count(*) from logintable where userid='%s' and password='%s' and email='%s'"%(xa,xb,xc)
    cur.execute(sql)
    data=cur.fetchone()
    db.close()
    
    f=open('emailotp.txt','r')
    s=f.read()
    ta=s.split()
    if data[0]==1 and ta[0]==e3.get() and ta[1]==e4.get():
        messagebox.showinfo('hi','login successful')
        t.withdraw()
        showmain()
    else:
        messagebox.showinfo('hi','login failed')
def sendpassword():
    db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
    cur=db.cursor()
    xa=e1.get()
    xb=e3.get()
    sql="select password from logintable where userid='%s' and email='%s'"%(xa,xb)    
    cur.execute(sql)
    data=cur.fetchone()
    em=data[0]
    db.close()
    from_address = "thekenstudy@gmail.com"
    to_address = e3.get()

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "password"
    msg['From'] = from_address
    msg['To'] = to_address
    mes=em

    # Create the message (HTML).
    Text = "thanks your password is <br>"+mes

    # Record the MIME type - text/html.
    part1 = MIMEText(Text, 'html')

    # Attach parts into message container
    msg.attach(part1)

    # Credentials
    username = 'thekenstudy@gmail.com'  
    password = 'tzfvqdwitwjzkfbd'

    # Sending the email
    ## note - this smtp config worked for me, I found it googling around, you may have to tweak the # (587) to get yours to work
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo()
    server.starttls()
    server.login(username,password)  
    server.sendmail(from_address, to_address, msg.as_string())  
    server.quit()
    messagebox.showinfo('hii','mail send')

hd=Label(t,text='login mainscreen',font=('arial',25),fg='black',bg='light blue')
hd.place(x=250,y=5)
    
    
a=Label(t,text='Login id',fg='black',bg='light blue',font=('BOLD',15))
a.place(x=450,y=50)
e1=Entry(t,width=50,bd=4)
e1.place(x=450,y=90)
b=Label(t,text='Password',fg='black',bg='light blue',font=('BOLD',15))
b.place(x=450,y=130)
e2=Entry(t,width=50,bd=4)
e2.place(x=450,y=170)
c=Label(t,text='Email',fg='black',bg='light blue',font=('BOLD',15))
c.place(x=450,y=210)
e3=Entry(t,width=50,bd=4)
e3.place(x=450,y=250)


b1=Button(t,text='send OTP',font=('arial',10),fg='black',bg='white',bd=4,command=sendgmail)
b1.place(x=450,y=290,width='80')
d=Label(t,text='Type OTP',bg='light blue',fg='black',font=('BOLD',15))
d.place(x=450,y=330)
e4=Entry(t,width=50,bd=4)
e4.place(x=450,y=370)
b2=Button(t,text='verfiy ✓' ,font=('arial',10),fg='black',bg='white',bd=4,command=verify)
b2.place(x=450,y=410,width='80')
b3=Button(t,text='forget password ! ',font=('arial',10),fg='black',bg='white',bd=4,command=sendpassword)
b3.place(x=650,y=410)

img=Image.open(r"D:\project-scm\oo.png")
img=img.resize((380,450),Image.LANCZOS)
photo=ImageTk.PhotoImage(img)
label=tk.Label(t,image=photo,bg="light blue")
label.image=photo
label.place(x=20,y=50)

t.mainloop()