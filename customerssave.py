import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

t=tkinter.Tk()
t.geometry('800x800')
def savedata():
    db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
    cur=db.cursor()
    xa=int(e1.get())
    xb=e2.get()
    xc=e3.get()
    xd=e4.get()
    xe=int(e5.get())
    xf=int(e6.get())
    xg=int(e7.get())
    sql="insert into customers values('%d','%s','%s','%s','%d','%d','%d')"%(xa,xb,xc,xd,xe,xf,xg)
    cur.execute(sql)
    db.commit()
    messagebox.showinfo('hi','saved')
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    
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
b=Label(t,text='cname')
b.place(x=50,y=100)
e2=Entry(t,width=30)
e2.place(x=450,y=100)
g=Label(t,text='address')
g.place(x=50,y=140)
e3=Entry(t,width=30)
e3.place(x=450,y=140)

h=Label(t,text='email')
h.place(x=50,y=180)
e4=Entry(t,width=30)
e4.place(x=450,y=180)

g=Label(t,text='catid')
g.place(x=50,y=220)
e5=Entry(t,width=30)
e5.place(x=450,y=220)
h=Label(t,text='productid')
h.place(x=50,y=260)
e6=Entry(t,width=30)
e6.place(x=450,y=260)
i=Label(t,text='dateofpurchase')
i.place(x=50,y=300)
e7=Entry(t,width=30)
e7.place(x=450,y=300)


bt=Button(t,text='save',command=savedata)
bt.place(x=200,y=350)
t.mainloop()