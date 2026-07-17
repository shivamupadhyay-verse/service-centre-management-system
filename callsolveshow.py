import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
def showcallsolveshow():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.config(bg='lightgreen')
    
    def showdata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        msg=''
        sql="select * from callsolve"
        cur.execute(sql)
        data=cur.fetchall()
        # clear
        ta.delete('1.0', END)
    
        heading = "{:<10}{:<10}{:<12}{:<18}{:<35}\n".format("callid","custid","productid","dateofresolve","Remark")
        ta.insert(END, heading)
        ta.insert(END, "-"*100 + "\n")

    
        # data
        for res in data:
            row = "{:<10}{:<10}{:<12}{:<18}{:<35}\n".format(res[0], res[1], res[2], str(res[3]), res[4])
            ta.insert(END, row)

        db.close()
    ta=Text(t,width=100,height=30,bg='Light blue',fg='black')
    ta.place(x=10,y=50)
    showdata()
    
    hd=Label(t,text='Call Solve Show Form',font=('bold',25),fg='black',bg='Lightgreen')
    hd.place(x=400,y=5)
    def cancel():
     t.destroy()
    b7=Button(t,text='cancel',font=('arial',15,"bold"),fg='white',bg='black',bd=4,width=8,command=cancel)
    b7.place(x=10,y=650)
    
    t.mainloop()