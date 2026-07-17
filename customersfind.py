import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
def showcustomersfind():
    t=tkinter.Tk()
    t.geometry('800x800')
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select cname,address,email,catid,productid,dateofpurchase from customers where custid=%d"%(xa)
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
        e6.delete(0,END)
        e6.insert(0,str(data[4]))
        e7.delete(0,END)
        e7.insert(0,str(data[5]))
        
    def fillid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xb=[]
        sql="select custid from customers"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xb.append(res[0])
        e1['values']=xb
        db.close()
    a=Label(t,text='custid')
    a.place(x=50,y=60)
    e1=ttk.Combobox(t)
    fillid()
    e1.place(x=450,y=60)
    
    bt=Button(t,text='find',command=finddata)
    bt.place(x=50,y=100)
    
    b=Label(t,text='cname')
    b.place(x=50,y=140)
    e2=Entry(t,width=30)
    e2.place(x=450,y=140)
    g=Label(t,text='address')
    g.place(x=50,y=180)
    e3=Entry(t,width=30)
    e3.place(x=450,y=180)
    
    h=Label(t,text='email')
    h.place(x=50,y=220)
    e4=Entry(t,width=30)
    e4.place(x=450,y=220)
    
    g=Label(t,text='catid')
    g.place(x=50,y=260)
    e5=Entry(t,width=30)
    e5.place(x=450,y=260)
    h=Label(t,text='productid')
    h.place(x=50,y=300)
    e6=Entry(t,width=30)
    e6.place(x=450,y=300)
    i=Label(t,text='dateofpurchase')
    i.place(x=50,y=340)
    e7=Entry(t,width=30)
    e7.place(x=450,y=340)
    
    
    t.mainloop()