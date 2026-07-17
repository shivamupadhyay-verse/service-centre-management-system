import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

t=tkinter.Tk()
t.geometry('800x800')
t.configure(bg='yellow')
def savedata():

    db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
    cur=db.cursor()
    xa=e1.get()
    xb=e2.get()
    xc=e3.get()
    
    sql="insert into logintable values(%s,%s,%s)"
    cur.execute(sql,(xa,xb,xc))
    db.commit()
    messagebox.showinfo('hi','saved')
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)


   

hd=Label(t,text='data enter page to sql',font=('arial',25),fg='black',bg='yellow')
hd.place(x=350,y=5)
   
a=Label(t,text='userid',bg='yellow',font=('BOLD',15))
a.place(x=50,y=60)
e1=Entry(t,width=30,bd=4)
e1.place(x=450,y=60)


b=Label(t,text='password',bg='yellow',font=('BOLD',15))
b.place(x=50,y=100)
e2=Entry(t,width=30,bd=4)
e2.place(x=450,y=100)

g=Label(t,text='email',bg='yellow',font=('BOLD',15))
g.place(x=50,y=140)
e3=Entry(t,width=30,bd=4)
e3.place(x=450,y=140)




bt=Button(t,text='save',font=('arial',20),fg='black',bg='red',command=savedata,bd=4)
bt.place(x=200,y=350)
t.mainloop()