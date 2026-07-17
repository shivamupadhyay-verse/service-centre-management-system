import tkinter
from tkinter import *
from tkinter import messagebox
import time
import threading
from tkinter import ttk
import pymysql
def showcustomersnavigate():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.config(bg='white')
    t.title('Projesct scm')
    xa=[]
    xb=[]
    xc=[]
    xd=[]
    xe=[]
    xf=[]
    xi=[]
    
    i=0
    def filldata():
        nonlocal xa,xb,xc,xd,xe,xf,xi
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        sql="select * from customers"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xa.append(res[0])
            xb.append(res[1])
            xc.append(res[2])
            xd.append(res[3])
            xe.append(res[4])
            xf.append(res[5])
            xi.append(res[6])
        db.close()
    def firstdata():
        nonlocal i,xa,xb,xc,xd,xe,xf,xi
        i=0
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        
        e1.insert(0, xa[i])
        e2.insert(0, xb[i])
        e3.insert(0, xc[i])
        e4.insert(0, xd[i])
        e5.insert(0, xe[i])
        e6.insert(0, xf[i])
        e7.insert(0, xi[i])
        
    def nextdata():
     nonlocal i,xa,xb,xc,xd,xe,xf,xi
     if i < len(xa) - 1:
        i += 1
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        
        e1.insert(0, xa[i])
        e2.insert(0, xb[i])
        e3.insert(0, xc[i])
        e4.insert(0, xd[i])
        e5.insert(0, xe[i])
        e6.insert(0, xf[i])
        e7.insert(0, xi[i])
     else:
         messagebox.showinfo("Info", "No more records")
       
    def prevdata():
     nonlocal i,xa,xb,xc,xd,xe,xf,xi
     if i > 0:
        i -= 1
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        
        e1.insert(0, xa[i])
        e2.insert(0, xb[i])
        e3.insert(0, xc[i])
        e4.insert(0, xd[i])
        e5.insert(0, xe[i])
        e6.insert(0, xf[i])
        e7.insert(0, xi[i])
     else:
         messagebox.showinfo("Info", "This is first record")
        
    
    def lastdata():
        nonlocal i,xa,xb,xc,xd,xe,xf,xi
        i=len(xa)-1
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        
        e1.insert(0, xa[i])
        e2.insert(0, xb[i])
        e3.insert(0, xc[i])
        e4.insert(0, xd[i])
        e5.insert(0, xe[i])
        e6.insert(0, xf[i])
        e7.insert(0, xi[i])
        
    
    h1=Label(t,text='Customers navigate',font=("times New Roman","30","bold"),fg='black',background='white') 
    h1.place(x=250,y=5)
    a1=Label(t,text='Cust Id',background='white',font=("times New Roman","18","bold"))
    a1.place(x=50,y=60)
    e1=Entry(t,width=30,background='white',bd=2, bg='white')
    e1.place(x=450,y=60)
    a2=Label(t,text='Cname',background='white',font=("times New Roman","18","bold"))
    a2.place(x=50,y=100)
    e2=Entry(t,width=30,background='white',bd=2, bg='white')
    e2.place(x=450,y=100)
    a3=Label(t,text='Address',background='white',font=("times New Roman","18","bold"))
    a3.place(x=50,y=140,)
    e3=Entry(t,width=30,background='white',bd=2, bg='white')
    e3.place(x=450,y=140)
    a4=Label(t,text='Email',background='white',font=("times New Roman","18","bold"))
    a4.place(x=50,y=200,)
    e4=Entry(t,width=30,background='white',bd=2, bg='white')
    e4.place(x=450,y=200)
    a5=Label(t,text='Cat Id',background='white',font=("times New Roman","18","bold"))
    a5.place(x=50,y=240,)
    e5=Entry(t,width=30,background='white',bd=2, bg='white')
    e5.place(x=450,y=240)
    a6=Label(t,text='Product Id',background='white',font=("times New Roman","18","bold"))
    a6.place(x=50,y=300,)
    e6=Entry(t,width=30,background='white',bd=2, bg='white')
    e6.place(x=450,y=300)
    a7=Label(t,text='Date of Purchase',background='white',font=("times New Roman","18","bold"))
    a7.place(x=50,y=340,)
    e7=Entry(t,width=30,background='white',bd=2, bg='white')
    e7.place(x=450,y=340)
    
    b1=Button(t,text='First',font=("times New Roman","15","bold"),fg='yellow',bg='red',bd=4,width=8,command=firstdata)
    b1.place(x=50,y=460)
    b2=Button(t,text="Next",font=("times New Roman","15","bold"),fg='yellow',bg='red',bd=4,width=8,command=nextdata)
    b2.place(x=200,y=460)
    b3=Button(t,text="Previous",font=("times New Roman","15","bold"),fg='yellow',bg='red',bd=4,width=8,command=prevdata)
    b3.place(x=350,y=460)
    b4=Button(t,text="Last",font=("times New Roman","15","bold"),fg='yellow',bg='red',bd=4,width=8,command=lastdata)
    b4.place(x=500,y=460)
    filldata()
    def cancel():
        t.destroy()
    b7=Button(t,text='cancel',font=('times new roman',15,"bold"),fg='yellow',bg='red',bd=4,width=8,command=cancel)
    b7.place(x=650,y=460)

    t.mainloop()