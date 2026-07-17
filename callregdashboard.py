import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
from callregistersave import *
from callregistersfind import *
from callregisterupdate import *
from callregisterdelete import *
from callregisternavigate import *
from callregistershow import *

import tkinter as tk 
from PIL import Image,ImageTk

def showcallregdashboard():
    t=Toplevel()
    t.title("callregdashboard")
    t.geometry('800x800')
    t.config(bg='cadetblue1')
    b1=Button(t,text='save & email',font=('arial',15,'bold'),fg='black',bg='white',bd=4,width=14,command=showcallregistersave)
    b1.place(x=50,y=50)
    b2=Button(t,text='delete',font=('arial',15,'bold'),fg='black',bg='white',bd=4,width=14,command=showcallregisterdelete)
    b2.place(x=50,y=100)
    b3=Button(t,text='find',font=('arial',15,'bold'),fg='black',bg='white',bd=4,width=14,command=showcallregisterfind)
    b3.place(x=50,y=150)
    b4=Button(t,text='update',font=('arial',15,'bold'),fg='black',bg='white',bd=4,width=14,command=showcallregisterupdate)
    b4.place(x=50,y=200)
    b5=Button(t,text='show',font=('arial',15,'bold'),fg='black',bg='white',bd=4,width=14,command=showcallregistershow)
    b5.place(x=50,y=250)
    b6=Button(t,text='navigate',font=('arial',15,'bold'),fg='black',bg='white',bd=4,width=14,command=showcallregisternavigate)
    b6.place(x=50,y=300)
    
    hd=Label(t,text='call register dashboard',font=('bold',25),fg='black',bg='cadetblue1')
    hd.place(x=250,y=5)
    def showgraph():
        print("graph called")
        
        import matplotlib
        matplotlib.use('TkAgg')
        import matplotlib.pyplot as plt
        import pymysql

    
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
    
        cur.execute("select serviceid, count(*) from callregisters group by serviceid")
        data = cur.fetchall()
        print(data)
    
        service=[]
        total=[]
    
        for row in data:
            service.append(row[0])
            total.append(row[1])
    
        db.close()
    
        plt.figure()
        plt.bar(service,total)
        plt.xlabel("Service ID")
        plt.ylabel("Total Calls")
        plt.title("Service Wise Calls")
        plt.show()

    

    def cancel():
        t.destroy()
    b7=Button(t,text='cancel',font=('arial',15,"bold"),fg='black',bg='white',bd=4,width=14,command=cancel)
    b7.place(x=50,y=400)
    Button(t, text="show Graph", font=('arial',15,'bold'),fg='black',bg='white',bd=4,width=14,
       command=showgraph).place(x=50, y=350)
    

    img=Image.open(r"D:\project-scm\hh.png")
    img=img.resize((650,300),Image.LANCZOS)
    
    photo=ImageTk.PhotoImage(img)
    label=tk.Label(t,image=photo,bg="cadetblue1")
    
    label.image=photo
    label.place(x=100,y=450)
    
