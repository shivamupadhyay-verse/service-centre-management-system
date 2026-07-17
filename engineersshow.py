import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
def showengineersshow():
    t=Toplevel()
    t.geometry('800x800')
    t.config(bg='orange')
    
    def showdata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        msg=''
        sql="select * from engineers"
        cur.execute(sql)
        data=cur.fetchall()
        # clear
        ta.delete('1.0', END)
   
        # heading
        heading = "{:<10}{:<15}{:<30}{:<15}{:<10}\n".format("Engid","ename","email","phoneno","catid")
        ta.insert(END, heading)
        ta.insert(END, "-"*80 + "\n")
        
        # data
        for res in data: 
                row = "{:<10}{:<15}{:<30}{:<15}{:<10}\n".format(res[0], res[1], res[2], res[3], res[4])
                ta.insert(END, row)
        db.close()
    hd=Label(t,text='engineers show Form',font=('arial',25),fg='black',bg='orange')
    hd.place(x=250,y=5)
    
    ta=Text(t,width=80,height=20)
    ta.place(x=50,y=50)
    showdata()
    def cancel():
        t.destroy()
    b7=Button(t,text='cancel',font=('arial',12,"bold"),fg='white',bg='cyan3',bd=4,width=10,command=cancel)
    b7.place(x=50,y=450)
    
    t.mainloop()