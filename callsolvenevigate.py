import tkinter
from tkinter import *
from tkinter import messagebox
import time
import threading
from tkinter import ttk
import pymysql
def showcallsolvenavigate():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.config(bg='lightgreen')
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
        sql="select * from callsolve"
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
    h1=Label(t,text='Call solve nagivate',font=("times New Roman","30","bold"),fg='black',background='Lightgreen') 
    h1.place(x=400,y=20)
    a1=Label(t,text='Call Id',background='Lightgreen',font=("times New Roman","18","bold"))
    a1.place(x=30,y=100)
    e1=Entry(t,width=30,background='Lightgreen',bd=2, bg='white')
    e1.place(x=200,y=100)
    a2=Label(t,text='Customer Id',background='Lightgreen',font=("times New Roman","18","bold"))
    a2.place(x=30,y=150)
    e2=Entry(t,width=30,background='Lightgreen',bd=2, bg='white')
    e2.place(x=200,y=150)
    a3=Label(t,text='Product Id',background='Lightgreen',font=("times New Roman","18","bold"))
    a3.place(x=30,y=200,)
    e3=Entry(t,width=30,background='Lightgreen',bd=2, bg='white')
    e3.place(x=200,y=200)
    a4=Label(t,text='Date of Resolve',background='Lightgreen',font=("times New Roman","18","bold"))
    a4.place(x=30,y=240,)
    e4=Entry(t,width=30,background='Lightgreen',bd=2, bg='white')
    e4.place(x=200,y=240)
    a5=Label(t,text='Remarks',background='Lightgreen',font=("times New Roman","18","bold"))
    a5.place(x=30,y=280,)
    e5=Entry(t,width=30,background='Lightgreen',bd=2, bg='white')
    e5.place(x=200,y=280)
    
    b1=Button(t,text='First',font=("times New Roman","15","bold"),fg='White',bg='Black',bd=4,width=8,command=firstdata)
    b1.place(x=50,y=340)
    b2=Button(t,text="Next",font=("times New Roman","15","bold"),fg='White',bg='Black',bd=4,width=8,command=nextdata)
    b2.place(x=200,y=340)
    b3=Button(t,text="Previous",font=("times New Roman","15","bold"),fg='White',bg='Black',bd=4,width=8,command=prevdata)
    b3.place(x=350,y=340)
    b4=Button(t,text="Last",font=("times New Roman","15","bold"),fg='White',bg='Black',bd=4,width=8,command=lastdata)
    b4.place(x=500,y=340)
    filldata()
    def cancel():
     t.destroy()
    b7=Button(t,text='cancel',font=('times new roman',15,"bold"),fg='white',bg='black',bd=4,width=8,command=cancel)
    b7.place(x=650,y=340)
    t.mainloop()