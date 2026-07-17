import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
def showcustomersshow():
    t=Toplevel()
    t.geometry('800x800')
    t.config(bg='white')
    
    def showdata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        msg=''
        sql="select * from customers"
        cur.execute(sql)
        data=cur.fetchall()
        # clear old data
        ta.delete('1.0', END)
    
        # heading
        heading = f"{'CustID':<10}{'Name':<25}{'Address':<30}{'Email':<40}{'Age':<6}{'Phone':<12}\n"
        ta.insert(END, heading)
        ta.insert(END, "-"*90 + "\n")
    
        # data
        for res in data:
            row = f"{res[0]:<10}{res[1]:<25}{res[2]:<30}{res[3]:<40}{res[4]:<6}{res[5]:<12}\n"
            ta.insert(END, row)
        db.close()
    ta=Text(t,width=120,height=30,bg='yellow',fg='black')
    ta.place(x=10,y=50)
    
    hd=Label(t,text='Customers Show Form',font=('bold',25),fg='black',bg='white')
    hd.place(x=400,y=5)
    showdata()
    def cancel():
        t.destroy()
    b7=Button(t,text='cancel',font=('arial',15,"bold"),fg='yellow',bg='red',bd=4,width=10,command=cancel)
    b7.place(x=10,y=650)

    t.mainloop()