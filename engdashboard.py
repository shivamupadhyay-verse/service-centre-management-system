import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
from engineerssave import showengineerssave
from engineersfind import *
from engineersupdate import *
from engineersdelete import *
from engineersnavi import *
from engineersshow import *
import tkinter as tk 
from PIL import Image,ImageTk
def showengdashboard():
    t=Toplevel()
    t.title("pdashboard")
    t.geometry('800x800')
    t.config(bg='orange')
    b1=Button(t,text='save',font=('arial',15,'bold'),fg='white',bg='cyan3',bd=4,width=14,command=showengineerssave)
    b1.place(x=50,y=50)
    b2=Button(t,text='delete',font=('arial',15,'bold'),fg='white',bg='cyan3',bd=4,width=14,command=showengineersdelete)
    b2.place(x=50,y=100)
    b3=Button(t,text='find',font=('arial',15,'bold'),fg='white',bg='cyan3',bd=4,width=14,command=showengineersfind)
    b3.place(x=50,y=150)
    b4=Button(t,text='update',font=('arial',15,'bold'),fg='white',bg='cyan3',bd=4,width=14,command=showengineersupdate)
    b4.place(x=50,y=200)
    b5=Button(t,text='show',font=('arial',15,'bold'),fg='white',bg='cyan3',bd=4,width=14,command=showengineersshow)
    b5.place(x=50,y=250)
    b6=Button(t,text='navigate',font=('arial',15,'bold'),fg='white',bg='cyan3',bd=4,width=14,command=showengineersnavi)
    b6.place(x=50,y=300)
    hd=Label(t,text='engineers dashboard',font=('bold',25),fg='black',bg='orange')
    hd.place(x=250,y=5)
    img=Image.open(r"D:\project-scm\tt.png")
    img=img.resize((400,300),Image.LANCZOS)

    photo=ImageTk.PhotoImage(img)
    label=tk.Label(t,image=photo,bg="orange")

    label.image=photo
    label.place(x=350,y=100)
    def cancel():
        t.destroy()
    b7=Button(t,text='cancel',font=('arial',15,"bold"),fg='white',bg='cyan3',bd=4,width=14,command=cancel)
    b7.place(x=50,y=350)
    

    t.mainloop()