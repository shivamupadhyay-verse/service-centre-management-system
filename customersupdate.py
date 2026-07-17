import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
def showcustomersupdate():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.config(bg='white')
    
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
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xa=int(e1.get())
        xb=e2.get()
        xc=e3.get()
        xd=e4.get()
        xe=int(e5.get())
        xf=int(e6.get())
        xg=e7.get()
        sql="update customers set cname='%s',address='%s', email='%s',catid=%d,productid=%d,dateofpurchase='%s' where custid=%d"%(xb,xc,xd,xe,xf,xg,xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('hi','data updated')
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
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
    
    bt=Button(t,text='find',font=('arial',12,'bold'),fg='yellow',bg='red',width=10,bd=4,command=finddata)
    bt.place(x=50,y=100)
    
    b=Label(t,text='Cname',bg='White',font=('BOLD',15))
    b.place(x=50,y=140)
    e2=Entry(t,width=30,bd=4,bg='White')
    e2.place(x=450,y=140)
    
    c=Label(t,text='Address',bg='White',font=('BOLD',15))
    c.place(x=50,y=180)
    e3=Entry(t,width=30,bd=4,bg='White')
    e3.place(x=450,y=180)
    
    
    d=Label(t,text='Email',bg='White',font=('BOLD',15))
    d.place(x=50,y=220)
    e4=Entry(t,width=30,bd=4,bg='White')
    e4.place(x=450,y=220)
    
    e=Label(t,text='Cat Id',bg='White',font=('BOLD',15))
    e.place(x=50,y=260)
    e5=Entry(t,width=30,bd=4,bg='White')
    e5.place(x=450,y=260)
    
    f=Label(t,text='Product Id',bg='White',font=('BOLD',15))
    f.place(x=50,y=300)
    e6=Entry(t,width=30,bd=4,bg='White')
    e6.place(x=450,y=300)
    
    g=Label(t,text='Date of Purchase',bg='White',font=('BOLD',15))
    g.place(x=50,y=340)
    e7=Entry(t,width=30,bd=4,bg='White')
    e7.place(x=450,y=340)
    
    bt=Button(t,text='update',font=('arial',15,'bold'),fg='yellow',bg='red',width=10,bd=4,command=updatedata)
    bt.place(x=50,y=380)
    
    hd=Label(t,text='Customers Update Form',font=('bold',25),fg='black',bg='white')
    hd.place(x=400,y=5)
    def cancel():
        t.destroy()
    b7=Button(t,text='cancel',font=('arial',15,"bold"),fg='yellow',bg='red',bd=4,width=10,command=cancel)
    b7.place(x=450,y=380)

    
    t.mainloop()