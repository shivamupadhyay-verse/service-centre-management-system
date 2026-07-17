import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
def showengineersfind():
    t=Toplevel()
    t.geometry('800x800')
    t.config(bg='orange')
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select ename,email,phoneno,catid from engineers where engid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.delete(0,END)
        e2.insert(0,data[0])
        e3.delete(0,END)
        e3.insert(0,str(data[1]))
        e4.delete(0,END)
        e4.insert(0,str(data[2]))
        e5.delete(0,END)
        e5.insert(0,str(data[3]))
           
    def fillid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xb=[]
        sql="select engid from engineers"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xb.append(res[0])
        e1['values']=xb
        db.close()
    hd=Label(t,text='engineers find Form',font=('arial',25),fg='black',bg='orange')
    hd.place(x=250,y=5)
    
    a=Label(t,text='engid',bg='orange',font=('BOLD',15))
    a.place(x=50,y=60)
    e1=ttk.Combobox(t)
    fillid()
    e1.place(x=450,y=60)
    
    bt=Button(t,text='find',font=('arial',12,'bold'),fg='white',bg='cyan3',width=10,bd=4,command=finddata)
    bt.place(x=50,y=100)
    
    b=Label(t,text='ename',bg='orange',font=('BOLD',15))
    b.place(x=50,y=140)
    e2=Entry(t,width=30,bd=4)
    e2.place(x=450,y=140)
    g=Label(t,text='email',bg='orange',font=('BOLD',15))
    g.place(x=50,y=180)
    e3=Entry(t,width=30,bd=4)
    e3.place(x=450,y=180)
    
    h=Label(t,text='phoneno',bg='orange',font=('BOLD',15))
    h.place(x=50,y=220)
    e4=Entry(t,width=30,bd=4)
    e4.place(x=450,y=220)
    
    g=Label(t,text='catid',bg='orange',font=('BOLD',15))
    g.place(x=50,y=260)
    e5=Entry(t,width=30,bd=4)
    e5.place(x=450,y=260)
    def cancel():
        t.destroy()
    b7=Button(t,text='cancel',font=('arial',12,"bold"),fg='white',bg='cyan3',bd=4,width=10,command=cancel)
    b7.place(x=50,y=450)
    
    t.mainloop()