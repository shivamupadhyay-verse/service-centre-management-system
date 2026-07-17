import tkinter
from tkinter import *
from tkinter import messagebox
import time
import threading
from tkinter import ttk
import pymysql
def showcallregisternavigate():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.config(bg='cadetblue1')
    t.title('Projesct scm')
    xa=[]
    xb=[]
    xc=[]
    xd=[]
    xe=[]
    xf=[]
    xi=[]
    xg=[]
    i=0
    def filldata():
        nonlocal xa,xb,xc,xd,xe,xf,xi,xg
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        sql="select * from callregisters"
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
            xg.append(res[7])
        db.close()
    def firstdata():
        nonlocal i,xa,xb,xc,xd,xe,xf,xi,xg
        i=0
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e1.insert(0, xa[i])
        e2.insert(0, xb[i])
        e3.insert(0, xc[i])
        e4.insert(0, xd[i])
        e5.insert(0, xe[i])
        e6.insert(0, xf[i])
        e7.insert(0, xi[i])
        e8.insert(0, xg[i])
    def nextdata():
     nonlocal i,xa,xb,xc,xd,xe,xf,xi,xg
     if i < len(xa) - 1:
        i += 1
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e1.insert(0, xa[i])
        e2.insert(0, xb[i])
        e3.insert(0, xc[i])
        e4.insert(0, xd[i])
        e5.insert(0, xe[i])
        e6.insert(0, xf[i])
        e7.insert(0, xi[i])
        e8.insert(0, xg[i])
     else:
           messagebox.showinfo("Info", "No more records")
    def prevdata():
     nonlocal i,xa,xb,xc,xd,xe,xf,xi,xg
     if i > 0:
        i -= 1
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e1.insert(0, xa[i])
        e2.insert(0, xb[i])
        e3.insert(0, xc[i])
        e4.insert(0, xd[i])
        e5.insert(0, xe[i])
        e6.insert(0, xf[i])
        e7.insert(0, xi[i])
        e8.insert(0, xg[i])
     else:
       messagebox.showinfo("Info", "This is first record")
    
    def lastdata():
        nonlocal i,xa,xb,xc,xd,xe,xf,xi,xg
        i=len(xa)-1
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e1.insert(0, xa[i])
        e2.insert(0, xb[i])
        e3.insert(0, xc[i])
        e4.insert(0, xd[i])
        e5.insert(0, xe[i])
        e6.insert(0, xf[i])
        e7.insert(0, xi[i])
        e8.insert(0, xg[i])
    
    h1=Label(t,text=' Call register navigate',font=("times New Roman","30","bold"),fg='black',background='cadetblue1') 
    h1.place(x=400,y=20)
    a1=Label(t,text='Call Id',background='cadetblue1',font=("times New Roman","18","bold"))
    a1.place(x=30,y=100)
    e1=Entry(t,width=30,background='cadetblue1',bd=2, bg='white')
    e1.place(x=200,y=100)
    a2=Label(t,text='Customer Id',background='cadetblue1',font=("times New Roman","18","bold"))
    a2.place(x=30,y=150)
    e2=Entry(t,width=30,background='cadetblue1',bd=2, bg='white')
    e2.place(x=200,y=150)
    a3=Label(t,text='Product Id',background='cadetblue1',font=("times New Roman","18","bold"))
    a3.place(x=30,y=200,)
    e3=Entry(t,width=30,background='cadetblue1',bd=2, bg='white')
    e3.place(x=200,y=200)
    a4=Label(t,text='Service Id',background='cadetblue1',font=("times New Roman","18","bold"))
    a4.place(x=30,y=240,)
    e4=Entry(t,width=30,background='cadetblue1',bd=2, bg='white')
    e4.place(x=200,y=240)
    a5=Label(t,text='Eng Id',background='cadetblue1',font=("times New Roman","18","bold"))
    a5.place(x=30,y=280,)
    e5=Entry(t,width=30,background='cadetblue1',bd=2, bg='white')
    e5.place(x=200,y=280)
    a6=Label(t,text='Date of Call',background='cadetblue1',font=("times New Roman","18","bold"))
    a6.place(x=30,y=320,)
    e6=Entry(t,width=30,background='cadetblue1',bd=2, bg='white')
    e6.place(x=200,y=320)
    a7=Label(t,text='Date of Solve',background='cadetblue1',font=("times New Roman","18","bold"))
    a7.place(x=30,y=360,)
    e7=Entry(t,width=30,background='cadetblue1',bd=2, bg='white')
    e7.place(x=200,y=360)
    a8=Label(t,text='Est Bill',background='cadetblue1',font=("times New Roman","18","bold"))
    a8.place(x=30,y=400,)
    e8=Entry(t,width=30,background='cadetblue1',bd=2, bg='white')
    e8.place(x=200,y=400)
    
    b1=Button(t,text='First',font=("times New Roman","15","bold"),fg='Black',bg='white',bd=4,width=8,command=firstdata)
    b1.place(x=50,y=460)
    b2=Button(t,text="Next",font=("times New Roman","15","bold"),fg='Black',bg='white',bd=4,width=8,command=nextdata)
    b2.place(x=200,y=460)
    b3=Button(t,text="Previous",font=("times New Roman","15","bold"),fg='Black',bg='white',bd=4,width=8,command=prevdata)
    b3.place(x=350,y=460)
    b4=Button(t,text="Last",font=("times New Roman","15","bold"),fg='Black',bg='white',bd=4,width=8,command=lastdata)
    b4.place(x=500,y=460)
    filldata()
    def cancel():
        t.destroy()
    b7=Button(t,text='cancel',font=('times new roman',15,"bold"),fg='black',bg='white',bd=4,width=8,command=cancel)
    b7.place(x=650,y=460)
    t.mainloop()