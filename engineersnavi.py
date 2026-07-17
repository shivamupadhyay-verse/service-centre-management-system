import tkinter
from tkinter import *
from tkinter import messagebox
import time
import threading
from tkinter import *
from tkinter import messagebox
import time
import threading
from tkinter import ttk
import pymysql
def showengineersnavi():
    t=Toplevel()
    t.geometry('800x800')
    t.config(bg='orange')
    t.title('Projesct scm')
    xa=[]
    xb=[]
    xc=[]
    xd=[]
    xe=[]
    i=0
    def filldata():
        nonlocal xa,xb,xc
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        sql="select * from engineers navigate"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xa.append(res[0])
            xb.append(res[1])
            xc.append(res[2])
            xd.append(res[3])
            xe.append(res[4])
        db.close()
    def firstdata():
        nonlocal i,xa,xb,xc,xd,xe
        i=0
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e1.insert(0, xa[i])
        e2.insert(0, xb[i])
        e3.insert(0, xc[i])
        e4.insert(0, xd[i])
        e5.insert(0, xe[i])
        
    def nextdata():
     nonlocal i,xa,xb,xc,xd,xe
     if i < len(xa) - 1:
        i += 1
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        
        e1.insert(0, xa[i])
        e2.insert(0, xb[i])
        e3.insert(0, xc[i])
        e4.insert(0, xd[i])
        e5.insert(0, xe[i])
     else:
        messagebox.showinfo("Info", "No more records")   
        
        
    def prevdata():
     nonlocal i,xa,xb,xc,xd,xe
     if i > 0:
        i -= 1
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
       
        e1.insert(0, xa[i])
        e2.insert(0, xb[i])
        e3.insert(0, xc[i])
        e4.insert(0, xd[i])
        e5.insert(0, xe[i])
     else:
         messagebox.showinfo("Info", "This is first record")  
    def lastdata():
        nonlocal i,xa,xb,xc,xd,xe
        i=len(xa)-1
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e1.insert(0, xa[i])
        e2.insert(0, xb[i])
        e3.insert(0, xc[i])
        e4.insert(0, xd[i])
        e5.insert(0, xe[i])
        
    h1=Label(t,text='engineers navigate',font=("times New Roman","30","bold"),fg='black',background='orange') 
    h1.place(x=400,y=5)
    a1=Label(t,text='engid',background='orange',font=("times New Roman","18","bold"))
    a1.place(x=50,y=60)
    e1=Entry(t,width=30,background='orange',bd=2, bg='white')
    e1.place(x=450,y=60)
    a2=Label(t,text='ename',background='orange',font=("times New Roman","18","bold"))
    a2.place(x=50,y=100)
    e2=Entry(t,width=30,background='orange',bd=2, bg='white')
    e2.place(x=450,y=100)
    a3=Label(t,text='email',background='orange',font=("times New Roman","18","bold"))
    a3.place(x=50,y=140,)
    e3=Entry(t,width=30,background='orange',bd=2, bg='white')
    e3.place(x=450,y=140)
    
    a4=Label(t,text='phoneno',background='orange',font=("times New Roman","18","bold"))
    a4.place(x=50,y=200,)
    e4=Entry(t,width=30,background='orange',bd=2, bg='white')
    e4.place(x=450,y=200)
    a5=Label(t,text='catid',background='orange',font=("times New Roman","18","bold"))
    a5.place(x=50,y=240,)
    e5=Entry(t,width=30,background='orange',bd=2, bg='white')
    e5.place(x=450,y=240)
    
    
    b1=Button(t,text='First',font=("times New Roman","15","bold"),fg='white', bg='cyan3',bd=4,width=8,command=firstdata)
    b1.place(x=50,y=300)
    b2=Button(t,text="Next",font=("times New Roman","15","bold"),fg='white', bg='cyan3',bd=4,width=8,command=nextdata)
    b2.place(x=200,y=300)
    b3=Button(t,text="Previous",font=("times New Roman","15","bold"),fg='white', bg='cyan3',bd=4,width=8,command=prevdata)
    b3.place(x=350,y=300)
    b4=Button(t,text="Last",font=("times New Roman","15","bold"),fg='white', bg='cyan3',bd=4,width=8,command=lastdata)
    b4.place(x=500,y=300)
    filldata()
    def cancel():
        t.destroy()
    b7=Button(t,text='cancel',font=('times new roman',15,"bold"),fg='white',bg='cyan3',bd=4,width=8,command=cancel)
    b7.place(x=650,y=300)
    t.mainloop()
