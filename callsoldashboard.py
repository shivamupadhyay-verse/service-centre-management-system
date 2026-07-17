import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
from callsolvesave import *
from callsolvefind import *
from callsolveupdate import *
from callsolvedelete import *
from callsolvenevigate import *
from callsolveshow import *

import tkinter as tk 
from PIL import Image,ImageTk

def showcallsoldashboard():
    t=Toplevel()
    t.title("callsoldashboard")
    t.geometry('800x800')
    t.config(bg='lightgreen')
    b1=Button(t,text='save & email',font=('arial',15,'bold'),fg='white',bg='black',bd=4,width=14,command=showcallsolvesave)
    b1.place(x=50,y=50)
    b2=Button(t,text='delete',font=('arial',15,'bold'),fg='white',bg='black',bd=4,width=14,command=showcallsolvedelete)
    b2.place(x=50,y=100)
    b3=Button(t,text='find',font=('arial',15,'bold'),fg='white',bg='black',bd=4,width=14,command=showcallsolvefind)
    b3.place(x=50,y=150)
    b4=Button(t,text='update',font=('arial',15,'bold'),fg='white',bg='black',bd=4,width=14,command=showcallsolveupdate)
    b4.place(x=50,y=200)
    b5=Button(t,text='show',font=('arial',15,'bold'),fg='white',bg='black',bd=4,width=14,command=showcallsolveshow)
    b5.place(x=50,y=250)
    b6=Button(t,text='navigate',font=('arial',15,'bold'),fg='white',bg='black',bd=4,width=14,command=showcallsolvenavigate)
    b6.place(x=50,y=300)
    
    hd=Label(t,text='call solve dashboard',font=('bold',25),fg='white',bg='lightgreen')
    hd.place(x=250,y=5)
    def cancel():
     t.destroy()
    b7=Button(t,text='cancel',font=('arial',15,"bold"),fg='white',bg='black',bd=4,width=14,command=cancel)
    b7.place(x=50,y=350)
    img=Image.open(r"D:\project-scm\sup.png")
    img=img.resize((500,300),Image.LANCZOS)
    
    photo=ImageTk.PhotoImage(img)
    label=tk.Label(t,image=photo,bg="lightgreen")
    
    label.image=photo
    label.place(x=300,y=100)


    t.mainloop()