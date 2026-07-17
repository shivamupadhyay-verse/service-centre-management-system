import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
from customersave import *
from customerfind import *
from customersupdate import *
from customerdelete import *
from customersnavigate import *
from customershow import *
import tkinter as tk 
from PIL import Image,ImageTk

def showcusdashboard():
    t=Toplevel()
    t.title("cusdashboard")
    t.geometry('800x800')
    t.config(bg='white')
    b1=Button(t,text='save',font=('arial',15,'bold'),fg='yellow',bg='red',bd=4,width=14,command=showcustomersave)
    b1.place(x=50,y=50)
    b2=Button(t,text='delete',font=('arial',15,'bold'),fg='yellow',bg='red',bd=4,width=14,command=showcustomerdelete)
    b2.place(x=50,y=100)
    b3=Button(t,text='find',font=('arial',15,'bold'),fg='yellow',bg='red',bd=4,width=14,command=showcustomerfind)
    b3.place(x=50,y=150)
    b4=Button(t,text='update',font=('arial',15,'bold'),fg='yellow',bg='red',bd=4,width=14,command=showcustomersupdate)
    b4.place(x=50,y=200)
    b5=Button(t,text='show',font=('arial',15,'bold'),fg='yellow',bg='red',bd=4,width=14,command=showcustomersshow)
    b5.place(x=50,y=250)
    b6=Button(t,text='navigate',font=('arial',15,'bold'),fg='yellow',bg='red',bd=4,width=14,command=showcustomersnavigate)
    b6.place(x=50,y=300)
    hd=Label(t,text='customers dashboard',font=('bold',25),fg='black',bg='white')
    hd.place(x=250,y=5)
    def cancel():
        t.destroy()
    b7=Button(t,text='cancel',font=('arial',15,"bold"),fg='yellow',bg='red',bd=4,width=14,command=cancel)
    b7.place(x=50,y=350)
    img=Image.open(r"D:\project-scm\vv.png")
    img=img.resize((600,300),Image.LANCZOS)
    
    photo=ImageTk.PhotoImage(img)
    label=tk.Label(t,image=photo,bg="white")
    
    label.image=photo
    label.place(x=200,y=400)

    t.mainloop()