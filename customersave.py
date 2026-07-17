import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
from tkcalendar import DateEntry

def showcustomersave():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.config(bg='white')
    ind=0
    def savedata():
        nonlocal ind
        
        if ind != 1:
            messagebox.showerror('Error', 'Please check first')
            return

        try:
          xa = int(e1.get())
          xb = e2.get()
          xc = e3.get()
          xd = e4.get()
          xe = e5.get()
          xf = e6.get()
          xg= e7.get()
          if xb == "" or xc == "" or xd=="" or xe=="" or xf=="" or  xg=="":
              raise ValueError
        except ValueError:
          messagebox.showerror("Error", "Please fill all details correctly")
          return
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xa=e1.get()
        xb=e2.get()
        xc=e3.get()
        xd=e4.get()
        xe=int(e5.get())
        xf=int(e6.get())
        xg=e7.get()
        sql="insert into customers values('%s','%s','%s','%s',%d,%d,'%s')"%(xa,xb,xc,xd,xe,xf,xg)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('hi','saved')
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        ind=0
        
    def checkdata():
        nonlocal ind
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select count(*) from Customers where custid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        if data[0]==0:
            messagebox.showinfo('Ok','Go a head')
            ind=1
        else:
            messagebox.showinfo('Not ok','Choose another')
            ind=0
        db.close()
    def fillid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xb=[]
        xc=[]
        sql="select distinct catid,productid from Customers"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xb.append(res[0])
            xc.append(res[1])
            
        e5['values']=xb
        e6['values']=xc
        db.close()
    
        
    a=Label(t,text='Cust Id',bg='White',font=('BOLD',15))
    a.place(x=50,y=60)
    e1=Entry(t,width=30,bd=4,bg='White')
    e1.place(x=450,y=60)
    
    b2=Button(t,text='Check',font=('arial',15,'bold'),bd=4,fg='yellow',bg='red',command=checkdata)
    b2.place(x=650,y=60)
    
    
    b=Label(t,text='Cname',bg='White',font=('BOLD',15))
    b.place(x=50,y=100)
    e2=Entry(t,width=30,bd=4,bg='White')
    e2.place(x=450,y=100)
    
    c=Label(t,text='Address',bg='White',font=('BOLD',15))
    c.place(x=50,y=140)
    e3=Entry(t,width=30,bd=4,bg='White')
    e3.place(x=450,y=140)
    
    d=Label(t,text='Email',bg='White',font=('BOLD',15))
    d.place(x=50,y=180)
    e4=Entry(t,width=30,bd=4,bg='White')
    e4.place(x=450,y=180)
    
    e=Label(t,text='Cat Id',bg='White',font=('BOLD',15))
    e.place(x=50,y=220)
    e5=ttk.Combobox(t)
    e5.place(x=450,y=220)
    
    f=Label(t,text='Product Id',bg='White',font=('BOLD',15))
    f.place(x=50,y=260)
    e6=ttk.Combobox(t)
    e6.place(x=450,y=260)
    fillid()
    
    g=Label(t,text='Date of Purchase',bg='White',font=('BOLD',15))
    g.place(x=50,y=300)
    e7 = DateEntry(t, width=27, bd=4, background='darkblue',
               foreground='white', date_pattern='yyyy-mm-dd')

    e7.place(x=450,y=300)
    
    
    bt=Button(t,text='save',font=('arial',15,'bold'),fg='yellow',bg='red',width=10,bd=4,command=savedata)
    bt.place(x=200,y=350)
    
    hd=Label(t,text='Customers Save Form',font=('bold',25),fg='black',bg='white')
    hd.place(x=400,y=5)
    def cancel():
        t.destroy()
    b7=Button(t,text='cancel',font=('arial',15,"bold"),fg='yellow',bg='red',bd=4,width=10,command=cancel)
    b7.place(x=450,y=350)

    
    t.mainloop()