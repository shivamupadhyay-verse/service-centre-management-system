import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from scdashboard import *
from pcatdashboard import *
from pdashboard import *
from serdashboard import *
from engdashboard import *
from cusdashboard import *
from callregdashboard import *
from callsoldashboard import *
from feeddashboard import *
import tkinter as tk 
from PIL import Image,ImageTk
def showmain():
    t=Toplevel()
    t.title("mainscreen")
    t.config(bg='light yellow')
    t.geometry('800x800')
    b1=Button(t,text='service centre',font=('arial',14,'bold'),fg='black',bg='light blue',bd=4,width=14,command=showscdashboard)
    b1.place(x=30,y=100)
    b2=Button(t,text='product category',font=('arial',14,'bold'),fg='black',bg='light blue',bd=4,width=14,command=showpcatdashboard)
    b2.place(x=30,y=150)
    b3=Button(t,text='products',font=('arial',14,'bold'),fg='black',bg='light blue',bd=4,width=14,command=showpdashboard)
    b3.place(x=30,y=200)
    b4=Button(t,text='services',font=('arial',14,'bold'),fg='black',bg='light blue',bd=4,width=14,command=showserdashboard)
    b4.place(x=30,y=250)
    b15=Button(t,text='engineers',font=('arial',14,'bold'),fg='black',bg='light blue',bd=4,width=14,command=showengdashboard)
    b15.place(x=30,y=300)
    b6=Button(t,text='customers',font=('arial',14,'bold'),fg='black',bg='light blue',bd=4,width=14,command=showcusdashboard)
    b6.place(x=30,y=350)
    b7=Button(t,text='callregisters',font=('arial',14,'bold'),fg='black',bg='light blue',width=14,bd=4,command=showcallregdashboard)
    b7.place(x=30,y=400)
    b8=Button(t,text='callsolve',font=('arial',14,'bold'),fg='black',bg='light blue',bd=4,width=14,command=showcallsoldashboard)
    b8.place(x=30,y=450)
    b9=Button(t,text='feedback',font=('arial',14,'bold'),fg='black',bg='light blue',bd=4,width=14,command=showfeeddashboard)
    b9.place(x=30,y=500)
    
    hd=Label(t,text='mainscreen',font=('bold',25),fg='black',bg='light yellow')
    hd.place(x=350,y=5)
    def cancel():
        t.destroy()
    b7=Button(t,text='cancel',font=('arial',14,"bold"),fg='black',bg='lavender',bd=4,width=8,command=cancel)
    b7.place(x=600,y=500)
    
    img=Image.open(r"D:\project-scm\tin.png")
    img=img.resize((550,350),Image.LANCZOS)
    
    photo=ImageTk.PhotoImage(img)
    label=tk.Label(t,image=photo,bg="light yellow")
    
    label.image=photo
    label.place(x=220,y=100)
    
    
    t.mainloop()