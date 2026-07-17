import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
import time
import threading
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkcalendar import DateEntry

def showcallregistersave():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.config(bg='cadetblue1')
    ind=0
    def newdata():
        d=datetime.datetime.now()
        msg=str(d.year)+str(d.month)+str(d.day)+str(d.hour)+str(d.minute)+str(d.second)
        e1.delete(0,END)
        e1.insert(0, msg) 
    def sendcustgmail():
        #find email for customer
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor() #connect mysql
        custid=int(e2.get())
        sql="select email from customers where custid=%d"%(custid)
        cur.execute(sql)
        data=cur.fetchone()
        toem=data[0]
        db.close()
        #now email
        from_address = "thekenstudy@gmail.com"
        to_address = toem
        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Welcome your call registered"
        msg['From'] = from_address
        msg['To'] = to_address
        
        # Create the message (HTML).
        Text = """Thanks for your call registration your call number"""+e1.get()+"your bill will be<br> Rs."+e8.get()+"<br> In case any issue call customer care with in 2 hrs."
        
        # Record the MIME type - text/html.
        part1 = MIMEText(Text, 'html')
        
        # Attach parts into message container
        msg.attach(part1)
        # Credentials
        username = 'thekenstudy@gmail.com'  
        password = 'tzfvqdwitwjzkfbd'
        
        # Sending the email
        ## note - this smtp config worked for me, I found it googling around, you may have to tweak the # (587) to get yours to work
        server = smtplib.SMTP('smtp.gmail.com', 587) 
        server.ehlo()
        server.starttls()
        server.login(username,password)  
        server.sendmail(from_address, to_address, msg.as_string())  
        server.quit()
        messagebox.showinfo('Hi','Mail send')
    def sendenggmail():
        #find email for customer
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor() #connect mysql
        eid=int(e5.get())
        sql="select email from engineers where engid=%d"%(eid)
        cur.execute(sql)
        data=cur.fetchone()
        toem=data[0]
        db.close()
        #now email
        from_address = "thekenstudy@gmail.com"
        to_address = toem
        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "You got a new call registered"
        msg['From'] = from_address
        msg['To'] = to_address
        
        # Create the message (HTML).
        Text = """Your  call number"""+e1.get()
        
        # Record the MIME type - text/html.
        part1 = MIMEText(Text, 'html')
        
        # Attach parts into message container
        msg.attach(part1)
        # Credentials
        username = 'thekenstudy@gmail.com'  
        password = 'tzfvqdwitwjzkfbd'
        
        # Sending the email
        ## note - this smtp config worked for me, I found it googling around, you may have to tweak the # (587) to get yours to work
        server = smtplib.SMTP('smtp.gmail.com', 587) 
        server.ehlo()
        server.starttls()
        server.login(username,password)  
        server.sendmail(from_address, to_address, msg.as_string())  
        server.quit()
        messagebox.showinfo('Hi','Mail send')
        db.commit()
        messagebox.showinfo('hi','saved')
        
        
    def savedata():
        nonlocal ind
        
        try:
          xa = int(e1.get())
          xb = e2.get()
          xc = e3.get()
          xd = e4.get()
          xe = e5.get()
          xf = e6.get()
          xg = e7.get()
          xh = e8.get()
          if xb == "" or xc == "" or xd=="" or xe=="" or xf==""or xg==""or xh=="":
              raise ValueError
        except ValueError:
          messagebox.showerror("Error", "Please fill all details correctly")
          return
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor() #connect mysql
        callid=int(e1.get())
        custid=int(e2.get())
        productid=int(e3.get())
        serviceid=int(e4.get())
        engid=int(e5.get())
        dateofcall=e6.get()
        dateofsolve=e7.get()
        estbill=int(e8.get())
        
        sql="insert into callregisters values(%d,%d,%d,%d,%d,'%s','%s',%d)"%(callid,custid,productid,serviceid,engid,dateofcall,dateofsolve,estbill)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('hi','saved')
        sendcustgmail()   # ⭐ add
        sendenggmail()    # ⭐ add
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        ind=0
        db.close()
        

    def fill_customer_details(event):
        try:
            custid = int(e2.get())
        except:
            return
    
        db = pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur = db.cursor()
    
        sql = "select productid from customers where custid=%s"
        cur.execute(sql, (custid,))
        data = cur.fetchone()
    
        if data:
            e3.set(data[0])   # product id
            
    
        db.close()

            
    def fillid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
    
        cust_list=[]
        service_list=[]
        eng_list=[]   # ⭐ new
    
        cur.execute("select custid from customers")
        data = cur.fetchall()
    
        for res in data:
            cust_list.append(res[0])
    
        cur.execute("select serviceid from services")
        data = cur.fetchall()
    
        for res in data:
            service_list.append(res[0])
       
        cur.execute("select engid from engineers")
        data = cur.fetchall()
    
        for res in data:
            eng_list.append(res[0])
    
        e2['values'] = cust_list
        e4['values'] = service_list
        e5['values'] = eng_list   # ⭐ ye missing tha
    
        db.close()

        
    def fetchbill():
     try:
        serviceid = int(e4.get())
     except ValueError:
        messagebox.showerror("Error", "Select valid Service ID")
        return

     db = pymysql.connect(host='localhost',user='root',password='root',database='scm')
     cur = db.cursor()

     sql = "SELECT cost FROM services WHERE serviceid=%s"
     cur.execute(sql,(serviceid,))
     data = cur.fetchone()

     if data:
        e8.delete(0, END)
        e8.insert(0, data[0])
     else:
        messagebox.showerror("Error", "Bill not found")

     db.close()

    a=Label(t,text='Callid',bg='cadetblue1',font=('BOLD',15))
    a.place(x=50,y=60)
    e1=Entry(t,width=30,bd=4,bg='White')
    e1.place(x=450,y=60)
    
    b2=Button(t,text='new',bd=4,font=('ariel',10,'bold'),command=newdata)
    b2.place(x=650,y=60)
    
    
    b=Label(t,text='Cust Id',bg='cadetblue1',font=('BOLD',15))
    b.place(x=50,y=100)
    e2=ttk.Combobox(t)
    e2.place(x=450,y=100)
    e2.bind("<<ComboboxSelected>>", fill_customer_details)

    
    c=Label(t,text='Produt Id',bg='cadetblue1',font=('BOLD',15))
    c.place(x=50,y=140)
    e3=ttk.Combobox(t)
    e3.place(x=450,y=140)
    
    d=Label(t,text='Service Id',bg='cadetblue1',font=('BOLD',15))
    d.place(x=50,y=180)
    e4=ttk.Combobox(t)
    e4.place(x=450,y=180)
    
    e=Label(t,text='Eng Id',bg='cadetblue1',font=('BOLD',15))
    e.place(x=50,y=220)
    e5=ttk.Combobox(t)
    e5.place(x=450,y=220)
    fillid()
    
    f=Label(t,text='Date of call',bg='cadetblue1',font=('BOLD',15))
    f.place(x=50,y=260)
    e6 = DateEntry(t, width=27, background='darkblue',
               foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
    e6.place(x=450,y=260)

    g=Label(t,text='Date of solve',bg='cadetblue1',font=('BOLD',15))
    g.place(x=50,y=300)
    
    e7 = DateEntry(t, width=27, background='darkblue',
                   foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
    e7.place(x=450,y=300)

    
    h=Label(t,text='Est Bill',bg='cadetblue1',font=('BOLD',15))
    h.place(x=50,y=340)
    e8=Entry(t,width=30,bd=4,bg='White')
    e8.place(x=450,y=340)
    
    bf=Button(t,text="Fetch Bill",font=('arial',10,'bold'),bg='white',command=fetchbill)
    bf.place(x=680,y=340)

    
    bt=Button(t,text='save',font=('arial',15,'bold'),fg='Black',bg='White',width=10,bd=4,command=savedata)
    bt.place(x=50,y=380)
    
    
    hd=Label(t,text='Call Register Save Form',font=('bold',25),fg='black',bg='cadetblue1')
    hd.place(x=400,y=5)
    def cancel():
        t.destroy()
    b7=Button(t,text='cancel',font=('arial',15,"bold"),fg='black',bg='white',bd=4,width=10,command=cancel)
    b7.place(x=450,y=380)
    
    t.mainloop()