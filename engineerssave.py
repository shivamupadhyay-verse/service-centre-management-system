import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
def showengineerssave():
    t=Toplevel()
    t.geometry('800x800')
    t.config(bg='orange')
    ind=0
    def savedata():
        nonlocal ind
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
          
          if xb == "" or xc == "" or xd=="" or xe=="" :
              raise ValueError
        except ValueError:
          messagebox.showerror("Error", "Please fill all details correctly")
          return
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xa=int(e1.get())
        xb=e2.get()
        xc=e3.get()
        xd=e4.get()
        xe=int(e5.get())
        sql="insert into engineers values('%d','%s','%s','%s','%d')"%(xa,xb,xc,xd,xe)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('hi','saved')
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        ind=0
        
    def checkdata():
        nonlocal ind
        ind=1
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select count(*) from engineers where engid=%d"%(xa)
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
        sql="select catid from engineers"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xb.append(res[0])
            
        e5['values']=xb
        db.close()
    
    hd=Label(t,text='engineers save Form',font=('arial',25),fg='black',bg='orange')
    hd.place(x=250,y=5)
        
    a=Label(t,text='engid',bg='orange',font=('BOLD',15))
    a.place(x=50,y=60)
    e1=Entry(t,width=30,bd=4)
    e1.place(x=450,y=60)
    b2=Button(t,text='Check',font=('arial',12,'bold'),fg='white',bg='cyan3',width=10,bd=4,command=checkdata)
    b2.place(x=650,y=60)
    
    b=Label(t,text='ename',bg='orange',font=('BOLD',15))
    b.place(x=50,y=100)
    e2=Entry(t,width=30,bd=4)
    e2.place(x=450,y=100)
    g=Label(t,text='email',bg='orange',font=('BOLD',15))
    g.place(x=50,y=140)
    e3=Entry(t,width=30,bd=4)
    e3.place(x=450,y=140)
    
    h=Label(t,text='phoneno',bg='orange',font=('BOLD',15))
    h.place(x=50,y=180)
    e4=Entry(t,width=30,bd=4)
    e4.place(x=450,y=180)
    
    g=Label(t,text='catid',bg='orange',font=('BOLD',15))
    g.place(x=50,y=220)
    e5=ttk.Combobox(t)
    e5.place(x=450,y=220)
    fillid()
    
    bt=Button(t,text='save',font=('arial',12,'bold'),fg='white',bg='cyan3',width=10,bd=4,command=savedata)
    bt.place(x=200,y=350)
    def cancel():
        t.destroy()
    b7=Button(t,text='cancel',font=('arial',12,"bold"),fg='white',bg='cyan3',bd=4,width=10,command=cancel)
    b7.place(x=450,y=350)
    
    t.mainloop()