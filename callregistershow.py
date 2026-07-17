import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql

def showcallregistershow():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.config(bg='cadetblue1')
    
    def showdata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        msg=''
        sql="select * from callregisters"
        cur.execute(sql)
        data=cur.fetchall()
        # clear
        ta.delete('1.0', END)
        
        heading = "{:<18}{:<10}{:<10}{:<12}{:<10}{:<15}{:<15}{:<10}\n".format(
        "CallID","CustID","ProdID","ServiceID","EngID","DateOfCall","DateOfSolve","EstBill")
        ta.insert(END, heading)
        ta.insert(END, "-"*100 + "\n")
        
        for res in data:
            row = "{:<18}{:<10}{:<10}{:<12}{:<10}{:<15}{:<15}{:<10}\n".format(
                str(res[0]), str(res[1]), str(res[2]), str(res[3]),str(res[4]), str(res[5]), str(res[6]), str(res[7]))
            ta.insert(END, row)



        db.close()
    ta=Text(t,width=100,height=30,bg='sky blue',fg='black')
    ta.place(x=10,y=50)
    
    
    hd=Label(t,text='Call Register Show Form',font=('bold',25),fg='black',bg='cadetblue1')
    hd.place(x=400,y=5)
    
    
    showdata()
    def cancel():
        t.destroy()
    b7=Button(t,text='cancel',font=('arial',15,"bold"),fg='black',bg='white',bd=4,width=8,command=cancel)
    b7.place(x=10,y=650)
    t.mainloop()