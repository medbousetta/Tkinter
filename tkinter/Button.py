from tkinter import *
from tkinter import ttk

n=Tk()
n.geometry("400x400")
n.title("seconde")
#############################################################################################
Style=ttk.Style()
Style.theme_use('classic')
Style.configure('TLabel',background="#e1d8b2")
Style.configure('TButton',background="#e1d8b2")
Style.configure('TRadiobutton',background="#e1d8b2")

'''
v1=IntVar()
v2=IntVar()

#c1=Checkbutton(n,text="python" , fg="red",selectcolor="yellow",variable=var1,onvalue=1,offvalue=0).place(x=10,y=20)
c1=Radiobutton(n,text="python" , fg="red",selectcolor="yellow",variable=v1, value=1).place(x=10,y=20)
c2=Radiobutton(n,text="jee" , fg="red",selectcolor="yellow",variable=v1, value=2).place(x=10,y=40)
s1=Radiobutton(n,text="java" , fg="red",selectcolor="yellow",variable=v2, value=1).place(x=50,y=20)
s2=Radiobutton(n,text="c" , fg="red",selectcolor="yellow",variable=v2, value=2).place(x=50,y=40)
s2=Radiobutton(n,text="django" , fg="red",selectcolor="yellow",variable=v2 ,value=3).place(x=50,y=60)

def p():
    if v1.get()==1:
      print("python")
    if v1.get()==2:
      print("jee")



b1=Button(n,text='ok',command=p).pack()
'''
#######################################################################""""""
l1=Listbox(n,bg="green",fg="white",selectbackground="black",highlightcolor='yellow',highlightthickness=5,selectmode=MULTIPLE)#selectmode=BROWSE/SINGLE
l1.place(x=0,y=0)
l1.insert(0,"bbbbb")
l1.insert(0,"cccccccc")
l1.insert(0,"tttttttt")
l1.insert(0,"rrrrr")

print(l1.size())
def p():
    print(l1.curselection())
    #print(l1.delete(0))
    print(l1.get(0,2))


b1=Button(n,text='ok',command=p).pack()



n.mainloop()