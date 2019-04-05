from tkinter import *
n=Tk()
n.geometry("400x400")
n.title("simple project")
v=IntVar()
v1=IntVar()
v2=IntVar()
v3=IntVar()
vn=StringVar()
vn.set("hellllllllllooooooooooooooooooo")
img=PhotoImage(name="ok.png")
r1=Radiobutton(n,text="fecsbook ",variable=v,value=1).place(x=10,y=50)
r2=Radiobutton(n,text="youtube " ,variable=v, value=2).place(x=10,y=100)
c2=Checkbutton(n,text="python" ,variable=v1,onvalue=1,offvalue=0).place(x=100,y=40)
c2=Checkbutton(n,text="java" ,variable=v2,onvalue=2,offvalue=0).place(x=100,y=80)
c3=Checkbutton(n,text="c++" ,variable=v3,onvalue=3,offvalue=0).place(x=100,y=120)
lab=Label(n,text="aaaaaaaaaaaa",textvariable=vn).place(x=110,y=170)
l1=Listbox(n,bg="green",fg="white",selectbackground="black",highlightcolor='yellow',highlightthickness=5,selectmode=MULTIPLE)#selectmode=BROWSE/SINGLE
l1.place(x=95,y=200)



def kl():
    var1= v.get()
    var2=v1.get()
    var3=v2.get()
    var4=v3.get()
    if var1==1:
     vn.set('hello fecsbook ')
    elif var1==2:
     vn.set("hello youtube")
    if var2 == 1:
        l1.insert(0, "python")
    if var3 == 2:
        l1.insert(0,"java")
    if var4 ==3:
        l1.insert(0, "c++")


b1=Button(n,text='ok',command=kl).place(x=95,y=140)

n.mainloop()