import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
def showcustomersdelete():
    t=tkinter.Tk()
    t.geometry('800x800')
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xa=int(e1.get())
        sql="delete from customers where custid=%d"%(xa)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('hi','delete')
        e1.delete(0,END)    
        db.close()
        
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
    
    bt=Button(t,text='delete',command=deletedata)
    bt.place(x=50,y=250)
    t.mainloop()