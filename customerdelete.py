import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
def showcustomerdelete():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.config(bg='white')
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
    a=Label(t,text='Cust Id',bg='White',font=('BOLD',15))
    a.place(x=50,y=60)
    e1=ttk.Combobox(t)
    fillid()
    e1.place(x=450,y=60)
    
    bt=Button(t,text='delete',font=('arial',15,'bold'),fg='yellow',bg='red',width=14,bd=4,command=deletedata)
    bt.place(x=50,y=250)
    
    hd=Label(t,text='Customers Delete Form',font=('bold',25),fg='black',bg='white')
    hd.place(x=400,y=5)
    def cancel():
        t.destroy()
    b7=Button(t,text='cancel',font=('arial',15,"bold"),fg='yellow',bg='red',bd=4,width=14,command=cancel)
    b7.place(x=450,y=250)

    
    t.mainloop()