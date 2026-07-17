import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql

t=tkinter.Tk()
t.geometry('800x800')
def showdata():
    db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
    cur=db.cursor()
    msg=''
    sql="select * from callregisters"
    cur.execute(sql)
    data=cur.fetchall()
    for res in data:
        msg+=f"{res[0]:<10}{res[1]:<25}{res[2]:<10}{res[3]:<10}{res[4]:<6}{res[5]:<12}\n"
    ta.insert(END,msg)
    db.close()
ta=Text(t,width=120,height=20)
ta.place(x=10,y=20)
showdata()
t.mainloop()