import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

ind=1
def showcallsolvesave():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.config(bg='lightgreen')
    
    ind=0
    def savedata():
        nonlocal ind
        try:
          xa = int(e1.get())
          xb = e2.get()
          xc = e3.get()
          xd = e4.get()
          xe = e5.get()
          
          if xb == "" or xc == "" or xd=="" or xe=="" :
              raise ValueError
        except ValueError:
          messagebox.showerror("Error", "Please fill all details correctly")
          return
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xa=int(e1.get())
        xb=int(e2.get())
        xc=int(e3.get())
        xd=e4.get()
        xe=e5.get()
        sql="insert into callsolve values(%d,%d,%d,'%s','%s')"%(xa,xb,xc,xd,xe)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('hi','saved')
        sendcustgmail()
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        ind=0
    def autofill(event):
        try:
            callid = int(e1.get())
        except ValueError:
            return
    
        db = pymysql.connect(host='localhost', user='root', password='root', database='scm')
        cur = db.cursor()
    
        sql = "select custid, productid, dateofsolve from callregisters where callid=%s"
        cur.execute(sql, (callid,))
        data = cur.fetchone()
    
        if data:
            e2.set(data[0])
            e3.set(data[1])
    
            e4.delete(0, END)
            e4.insert(0, data[2])   # date of resolve
    
        db.close()

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
        msg['Subject'] = "Welcome your call closed"
        msg['From'] = from_address
        msg['To'] = to_address
        
        # Create the message (HTML).
        Text = """Thanks for your call registration your call number"""+e1.get()+"your query is solved<br>"+"<br>In case any issue call customer care with in 2 hrs."
        
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
           
    
    def fillid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xb=[]
        xc=[]
        xd=[]
        sql="select callid,custid,productid from callregisters"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xb.append(res[0])
            xc.append(res[1])
            xd.append(res[2])
        e1['values']=xb
        e2['values']=xc
        e3['values']=xd
        db.close()
    
        
    a=Label(t,text='Call Id',bg='Light Green',font=('BOLD',15))
    a.place(x=50,y=60)
    e1=ttk.Combobox(t)
    e1.place(x=450,y=60)
    e1.bind("<<ComboboxSelected>>", autofill)

    #b2=Button(t,text='Check',bd=4,font=('arial',12,'bold'),fg='White',bg='Black',command=checkdata)
    #b2.place(x=650,y=60)
    
    
    b=Label(t,text='Cust Id',bg='Light Green',font=('BOLD',15))
    b.place(x=50,y=140)
    e2=ttk.Combobox(t)
    
    e2.place(x=450,y=140)
    
    c=Label(t,text='Product Id',bg='Light Green',font=('BOLD',15))
    c.place(x=50,y=180)
    e3=ttk.Combobox(t)
    e3.place(x=450,y=180)
    fillid()
    d=Label(t,text='Date of Resolve',bg='Light Green',font=('BOLD',15))
    d.place(x=50,y=220)
    e4=Entry(t,width=30)
    e4.place(x=450,y=220)
    
    e=Label(t,text='Remarks',bg='Light Green',font=('BOLD',15))
    e.place(x=50,y=260)
    e5=Entry(t,width=70)
    e5.place(x=450,y=260)
    
    bt=Button(t,text='Save',font=('arial',15,'bold'),fg='White',bg='Black',width=8,bd=4,command=savedata)
    bt.place(x=50,y=350)
    
    
    hd=Label(t,text='Call Solve Save Form',font=('bold',25),fg='black',bg='Lightgreen')
    hd.place(x=400,y=5)
    def cancel():
     t.destroy()
    b7=Button(t,text='cancel',font=('arial',15,"bold"),fg='white',bg='black',bd=4,width=8,command=cancel)
    b7.place(x=450,y=350)
    
    t.mainloop()