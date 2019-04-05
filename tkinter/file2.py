from tkinter import *
from tkinter import messagebox
n=Tk()
n.geometry("400x400")
def p1():
    print(v1.get())
def showme():
    #messagebox.showinfo("message", 'hello hello')
    v1.set("hello")
    '''
def delate():
    print(v1.get())
    e.delete(0,100)
'''
################################textviex######################################################################
v1=StringVar()
ss='heloooooo'
var =Label(n,textvariable=v1).place(x=100,y=100)
b1=Button(n,text='ok',command=showme).place(x=100,y=50)


'''
######################################################################################################
v1=StringVar()
e=Entry(n ,textvariable=v1,justify=CENTER,show="*",relief=GROOVE,font=20,bd=20)
e.place(x=50,y=50)
e.focus()
b1=Button(n,text='ok',command=delate)
b1.place(x=20,y=50)
'''

n.mainloop()
