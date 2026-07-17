import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

def showengineersdelete():
    t=Toplevel()
    t.geometry('800x800')
    t.config(bg='orange')
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xa=int(e1.get())
        sql="delete from engineers where engid=%d"%(xa)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('hi','delete')
        e1.delete(0,END)    
        db.close()
        
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
    hd=Label(t,text='engineers delete Form',font=('arial',25),fg='black',bg='orange')
    hd.place(x=250,y=5)
    
    a=Label(t,text='engid',bg='orange',font=('BOLD',15))
    a.place(x=50,y=60)
    e1=ttk.Combobox(t)
    fillid()
    e1.place(x=450,y=60)
    
    bt=Button(t,text='delete',font=('arial',12,'bold'),fg='white',bg='cyan3',width=10,bd=4,command=deletedata)
    bt.place(x=50,y=250)
    def cancel():
        t.destroy()
    b7=Button(t,text='cancel',font=('arial',12,"bold"),fg='white',bg='cyan3',bd=4,width=10,command=cancel)
    b7.place(x=450,y=250)
    t.mainloop()