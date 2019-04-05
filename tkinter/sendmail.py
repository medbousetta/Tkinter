from tkinter import *
from tkinter import messagebox
n=Tk()
n.geometry("400x400")
n.configure(background='Brown')
n.title("gmail")

def p2():
    print(e2.get())

def p1():
    import smtplib

    gmail_user = e.get()
    gmail_password = e1.get()

    sent_from = gmail_user
    to = e2.get()
    subject = 'projetelpfe'
    body = 'bbbbbbbbbbbbbbb'

    email_text = """\  
   From: %s  
   To: %s  
   Subject: %s

   %s
   """ % (sent_from, ", ".join(to), subject, body)

    def send_email(subject, msg):
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            message = 'Subject: {}\n\n{}'.format(subject, msg)
            server.sendmail(sent_from, to, message)
            server.close()
            messagebox.showinfo('Email sent!')

        except:
            messagebox.showinfo("message", 'Something went wrong...')




    send_email(e3.get(),e4.get())

v1=StringVar()
b1=Button(n,text='send',command=p1)
b1.place(x=150,y=350)
ss='heloooooo'
var =Label(n,text=ss)
var.place(x=100,y=50)
e=Entry(n, width="40")
e.place(x=100,y=50)
e.focus()
e1=Entry(n, width="40",show="*")
e1.place(x=100,y=100)
e.focus()
e2=Entry(n, width="40",)
e2.place(x=100,y=150)
e2.focus()
e3=Entry(n, width="40")
e3.place(x=100,y=200)
e3.focus()
e4=Entry(n, width="40")
e4.place(x=100,y=250)
e4.focus()
l1 =Label(n,text="gmail Sender").place(x=20,y=50)
l2 =Label(n,text="password").place(x=20,y=100)
l3 =Label(n,text="to").place(x=20,y=150)
l4 =Label(n,text="subject").place(x=20,y=200)
l4 =Label(n,text="body").place(x=20,y=250)


n.mainloop()
