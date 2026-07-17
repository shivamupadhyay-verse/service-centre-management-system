import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
def showcallsolveupdate():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.config(bg='lightgreen')
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select custid,productid,dateofresolve,remarks from callsolve where callid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.delete(0,END)
        e2.insert(0,str(data[0]))
        e3.delete(0,END)
        e3.insert(0,str(data[1]))
        e4.delete(0,END)
        e4.insert(0,str(data[2]))
        e5.delete(0,END)
        e5.insert(0,data[3])
    
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xa=int(e1.get())
        xb=int(e2.get())
        xc=int(e3.get())
        xd=e4.get()
        xe=e5.get()
        sql="update callsolve set custid=%d,productid=%d,dateofresolve='%s',remarks='%s' where callid=%d"%(xb,xc,xd,xe,xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('hi','data updated')
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
            
    def fillid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xb=[]
        sql="select callid from callsolve"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xb.append(res[0])
        e1['values']=xb
        db.close()
    
    
    a=Label(t,text='Call Id',bg='Light Green',font=('BOLD',15))
    a.place(x=50,y=60)
    e1=ttk.Combobox(t)
    fillid()
    e1.place(x=450,y=60)
    
    bt=Button(t,text='find',font=('arial',12,'bold'),fg='White',bg='Black',command=finddata)
    bt.place(x=50,y=100)
    
    b=Label(t,text='Cust Id',bg='Light Green',font=('BOLD',15))
    b.place(x=50,y=140)
    e2=Entry(t,width=30,bd=4,bg='white')
    e2.place(x=450,y=140)
    
    c=Label(t,text='Product Id',bg='Light Green',font=('BOLD',15))
    c.place(x=50,y=180)
    e3=Entry(t,width=30,bd=4,bg='white')
    e3.place(x=450,y=180)
    
    d=Label(t,text='Date of Resolve',bg='Light Green',font=('BOLD',15))
    d.place(x=50,y=220)
    e4=Entry(t,width=30,bd=4,bg='white')
    e4.place(x=450,y=220)
    
    e=Label(t,text='Remarks',bg='Light Green',font=('BOLD',15))
    e.place(x=50,y=260)
    e5=Entry(t,width=70,bd=4,bg='white')
    e5.place(x=450,y=260)
    
    bt=Button(t,text='update',font=('arial',15,'bold'),fg='White',bg='Black',bd=4,width=8,command=updatedata)
    bt.place(x=50,y=350)
    
    
    hd=Label(t,text='Call Solve Update Form',font=('bold',25),fg='black',bg='Lightgreen')
    hd.place(x=400,y=5)
    def cancel():
     t.destroy()
    b7=Button(t,text='cancel',font=('arial',15,"bold"),fg='white',bg='black',bd=4,width=8,command=cancel)
    b7.place(x=450,y=350)
    
    t.mainloop()