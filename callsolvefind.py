import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
def showcallsolvefind():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.config(bg='lightgreen')
    
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select custid,productid,Dateofresolve,remarks from callsolve where callid=%d"%(xa)
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
    
    bt=Button(t,text='find',font=('arial',12,'bold'),fg='White',bg='Black',bd=4,width=10,command=finddata)
    bt.place(x=50,y=100)
    
    b=Label(t,text='Cust Id',bg='Light Green',font=('BOLD',15))
    b.place(x=50,y=140)
    e2=Entry(t,width=30,bd=4,bg='White')
    e2.place(x=450,y=140)
    
    c=Label(t,text='Product Id',bg='Light Green',font=('BOLD',15))
    c.place(x=50,y=180)
    e3=Entry(t,width=30,bd=4,bg='White')
    e3.place(x=450,y=180)
    
    d=Label(t,text='Date of Resolve',bg='Light Green',font=('BOLD',15))
    d.place(x=50,y=220)
    e4=Entry(t,width=30,bd=4,bg='White')
    e4.place(x=450,y=220)
    
    e=Label(t,text='Remarks',bg='Light Green',font=('BOLD',15))
    e.place(x=50,y=260)
    e5=Entry(t,width=70,bd=4,bg='White')
    e5.place(x=450,y=260)
    
    hd=Label(t,text='Call Solve Find Form',font=('bold',25),fg='black',bg='Lightgreen')
    hd.place(x=400,y=5)
    def cancel():
     t.destroy()
    b7=Button(t,text='cancel',font=('arial',12,"bold"),fg='white',bg='black',bd=4,width=14,command=cancel)
    b7.place(x=50,y=300)
    
    t.mainloop()